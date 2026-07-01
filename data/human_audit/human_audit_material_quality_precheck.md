# Human Audit Material-Quality Precheck

This file summarizes the material-quality precheck used for the exploratory
APPS human audit. The public CSV keeps only case identifiers, risk flags,
independent labels, final consensus labels, and Arbiter decisions. Full case
materials and complete annotator rationales are not included in this artifact.

## Summary

- Total audit cases: 80.
- Flagged for material-risk review: 44.
- Clean-candidate cases after the precheck: 36.
- Final consensus labels in flagged cases: 35 faulty tests, 7 code defects, 2 unclear.
- Final consensus labels in clean-candidate cases: 27 faulty tests, 7 code defects, 2 unclear.

## Agreement

- All cases: 55/80 independent exact agreement, Cohen's kappa = 0.270.
- Material-risk cases: 27/44 independent exact agreement, Cohen's kappa = 0.012.
- Clean-candidate cases: 28/36 independent exact agreement, Cohen's kappa = 0.524.

## Risk Flags

- `reconstructed_code_with_missing_or_mismatched_trace`: 23 cases.
- `no_diagnostic_trace`: 13 cases.
- `blank_trace`: 11 cases.
- `locator_trace_mismatch`: 10 cases.
- `non_test_locator`: 7 cases.
- `interface_or_function_name_mismatch`: 7 cases.
- `testgen_or_tracer_timeout`: 5 cases.
- `test_runner_failed_input`: 1 case.
- `undefined_input_domain`: 1 case.

The paper reports the six main risk indicators in its material-risk table. The
verification script prints the full flag distribution from the reduced CSV.
