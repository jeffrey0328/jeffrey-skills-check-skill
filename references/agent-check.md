# Agent content check — the mandatory gate

Every covered content type is created and maintained to **two standards**: the **current agent app’s own spec** for that type, and **Jeffrey’s preferences** (`preferences.md`). This file is the check that runs before content is used or updated. There is no Review page; checks run in the conversation and report in chat.

**读法:** § When + § Depth on every gate; § Flow for the steps; § Domains to route one domain; § Cross-domain for fleet-wide sweeps; § Report for the reply shape.

## Covered content

| Domain | What is covered | Norms file |
|--------|-----------------|------------|
| **skill** | Every skill under the current agent app’s default skills path (project skills and system skills: structure check only, no rename/id rule) | `skill-authoring.md` |
| **plugin** | Installed plugins and any plugin being authored: manifests, bundled skills, MCP config, version pins, install records | `plugin-norms.md` |
| **project** | A project’s governance files: `AGENTS.md`, `.agents/`, agent adapter files, `README.md`, `DEVLOG.md`, skill pointers — not product code | `project-norms.md` |
| **rule** | User-level rules (`AGENTS.md` in the agent config home), project `.mdc` rules, global commands | `rule-norms.md` |
| **memory** | Auto-memory indexes and topic files, user scope and project scope | `memory-norms.md` |

## When (required)

- **Before use:** before relying on covered content in a task — loading a skill’s instructions, applying a rule, enabling/using a plugin, acting on a memory entry, working under a project’s `AGENTS.md` — run the **quick check** on that item. Content already checked this conversation with no change since needs no re-check.
- **Before update:** before creating or editing any covered content, run the **full check** on it first, then apply the norms file while writing.
- **On demand:** `/agent-check` (all domains), `/agent-check <domain>`, `/agent-check <name-or-path>` (one item).

## Depth

| Depth | When | What it covers |
|-------|------|----------------|
| **Quick** | before use | Structure present (required files/fields), id/name consistency, pointers resolve to existing files/skills, no machine-local values in committed content, bind points match the current agent app, file language matches the domain norms (skill: English except the README pair; project: Chinese `README.md`/`DEVLOG.md`, everything else English) |
| **Full** | before update; `/agent-check` | Everything in Quick + the domain norms file’s full checklist + `preferences.md` + (skills) the current app’s skill-spec conformance and the agent-specific split (`skill-authoring.md` § Agent-specific spec file) |

A check reads the current app’s spec for that content type first (the same spec the skill Install prompt reads). Never check against another app’s spec from memory.

## Flow

1. Resolve the target(s): one item, one domain, or all five. Skills root = the current agent app’s default personal-skills path; skip non-skill dirs (`logs`, `scripts`, `.git`, dot-names).
2. Read the matched norms file(s) — one per domain, partial-read by `##` when long. Read `preferences.md` once per full check.
3. Run the checks at the required depth. Verify claims against the files as they are now (a memory or a rule may be stale).
4. **Must-fix found:** fix it before proceeding with the use/update (rename leftovers, broken pointers, missing required files, machine-local values in committed content, id mismatch, file language against the norms). Fixes follow the norms files and the git workflow of `jeffrey-agent-workflow-skill`.
5. **Preference-level findings** (wording, structure taste): report them; fix in the same turn when the user asked for a check-and-fix, otherwise list them for his decision.
6. Report (§ Report). No page, no viewer.

## Domains

Route each domain to its norms file; the check items live there, not here:

- skill → `skill-authoring.md` (shape, companions, id, 叫法, language, agent-spec conformance)
- plugin → `plugin-norms.md`
- project → `project-norms.md`
- rule → `rule-norms.md`
- memory → `memory-norms.md`

## Cross-domain

Run these on `/agent-check` (all) and whenever a rename or move happened:

| Check | Pass |
|-------|------|
| **Renamed-skill leftovers** | No path in global skills, commands, or rules still points at a missing skill directory (`skills/<old-name>`, `<old-name>/SKILL.md`, `<old-name>/references/`) |
| **Pointer resolution** | Every skill/rule/memory-index pointer to another file resolves to an existing file |
| **Machine-local values** | Committed content carries no absolute paths, drive letters, usernames, host names, local ports/URLs, account ids, or tokens; such values live in git-ignored `local.md` with a committed `local.example.md` |
| **Preference drift** | Content that states a preference contradicts `preferences.md` → update the content or ask Jeffrey which wins |

## Report

Short Chinese summary in chat:

- Per domain: 通过 / 需修复 counts, then one line per finding (item + what is wrong + fixed-or-listed).
- Must-fix items already fixed: say what changed.
- Nothing found: one line per domain, no padding.

## Must

- Run the gate before using or updating covered content; quick before use, full before update.
- Read the current agent app’s spec for the content type before checking it.
- Fix must-fix findings before proceeding; report preference-level findings for Jeffrey’s decision.
- Verify against current file state, not against what a memory or an old rule claims.

## Must not

- Skip the gate because the content “worked last time”. *(← Must: run the gate before use/update)*
- Check against another agent app’s spec from memory. *(← Must: read the current app’s spec first)*
- Proceed with a use/update while a must-fix finding is open. *(← Must: fix must-fix before proceeding)*