# 02 — AIDA Sentence

> Pre-flight: documented field list pasted verbatim below from `docs/forrt-form-fields.md` § AIDA sentence. AIDA pre-write checklist run (no numerical values, no method names, no cryptic identifiers, world-talk, one finding, ends with full stop).

**Form heading:** *"AIDA Sentence — Make structured scientific claims following the AIDA model"*

## Documented field list (verbatim from `docs/forrt-form-fields.md`)

| Field label | Field type | Notes |
|---|---|---|
| Enter your AIDA sentence here (ending with a full stop) | textarea, **required** | atomic, independent, declarative, absolute; ends with full stop |
| Select related topics/tags | dropdown, **optional** | predefined topic vocabulary |
| Relates to this nanopublication | text input, **required** | URI of nanopub the AIDA derives from (the Quote URI here) |
| Supported by datasets | repeatable group, **optional** | dataset DOIs/URLs |
| Supported by other publications | repeatable group, **optional** | supporting publication DOIs/URLs |

## Field-by-field draft

### AIDA sentence (textarea, required)

```
Using target-group background increases the mean AUC of presence-only species distribution models relative to using random background.
```

> Pre-write checklist: no numbers; no engine/library names; "AUC" is the standard performance metric the claim is about, not an internal identifier; states what is true in the world (target-group background increases predictive performance); one empirical finding; ends with a full stop.

### Select related topics/tags (dropdown, optional)

Intended labels if present in the platform vocabulary: `species distribution modelling`, `model evaluation`. *(Skip if no close match in the dropdown.)*

### Relates to this nanopublication (text input, required)

```
<pending step 01 publication — paste the Quote-with-comment URI here>
```

### Supported by datasets (repeatable group, optional)

*(skip — optional. The grounding dataset belongs on the Replication Study; leaving this empty also avoids the known platform bug when both dataset + publication groups are populated.)*

### Supported by other publications (repeatable group, optional)

*(skip — optional. The source paper is already cited via the Quote at step 01.)*

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 02.
