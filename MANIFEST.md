# Manifest

## Repository-Level Files

- `README.md`: overview and quick checks.
- `LICENSE`: anonymous review-only artifact license.
- `requirements.txt`: root dependency entry point.
- `.gitignore`: excludes generated outputs, credentials, caches, and temporary files.

## Source Code

- `src/tracealign/components/`: TraceAlign generation, repair, arbitration, and test-handling components.
- `src/tracealign/runners/`: dataset-specific experiment runners.
- `src/tracealign/utils/`: execution tracing and helper utilities.
- `src/tracealign/llm/`: OpenAI-compatible client wrapper and prompts.
- `src/tracealign/datasets/`: lightweight dataset adapters.
- `src/tracealign/config/api.env.example`: credential-free API configuration template.

## Evidence and Results

- `data/human_audit/`: reduced APPS human-audit labels, material-quality
  precheck data, aggregate metrics, and two illustrative rationale excerpts.
- `results/tables/`: CSV versions of the reported RQ1--RQ4 tables.

## Verification Scripts

- `scripts/verify_rq2_summary.py`: recomputes RQ2 wins, top-two finishes, and APPS gain from `table1_pass_at1.csv`.
- `scripts/verify_human_audit_metrics.py`: recomputes RQ3 agreement, kappa, consensus counts, and material-risk indicators.
- `scripts/check_anonymity.py`: scans for personal paths, credentials, caches, and obvious transcript markers.

## Documentation

- `docs/ARTIFACT_EVALUATION.md`: what can be checked directly and what requires full reruns.
- `docs/DATA_PROVENANCE.md`: provenance of source, audit data, and table files.
- `docs/ANONYMIZATION.md`: anonymization and exclusion notes.
