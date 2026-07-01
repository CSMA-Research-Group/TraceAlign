# Anonymization Notes

The artifact was prepared as an anonymous review package.

Removed or excluded:

- personal absolute paths and machine-specific working directories;
- API keys, endpoint credentials, cookies, and `.env` files;
- local caches, bytecode, coverage outputs, raw temporary logs, and editor files;
- duplicate annotation drafts and preliminary metric files not used by the paper;
- large benchmark shards that should be obtained from the public benchmark sources.
- full human-audit case text, candidate code, generated tests, trace excerpts,
  hidden key files, raw event text, and complete annotator rationales.

Preserved:

- source code required to inspect TraceAlign's implementation;
- final human-audit CSV/JSON/Markdown files used for RQ3;
- reduced per-case audit labels and material-risk flags sufficient to recompute
  the reported aggregate metrics;
- two short illustrative rationale excerpts;
- CSV versions of the paper's reported tables;
- scripts that recompute derived summary statistics from the included files.

The anonymization process does not alter reported experimental values or human
annotation labels.
