# Human Audit Annotator Instructions

Note: this protocol documents the internal annotation procedure. The public
artifact does not include the full annotator-facing case file, hidden key file,
complete case text, code, traces, or complete annotator rationales. It includes
only reduced labels, aggregate metrics, and two short illustrative rationale
excerpts.

You will label APPS cases from TraceAlign's repair loop. Each row contains a
problem statement, sample I/O, candidate code, a generated test, observed
failure information, and when available a trace/diagnostic excerpt.

The internal hidden key contains the system decision and is used only after both
annotators finish independent labeling. It is not part of the public artifact.

## Labels

Use exactly one of the following labels in `annotator_label`:

- `code_defect`
- `faulty_test`
- `unclear`

### `code_defect`

Choose this label when the generated test appears consistent with the problem
statement and visible samples, and the candidate code appears to violate the
intended behavior.

### `faulty_test`

Choose this label when the candidate behavior appears consistent with the
problem statement and visible samples, or when the generated test's expected
output or input assumption is unsupported by or contradicts the specification.

### `unclear`

Choose this label when the evidence is insufficient, the specification is
ambiguous, both code and test appear questionable, or the log/trace does not
provide enough information to assign responsibility confidently.

## Confidence

Use `annotator_confidence` from 1 to 5:

- 1: very uncertain
- 2: weak judgment
- 3: moderate confidence
- 4: high confidence
- 5: very high confidence

## Rationale

Write one or two concise sentences in `annotator_rationale`.

Mention the key evidence you used, such as:

- a requirement sentence from the problem statement;
- a sample I/O example;
- the generated test's expected output;
- the candidate code behavior;
- the observed failure or trace excerpt.

## Discussion Flag

Set `needs_discussion` to `yes` if:

- you choose `unclear`;
- your confidence is 1 or 2;
- the generated test and code both seem wrong;
- the case depends on an ambiguous interpretation of the problem statement;
- the trace excerpt is missing and the remaining evidence is not enough.

Otherwise set it to `no`.

## Known Log Limitations

Some rows have no recoverable trace excerpt because the original logs were
free-form text rather than structured JSONL. In those cases, label from the
problem statement, generated test, observed failure, and candidate code. If
that evidence is not enough, choose `unclear`.

Some code or generated-test fields may include `[TRUNCATED]` when the original
text was very long. If truncation prevents a confident judgment, choose
`unclear` and set `needs_discussion` to `yes`.
