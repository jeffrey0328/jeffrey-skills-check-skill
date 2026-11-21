# Rule norms & checks

Rules (user-level `AGENTS.md` in the agent config home, project `.mdc`, global commands) are created and maintained per the current agent app’s rule spec plus `preferences.md`. Canonical decision and format rules live in `jeffrey-agent-workflow-skill/references/rule-vs-skill.md` and `project-rules.md`; placement of agent-only content is canonical in § Which home below. This file routes there and adds the check standard.

**读法:** § Which home for placement; § Check list for the gate.

## Which home

Triage before creating (Rule vs Skill, wait for Jeffrey’s confirmation) follows `jeffrey-agent-workflow-skill/references/rule-vs-skill.md` § Decision criteria. Placement of agent-only content is canonical here:

| Content | Home |
| --- | --- |
| Rule, script, command or hook for one agent app, outside any skill | That app’s own config repo (one repo per agent app, no branches), in its global config directory, not in a project |
| Agent-only part of a skill that several agent apps share | A per-agent branch of that skill’s own repo (`agent/<agent>`), as one `<agent>-spec.md` in the skill folder root — `skill-authoring.md` § Agent-specific spec file |
| Skill for one agent app only | That app’s skills parent repo |
| What every agent app reads | The shared parts: skill on the default branch, plugin, `AGENTS.md` |

A shared skill mentions an agent-specific procedure only generically (“the current agent app’s procedure”) and points to where it lives.

## Check list (full)

| Check | Pass |
|-------|------|
| Placement | Content sits in the home § Which home assigns; agent-only content is on the `agent/<agent>` branch, not in shared files |
| Format | `.mdc` frontmatter and structure per `project-rules.md` § 3; user `AGENTS.md` sections current |
| Writing norms | Positive/negative pairing per `skill-authoring.md` § Positive / negative norms; partial-read friendly (sectioned, 读法 table when long) |
| Pointers | Every skill/file pointer resolves; no leftover path to a renamed skill directory |
| Machine-local values | None in committed rules; such values live in git-ignored `local.md` with a committed `local.example.md` |
| No secrets | No tokens, passwords, `mcp.json` / auth files committed; MCP travels as sanitized examples |
| Freshness | A rule naming a file, function, or flag is verified against current state before it is relied on |

Quick check (before use): pointers resolve, no machine-local values, the rule’s claims still match current files.

## Must

- Run the Rule-vs-Skill triage and wait for Jeffrey’s confirmation before creating either.
- Keep agent-only rule content on the owning skill’s `agent/<agent>` branch in `<agent>-spec.md`.
- Verify a rule’s factual claims against current state before applying it.

## Must not

- Create a Rule or Skill before Jeffrey confirms the triage. *(← Must: triage + confirmation first)*
- Write agent-only content into shared rule files to make one app work. *(← Must: agent-only content on agent/<agent> branches)*