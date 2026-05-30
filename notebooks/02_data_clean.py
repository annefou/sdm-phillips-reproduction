# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 02 — Data clean: load the disdat `.rds` tables into tidy parquet
#
# Read the cached `.rds` tables (notebook 01) with **`pyreadr`** — no R runtime
# — and assemble tidy per-region/group tables, written as parquet under
# `data/clean/`. Splitting loading + cleaning out of the analysis keeps the
# 4-stage structure clean: notebook 03 reads only the parquet.
#
# For each region we emit three table families (one parquet per group where the
# region is split into target groups):
#
# - **presence-only** (`po_<region>.parquet`) — `train_po` rows: `spid`,
#   `group`, env predictors. One row per presence locality. This is both the
#   per-species presence source AND the target-group-background source.
# - **background** (`bg_<region>.parquet`) — `train_bg` rows: 10000 uniform
#   random background sites, env predictors only (the RANDOM background).
# - **presence-absence + env** (`pa_<region>[_<group>].parquet`) — the
#   independent evaluation sites: env predictors plus one 0/1 column per species
#   (`spid`-named), joined from `test_env` + `test_pa` on row order.
#
# A `clean_manifest.json` records the per-region/group shapes and the predictor
# column list so the analysis notebook does not have to re-derive them.

# %%
import json
import re
from pathlib import Path

import pandas as pd
import pyreadr

# %% [markdown]
# ## Paths and constants

# %%
ROOT = Path("..").resolve()
DATA = ROOT / "data"
DISDAT_DIR = DATA / "disdat"
CLEAN_DIR = DATA / "clean"
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

SOURCES_JSON = DATA / "raw" / "sources.json"
MANIFEST_JSON = CLEAN_DIR / "clean_manifest.json"

# Non-predictor columns common to the disdat tables.
META_COLS = {"siteid", "spid", "x", "y", "occ", "group"}

REGIONS = ["AWT", "CAN", "NSW", "NZ", "SA", "SWI"]

with open(SOURCES_JSON) as f:
    sources = json.load(f)
print(f"sources registry lists {len(sources['files'])} cached .rds files")
print(f"disdat dir = {DISDAT_DIR} (exists={DISDAT_DIR.exists()})")


# %% [markdown]
# ## Load helpers
#
# `pyreadr.read_r` returns an ordered dict keyed by the R object name (or `None`
# for an unnamed top-level data.frame, as here). Predictor columns are every
# column that is not metadata.

# %%
def load_rds(name: str) -> pd.DataFrame:
    """Load one disdat .rds table as a DataFrame."""
    result = pyreadr.read_r(str(DISDAT_DIR / name))
    return next(iter(result.values()))


def predictor_cols(df: pd.DataFrame) -> list[str]:
    """Env predictor column names = all columns minus the known metadata."""
    return [c for c in df.columns if c not in META_COLS]


def test_pa_files(region: str) -> list[tuple[str, str | None]]:
    """[(test_pa filename, group)] for a region; group parsed from the suffix.

    `<R>test_pa.rds` -> group None (single-group region); `<R>test_pa_<g>.rds`
    -> group `<g>` (AWT bird/plant; NSW ba/db/...)."""
    out: list[tuple[str, str | None]] = []
    for path in sorted(DISDAT_DIR.glob(f"{region}test_pa*.rds")):
        m = re.match(rf"{region}test_pa(?:_(\w+))?\.rds$", path.name)
        if m:
            out.append((path.name, m.group(1)))
    return out


# %% [markdown]
# ## Assemble + write tidy parquet per region/group
#
# Presence-only and background are per-region. The presence-absence evaluation
# tables are per-group where the region is split (AWT, NSW). We join `test_env`
# (predictors) and `test_pa` (per-species 0/1 columns) by row position — they
# are aligned site-for-site in the disdat distribution.

# %%
manifest = {"regions": {}, "predictor_cols": {}}

for region in REGIONS:
    po = load_rds(f"{region}train_po.rds")
    bg = load_rds(f"{region}train_bg.rds")
    env = predictor_cols(po)
    manifest["predictor_cols"][region] = env

    po.to_parquet(CLEAN_DIR / f"po_{region}.parquet", index=False)
    bg.to_parquet(CLEAN_DIR / f"bg_{region}.parquet", index=False)

    groups_info = []
    for pa_name, group in test_pa_files(region):
        suffix = "" if group is None else f"_{group}"
        test_pa = load_rds(pa_name)
        test_env = load_rds(f"{region}test_env{suffix}.rds")
        species = [c for c in test_pa.columns if c not in META_COLS]

        # Join the predictor columns (same env list as po) with the per-species
        # PA 0/1 columns by row position — disdat aligns them site-for-site.
        pa_env = test_env[env].reset_index(drop=True)
        pa_cols = test_pa[species].reset_index(drop=True)
        pa_tidy = pd.concat([pa_env, pa_cols], axis=1)

        out_name = f"pa_{region}{suffix}.parquet"
        pa_tidy.to_parquet(CLEAN_DIR / out_name, index=False)
        groups_info.append({
            "group": group, "pa_parquet": out_name,
            "n_species": len(species), "n_sites": int(len(pa_tidy)),
            "species": species,
        })

    manifest["regions"][region] = {
        "po_parquet": f"po_{region}.parquet",
        "bg_parquet": f"bg_{region}.parquet",
        "n_po_rows": int(len(po)),
        "n_bg_rows": int(len(bg)),
        "groups": groups_info,
    }
    n_grp = len(groups_info)
    n_sp = sum(g["n_species"] for g in groups_info)
    print(f"  {region:<4}: po={len(po):>6} bg={len(bg):>6} "
          f"groups={n_grp} species={n_sp} predictors={len(env)}")

# %% [markdown]
# ## Persist the clean manifest

# %%
with open(MANIFEST_JSON, "w") as f:
    json.dump(manifest, f, indent=2)

total_species = sum(g["n_species"] for r in manifest["regions"].values()
                    for g in r["groups"])
print(f"\nwrote {MANIFEST_JSON}")
print(f"total species across all region/groups: {total_species}")
print(f"clean parquet files: {len(list(CLEAN_DIR.glob('*.parquet')))}")
