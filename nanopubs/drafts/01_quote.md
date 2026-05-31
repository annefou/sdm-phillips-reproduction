# 01 — Quote-with-comment (paper-rooted)

> Pre-flight: documented field list pasted verbatim below from `docs/forrt-form-fields.md` § Quote-with-comment.

**Form heading:** *"Annotate a paper quotation — Annotating a paper quotation with personal interpretation"*

## Documented field list (verbatim from `docs/forrt-form-fields.md`)

| Field label | Field type | Notes |
|---|---|---|
| Cited DOI | text input | bare `10.` form, NOT `https://doi.org/...` |
| Quote whole text (less than 500 characters) | radio button (default selected) | ≤ 500 chars |
| Quote start/end | radio button (alternative) | start phrase + end phrase, for longer spans |
| Quoted Text | textarea, **required** | verbatim, ≤ 500 chars in whole-text mode |
| Comment | textarea, **required** | why the quotation is relevant; target ≤ 500 chars |

## Field-by-field draft

### Cited DOI (text input, required)

```
10.1890/07-2153.1
```

### Quote mode (radio button)

- [x] **Quote whole text (less than 500 characters)**
- [ ] Quote start/end

### Quoted Text (textarea, required)

Verbatim from Phillips et al. 2009, Abstract, p. 181. Character-for-character.

```
We find that target-group background improves average performance for all the modeling methods we consider, with the choice of background data having as large an effect on predictive performance as the choice of modeling method.
```

Character count: 228 / 500.

### Comment (textarea, required)

```
Can we reproduce the AUC-improvement result behind this sentence on Phillips' own data (the Elith et al. 2006 NCEAS dataset)? Using per-species MaxEnt, we can compare random background against target-group background and measure AUC on the independent presence-absence evaluation sites, testing whether the target-group gain reported in Phillips Table 2 reproduces in sign and magnitude with an independent open-source MaxEnt engine.
```

Character count: 437 / 500.

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 01.
