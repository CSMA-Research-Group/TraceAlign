# Artifact Evaluation Guide

## Claims Directly Checkable From This Package

1. RQ2 summary: TraceAlign ranks first in 8 of 12 model-dataset settings,
   remains top-two when ties are counted in all 12 settings, and has an average
   APPS gain of +7.56 percentage points over the strongest reproduced baseline.
2. RQ3 audit summary: using the reduced per-case label file, the 80-case APPS
   audit has 68.8% independent agreement and Cohen's kappa 0.270; the
   clean-candidate subset has 36 cases, 77.8% agreement, kappa 0.524, and 27
   faulty-test consensus labels.
3. Material-quality precheck: the main risk indicators in the audit match the
   counts reported in the paper.

Run:

```bash
python3 scripts/verify_rq2_summary.py
python3 scripts/verify_human_audit_metrics.py
python3 scripts/check_anonymity.py
```

## Full Rerun Requirements

To fully rerun TraceAlign rather than checking the processed evidence, install
the Python dependencies under `src/tracealign/`, configure an OpenAI-compatible
API endpoint, and place the public benchmark datasets according to
`src/tracealign/docs/DATASETS.md`.

Because LLM outputs and hosted model versions can vary over time, exact full
rerun equality is not guaranteed. The included CSV/JSON evidence files preserve
the reported run summaries and reduced human-audit labels used to recompute the
submission's aggregate audit statistics.
