# Hub norms & file index

**读法:** § File index when locating assets; § Must / Must not when unsure; § Definition of Done before closing a create/update.

| Need | Section |
|------|---------|
| Where is X? | § File index |
| Standing rules | § Must / § Must not |
| Finish checklist | § Definition of Done |
| Who references a file before I edit it? | `references/cross-reference.md` |

## File index

| Path | Audience | When to read |
|------|----------|--------------|
| `SKILL.md` | Agent | Thin hub; pasted on `/` or `@` |
| `README.md` | Human | Chinese README（默认人类页）：简介 → `## 安装`（中文 Agent 提示词：仓库 + 步骤）→ 功能介绍 → 怎么用 → 常见改动；链到 `README-EN.md` |
| `README-EN.md` | Human | English README：简介 → `## Install`（英文 Agent 提示词：仓库 + Steps）→ `## Features` → `## How to use` → `## Common changes`；链到 `README.md` |
| `DEVLOG.md` | Human | 全中文更新日志：最新在前，每条 改了什么 / 为何 / 涉及 — `skill-authoring.md` § Update log |
| `references/hub-norms.md` | Agent | This file |
| `references/cross-reference.md` | Agent | 关联记录 |
| `references/agent-check.md` | Agent | The mandatory gate: when/depth/flow/report; `/agent-check` |
| `references/skill-authoring.md` | Agent | Create/update any Agent Skill (shape, layers, companions, id, agent-specific branches) |
| `references/plugin-norms.md` | Agent | Plugin structure, versions/pins, install records, checks |
| `references/project-norms.md` | Agent | Project governance files and checks |
| `references/rule-norms.md` | Agent | Rule placement, format, checks |
| `references/memory-norms.md` | Agent | Memory write/read norms and checks |
| `references/preferences.md` | Agent | Jeffrey’s standing preferences (second half of the standard) |
| `references/sync-on-update.md` | Agent | Sync after another skill is created/updated this turn |
| `scripts/run_agent_check.py` | Agent / local | Fixed gate check script: structure, id, pointers, machine-local values, file language, README pair, DEVLOG; quick/full depth — `agent-check.md` § Flow |
| `kind.txt` | Agent | This skill’s rewrite policy: one line `演进` or `底本` |
| `examples/three-layer-layout.md` | Both | Three-layer layout example |
| `examples/agent-snippet.md` | Agent | Wording example for a skill's Workflow and Norms |

**Human entry:** `README.md` + `README-EN.md`（互相入口；`README.md` 中文默认；简介 → 安装提示词 → 功能介绍 → 怎么用 → 常见改动 → 其他；中文页中文提示词、英文页英文提示词；内容部分只有这三节，不写 `何时` / `怎么调用` / 文件角色 / 目录清单表；**required**，缺一份或入口/顺序不对 = must-fix）。另有全中文更新日志 `DEVLOG.md`（**required**，最新在前，每条 改了什么 / 为何 / 涉及；缺失或非中文 = must-fix）。全文不要用具体 Agent 应用名，写成当前 Agent / Agent（唯一例外：某 Agent 分支上的根目录专属文件 `<agent>-spec.md`，命名规则见 `skill-authoring.md` § Agent-specific spec file）。细节：`skill-authoring.md` § README / § Install prompt / § Update log / § Agent-app names。

## Must

- **The gate runs before use and before update** of any covered content (skill, plugin, project governance files, rule, memory): quick before use, full before update — `agent-check.md`. Scriptable checks run through the fixed `scripts/run_agent_check.py`; a newly discovered repeatable check is added to that script (or the owning skill's `scripts/`), not re-written as chat-only code each run.
- The standard is the current agent app’s spec for that content type + `preferences.md`; read the current app’s spec first.
- Creating or editing any skill reads `skill-authoring.md` first.
- This skill is resident: other skills created or updated this turn follow `sync-on-update.md`.
- **Check the 关联记录 before editing:** Read `cross-reference.md` first; update it after any cross-reference change.
- Keep this hub thin; long runbooks stay in `references/`.
- **Every skill must have the companion files** (README pair, `DEVLOG.md`, `kind.txt`). This skill is the only place that states the requirement — `skill-authoring.md` § File roles; other skills point here instead of restating it.
- **叫法 and file language are decided here for every skill:** ask Jeffrey for the 叫法 first and record them only in that skill’s `SKILL.md` `description`; `README.md` is the Chinese default human page with an English `README-EN.md` companion, `DEVLOG.md` is the Chinese update log, and everything else is English — `skill-authoring.md` § Spoken names / § Language / § Update log.
- Updating any skill runs the agent-spec conformance check: generic fixes on the default branch; fixes only the current agent app needs go to its `agent/<agent>` branch (create if missing) in `<agent>-spec.md` — `skill-authoring.md` § Agent-specific spec file.
- Global skills (direct children of the current app’s default skills path) use one id for the folder, frontmatter `name`, and origin repo name: `jeffrey-<function>-skill` (`aaa` or `aaa-bbb-ccc`). A Stride skill uses the `stride-` prefix instead, for example `stride-workbench`. The check marks a mismatch must-fix. Project skills and system skills stay out of this rule — `skill-authoring.md` § Global skill id.
- After a global skill rename, update the old directory name in global skills, commands, and rules. The check marks a leftover path to a missing skill directory must-fix.

## Must not

- Use or update covered content with the gate skipped or a must-fix finding open. *(← Must: the gate runs before use and update)*
- Rename a project skill or a system skill, or apply the global skill id check to one. *(← Must: global skill id)*
- Leave a global skill whose folder, frontmatter name, or origin repo name is not that same id. *(← Must: global skill id)*
- Leave the old directory name in global skills, commands, or rules after a rename. *(← Must: update the old directory name)*
- Stuff the playbooks into `SKILL.md`. *(← Must: keep this hub thin)*
- Write an agent-specific fix into a default-branch file. *(← Must: agent-spec conformance check — agent-only fixes on `agent/<agent>`)*

## Definition of Done

- [ ] The gate ran at the required depth before the use/update; must-fix findings fixed, preference-level findings reported.
- [ ] Create/update skill work read `skill-authoring.md` first.
- [ ] Intent routed to one of: `agent-check.md` / `skill-authoring.md` / `plugin-norms.md` / `project-norms.md` / `rule-norms.md` / `memory-norms.md` / `preferences.md` / `sync-on-update.md`.
- [ ] 关联记录 checked + updated when files or `##` headings changed.
- [ ] Global skill folder, frontmatter `name`, and origin repo name are the same `jeffrey-<function>-skill` id, or the same `stride-` id when the skill’s job is Stride. Project skills and system skills were not renamed for this rule.
- [ ] After a global skill rename, old directory names are updated in global skills, commands, and rules.
- [ ] Companions aligned (`README.md` / `README-EN.md` / `DEVLOG.md` / `kind.txt`) or explicitly unchanged with reason.
- [ ] Update-time agent-spec check ran; agent-only fixes are on the `agent/<agent>` branch in `<agent>-spec.md`, not in `SKILL.md` or the default branch.
- [ ] Post-write user brief when this skill’s Route / workflow changed.