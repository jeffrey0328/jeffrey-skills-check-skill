# 关联记录 / Cross-reference map

Records **who references each tracked file** and whether the reference is to the **whole file (整篇)** or a **specific section (§)**.

**读法:** Grep `^## ` for the target filename, then read only its row group.

## Maintenance rule (required)

- **Before editing** any file listed below (rename, move, delete, or rename/remove a `##` / `§` heading that appears in the 范围 column), **read this record first** and update every listed referencer.
- **After editing**, keep this record in sync.
- **Scope of tracking:** all `references/*.md`, `examples/*`, and `kind.txt`. `SKILL.md` / `README.md` / `README.zh.md` appear as **referencers** only.

## references/

### cross-reference.md (this file)
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「Editing…」+ Always | 整篇 |
| `hub-norms.md` (top table + File index + Must + DoD) | 整篇 |
| `skill-authoring.md` § Exploration checklist | 整篇 |

### agent-check.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Commands + Route「Check before using or updating」+ Always | 整篇 + § When / § Depth |
| `hub-norms.md` File index + Must + DoD | 整篇 |
| `skill-authoring.md` header + § File roles + § Positive / negative norms + § Language | 整篇（gate）+ § Depth |
| `plugin-norms.md` / `project-norms.md` / `rule-norms.md` / `memory-norms.md` headers + check lists | § Depth / § Flow |
| `sync-on-update.md` § Resident | 整篇（full depth） |

### skill-authoring.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「Create/update Skill」+ Always「Authoring」| 整篇 + § Install prompt + § Global skill id + § Agent-specific spec file |
| `hub-norms.md` File index + Must + DoD | 整篇 + § File roles / § Spoken names / § Language / § Global skill id / § Agent-specific spec file |
| `agent-check.md` § Domains | 整篇 |
| `plugin-norms.md` § Structure | § Agent-app names + 整篇（bundled skills） |
| `project-norms.md` § Check list | § Positive / negative norms |
| `rule-norms.md` § Which home + § Check list | § Agent-specific spec file + § Positive / negative norms |
| `preferences.md` § Skill shape & language | § Skill kind |
| `sync-on-update.md` § Resident + § Companion sync | § Agent-specific spec file + § Synchronize companion files |
| sibling `jeffrey-agent-workflow-skill/SKILL.md` § Updating skills + § Projects | § Spoken names + § Language |
| sibling `jeffrey-agent-workflow-skill/references/rule-vs-skill.md` (Skill Structure row + § Where agent-specific content lives) | § File roles + § Agent-specific spec file |
| sibling `jeffrey-agent-config-skill` references (authoring pointer) | 整篇 |
| sibling `jeffrey-ue-dev-skill` (authoring pointer) | 整篇 |
| `examples/three-layer-layout.md` | § Three layers |
| `examples/agent-snippet.md` | § Prefer static / § Positive / negative norms |

### plugin-norms.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「Plugin」| 整篇 |
| `hub-norms.md` File index | 整篇 |
| `agent-check.md` § Covered content + § Domains | 整篇 |

### project-norms.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「Project」| 整篇 |
| `hub-norms.md` File index | 整篇 |
| `agent-check.md` § Covered content + § Domains | 整篇 |
| **Cites:** sibling `jeffrey-agent-workflow-skill/SKILL.md` § Projects (Governance files 表 + § Check list File language 行) | § Projects |

### rule-norms.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「Rule」| 整篇 |
| `hub-norms.md` File index | 整篇 |
| `agent-check.md` § Covered content + § Domains | 整篇 |

### memory-norms.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「Memory」| 整篇 |
| `hub-norms.md` File index | 整篇 |
| `agent-check.md` § Covered content + § Domains | 整篇 |

### preferences.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「preferences」+ Always | 整篇 |
| `hub-norms.md` File index + Must | 整篇 |
| `agent-check.md` § Depth + § Flow + § Cross-domain | 整篇 |
| `plugin-norms.md` / `project-norms.md` / `rule-norms.md` / `memory-norms.md` headers | 整篇 |

### sync-on-update.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「本轮被创建或修改」+ Always | 整篇 |
| `hub-norms.md` File index + Must | 整篇 |
| `skill-authoring.md` header | 整篇 |

### hub-norms.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Route「Norms/DoD」+ Always | 整篇 |

## examples/

### three-layer-layout.md
| Referenced by | 范围 |
|---------------|------|
| `SKILL.md` Layers 表 | 整篇 |
| `hub-norms.md` File index | 整篇 |
| `skill-authoring.md` § Thin hub / slash-attach budget (Reference layout line) | 整篇 |

### agent-snippet.md
| Referenced by | 范围 |
|---------------|------|
| `hub-norms.md` File index | 整篇 |
| `skill-authoring.md` § Thin hub / slash-attach budget (Reference layout line) | 整篇 |
| **Cites:** `skill-authoring.md` § Prefer static / § Positive / negative norms; sibling `jeffrey-agent-workflow-skill/references/repo-exploration.md` | 指针 |

## kind.txt
| Referenced by | 范围 |
|---------------|------|
| `skill-authoring.md` § Skill kind + § File roles + § Synchronize companion files | 整篇 |
| `hub-norms.md` File index | 整篇 |
| `preferences.md` § Skill shape & language | 整篇 |