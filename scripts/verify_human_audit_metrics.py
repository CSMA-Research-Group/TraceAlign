#!/usr/bin/env python3
"""Verify human-audit metrics from the material-quality precheck CSV."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "data" / "human_audit" / "human_audit_material_quality_precheck.csv"
TABLE4 = ROOT / "results" / "tables" / "table4_human_audit_summary.csv"
TABLE5 = ROOT / "results" / "tables" / "table5_material_risk_indicators.csv"

LABELS = ["code_defect", "faulty_test", "unclear"]
FLAG_TO_DISPLAY = {
    "reconstructed_code_with_missing_or_mismatched_trace": "Reconstructed code w/ trace mismatch",
    "no_diagnostic_trace": "No diagnostic trace",
    "blank_trace": "Empty trace",
    "locator_trace_mismatch": "Locator--trace mismatch",
    "interface_or_function_name_mismatch": "Interface/function-name mismatch",
    "testgen_or_tracer_timeout": "Test-generation/tracing timeout",
}
TOL = 0.001


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def kappa(rows: list[dict[str, str]]) -> tuple[int, float, float]:
    n = len(rows)
    agreement_count = sum(
        row["annotator_a_label"] == row["annotator_b_label"] for row in rows
    )
    observed = agreement_count / n
    a_counts = Counter(row["annotator_a_label"] for row in rows)
    b_counts = Counter(row["annotator_b_label"] for row in rows)
    expected = sum(a_counts[label] * b_counts[label] for label in LABELS) / (n * n)
    return agreement_count, observed, (observed - expected) / (1 - expected)


def summarize(rows: list[dict[str, str]]) -> dict[str, float | int]:
    agreement_count, agreement, score = kappa(rows)
    labels = Counter(row["final_consensus_label"] for row in rows)
    return {
        "n": len(rows),
        "agreement_count": agreement_count,
        "agreement_percent": round(agreement * 100, 1),
        "kappa": round(score, 3),
        "faulty_test": labels["faulty_test"],
        "code_defect": labels["code_defect"],
        "unclear": labels["unclear"],
    }


def assert_close(name: str, actual: float, expected: float, tol: float = TOL) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{name}: expected {expected}, got {actual}")


def verify_table4(rows: list[dict[str, str]]) -> None:
    summaries = {
        "All sampled cases": summarize(rows),
        "Material-risk cases": summarize(
            [row for row in rows if row["material_precheck_status"] == "flagged_material_risk"]
        ),
        "Clean-candidate cases": summarize(
            [row for row in rows if row["material_precheck_status"] == "clean_candidate"]
        ),
    }
    expected_rows = read_rows(TABLE4)
    for expected in expected_rows:
        name = expected["case_set"]
        actual = summaries[name]
        for field in ["n", "faulty_test", "code_defect", "unclear"]:
            if int(actual[field]) != int(expected[field]):
                raise AssertionError(f"{name} {field}: expected {expected[field]}, got {actual[field]}")
        assert_close(f"{name} agreement", float(actual["agreement_percent"]), float(expected["agreement_percent"]))
        assert_close(f"{name} kappa", float(actual["kappa"]), float(expected["kappa"]))


def verify_table5(rows: list[dict[str, str]]) -> None:
    expected_rows = read_rows(TABLE5)
    computed: dict[str, Counter[str]] = {}
    for flag, display in FLAG_TO_DISPLAY.items():
        selected = [
            row for row in rows if flag in [item for item in row["risk_flags"].split(";") if item]
        ]
        counts = Counter(row["final_consensus_label"] for row in selected)
        counts["n"] = len(selected)
        computed[display] = counts

    for expected in expected_rows:
        name = expected["risk_indicator"]
        actual = computed[name]
        checks = {
            "n": "n",
            "faulty_test": "faulty_test",
            "code_defect": "code_defect",
            "unclear": "unclear",
        }
        for actual_key, expected_key in checks.items():
            if int(actual[actual_key]) != int(expected[expected_key]):
                raise AssertionError(
                    f"{name} {expected_key}: expected {expected[expected_key]}, got {actual[actual_key]}"
                )

    all_flags = Counter()
    for row in rows:
        for flag in [item for item in row["risk_flags"].split(";") if item]:
            all_flags[flag] += 1

    print("All material-risk flags present in the CSV:")
    for flag, count in sorted(all_flags.items()):
        print(f"- {flag}: {count}")


def main() -> int:
    rows = read_rows(AUDIT)
    verify_table4(rows)
    verify_table5(rows)

    all_summary = summarize(rows)
    clean_summary = summarize(
        [row for row in rows if row["material_precheck_status"] == "clean_candidate"]
    )

    print("Human audit metrics verified")
    print(
        f"- all cases: n={all_summary['n']}, "
        f"agreement={all_summary['agreement_percent']}%, kappa={all_summary['kappa']:.3f}"
    )
    print(
        f"- clean-candidate cases: n={clean_summary['n']}, "
        f"agreement={clean_summary['agreement_percent']}%, "
        f"kappa={clean_summary['kappa']:.3f}, "
        f"faulty_test={clean_summary['faulty_test']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
