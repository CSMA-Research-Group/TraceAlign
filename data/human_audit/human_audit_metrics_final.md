# Human Audit Final Metrics
Final metrics after resolving all annotation disagreements. Arbiter-vs-human metrics are reported primarily on the binary subset after excluding human-consensus `unclear` cases.

## Independent Annotation Quality
- Cases: 80
- Exact agreement before discussion: 55/80 = 0.688
- Cohen's kappa before discussion, three labels: 0.270
- Disagreements resolved by discussion: 25

Label counts before discussion:
| Label | Annotator A | Annotator B |
|---|---:|---:|
| `code_defect` | 15 | 18 |
| `faulty_test` | 60 | 56 |
| `unclear` | 5 | 6 |

Confusion matrix before discussion, rows = Annotator A, columns = Annotator B:
| A \ B | code_defect | faulty_test | unclear |
|---|---:|---:|---:|
| `code_defect` | 8 | 6 | 1 |
| `faulty_test` | 8 | 47 | 5 |
| `unclear` | 2 | 3 | 0 |

## Final Consensus Labels
| Label | Count |
|---|---:|
| `code_defect` | 14 |
| `faulty_test` | 62 |
| `unclear` | 4 |

Resolved by post-annotation discussion: 25.

## Arbiter vs. Human Consensus \(Binary, Excluding `unclear`\)
- Evaluated cases: 76
- Excluded `unclear` cases: 4
- Accuracy: 0.618
- Macro-F1: 0.572

Confusion matrix, rows = human consensus, columns = Arbiter:
| Human \ Arbiter | code_defect | faulty_test |
|---|---:|---:|
| `code_defect` | 11 | 3 |
| `faulty_test` | 26 | 36 |

Per-class metrics:
| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| `code_defect` | 0.297 | 0.786 | 0.431 | 14 |
| `faulty_test` | 0.923 | 0.581 | 0.713 | 62 |

## Diagnostic Three-Way View
The Arbiter does not produce an `unclear` label in this audit key, so the binary view above is the primary result. For completeness, if `unclear` consensus cases are counted as unpredicted by the Arbiter, the three-way diagnostic metrics are:
- Accuracy: 0.588
- Macro-F1: 0.371
