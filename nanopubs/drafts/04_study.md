# 04 — FORRT Replication Study

> Pre-flight: documented field list pasted verbatim below from `docs/forrt-form-fields.md` § FORRT Replication Study. Methodology and Deviations verified against `notebooks/03_analysis.py` and `notebooks/01_data_download.py` per `docs/verify-before-drafting.md` Rule 2. No numerical results in this draft — those live only in the Outcome.

## Documented field list (verbatim from `docs/forrt-form-fields.md`)

| Field label | Field type | Notes |
|---|---|---|
| Short URI suffix for study ID | text input, **required** | short slug |
| Label/name of replication study | text input, **required** | human-readable title |
| Study type | dropdown, **required** | (1) Reproduction Study; (2) Replication Study; (3) Reproduction/Replication Study |
| Search for a FORRT claim | search/select, **required** | pick published Claim URI |
| Describe what part of the claim is reproduced/replicated | textarea, **required** | scope, NOT method, NOT results |
| Describe how the claim is reproduced/replicated | textarea, **required** | method in plain prose, NOT results |
| Describe any deviations from original methodology | textarea, **optional** | verified against code |
| Search keywords (Wikidata) | multi-select, **optional** | labels not QIDs |
| Search discipline (Wikidata) | search, **optional** | labels not QIDs |

## Field-by-field draft

### Short URI suffix for study ID (text input, required)

```
phillips-table2-maxent-reproduction
```

### Label/name of replication study (text input, required)

```
Reproduction of Phillips et al. 2009 Table 2 — MaxEnt random vs target-group background AUC
```

### Study type (dropdown, required)

- [x] **Reproduction Study** — direct reproduction: same methodology, same tools.
- [ ] Replication Study
- [ ] Reproduction/Replication Study

> Same data (Phillips' own NCEAS benchmark) and same method family (per-species MaxEnt, random vs target-group background, AUC on independent presence-absence sites) — a Reproduction.

### Search for a FORRT claim (search/select, required)

```
<pending step 03 publication — paste the FORRT Claim URI here>
```

### Describe what part of the claim is reproduced/replicated (textarea, required)

```
This study reproduces the Maxent row of Phillips et al. 2009 Table 2: the comparison of mean predictive AUC for presence-only species distribution models trained with random background versus target-group background. In scope: the direction and magnitude of the AUC gain from target-group background, aggregated across species, and the stronger gain in regions with greater sampling bias. Out of scope: the other modelling methods Phillips also tested (BRT, MARS, GAM and others) and the absolute predicted-distribution maps — only the MaxEnt AUC comparison on this benchmark is tested here.
```

### Describe how the claim is reproduced/replicated (textarea, required)

```
The Elith et al. 2006 NCEAS presence-only / presence-absence benchmark — the same data Phillips used — is obtained from the rspatial/disdat R data package (data paper doi 10.17161/bi.v15i2.13384) by downloading its .rds tables and reading them in Python with pyreadr. For each species across the six regions (AWT, CAN, NSW, NZ, SA, SWI), a MaxEnt model (elapid engine, linear + quadratic + hinge features) is fit twice: once against the region's random background sites supplied by disdat, and once against a target-group background formed from the pooled presence localities of all species in the same biological target group. Both models predict at the independent presence-absence evaluation sites and AUC is computed with scikit-learn. Per-species AUC for the two background types is aggregated to region, group and overall means, and the paired difference is tested with a Wilcoxon signed-rank test. 225 species across 6 regions are modelled.
```

### Describe any deviations from original methodology (textarea, optional)

```
(1) MaxEnt engine: the open-source elapid/maxnet implementation is used rather than Phillips' original Java Maxent, so exact AUC decimals are expected to differ even where direction and magnitude agree. (2) Only MaxEnt is run — Phillips' broader Table 2 also covered BRT, MARS, GAM and other methods, which are not reproduced here. (3) One species fewer is modelled than Phillips' 226 (225 here) because a species whose presence-absence evaluation column has no presence/absence variation gives an undefined AUC and is dropped. (4) A minimum-presence threshold of 5 occurrences is applied before a species is fit.
```

### Search keywords (Wikidata) (multi-select, optional)

Intended labels: `species distribution model`, `MaxEnt`, `sampling bias`, `receiver operating characteristic`. *(Provide as search labels in the UI; skip any without a clean match.)*

### Search discipline (Wikidata) (search, optional)

Intended label: `ecology` (or `biodiversity informatics` if available).

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 04.
