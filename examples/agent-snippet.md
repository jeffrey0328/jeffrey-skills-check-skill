# Snippet: how to word a skill's Workflow and Norms (adapt as needed)

Layout of a skill folder: `examples/three-layer-layout.md`. This file only shows the wording.

## Workflow (example)

1. Read user-provided `src/…` and `docs/…`; on large trees use scoped Glob / Grep / Read (`jeffrey-agent-workflow-skill/references/repo-exploration.md`).
2. Search the repo for key symbols; confirm signatures and call sites.
3. Write steps only from files you read; list questions if missing.

## Norms (example)

- **Must**: Commands, paths, and type names match the repo; explore before writing; scoped Glob/Grep/Read on large trees; repeatable helpers → static under the skill + document when (`jeffrey-agent-check-skill/references/skill-authoring.md` § Prefer static).
- **Must not** (a carve-out of a Must above whose range is too broad, so part of it needs excluding): Invent behavior; web search for repo facts unless allowed; whole-tree recursive scans when scoped tools suffice; reinvent the same skill helper as chat-only dynamic code every session.
- **Affirmative first**: state the positive; add a negative only when the positive's range is too broad and part of it must be excluded. A negative with no positive containing it → rewrite as Must only (`jeffrey-agent-check-skill/references/skill-authoring.md` § Positive / negative norms).
