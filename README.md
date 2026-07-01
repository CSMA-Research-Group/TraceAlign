# TraceAlign Anonymous Artifact

This repository is the anonymous artifact package for the ICSE submission
"When Tests Mislead Repair: Trace-Guided Adjudication for Self-Testing LLM Code
Generation".

The package contains:

- `src/tracealign/`: TraceAlign implementation and dataset-specific runners.
- `data/human_audit/`: reduced public audit data. It preserves labels,
  material-risk flags, final consensus labels, aggregate metrics, and two short
  illustrative rationale excerpts, but excludes full case text, code, traces,
  hidden keys, and complete annotator rationales.
- `results/tables/`: CSV versions of the paper tables and ablation summaries.
- `scripts/`: reproducibility checks for the derived RQ2 and RQ3 statistics.
- `docs/`: provenance, anonymization, and artifact evaluation notes.

## Quick Checks

From the repository root:

```bash
python3 scripts/verify_rq2_summary.py
python3 scripts/verify_human_audit_metrics.py
python3 scripts/check_anonymity.py
```

These checks recompute the derived RQ2 win/top-two/gain summary and the RQ3
human-audit statistics from the reduced CSV files included in this artifact.

## Running TraceAlign

Create an environment and install dependencies:

```bash
cd src/tracealign
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp config/api.env.example config/api.env
```

Fill `config/api.env` with an OpenAI-compatible endpoint and run, for example:

```bash
bash run.sh --dataset humaneval_plus --model gemini_2_5_flash --start-index 0 --end-index 10
```

Full benchmark reruns require external API credentials and the public benchmark
datasets described in `src/tracealign/docs/DATASETS.md`.

## Scope

This artifact is intentionally conservative. It includes implementation code,
processed aggregate evidence, reduced audit labels, and table summaries used in
the paper, while excluding full manual rationales, raw case materials, local
caches, personal paths, temporary logs, cookies, raw large benchmark shards, and
private credentials.
