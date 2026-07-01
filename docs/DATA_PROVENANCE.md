# Data Provenance

## Source Code

The implementation under `src/tracealign/` is copied from the project's clean
release source tree. Generated caches, local environment files, raw run outputs,
and large benchmark shards are excluded.

## Human Audit

The APPS human-audit files in `data/human_audit/` are reduced public views of
the final processed files used by the paper's RQ3 analysis:

- reduced per-case label/risk precheck: `human_audit_material_quality_precheck.csv`;
- independent annotator labels, reduced to labels/confidence/discussion flags:
  `human_audit_annotations_annotator_a.csv` and
  `human_audit_annotations_annotator_b.csv`;
- final consensus labels: `human_audit_consensus_final.csv`;
- final metrics: `human_audit_metrics_final.json`.
- two short illustrative rationales: `human_audit_examples.csv`.

The public package intentionally excludes full problem statements, candidate
code, generated tests, trace excerpts, hidden key files, raw event text, and
complete annotator rationales. Those materials are treated as internal research
work product rather than public artifact data.

The audit is exploratory. It supports the paper's claim that faulty generated
tests are common among attributable audited APPS failures after material-quality
screening; it is not presented as a population-level rate.

## Paper Tables

The CSV files in `results/tables/` mirror the paper tables and ablation values.
The verification scripts recompute the derived summaries used in the text.

## External Dependencies

Full reruns require user-provided API credentials and public benchmark data for
APPS, HumanEval+, MBPP+, and LiveCodeBench. The artifact does not contain
private credentials or hidden test suites.
