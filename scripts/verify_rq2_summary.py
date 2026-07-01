#!/usr/bin/env python3
"""Verify RQ2 summary statistics from the Pass@1 table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TABLE1 = ROOT / "results" / "tables" / "table1_pass_at1.csv"
TABLE3 = ROOT / "results" / "tables" / "table3_gain_summary.csv"

BENCHMARKS = ["HumanEval_plus", "MBPP_plus", "APPS", "LiveCodeBench"]
OURS = "TraceAlign"
EXPECTED_WINS = 8
EXPECTED_TOP_TWO_INCL_TIES = 12
EXPECTED_APPS_GAIN = 7.56
TOL = 0.01


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def assert_close(name: str, actual: float, expected: float, tol: float = TOL) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{name}: expected {expected}, got {actual}")


def main() -> int:
    rows = read_rows(TABLE1)
    expected_gains = {
        row["model"]: {bench: float(row[bench]) for bench in BENCHMARKS}
        for row in read_rows(TABLE3)
    }

    models = list(dict.fromkeys(row["model"] for row in rows))
    gains: dict[tuple[str, str], float] = {}
    wins = 0
    top_two_incl_ties = 0

    for model in models:
        model_rows = [row for row in rows if row["model"] == model]
        by_method = {row["method"]: row for row in model_rows}
        if OURS not in by_method:
            raise AssertionError(f"missing {OURS} row for {model}")

        for bench in BENCHMARKS:
            ours_score = float(by_method[OURS][bench])
            all_scores = {method: float(row[bench]) for method, row in by_method.items()}
            non_ours_best = max(score for method, score in all_scores.items() if method != OURS)
            gain = round(ours_score - non_ours_best, 2)
            gains[(model, bench)] = gain
            assert_close(f"gain {model} {bench}", gain, expected_gains[model][bench])

            best_score = max(all_scores.values())
            if abs(ours_score - best_score) <= TOL:
                wins += 1

            unique_scores = sorted(set(all_scores.values()), reverse=True)
            second_threshold = unique_scores[1] if len(unique_scores) > 1 else unique_scores[0]
            if ours_score + TOL >= second_threshold:
                top_two_incl_ties += 1

    apps_gain = round(sum(gains[(model, "APPS")] for model in models) / len(models), 2)

    if wins != EXPECTED_WINS:
        raise AssertionError(f"wins: expected {EXPECTED_WINS}, got {wins}")
    if top_two_incl_ties != EXPECTED_TOP_TWO_INCL_TIES:
        raise AssertionError(
            "top-two incl. ties: "
            f"expected {EXPECTED_TOP_TWO_INCL_TIES}, got {top_two_incl_ties}"
        )
    assert_close("average APPS gain", apps_gain, EXPECTED_APPS_GAIN)

    print("RQ2 summary verified")
    print(f"- wins: {wins}/12")
    print(f"- top-two finishes incl. ties: {top_two_incl_ties}/12")
    print(f"- average APPS gain: +{apps_gain:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
