# Snakefile — orchestrates the Phillips (2009) reproduction pipeline end-to-end.
#
# Reproduces Phillips et al. (2009, 10.1890/07-2153.1) Table 2 (Maxent row) on
# the Elith et al. (2006) NCEAS benchmark (distributed as the disdat R package,
# read via pyreadr). Four notebooks, four rules; each rule converts the jupytext
# .py to .ipynb and executes it in place so the notebook stays the source of
# truth and Snakemake just sequences them.
#
#   01_data_download -> data/raw/sources.json + data/disdat/*.rds
#   02_data_clean    -> data/clean/*.parquet + data/clean/clean_manifest.json
#   03_analysis      -> results/repro_phillips_auc.parquet + results/headline.json
#   04_figures       -> figures/main_result.{png,pdf}
#
# Usage:
#   pixi run snakemake --cores 1            # run everything
#   pixi run snakemake --cores 1 -n         # dry run
#
# Smoke test (cap the work for a quick DAG check), set env vars first, e.g.:
#   REPRO_REGIONS=AWT,CAN REPRO_MIN_PRESENCE=20 pixi run snakemake --cores 1

NOTEBOOKS = "notebooks"
DATA = "data"
RESULTS = "results"
FIGURES = "figures"


rule all:
    input:
        f"{FIGURES}/main_result.png",
        f"{RESULTS}/headline.json",


# ---------- 01: Data download ----------
# Self-contained: enumerate + fetch the disdat .rds tables (train_po / train_bg
# / test_pa / test_env for 6 regions) from rspatial/disdat; write a provenance
# registry. No credentials needed.
rule data_download:
    output:
        sources = f"{DATA}/raw/sources.json",
    log:
        f"{RESULTS}/logs/01_data_download.log",
    shell:
        "mkdir -p $(dirname {log}) {DATA}/disdat && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 01_data_download.py && "
        "jupyter execute --inplace 01_data_download.ipynb 2>&1 | tee ../{log}"


# ---------- 02: Data clean ----------
# Read the .rds via pyreadr; assemble tidy per-region/group parquet tables
# (presence-only, random background, presence-absence + env) + a manifest.
rule data_clean:
    input:
        sources = f"{DATA}/raw/sources.json",
    output:
        manifest = f"{DATA}/clean/clean_manifest.json",
    log:
        f"{RESULTS}/logs/02_data_clean.log",
    shell:
        "mkdir -p $(dirname {log}) {DATA}/clean && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 02_data_clean.py && "
        "jupyter execute --inplace 02_data_clean.ipynb 2>&1 | tee ../{log}"


# ---------- 03: Analysis ----------
# Per region/group: fit elapid MaxEnt with random vs target-group background,
# evaluate per-species AUC on the independent presence-absence sites, aggregate.
rule analysis:
    input:
        manifest = f"{DATA}/clean/clean_manifest.json",
    output:
        auc = f"{RESULTS}/repro_phillips_auc.parquet",
        headline = f"{RESULTS}/headline.json",
    log:
        f"{RESULTS}/logs/03_analysis.log",
    shell:
        "mkdir -p $(dirname {log}) " + RESULTS + " && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 03_analysis.py && "
        "jupyter execute --inplace 03_analysis.ipynb 2>&1 | tee ../{log}"


# ---------- 04: Figures ----------
# Mean AUC random vs target-group (overall + per region), with Phillips' Table 2
# (Maxent) reference values marked.
rule figures:
    input:
        auc = f"{RESULTS}/repro_phillips_auc.parquet",
        headline = f"{RESULTS}/headline.json",
    output:
        main_png = f"{FIGURES}/main_result.png",
        main_pdf = f"{FIGURES}/main_result.pdf",
    log:
        f"{RESULTS}/logs/04_figures.log",
    shell:
        "mkdir -p $(dirname {log}) " + FIGURES + " && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 04_figures.py && "
        "jupyter execute --inplace 04_figures.ipynb 2>&1 | tee ../{log}"
