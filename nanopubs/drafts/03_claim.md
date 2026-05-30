# 03 — FORRT Claim

> Pre-flight: documented field list pasted verbatim below from `docs/forrt-form-fields.md` § FORRT Claim. Claim type chosen per `docs/claim-type-vocabulary.md`.

**Form heading:** *"FORRT Claim — Declare an original claim according to FORRT, linking it to an AIDA sentence with a specific FORRT type."*

## Documented field list (verbatim from `docs/forrt-form-fields.md`)

| Field label | Field type | Notes |
|---|---|---|
| Short URI suffix as claim ID | text input, **required** | kebab-case slug |
| Label of the claim (to find it later) | text input, **required** | descriptive title, not a sentence |
| Search for an AIDA sentence | search/select dropdown, **required** | pick published AIDA URI |
| Type of FORRT claim | dropdown, **required** | single-select from 7 options |
| Source URI (optional) | text input, **optional** | full `https://doi.org/...` URL form |

## Field-by-field draft

### Short URI suffix as claim ID (text input, required)

```
target-group-background-improves-auc
```

### Label of the claim (text input, required)

```
Target-group background improves presence-only SDM AUC
```

### Search for an AIDA sentence (search/select, required)

```
<pending step 02 publication — paste the AIDA URI here>
```

> If the AIDA was published via Nanodash (`w3id.org/np/...`), paste the URI manually rather than relying on search.

### Type of FORRT claim (dropdown, required)

- [ ] computational performance
- [ ] scalability
- [ ] data quality
- [ ] data governance
- [ ] descriptive pattern
- [x] **model performance**
- [ ] statistical significance

> Rationale: the claim is about a species distribution **model's evaluation metric** (AUC) — which background-data condition yields better predictive performance. Per `docs/claim-type-vocabulary.md`, performance of a model measured by an evaluation metric on independent sites is `model performance`, not `descriptive pattern` (the claim is not an empirical relationship between environmental variables, it is about the models' predictive accuracy). Consistent with the AIDA label "increases the mean AUC of presence-only species distribution models".

### Source URI (text input, optional)

```
https://doi.org/10.1890/07-2153.1
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 03.
