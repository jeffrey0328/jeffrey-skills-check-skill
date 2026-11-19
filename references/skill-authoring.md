# Agent Skill authoring workflow

Read this when **creating or updating** any Agent Skill. This file is the skill-shape spec for **`jeffrey-agent-check-skill`**. For large-repo exploration, also read **`jeffrey-agent-workflow-skill/references/repo-exploration.md`**. Checks run through the gate in `agent-check.md`; sync after an update: `sync-on-update.md`.

## Exploration checklist (required)

Before editing `SKILL.md` or other skill content, read-only exploration in this order:

1. Source paths, modules, and call chains the user named.
2. In-repo **examples** (`examples/`, `samples/`, tests, similar skills).
3. In-repo **docs** (`README`, `docs/`, `*.md`, inline comments).

**关联记录 first:** before editing any skill, read **that skill’s** `cross-reference.md`. Before editing this skill’s files, read **this** skill’s `cross-reference.md`. After changing any cross-reference, update the matching record.

Write only from what you read. Prefer repo-local facts; use **web search** only when the user allows **and** the gap is not a repo-local fact. If information is missing: **list gaps** and ask for paths or excerpts.

**Must not** (overlaps above): guess APIs/paths/behavior without reading; invent to fill gaps; routine web search for repo-local facts.

**Large repos**: follow **`repo-exploration.md`**—scoped tools; no whole-tree recursive scans.

## File roles (canonical)

**Every skill must carry these companion files.** This skill owns the requirement; no other skill restates it. The check (`agent-check.md`) marks a missing companion must-fix, and § Synchronize companion files on create/update keeps them aligned.

| Path | Audience | Role |
|------|----------|------|
| `SKILL.md` | Agent | **Thin** English hub: routing + Commands (+ few always-on bullets) |
| `references/` | Agent | Long workflows, full Must/Must-not, DoD, file indexes — **read on demand** |
| `references/cross-reference.md` | Agent | 关联记录 — who references each tracked file (whole/§); read before editing, update after |
| `README.md` | Human | English README — **required**; link to `README.zh.md` |
| `README.zh.md` | Human | Chinese README — **required**; link to `README.md` |
| `kind.txt` | Agent | Rewrite policy: one line `演进` or `底本` — § Skill kind |
| `<agent>-spec.md` | Agent | Optional, **only on that agent app's branch** of the skill repo: the part only that app understands. Indexed from `SKILL.md` by the naming rule alone — see § Agent-specific spec file |
| `examples/` | Both | Layer-3 cases (see **Three layers**) |
| `scripts/` | Agent / local | Bound to flags / SKILL actions |

## Three layers (required)

Every skill has **at least** these three layers. The hub (layer 1) indexes the other two. Extra dirs are allowed when the skill’s work needs them.

| Layer | Default path | Role |
|-------|--------------|------|
| **1 Index** | `SKILL.md` | Route / Commands only. A short Layers table names layer-2 and layer-3 paths. |
| **2 Content** | `references/` | Playbooks, norms, DoD. Domain aliases: `modules/` (UE), `standards/` (video). |
| **3 Cases** | `examples/` | Concrete worked examples the agent can copy. If cases already live in `templates/`, `modules/*/code-templates.md`, or `standards/*模板*`, `examples/` still holds a `case-index.md` that points at them. |

**Optional extras** (only when the skill’s content needs them): `scripts/` / `tools/` (runnable), code next to playbooks.

A stub `examples/agent-snippet.md` that only says “load the skill → read X” does **not** count as layer 3. Write a real case or a `case-index.md`.

## Prefer static skill assets (required when **using or authoring** any skill)

When a skill workflow would **dynamically write code** (ad-hoc Shell that grows into a script, one-off `.py`/`.ps1` in the workspace, helpers reinvented each run), **judge staticizability first**.

| Signal → staticize into the **owning skill** | Keep dynamic (do not pollute the skill) |
|----------------------------------------------|-----------------------------------------|
| Same purpose / flags / inputs across runs or machines | Truly one-shot for this chat only |
| Agent (or human) will need it again for this skill’s Commands / Route | Tied to one user project’s product code, not the skill |
| Stable enough to version next to `SKILL.md` | Secrets, machine-only paths, or ephemeral debug |

**When staticizable — Must:**

1. **Add** the asset under the skill that owns the workflow: `scripts/` (runnable, bound to a Command/flag), `examples/` (templates to adapt), or `references/` (documented snippets).
2. **Document when to use**: Commands / Route row, and/or a short **When** in the script header or the matched `references/*.md` section.
3. **Sync companions** if humans need the new action (`README.md` + `README.zh.md`) — same as § Synchronize companion files.
4. Tell the user what was added and the **when** trigger.

**Must not:** Re-invent the same helper as chat-only dynamic code every session when it belongs in that skill. *(← Must: prefer static + document when)*

Authoring check: new repeatable automation → ship static + when as the documented path.

## Thin hub / slash-attach budget (required when creating **any** skill)

Applies to **every** Agent Skill created or materially reshaped under this workflow — not only `jeffrey-agent-check-skill`.

**Product fact:** `/skill-name` and `@skill-name` paste the **entire** hub `SKILL.md` into that user turn. Agents cannot lazy-load the pasted body. Description-only auto-attach (no slash) lists the skill without pasting the hub.

| Must | Must not *(← overlapping Must)* |
|------|----------------------------------|
| Keep `SKILL.md` **routing-only**: frontmatter `description`, purpose one-liner, Commands, Route table, optional ≤5 always-on bullets | Stuff full Must/Must-not lists, Definition of Done checklists, large file indexes, or long procedures into `SKILL.md` *(← thin hub)* |
| Put long agent content in `references/*.md` and route to them; after attach, Read **one** matched reference (partial `##` when long) | Default-Read every `references/*.md` or the whole skill tree on attach *(← route + partial read)* |
| Prefer a dedicated norms/DoD file when the hub would otherwise bloat (e.g. `references/hub-norms.md` or `references/<domain>-norms.md`) | Duplicate the same long norms in both hub and references *(← single source in references)* |

**Shape checklist (create / update):**

1. Frontmatter `description` (triggers) — what auto-attach exposes every turn.
2. Hub body = Commands + Route (+ minimal Always). Target: short enough that a slash paste is cheap (rough guide: prefer well under ~100 lines / ~4K characters of hub body).
3. Norms, DoD, indexes, multi-step playbooks → `references/`.
4. Long reference files: top **读法** / when→which `##` table — see **Partial read** below.
5. **Three layers:** hub indexes content + cases — § Three layers. Missing `examples/` or a stub-only examples dir is unfinished.

Reference layout: this hub’s thin `SKILL.md` + `references/hub-norms.md`. Layout example: `examples/three-layer-layout.md`. Wording example for Workflow / Norms: `examples/agent-snippet.md`.

## README at skill root (required)

Every skill **must** have **two** root README files. Both are **required companions** (the check marks a missing one, or a missing link between them, must-fix).

| File | Language | Entry to the other (first line after the `#` title) |
|------|----------|-----------------------------------------------------|
| `README.md` | English | `[中文](README.zh.md)` |
| `README.zh.md` | Chinese | `[English](README.md)` |

The two files cover the **same facts**. Do not keep a bilingual single file.

**Section order** (both files, same sequence):

1. **简介** — untitled prose right after the language link. One short paragraph: what the skill is.
2. **安装方法** — first H2: English `## Install` / Chinese `## 安装`. One short line: install **through the current agent**. Then **one fenced prompt** in **that file’s language** (`README.md` English, `README.zh.md` Chinese). The prompt **must** include the git URL and the install steps. Do **not** give a human `git clone` command. Extra install-only notes (e.g. `-setupproject`) may follow the fence, still inside this H2.
3. **具体内容介绍** — **exactly three** H2s, all written for **the person using the skill**: what it can do, how to use it, then how to change it. English: `## Features`, `## How to use`, `## Common changes`. Chinese: `## 功能介绍`, `## 怎么用`, `## 常见改动`. Nothing else belongs in this block.
4. **其他内容** — extras that are not install and not those three (e.g. Privacy).

**`Features` / `功能介绍` (required)** — what this skill can do, as a short bullet list (about 3–8 items). Each bullet is one capability a person would recognize. Write outcomes, not file names.

**`How to use` / `怎么用` (required)** — how a person triggers this skill, and *when* it fires, in one place:

- One lead line: resident / auto-attach vs `@<name>` vs keywords. Resident: say so plainly (no `@` needed).
- Then a two-column table: **你说什么 / You say** → **会发生什么 / What happens**. Rows are what the person types or says (`/flag`, `@<name>`, a plain request), never internal file paths.
- Fold “when it applies” into this section — do **not** add a separate `When` / `何时` or `How to invoke` / `怎么调用` H2. If the skill only fires in narrow cases, say so in the lead line.

**`Common changes` / `常见改动` (required)** — how the user changes this skill’s own content, as a two-column table:

| Column | Content |
|--------|---------|
| 想改什么 / What to change | The user-visible knob: this skill’s norms, its checking standards, its templates, its data store, its output paths, its triggers |
| 对 Agent 说 / Say to the agent | One sentence a person can paste. The agent locates the file itself |

Cover every knob a user actually wants to turn in that skill. Name a file only as a trailing hint after the intent, never as the row key. Write the say-to-the-agent sentence in **that README’s language** (English in `README.md`, Chinese in `README.zh.md`).

**Must not:** Add any other H2 to 具体内容介绍 — no `When` / `何时`, no `How to invoke` / `怎么调用`, no `What it does` / `做什么`, no file-roles / file-inventory / layout table (`File roles`, `文件角色`, `Layout`, `目录`). One-line purpose stays in the 简介 paragraph; capabilities go in `功能介绍`; trigger timing goes in `怎么用`; file roles are agent-facing (§ File roles + the skill’s `references/hub-norms.md` File index). *(← Must: 具体内容 = 功能介绍 + 怎么用 + 常见改动)*

**Must not:** Put `## What` / `## 做什么` before Install; or give a standalone `git clone` as the install method. *(← Must: 简介 → 通过 Agent 安装提示词 → 具体内容 → 其他)*

Include at minimum (split across those four blocks):

- Intro paragraph (purpose and outcomes).
- Install: agent prompt with git URL + steps — § Install prompt.
- `功能介绍`: what it can do. `怎么用`: how it is triggered and when it fires. `常见改动`: how to ask the agent to change its norms, standards, templates, and data.

**Language**

- `SKILL.md`: **English** default (agent control plane).
- `README.md`: English human page — **required companion** (missing, no link to `README.zh.md`, or wrong section order = must-fix).
- `README.zh.md`: Chinese human page — **required companion** (missing, no link to `README.md`, or wrong section order = must-fix).

## Install prompt (required)

`## Install` / `## 安装` is **install through the current agent**. After one short intro line, one fenced prompt in **that README’s language**.

The prompt **must** include:

1. The skill folder name.
2. The git URL (`Repo:` / `仓库：https://…/*.git`).
3. Numbered **Steps** / **步骤**: first read **this** agent app’s skill spec; then clone into that app’s default skills path (folder name = skill name); then adapt only the bind points. Paths come from that spec.

English intro + English prompt in `README.md`. Chinese intro + Chinese prompt in `README.zh.md`. Same facts; do **not** paste the Chinese block into `README.md`.

Fill `<name>` and `<repo.git>`.

English (`README.md`):

```
Install the skill "<name>" into the agent app you are currently running in.
Repo: https://github.com/<owner>/<repo>.git
Steps:
1. First read and follow this agent app's current skill spec (install directory, frontmatter, how skills are attached, project pointers, human-page requirements). Do not edit files until that spec is read. Do not apply another agent product's paths or fields from memory.
2. Following that spec, clone this repo into this agent app's default skills path, using the folder name "<name>".
3. Then change only the parts of this skill that must bind to the current agent, following that spec. Do not read through the process prose in references/ or examples/.
```

Chinese (`README.zh.md`):

```
请把 skill「<name>」安装到你当前所在的 Agent 应用。
仓库：https://github.com/<owner>/<repo>.git
步骤：
1. 先读取并遵守你当前这个 Agent 的 skill 规范（安装目录、frontmatter、挂载方式、项目指针、人类页要求）。未读到该规范之前不要改文件。不要凭记忆套用某一个 Agent 产品的路径和字段。
2. 按该规范把该仓库克隆到当前 Agent 的默认 skills 路径，文件夹名用「<name>」。
3. 再按该规范改本 skill 里需要对接到当前 Agent 的部分。不要通读 references/、examples/ 里的流程正文。
```

**Must:** `README.md` uses the English prompt; `README.zh.md` uses the Chinese prompt (git URL + steps + spec first).

**Must not:** Put a human `git clone` command in Install, put a Chinese prompt in `README.md`, or start installing before the current agent’s spec is read. *(← Must: one agent prompt per language; spec first)*

## Agent-app names (forbidden)

Do **not** use a specific agent app name or a specific project name. Write **the current agent app**, **Agent**, or **the agent**; for a project write a placeholder such as `<Project>` or `<Plugin>`. This applies **anywhere** in a skill (hub, README, references, examples, scripts, templates, agents, tools, filenames).

Forbidden names (any capitalization or spacing): Cursor, Claude, Claude Code, ClaudeCode, Codex, Gemini, Antigravity, Copilot, WorkBuddy, Trae, CodeBuddy — including those names inside paths and filenames (a file or directory named after an agent, such as that agent's own instruction file or config directory, counts).

The ban covers **every** agent app and **every** project, not only the names in the list above. The list is what the check matches; a project name has no list and is judged by reading.

**Must:** discover the current app’s skills path from this skill’s location or from that app’s spec; never hard-code an agent app directory. Refer to an agent-specific file as “the agent-specific adapter / rule file”; the agent finds its real name in its own spec.

**Must not:** Use a specific agent app name, that app’s path, or a specific project name. *(← Must: agent-agnostic wording, placeholders for projects)*

The install prompt says「某一个 Agent 产品」, not an agent app name.

### Agent-specific spec file (the one exception)

A skill repo can be referenced by several agent apps (each app's skills parent repo pins it). The part only one agent app understands lives on that app's own **branch** of the skill repo (named `agent/<agent>`, not `<agent>` alone, because a remote may already hold `<agent>/...` branches and git cannot hold both), as **one file in the skill folder root**, and nowhere else.

- **Naming rule:** `<agent>-spec.md`, where `<agent>` is the lowercase agent app name (one lowercase word, no spaces). It is the only file in a skill where an agent app name may appear, in its name and in its text.
- **Index:** `SKILL.md` on the default branch carries one line that states only this naming rule (`<agent>-spec.md` in this folder; read the one for the current agent app if it exists). It names no agent and does not describe the file.
- **Where it exists:** only on that agent's branch. The default branch holds no `*-spec.md`. Files the spec needs (scripts, examples) go on the same branch; rules that belong to that part go on it too.
- The check skips root files matching `*-spec.md` in the agent-app-name check.

**Update-time check (required when updating any skill):**

1. Check the skill against the current agent app's skill spec — the same spec the Install prompt reads first (install directory, frontmatter, attach mechanism, human-page requirements).
2. Split the fixes by audience: what every agent app reads goes to the **default branch**; what only the current agent app needs goes to its branch `agent/<agent>` — create it from the default branch when missing, reuse it when it exists.
3. On that branch the agent-specific part goes only into `<agent>-spec.md` (plus the scripts / examples that part needs).

**Must not:** Write an agent-specific fix into `SKILL.md` or any default-branch file to make the skill pass the current agent's spec. *(← Must: update-time check — agent-only fixes live on `agent/<agent>` in `<agent>-spec.md`)*

This section is the ban list (needed so the check can name what is forbidden). CSS `cursor:` in stylesheets is the CSS property, not an agent app name. A git host (`origin.cursor.com`, `cursor.com`), a hyphenated command or record id (`/push-cursor`, `cursor-config`), a git remote name written as a code span or after `add ` / `-u `, or a protocol prompt deeplink (`cursor://…`), is a host/CLI identifier, not an agent app name.

## Global skill id (required)

This id applies only to **global** skills: directories directly under the current agent app’s default skills path. Three strings are the same id:

- the skill directory name
- `SKILL.md` frontmatter `name`
- the git `origin` repository name (last path segment of the remote URL, without `.git`)

The id is `jeffrey-<function>-skill`. `<function>` is one or more lowercase segments: `aaa` or `aaa-bbb-ccc`. It must start with `jeffrey-` and end with `-skill`.

**Stride prefix.** A skill whose job is Stride uses the folder prefix `stride-` and that same string as frontmatter `name`. Example: `stride-workbench`. That skill does not use the `jeffrey-<function>-skill` id. When it has an origin, the repository name matches the folder.

Project skills (a skill that lives in a project, not in that default skills path) are out of scope. Built-in system skills are out of scope. Do not rename them for this rule, and do not flag them in the check.

**Must:** a global skill’s folder, frontmatter `name`, and origin repo name are one `jeffrey-<function>-skill` id, or one `stride-` id when the skill’s job is Stride. The check reports a mismatch as must-fix. Project skills and system skills are not checked.

**Must:** after that folder or repo is renamed, update every mention of the old directory name in global skills, global commands, and global rules. The check reports a leftover path to a missing skill directory as must-fix.

**Must not:** Rename a project skill, a system skill, or a `stride-` skill to satisfy the `jeffrey-<function>-skill` id. *(← Must: global skills only; Stride keeps the `stride-` prefix)*

**Must not:** Leave a global skill whose folder, frontmatter `name`, or origin repo name breaks that id or disagrees with the others. *(← Must: one id)*

**Must not:** Leave the old directory name in global skills, commands, or rules after the rename. *(← Must: update mentions after rename)*

## Spoken names / 叫法 (required when creating)

Every skill answers to the names Jeffrey actually says. This skill owns that rule for all skills.

1. **Ask Jeffrey for the 叫法 first**, before writing the skill. Use the names he gives.
2. **Record them only in the YAML `description` of that skill’s own `SKILL.md`.** The agent app matches skills from `description`, so every spoken name goes there; that lets a Chinese-only invoke load the skill. The body needs no separate names section.
3. **To look up a skill’s 叫法, open the `description` in its `SKILL.md`.** Product `AGENTS.md` files and `.mdc` files point at the skill and leave the name catalog to `SKILL.md`.

## Language (required)

| File | Language |
|------|----------|
| `README.md` | English (GitHub default); top link to `README.zh.md` |
| `README.zh.md` | Chinese (Jeffrey reads this one); top link to `README.md` |
| Everything else: `SKILL.md`, `references/`, `examples/`, headings, body | English |

- The YAML `description` is English and also carries the skill’s spoken names (which may be Chinese) — § Spoken names.
- Speak to Jeffrey in his language in conversation; the table above governs files only.
- A product / project repo (not a skill) follows its own file rules in `jeffrey-agent-workflow-skill` § Projects.

## Auto-invocation decision (required when creating)

Two **mechanisms** (configured differently; **both** must be explained to humans when used):

| Mechanism | Configured in (skill / project) | Tell the human in |
|-----------|----------------------------------|-------------------|
| **按 description 加载** | `SKILL.md` frontmatter: `description` triggers; **omit** `disable-model-invocation` to allow | README `怎么用` lead line: resident / `@` / keywords |
| **项目 AGENTS 拉起** | Project root **`AGENTS.md`** pointer | README `怎么用` lead line: the `@` or the words that fire it |

Skill frontmatter = control plane. The README tells the person how they invoke the skill. Agent-only fields stay in `SKILL.md`.

**Before finishing** a new skill (or when the user changes invoke policy), **ask once** which **product** mode:

| Mode | Skill frontmatter | Project `AGENTS.md` |
|------|----------------------------|---------------------|
| **仅手动** | `disable-model-invocation: true` | No required pointer |
| **条件自动** | Often `disable-model-invocation: true` + AGENTS；**or** omit disable and rely on `description` match | If AGENTS path: add pointer |
| **常驻 / 默认** | **Omit** `disable-model-invocation`；`description` 写清常驻意图 | Optional |

Defaults if unanswered: **ask** — do not guess. Current set: **`jeffrey-agent-workflow-skill`** → **常驻 / 默认**（description）；**`jeffrey-ue-dev-skill`**（UE 唯一入口，域内容在其 `modules/`）→ **条件自动**（`AGENTS.md` + `disable-model-invocation: true`）；**`jeffrey-agent-check-skill`** → **常驻 / 默认**（description：五域内容规范 + 使用前/更新前强制检查；创建/编辑 skill 先读本规范；其他 skill 本轮被改时同步配套）。

## Partial read (skills & rules → context/cache)

**Consuming** a Skill or project/plugin rules file: do **not** default-Read the whole file into context.

1. Prefer hub `SKILL.md` routing → **one** `references/<file>.md` for the intent.
2. Inside a multi-section `.md` (`##` headings, or an explicit 读法/index table): Grep `^## `, then Read **only** the needed section(s) via offset/limit.
3. Same for `AGENTS.md` / plugin rules docs when they document sectioned load rules.

**Authoring:** follow **Thin hub / slash-attach budget** (required above). For long single files, add a top **读法 / when→which `##`** table. Keep always-on adapters as pointers (omit full body copies).

## Positive / negative norms (Skills **and** Rules)

Applies to **Skill** `SKILL.md` / `references/` **and** project **Rules** (`AGENTS.md`, satellites, `.mdc`). Same rule in **`jeffrey-agent-workflow-skill/references/project-rules.md`** § Writing norms.

**Prefer affirmative** imperatives (**Must** / **Do** / **When→Then**).

Write a negative (**Must not / Do not / Never / 禁止 / 不要**) **only when** the affirmative's scope is too broad: it would also cover something that must be excluded, and that part needs saying. The negative is a carve-out inside a positive norm's scope (same concern: what to do instead, or the allowed path), so a **positive** norm that **contains or overlaps** it must already exist. The negative sharpens the positive; it must not stand alone.

| OK | Not OK |
|----|--------|
| Must: human pages = the README pair. Must not: create a separate `human-guide.html`. | Must not: create `human-guide.html`. *(alone)* |
| Must: partial-read needed `##` only. Must not: default-Read whole multi-section file. | Must not: read whole file. *(alone)* |
| 提交说明默认中文。 | 同句肯定后再加括号否定（例如默认中文后又写勿用英文）— 括号否定多余，只留肯定 |

**If you cannot name the overlapping positive** → rewrite as **Must** only (state the allowed behavior); drop the orphan negative.

**Human README prose:** prefer affirmative-only. After a complete positive, drop redundant paren negatives (the check flags those).

Authoring / update check: every new or touched Must not has an explicit paired Must (same file or clearly cited). The skill-domain check (`agent-check.md`) flags unpaired negatives **and** redundant paren negatives.

## Skill kind (rewrite policy)

Each skill is one type, stored as `kind.txt` (single line, UTF-8, only `演进` or `底本`; missing or any other value = must-fix).

| Value | Who may rewrite the skill |
|-------|---------------------------|
| `演进` | The agent may keep improving the skill from observed use, pitfalls, and implementations. **Required:** a documented update loop in `references/` (or that skill’s playbook). Each such update tells the user **更新标准 / 更新依据 / 更新条目**. |
| `底本` | The agent does **not** rewrite the skill on its own. Updates come only from the user’s direct command, or when a cited information source itself changed. |

**Before finishing** a new skill:

1. **Propose** a type from the work: growing from use / pitfalls → `演进`; a frozen playbook or source dump → `底本`.
2. **Ask** the user to confirm:
   > 建议类型为「演进型 / 底本型」，是否按这个落盘？可改。
3. Write the confirmed value to **`kind.txt`**.

Existing skills without a type: write `演进` and tell the user they can switch. On update, change `kind.txt` only when the user asks to switch type.

### 演进型 — update loop + user brief

Must have a written update mechanism (how observation becomes a write). After each agent-driven update (not a user command that already states the exact change), the user-facing brief is three lines:

- **更新标准** — which bar / rule this write is applying
- **更新依据** — what was observed (use / pitfall / implementation)
- **更新条目** — which files or bullets changed

### 底本型 — no spontaneous rewrite

Do not add a learn-from-runs or agent-driven rewrite loop. Source-change updates still need one-line **依据** naming the source. Other writes only when the user directly commands them.

## Synchronize companion files on create/update

After **every** skill update (any change to `SKILL.md`, `references/`, `scripts/`, `examples/`, or the layout), check whether `README.md` and `README.zh.md` still describe the skill, and update both when they do not. A typo fix needs only the check. Then check the rest:

- **`README.md`**: English; `[中文](README.zh.md)` after the title; order 简介 → `## Install` → `## Features` → `## How to use` → `## Common changes` → 其他. Install = one **English** agent prompt (git URL + Steps). No `When` / `How to invoke` H2, no file-roles table. See § README at skill root + § Install prompt.
- **`README.zh.md`**: Chinese; `[English](README.md)` after the title; same order with `## 安装` and the **Chinese** prompt, then 功能介绍 / 怎么用 / 常见改动. Same facts as `README.md`.
- **`常见改动` rows**: if this change added or moved a knob a user would ask to change (norms, checking standards, data store, output paths, triggers), update the row in **both** READMEs.
- **Wording:** do not use a specific agent app name or a specific project name. Write **the current agent app**, **Agent**, or **the agent**; a project is a placeholder — § Agent-app names.
- **`kind.txt`**: one line `演进` or `底本` (see **Skill kind** above). Write on create; change only when the user asks.
- **`examples/`**: layer-3 cases (or `case-index.md` pointing at in-skill templates) — § Three layers.
- **`references/`**: if agent workflows moved out of `SKILL.md`.
- **Thin hub:** create/update still satisfies **Thin hub / slash-attach budget** — hub stays routing-only; long norms/DoD/playbooks stay in `references/`.
- **Prefer static:** if the change adds repeatable automation that used to be chat-only dynamic code, ensure `scripts/` / `examples/` / `references/` + **when to use** are present — § Prefer static skill assets.
- **`cross-reference.md` (this skill's 关联记录):** if you added, renamed, moved, or deleted a `references/` / `scripts/` / `examples/` file or a cited `##` / `§` heading, update the affected rows so it stays the single source for "who references what (whole/§)".

## Cross-skill rollout (关联记录 & shared conventions)

When you **create or change a skill-wide convention** — the `cross-reference.md` 关联记录 mechanism, a companion-file requirement, hub / `references` shape, or a shared script / flag — **apply it to every skill**, not only the one in front of you, so all skills stay consistent.

1. **Enumerate** skills: list directories under the current agent app’s default skills path (skip parent-level `scripts/` / `logs/` and plugin / system-managed skills).
2. **Apply per skill, adapted to its layout:** a skill with a `references/` dir puts `cross-reference.md` there and wires the rule into `SKILL.md` + `references/hub-norms.md`; a skill with no `references/` puts `cross-reference.md` at its root and wires the rule into `SKILL.md` only.
3. **Keep each skill's `cross-reference.md` current** whenever that skill's files change — this per-skill sync is the ordinary case; the fleet-wide rollout above applies only to **shared conventions**.
4. **Parallelize** across skills when the change is uniform (one subagent per skill), then **report per skill**.

Scope: a routine content or typo fix in one skill only needs **that** skill's `cross-reference.md` kept in sync — it does **not** require touching the others. *(← rollout is for shared conventions, not every edit)*

**Loading:** the skills-repo root `AGENTS.md` points here, so this norm loads before editing any skill via the workspace's AGENTS rules — independent of whether another hub is auto-attached that turn.

## Post-write user brief (required)

After **create or meaningful update** of a Skill (new Route row, new `references/*.md`, new triggers, hub→child dispatch), the agent **must** end the turn with a clear user-facing brief — not only “已写入”. Cover:

1. **怎么写的（分层）** — which files changed and why (hub Route / `description` vs long playbook in `references/`; companions touched or why skipped).
2. **怎么调用 / 被触发** — every real entry path: `/` `@` paste, `description` auto-attach (or `disable-model-invocation: true` → no auto), parent hub Route, project `AGENTS.md` if any.
3. **执行逻辑** — step-by-step what the agent does when the new content matches (match intent → which file Read → what rules apply → report `Routed: …` when a hub is involved). Prefer a short numbered flow; name the exact reference path.

Skip only for pure typo/format fixes with no Route/`description`/workflow change — say so in one line.

If this write was an agent-driven update to a **演进型** skill (observed use / pitfall / implementation, not a user command that already stated the exact change), also include **更新标准 / 更新依据 / 更新条目** — § Skill kind.

If a companion file needs no change, say why in the summary. Meaningful skill changes should keep `SKILL.md`, `README.md`, `README.zh.md`, `examples/`, and `references/` aligned in substance.