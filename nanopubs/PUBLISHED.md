# Published nanopub chain — URI registry

This file is the canonical registry of published nanopub URIs for this replication. Update it as you publish each step.

## Release & archival artefacts

| Artefact | Identifier | Notes |
|---|---|---|
| Source — concept DOI | [10.5281/zenodo.20473156](https://doi.org/10.5281/zenodo.20473156) | Resolves to the latest version. Cited in `CITATION.cff` / `codemeta.json`. |
| Source — version DOI (v0.1.0) | [10.5281/zenodo.20473157](https://doi.org/10.5281/zenodo.20473157) | This release's immutable snapshot. |
| GitHub release | [v0.1.0](https://github.com/annefou/sdm-phillips-reproduction/releases/tag/v0.1.0) | |
| Docker image (GHCR) | `ghcr.io/annefou/sdm-phillips-reproduction:0.1.0` (also `:latest`) | Built + pushed by `docker.yml` on release. Make the package public in repo → Packages if not already. |
| Docker image — Zenodo DOI | [10.5281/zenodo.20474587](https://doi.org/10.5281/zenodo.20474587) | Concept DOI for the archived `:latest` image (version DOI `10.5281/zenodo.20474588`). FAIR4RS A2 — image preserved on Zenodo independently of GHCR. |

## Chain

| Step | Template | URI | Published |
|---|---|---|---|
| 01 | Quote-with-comment (or PICO / PCC) | https://w3id.org/sciencelive/np/RAaLMzZpNPytqGikM3VIvwux8bxJNctgTTeFB8srYHjy8 | |
| 02 | AIDA Sentence | https://w3id.org/sciencelive/np/RA_OZAEn8FwHzKGJSnvCSqvJk9lI4XMA2ZthNw111zURQ | |
| 03 | FORRT Claim | https://w3id.org/sciencelive/np/RAHF_1MUfAVbXhXvj_Wtq8GsP8ZWjc9LerDhdLqhv_SzE | |
| 04 | FORRT Replication Study | https://w3id.org/sciencelive/np/RAnYD9w4jylurPK2GH4-YmKtiqyNOy8is8itzxuTgd3Qw | |
| 05 | FORRT Replication Outcome | https://w3id.org/sciencelive/np/RA_uV84IchQAkkmCP_6amQir_flgCmvvt97DWIDmbu_V0 | |
| 06 | CiTO Citation | https://w3id.org/sciencelive/np/RAWsmCzWMKYQQK_ovRvE1o2wqjYkoxjfZRncHEcWAvv2g | |

## Format

URIs from Science Live are of the form `https://w3id.org/sciencelive/np/RA…`. URIs from Nanodash (used as a fallback when the Science Live UI hits a bug) are of the form `https://w3id.org/np/RA…`. Both are valid and citable.

If a URI is not in the Science Live namespace, view it via the Science Live viewer by wrapping the URI:

```
https://platform.sciencelive4all.org/np/?uri=<full-URI>
```

## Cross-references

- Drafts: `nanopubs/drafts/`
- Form structure: `docs/forrt-form-fields.md`
- Chain shape decision: `docs/chain-decision-tree.md`
