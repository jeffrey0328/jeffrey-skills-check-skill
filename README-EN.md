# jeffrey-agent-check-skill

[中文](README.md)

Norms and mandatory checks for all agent-related content — skills, plugins, projects, rules, and memory. Everything is created and maintained to two standards: the current agent app’s own spec for that content type, plus Jeffrey’s standing preferences. A check runs before any covered content is used or updated; results are reported in the conversation (there is no Review page).

## Install

Install through the current agent. Paste the fenced block to that agent.

```
Install the skill "jeffrey-agent-check-skill" into the agent app you are currently running in.
Repo: https://github.com/jeffrey0328/jeffrey-agent-check-skill.git
Steps:
1. First read and follow this agent app's current skill spec (install directory, frontmatter, how skills are attached, project pointers, human-page requirements). Do not edit files until that spec is read. Do not apply another agent product's paths or fields from memory.
2. Following that spec, clone this repo into this agent app's default skills path, using the folder name "jeffrey-agent-check-skill".
3. Then change only the parts of this skill that must bind to the current agent, following that spec. Do not read through the process prose in references/ or examples/.
```

## Features

- Covers five domains: skills, plugins, projects (governance files), rules, and memory — each with its own norms and check list, all measured against the current agent app’s spec plus Jeffrey’s preferences.
- Mandatory gate: a quick check before covered content is used, a full check before it is created or updated. Must-fix findings are fixed before proceeding; preference-level findings are listed for Jeffrey’s decision.
- Scriptable checks run through a fixed check script (structure, id, pointers, machine-local values, file language, README pair shape) instead of throwaway code each run; newly discovered repeatable checks are added to the script.
- `/agent-check` checks all five domains and reports in chat; it can be narrowed to one domain or one specific item.
- Keeps every skill in the same shape: thin routing hub, three layers, bilingual README pair (`README.md` Chinese default + `README-EN.md` English), spoken names (叫法) from Jeffrey, one `jeffrey-<function>-skill` id for folder / name / repo, and old-name cleanup after a rename.
- Agent-specific settings keep their own branch: what only one agent app needs lives on its `agent/<agent>` branch in `<agent>-spec.md`, never in the shared default branch; every skill update runs this conformance split.
- Records Jeffrey’s standing preferences in one page; a newly stated preference is written in place and existing content is checked for contradictions.
- Resident sync: when any other skill is created or updated in the same turn, its companions are checked and aligned before the turn ends.

## How to use

**Resident** — the agent attaches this skill on its own, in every conversation; you do not have to `@` it. It fires whenever covered content is about to be used or updated, and whenever you ask for a check. You can still say `/jeffrey-agent-check-skill` or `@jeffrey-agent-check-skill`.

| You say | What happens |
|---------|--------------|
| `/agent-check` | Checks skills, plugins, projects, rules, and memory; reports per domain in chat |
| `/agent-check skill` (or `plugin` / `project` / `rule` / `memory`) | Checks that one domain only |
| `/agent-check <name-or-path>` | Checks one specific skill, plugin, project, rule file, or memory scope |
| “create a skill that …” / “update this skill” | The agent reads the authoring spec, runs the update-time check, writes to the shared form, and syncs the READMEs |
| “check whether this plugin follows the spec” | The plugin norms check runs and reports |
| “from now on I prefer …” | The preference is recorded in place; contradicting content is listed |

## Common changes

Say one of these to the agent; it finds and edits the right file itself.

| What to change | Say to the agent |
|----------------|------------------|
| The skill-authoring norms (how any skill must be written) | “Change the skill-authoring norms: `<new requirement>`, and roll it out to every skill” |
| A domain’s checking standards (plugin / project / rule / memory) | “Add a check to the `<domain>` norms: `<rule>`, and treat it as must-fix” |
| When and how deep the gate checks | “Before use, also check `<item>`” / “Make the quick check cover `<item>`” |
| What the fixed check script covers | “Add `<check>` to the check script” — new checks go into the script, not chat-only code |
| A standing preference | “From now on I prefer `<preference>`” — recorded in the preferences page, contradictions reported |
| Which content types are covered | “Also cover `<content type>` in the check” |
| A shared convention across all skills (companion files, hub shape) | “`<new convention>` — apply it to every skill, not just this one” |