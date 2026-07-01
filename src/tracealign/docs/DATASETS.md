# Dataset Notes

This anonymous artifact contains the TraceAlign evaluation adapters and processed
audit data. It does not bundle full benchmark datasets or hidden/private tests.
Full benchmark reruns require obtaining the public benchmark distributions and
placing them in the paths below.

## APPS

- File: `datasets/APPS/data/selected150.jsonl`
- Evaluator: `datasets/APPS/test_one_solution.py`

## HumanEval+

- File: `datasets/human_eval_plus/data/test-00000-of-00001-5973903632b82d40.parquet`
- Evaluator: `datasets/human_eval_plus/execution.py`

## MBPP+

- File: `datasets/MBPP/Plus/test-00000-of-00001-d5781c9c51e02795.parquet`
- Evaluator: `datasets/MBPP/execution.py`

## LiveCodeBench

- Files: `datasets/LiveCodeBench/data/test6.jsonl` or `datasets/LiveCodeBench/data/test6.part*.jsonl`
- Evaluator: `datasets/LiveCodeBench/single_eval.py`
- Supporting runtime: the official LiveCodeBench runner package
- Loader behavior: `runners/livecodebench.py` automatically reads the single-file layout (`test6.jsonl`) or the sharded layout (`test6.part*.jsonl`)

No cached downloads, `.git` history, raw logs, private keys, or generated run
outputs are included in this anonymous release.
