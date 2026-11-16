# Snippet template: agent-facing Markdown (adapt as needed)

## Description and index (example)

- **Skill root**: `my-skill/`
- **Layer 1 Index**: `my-skill/SKILL.md` (English; **required** routing-only — `/` and `@` paste the whole file; see `jeffrey-skills-check-skill/references/skill-authoring.md` § Thin hub / slash-attach budget + § Three layers)
- **Layer 2 Content**: `my-skill/references/*.md` (read on demand; Must/Must-not, DoD, indexes, long steps)
- **Layer 3 Cases**: `my-skill/examples/…` (worked example or `case-index.md`)
- **README**: `my-skill/README.md` (English) + `my-skill/README.zh.md` (Chinese); mutual links; order 简介 → 安装 → 内容 → 其他; Install = one agent prompt (git URL + steps)
- **Review**: `review-intro.md` / `review-body.md` / `review-usage.md` (Chinese Feishu pages)
- **Usage (human Review)**: `my-skill/review-usage.md` (chat input / 子指令; auto-invoke section only if enabled)
- **Tag**: `my-skill/tag.txt` (one line; propose then confirm)
- **Review flags**: every skill `SKILL.md` has `/skill-review`; overview is `/skill-review` alone; Feishu Review page shows the overview command **only** on `jeffrey-skills-check-skill` (`jeffrey-skills-check-skill/references/skill-authoring.md` § Review flags)
- **Auto-invoke**: ask mode — 仅手动 / 条件自动 / 常驻默认 (`jeffrey-skills-check-skill/references/skill-authoring.md`)

## Workflow (example)

1. Read user-provided `src/…` and `docs/…`; on large trees use scoped Glob / Grep / Read (`jeffrey-agent-workflow-skill/references/repo-exploration.md`).
2. **Creating a skill folder**: add **`README.md`** and **`README.zh.md`** (`jeffrey-skills-check-skill/references/skill-authoring.md`).
3. Search the repo for key symbols; confirm signatures and call sites.
4. Write steps only from files you read; list questions if missing.

## Norms (example)

- **Must**: Commands, paths, and type names match the repo; explore before writing; scoped Glob/Grep/Read on large trees; repeatable helpers → static under the skill + document when (`jeffrey-skills-check-skill/references/skill-authoring.md` § Prefer static).
- **Must not** (a carve-out of a Must above whose range is too broad, so part of it needs excluding): Invent behavior; web search for repo facts unless allowed; whole-tree recursive scans when scoped tools suffice; reinvent the same skill helper as chat-only dynamic code every session.
- **Affirmative first**: state the positive; add a negative only when the positive's range is too broad and part of it must be excluded. A negative with no positive containing it → rewrite as Must only (`jeffrey-skills-check-skill/references/skill-authoring.md` § Positive / negative norms).
