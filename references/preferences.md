# Jeffrey’s standing preferences

The second half of the check standard (the first half is the current agent app’s spec). These are Jeffrey’s stated preferences that apply across agents and projects; a domain norms file plus this page is what a full check measures against. When a preference here conflicts with a project’s `AGENTS.md`, the project file wins inside that project — report the conflict.

**读法:** scan the section matching the domain being checked; § Adding a preference when Jeffrey states a new one.

## Naming & creation

- Global personal skills: folder, frontmatter `name`, and git repo name are one `jeffrey-<function>-skill` id. Propose the prefixed final name when Jeffrey gives one without it.
- Before creating any skill files: confirm the exact name, then ask whether to create a git repo and whether private or public. Never infer a default from silence or from a previous skill.
- Rule vs Skill: triage first, recommend with a one-sentence reason, wait for his confirmation before creating files (`jeffrey-agent-workflow-skill/references/rule-vs-skill.md`).

## Skill shape & language

- Agent-facing artifacts in English; a bilingual README pair (`README.md` English, `README.zh.md` Chinese) carrying the same facts, links both ways. Chinese belongs only in `README.zh.md`; conversation with Jeffrey is in Chinese.
- `SKILL.md` stays a thin routing hub; detail in English `references/`, user-facing explanation in the READMEs.
- 叫法: ask Jeffrey first; record only in that skill’s `description`.
- Rewrite policy per skill (`kind.txt`, one line): `演进` — the agent may improve it from observed use, with a documented update loop and the 更新标准 / 更新依据 / 更新条目 brief after each agent-driven update; `底本` — no spontaneous rewrite, updates only from Jeffrey’s direct command or a cited source change. This skill is `底本`.

## Working style

- Ask yes/no and small-choice questions on the question card with preset options; open-ended questions stay in conversation.
- One conversation does one thing (or a few related things); clearly unrelated input goes to a new chat.
- Edit the original in place — update the existing passage, or add at the fitting place; never append to the end by default.
- After every skill update, tell Jeffrey what changed and ask whether to push; commit and push only after he agrees. A push command he typed himself already counts as agreement.
- Decisions that are Jeffrey’s get asked before execution; execution makes no decisions (`jeffrey-agent-workflow-skill` § Workflow).

## Content hygiene

- Committed content carries no machine- or user-specific values (absolute paths, drive letters, usernames, hosts, local ports/URLs, account ids, tokens). Such values live in a git-ignored `local.md` beside a committed `local.example.md` with `<PLACEHOLDER>` keys.
- MCP config travels as sanitized `*.example.json` snippets only; never commit auth files or API keys.
- Plugins: only the sanitized lock inventory travels; install output and per-machine runtime state never get committed.

## Product & UI taste

- No helper captions or process-restating microcopy unless Jeffrey asks; follow `jeffrey-web-dev-skill` hub-norms for web UI.
- Projects keep a Chinese `README.md` (what the project is for) and a Chinese `DEVLOG.md` (current progress), updated on every project change.

## Adding a preference

When Jeffrey states a new standing preference: record it here at the fitting section (in place, not appended), in English, agent-agnostic wording; then check whether existing covered content contradicts it and report what needs updating. A preference stated for one project only goes to that project’s `AGENTS.md`, not here.