# 05 — FORRT Replication Outcome

> Pre-flight: documented field list pasted verbatim below from `docs/forrt-form-fields.md` § FORRT Replication Outcome. All numbers quoted from `results/headline.json`, not memory, per `docs/verify-before-drafting.md` Rule 2.

## Documented field list (verbatim from `docs/forrt-form-fields.md`)

| Field label | Field type | Notes |
|---|---|---|
| Short URI suffix for outcome ID | text input, **required** | kebab-case slug |
| Plain-text label for the outcome | text input, **required** | descriptive title |
| Search for a FORRT replication study | search/select, **required** | pick published Study URI |
| Repository URL | text input, **required** | GitHub URL |
| Completion date | date picker, **required** | ISO format |
| Validation status | dropdown, **required** | Validated / PartiallySupported / Contradicted / Inconclusive / NotTested |
| Confidence level | dropdown, **required** | VeryHighConfidence / HighConfidence / Moderate / LowConfidence / VeryLowConfidence |
| Describe the overall conclusion about the original claim | textarea, **required** | substantive interpretation + headline comparison |
| Describe the evidence that supports your conclusion | textarea, **required** | numbers, test statistics |
| Describe what limits the conclusions of the study | textarea, **optional** | honest caveats |

## Field-by-field draft

### Short URI suffix for outcome ID (text input, required)

```
phillips-table2-maxent-outcome
```

### Plain-text label for the outcome (text input, required)

```
Target-group background improves MaxEnt AUC — Phillips Table 2 reproduced
```

### Search for a FORRT replication study (search/select, required)

```
<pending step 04 publication — paste the Replication Study URI here>
```

### Repository URL (text input, required)

```
https://github.com/annefou/sdm-phillips-reproduction
```

### Completion date (date picker, required)

```
2026-05-30
```

### Validation status (dropdown, required)

- [x] **Validated**
- [ ] PartiallySupported
- [ ] Contradicted
- [ ] Inconclusive
- [ ] NotTested

> Maps to CiTO `confirms` in step 06.

### Confidence level (dropdown, required)

- [ ] VeryHighConfidence
- [x] **HighConfidence**
- [ ] Moderate
- [ ] LowConfidence
- [ ] VeryLowConfidence

> Strong evidence (highly significant paired test, gain magnitude matching the original to two decimal places, bias gradient reproduced) with a different MaxEnt engine — strong agreement, not identical, so HighConfidence rather than VeryHighConfidence.

### Describe the overall conclusion about the original claim (textarea, required)

```
The reproduction confirms Phillips et al. 2009 Table 2: target-group background improves the mean predictive AUC of presence-only MaxEnt models. Across 225 species in six regions, mean AUC rises from 0.7163 with random background to 0.7468 with target-group background, a gain of +0.0305. This closely matches Phillips' reported Maxent gain of +0.0293 (0.7276 to 0.7569) in both direction and magnitude, despite using the independent open-source elapid/maxnet engine rather than the original Java Maxent. Phillips' secondary finding that the gain is largest where sampling bias is greatest also reproduces: the Canadian region (CAN), the most biased, shows the largest gain.
```

### Describe the evidence that supports your conclusion (textarea, required)

```
Overall mean AUC: random 0.7163, target-group 0.7468, delta +0.0305 (Phillips Maxent: 0.7276, 0.7569, delta +0.0293). Paired Wilcoxon signed-rank test of target-group vs random per-species AUC: statistic 8028.0, p = 1.6e-06 (significant at p < 0.001). Per-region deltas: CAN +0.1317 (largest, 20 species), SWI +0.0394 (30), AWT +0.0451 (40), NSW +0.0184 (53), NZ +0.0135 (52), SA -0.0146 (30, the only region where target-group background did not help). The largest gain falls on CAN, the region flagged as most sampling-biased, reproducing Phillips' bias-gradient result.
```

### Describe what limits the conclusions of the study (textarea, optional)

```
(1) The MaxEnt engine differs from Phillips' original (elapid/maxnet vs Java Maxent), so absolute AUC decimals differ even though direction and magnitude agree. (2) Only MaxEnt is reproduced; Phillips' broader Table 2 also covered BRT, MARS, GAM and other methods, so the cross-method generality of the claim is not tested here. (3) 225 of Phillips' 226 species are modelled — one species was dropped because its presence-absence evaluation column had no presence/absence variation, leaving AUC undefined. (4) A minimum-presence threshold of 5 occurrences was applied. (5) One region (SA) showed a small negative gain, consistent with the original's observation that the benefit is not uniform across regions.
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 05.
