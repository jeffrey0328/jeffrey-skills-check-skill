# Case: required three-layer tree

**When:** creating a skill or the check finds a missing layer. Optional extras only if that skill’s work needs them.

```
<skill>/
├── SKILL.md                 # 1 Index — Route / Commands + Layers table
├── references/              # 2 Content — playbooks (or modules/ / standards/)
│   ├── <workflow>.md
│   └── cross-reference.md   # 关联记录
├── examples/                # 3 Cases — worked example or case-index.md
│   └── case-index.md
├── README.md
├── README.zh.md
├── kind.txt                 # rewrite policy: 演进 / 底本
├── scripts/                 # tools / code — only if Commands need them
└── tools/
```