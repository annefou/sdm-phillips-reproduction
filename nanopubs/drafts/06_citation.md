# 06 — CiTO Citation

> Pre-flight: documented field list pasted verbatim below from `docs/forrt-form-fields.md` § Citation with CiTO. Citation type maps from the Outcome's Validated status → `confirms`.

**Description:** *"Declare citations between papers or other works, using Citation Typing Ontology"*

## Documented field list (verbatim from `docs/forrt-form-fields.md`)

| Field label | Field type | Notes |
|---|---|---|
| Identifier for the citing creative work | text input, **required** | the Outcome's nanopub URI |
| List citations | repeatable group, **required** ≥1 | one or more entries, each Type + URL |
| ↳ Citation Type | dropdown | from controlled list (see below) |
| ↳ DOI or other URL of the cited work | text input | DOI URL form or other URL |

Available Citation Types: `confirms`, `qualifies`, `disputes`, `extends`, `usesMethodIn`, `citesAsAuthority`, `obtainsBackgroundFrom`, `discusses`, `citesAsDataSource`, `containsAssertionFrom`, `includesQuotationFrom`, `reviews`, `critiques`, `credits`. **NOT available:** `replicates`, `citesAsRelated`.

## Field-by-field draft

### Identifier for the citing creative work (text input, required)

```
<pending step 05 publication — paste the FORRT Outcome URI here>
```

### List citations (repeatable group, required ≥1)

#### Citation 1 — confirm the original paper

##### Citation Type (dropdown)

```
confirms
```

> The Outcome's validation status is Validated; per the mapping rule, Validated → `confirms`. We reproduced Phillips' published Table 2 Maxent AUC result.

##### DOI or other URL of the cited work (text input)

```
https://doi.org/10.1890/07-2153.1
```

#### Citation 2 — link to the sibling application repo (optional)

The sibling repo `sdm-hotspot-spatial-effort` reuses this validated method to test a hotspot question. The documented dropdown does **not** include `cito:citesAsRelated`, so it cannot be expressed as drafted. If you want this link, the closest available neutral type is `discusses`; alternatively, omit it here and instead record the relationship from the sibling repo's own chain (which would more naturally `usesMethodIn` / `extends` this Outcome). Recommendation: **skip in this CiTO step** and let the sibling repo cite this Outcome, to keep the citation direction clean (downstream → upstream).

If you do choose to include it:

##### Citation Type (dropdown)

```
discusses
```

##### DOI or other URL of the cited work (text input)

```
https://github.com/annefou/sdm-hotspot-spatial-effort
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 06.

This completes the six-step FORRT chain. Optional next layers (`07_research_software.md`, `08_synthesis.md`) are not part of this task.
