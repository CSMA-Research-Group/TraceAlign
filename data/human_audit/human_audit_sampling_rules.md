# Human Audit Sampling Rules

Note: this protocol describes how the internal audit sample was constructed.
The public artifact intentionally excludes full annotator-facing cases, hidden
keys, raw event text, code, traces, and complete rationales. It preserves only
reduced labels, risk flags, aggregate metrics, and two short illustrative
rationale excerpts.

Goal: validate whether TraceAlign's Arbiter decisions agree with independent
human judgment on a small but credible sample of APPS decision events.

## Scope

- Dataset: APPS only.
- Target sample size: 50 to 80 Arbiter decision events.
- Annotators: two independent annotators with Python/programming experience.
- Labels: `code_defect`, `faulty_test`, `unclear`.
- Primary metrics:
  - Inter-annotator Cohen's kappa on the three-way labels.
  - Arbiter vs. human-consensus accuracy, macro-F1, and per-class precision/recall/F1.

## Sampling Frame

Use only decision events where all of the following are available:

- Problem statement or APPS task id.
- Candidate code.
- Generated test or generated test failure.
- Observed output/failure and, when available, trace excerpt.
- Original Arbiter/system decision stored in a separate key file.

Exclude events with:

- API key errors, connection errors, or incomplete LLM responses.
- Missing generated test or missing candidate code.
- Tracebacks caused by the experiment harness rather than the candidate program.
- Duplicate near-identical events from the same task and same generated test.

Preferred source logs:

1. `TraceAlign/test/phase1_generation_Apps2.log`
2. `TraceAlign/test/analysis_Apps2.log`
3. `TraceAlign/test/analysis_Apps3.log`, only when event provenance is reconstructable

Avoid for the main audit sample:

- `TraceAlign/test/analysis_Apps.log`, because it contains many API/traceback markers.
- `TraceAlign/test/phase1_generation_Apps2_2.log`, because it has too few events.
- BigCodeBench, HumanEval, ClassEval, and LiveCodeBench logs, because the audit target for the ICSE revision should stay focused and APPS-centered.

## Stratification

Create a balanced sample from the hidden Arbiter/system decision key:

- 30 to 35 events originally labeled/actioned as code-side failures (`FIX_CODE`, code defect, or equivalent).
- 30 to 35 events originally labeled/actioned as test-side failures (`DISCARD_TEST`, `REMOVE_TEST`, faulty test, test hallucination, or equivalent).
- 5 to 10 hard/ambiguous events if available, such as boundary conditions, unclear specs, or long traces.

If the available test-side events are fewer than required, include all valid
test-side events and fill the remainder with randomly sampled code-side events.

Deduplication rules:

- At most two events per APPS task.
- Prefer events from different repair iterations and different generated tests.
- If multiple logs contain the same task/event, keep the clearest one with the most complete trace and source locator.

## Blinding

Annotators must receive only the blinded CSV based on
`human_audit_template.csv`.

Do not include these fields in the annotator-facing file:

- Original Arbiter decision.
- Original Arbiter reasoning.
- System action (`FIX_CODE`, `REMOVE_TEST`, `DISCARD_TEST`).
- LLM-generated `INSUFFICIENT_COVERAGE` or `INEFFECTIVE_REPAIR` root-cause label.

Keep a separate key file with:

```csv
case_id,source_log,source_event_locator,task_id,arbiter_decision,arbiter_reasoning,system_action,original_root_cause_label
```

Randomize case order before sending files to annotators.

## Label Definitions

`code_defect`:
The generated test is consistent with the problem statement and visible samples,
and the candidate code appears to violate the intended behavior.

`faulty_test`:
The candidate behavior is consistent with the problem statement and visible
samples, or the generated test's expected output/assumption is unsupported by
or contradicts the specification.

`unclear`:
The available evidence is insufficient, the specification is ambiguous, both
code and test appear questionable, or the trace/log is not enough to assign
responsibility confidently.

## Annotation Protocol

1. Each annotator independently labels every case.
2. Annotators record confidence on a 1-5 scale.
3. Annotators write a short rationale, especially for `faulty_test` and `unclear`.
4. Compute Cohen's kappa before any discussion.
5. Resolve disagreements through discussion and produce a consensus label.
6. Compare Arbiter decisions against consensus labels.

Recommended reporting:

- Report three-way kappa including `unclear`.
- Also report a binary analysis after excluding `unclear`, if enough cases remain.
- Report label distribution so reviewers can see whether the sample is balanced.

## Paper Wording Guardrails

Safe wording:

- "We conduct a small-scale double-annotator audit of Arbiter decisions."
- "The audit evaluates agreement with human consensus labels."
- "The log-derived table describes system behavior, not decision correctness."

Avoid:

- "The log analysis proves the Arbiter is correct."
- "The LLM-generated root-cause labels are gold labels."
- "The human audit establishes definitive correctness for all decisions."

## Internal Deliverables

- annotator-facing cases with full context.
- hidden original decisions and provenance.
- `human_audit_annotations_annotator_a.csv`.
- `human_audit_annotations_annotator_b.csv`.
- `human_audit_consensus.csv`.
- `human_audit_metrics.md` or `.json`: kappa, agreement, precision/recall/F1.

The public artifact provides reduced versions of these materials rather than
the full internal case files.
