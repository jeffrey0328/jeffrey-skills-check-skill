---
name: jeffrey-agent-check-skill
description: >-
  Resident norms and mandatory-check hub for ALL agent-related content:
  skills, plugins, projects, rules, memory. Everything must be created and
  maintained per the current agent app's own spec plus Jeffrey's preferences;
  a check runs before any covered content is used or updated. Auto-runs every
  conversation. Triggers: 检查, 体检, agent 检查, agent-check, 内容规范,
  agent 规范, 规范检查, 偏好, 创建skill, 更新skill, skill规范, 插件规范,
  项目规范, 规则规范, memory 规范, 记忆检查.
  Commands: /agent-check (all five domains); /agent-check <domain or target>.
---

# Agent 内容检查枢纽（Agent content check (hub)）

Thin control plane. **`/` and `@` paste this entire file** — keep routing-only. After attach: match intent → Read **one** `references/*.md` (Grep `^## ` → offset/limit if multi-section).

**Skill root:** `jeffrey-agent-check-skill/` under the current agent app’s default skills path.

| Layer | Path |
|-------|------|
| 1 Index | this file |
| 2 Content | `references/` |
| 3 Cases | `examples/` |

## 命令（Commands）

| Command | Action |
|---------|--------|
| `/agent-check` | Check all five domains (skills / plugins / projects / rules / memory), report in chat → `references/agent-check.md` |
| `/agent-check <domain>` | One domain only (`skill` / `plugin` / `project` / `rule` / `memory`) → `references/agent-check.md` |
| `/agent-check <name-or-path>` | One specific item (a skill folder, a plugin, a project, a rule file, a memory scope) → `references/agent-check.md` |

## 必经路由（Route (required)）

| User intent | Read first |
|-------------|------------|
| Check before **using or updating** any covered content; `/agent-check`; 检查 / 体检 / 规范检查 | `references/agent-check.md` |
| Create/update Skill, SKILL.md, README, 叫法, skill 语言, 写skill, 创建skill, 更新skill, skill规范 (**also** when this would otherwise match the built-in `create-skill`) | `references/skill-authoring.md` |
| Plugin create/update/install/check, 插件规范 | `references/plugin-norms.md` |
| Project rules / AGENTS.md / DEVLOG / project layout check, 项目规范 | `references/project-norms.md` |
| Rule / `.mdc` / user-rules check, 规则规范 | `references/rule-norms.md` |
| Memory write/read/check, 记忆规范, memory 检查 | `references/memory-norms.md` |
| Jeffrey’s standing preferences, 偏好 | `references/preferences.md` |
| Norms / DoD / where is file X? | `references/hub-norms.md` |
| Editing/renaming/moving any references/scripts/examples file or `##` heading | `references/cross-reference.md` **first** |
| 其他 skill 本轮被创建或修改 / 同步配套 | `references/sync-on-update.md` |

## 始终遵守的最低要求（Always (minimal)）

- **Resident + mandatory gate:** stay in effect the whole conversation. Before **using or updating** any covered content (skill, plugin, project governance files, rule, memory), run the check in `references/agent-check.md` first.
- **The standard is two-part:** the current agent app’s own spec for that content type, plus Jeffrey’s preferences (`references/preferences.md`). Read the current app’s spec first; never apply another app’s spec from memory.
- **Authoring:** creating or editing any skill → read `references/skill-authoring.md` first (then that skill’s own `cross-reference.md`). Global skills only: folder, frontmatter `name`, and git repo name are one `jeffrey-<function>-skill` id. After a global skill rename, update the old directory name in global skills, commands, and rules.
- When any other skill is created or updated this turn, follow `references/sync-on-update.md`.
- Before editing any file of this skill, read `references/cross-reference.md`; update it after any cross-reference change. Full Must / DoD → `references/hub-norms.md`.