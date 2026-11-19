"""Fixed gate check script for agent content (skill-authoring / agent-check norms).

When: agent-check.md § Flow — run at quick depth before using covered content,
full depth before updating it or on /agent-check. Scriptable checks live here;
the agent judges `review` findings and everything this script does not cover.
New repeatable checks are added to this file, not re-written as chat-only code.

Usage:
  python scripts/run_agent_check.py [--depth quick|full] [--json] [--skills-root PATH] [target ...]
  python scripts/run_agent_check.py --project PATH [--depth quick|full] [--json]

Targets: skill folder names under the skills root, or absolute skill paths.
No targets = every global skill under the skills root (dirs with SKILL.md).
Exit code: 1 when any must-fix finding exists, else 0.

Heuristics (language ratio, machine-local values, forbidden names) emit
`review` findings with context; the agent decides exceptions per the norms.
DEVLOG.md is Jeffrey's progress log (Chinese in practice) — language-exempt.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CJK = re.compile(r"[\u4e00-\u9fff]")
ASCII_LETTER = re.compile(r"[A-Za-z]")
FENCE = re.compile(r"^(```|~~~)")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
BACKTICK_PATH = re.compile(r"`((?:references|examples|scripts)/[^`<>{}\s]+\.(?:md|py|ps1|sh|json|txt))`")
H2 = re.compile(r"^##\s+(.+?)\s*$", re.M)

FORBIDDEN_NAMES = re.compile(
    r"\b(cursor|claude\s*code|claude|codex|gemini|antigravity|copilot|workbuddy|trae|codebuddy)\b",
    re.I,
)
NAME_EXCEPTION = re.compile(
    r"(cursor\.com|cursor://|`cursor:|push-cursor|cursor-config|-u\s+cursor|add\s+cursor|CSS|Forbidden names)",
    re.I,
)
MACHINE_LOCAL = [
    (re.compile(r"\b[A-Za-z]:[\\/][\w.\- ]"), "drive-letter path"),
    (re.compile(r"/(?:home|Users)/[\w.\-]+"), "user home path"),
    (re.compile(r"\b(?:localhost|127\.0\.0\.1):\d+"), "local port"),
    (re.compile(r"\b(?:ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]+)"), "token"),
    (re.compile(r"\bBasic [A-Za-z0-9+/=]{16,}"), "embedded Basic credential"),
]
SKIP_FILE_NAMES = {"local.md", "local.example.md"}
# Standard install locations and documented product defaults are generic, not
# machine-local: Program Files paths, and Unreal Remote Control API port 30010.
DEFAULT_PORTS = {"30010"}
# /home/box is the documented shared-agent-host alias (product AGENTS.md uses
# it as a fixed convention), not a per-machine secret.
DOCUMENTED_HOME_ALIASES = {"/home/box"}
# A cited path explicitly marked conditional is not a broken pointer.
OPTIONAL_PATH = re.compile(r"有的话|if present|if it exists", re.I)
# Historical logs record past file names, paths, and wording — exempt from
# language, pointer, and hygiene checks (they are records, not live guidance).
LOG_FILES = {"DEVLOG.md", "changelog.md", "error-log.md"}


def cjk_ratio(text: str) -> float:
    cjk = len(CJK.findall(text))
    letters = len(ASCII_LETTER.findall(text))
    return cjk / (cjk + letters) if cjk + letters else 0.0


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def strip_inline_code(text: str) -> str:
    # Backticked spans are identifiers (paths, commands, folder names), not prose.
    return re.sub(r"`[^`\n]*`", "", text)


def strip_fences(text: str) -> str:
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def frontmatter_field(text: str, field: str) -> str | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    m = re.search(rf"^{field}:\s*(.*)$", block, re.M)
    if not m:
        return None
    value = m.group(1).strip()
    if value in (">", "|", ">-", "|-"):
        lines = []
        for line in block[m.end():].splitlines():
            if line.startswith((" ", "\t")):
                lines.append(line.strip())
            elif line.strip():
                break
        value = " ".join(lines)
    return value.strip("'\"")


class Report:
    def __init__(self, target: Path):
        self.target = target
        self.findings: list[dict] = []

    def add(self, check: str, severity: str, detail: str, file: str = "", line: int = 0):
        self.findings.append(
            {"check": check, "severity": severity, "detail": detail, "file": file, "line": line}
        )

    def must_fix(self, check: str, detail: str, file: str = "", line: int = 0):
        self.add(check, "must-fix", detail, file, line)

    def review(self, check: str, detail: str, file: str = "", line: int = 0):
        self.add(check, "review", detail, file, line)


def iter_text_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".txt", ".py", ".ps1", ".sh", ".json"}:
            continue
        rel = path.relative_to(root)
        if any(part.startswith(".") or part in {"node_modules", "__pycache__"} for part in rel.parts):
            continue
        if path.name in SKIP_FILE_NAMES or path.name in LOG_FILES or path.name.endswith("-spec.md"):
            continue
        yield path


def check_language(report: Report, path: Path, rel: str, expect: str):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        report.must_fix("encoding", f"{rel} is not valid UTF-8", rel)
        return
    body = strip_inline_code(strip_fences(strip_frontmatter(text)))
    ratio = cjk_ratio(body)
    if expect == "zh" and ratio < 0.15:
        report.must_fix("language", f"{rel} must be Chinese (default human page); CJK ratio {ratio:.2f}", rel)
    elif expect == "en":
        if ratio > 0.20:
            report.must_fix("language", f"{rel} must be English; CJK ratio {ratio:.2f}", rel)
        elif ratio > 0.10:
            report.review("language", f"{rel} CJK ratio {ratio:.2f} — confirm English body", rel)


def check_links(report: Report, root: Path, path: Path, rel: str):
    text = path.read_text(encoding="utf-8")
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue  # fenced blocks hold templates/examples, not live links
        prose = re.sub(r"`[^`\n]*`", "", line)  # inline code spans hold link examples
        for m in LINK.finditer(prose):
            target = m.group(1).split("#")[0]
            if not target or re.match(r"^[a-z]+:", target) or target.startswith("<"):
                continue
            if not (path.parent / target).exists():
                report.must_fix("pointer", f"broken link → {target}", rel, i)
        for m in BACKTICK_PATH.finditer(line):
            target = m.group(1)
            if "*" in target:
                continue
            if OPTIONAL_PATH.search(line):
                continue
            if re.search(r"`(?:jeffrey-[a-z0-9-]+-skill|stride-[a-z0-9-]+)`", line):
                continue  # cross-skill citation — resolved by the agent, not this tree
            if not (root / target).exists() and not (path.parent / target).exists():
                report.must_fix("pointer", f"cited path missing → {target}", rel, i)


def check_hygiene(report: Report, path: Path, rel: str):
    text = path.read_text(encoding="utf-8")
    for i, line in enumerate(text.splitlines(), 1):
        for pattern, label in MACHINE_LOCAL:
            for m in pattern.finditer(line):
                snippet = m.group(0)
                start = m.start()
                if "<" in line[max(0, start - 1):start + len(snippet) + 1]:
                    continue
                if label == "drive-letter path" and re.search(r"Program Files", line, re.I):
                    continue
                if label == "local port" and snippet.rsplit(":", 1)[-1] in DEFAULT_PORTS:
                    continue
                if label == "user home path" and snippet in DOCUMENTED_HOME_ALIASES:
                    continue
                report.review("machine-local", f"possible {label}: {snippet!r} — confirm or move to local.md", rel, i)
        if path.suffix == ".md" and not NAME_EXCEPTION.search(line):
            for m in FORBIDDEN_NAMES.finditer(line):
                report.review("agent-name", f"forbidden app name {m.group(0)!r} — confirm exception or rewrite", rel, i)


def check_readme_pair(report: Report, root: Path, depth: str):
    zh, en = root / "README.md", root / "README-EN.md"
    if not zh.is_file():
        report.must_fix("structure", "README.md (Chinese default) missing", "README.md")
    if not en.is_file():
        report.must_fix("structure", "README-EN.md (English companion) missing", "README-EN.md")
    if (root / "README.zh.md").exists():
        report.must_fix("structure", "legacy README.zh.md present — migrate to README.md (zh) + README-EN.md (en)", "README.zh.md")
    for path, other, label in ((zh, "README-EN.md", "English"), (en, "README.md", "中文")):
        if not path.is_file():
            continue
        head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:6])
        if f"]({other})" not in head:
            report.must_fix("readme-link", f"{path.name} lacks top link [{label}]({other})", path.name)
    if zh.is_file():
        check_language(report, zh, "README.md", "zh")
    if en.is_file():
        check_language(report, en, "README-EN.md", "en")
    if depth != "full":
        return
    specs = (
        (zh, ["安装", "功能介绍", "怎么用", "常见改动"], "仓库：", "步骤"),
        (en, ["Install", "Features", "How to use", "Common changes"], "Repo:", "Steps"),
    )
    for path, order, repo_key, steps_key in specs:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        heads = H2.findall(text)
        if not heads or heads[0] != order[0]:
            report.must_fix("readme-order", f"first H2 must be {order[0]!r}, got {heads[:1]}", path.name)
        positions = []
        for want in order:
            if want not in heads:
                report.must_fix("readme-order", f"missing H2 {want!r}", path.name)
            else:
                positions.append(heads.index(want))
        if positions != sorted(positions):
            report.must_fix("readme-order", f"H2 order must be {' → '.join(order)}", path.name)
        if positions:
            block = heads[positions[0] + 1:positions[-1] + 1] if len(positions) > 1 else []
            allowed = set(order)
            for extra in block:
                if extra not in allowed:
                    report.must_fix("readme-order", f"unexpected H2 {extra!r} inside the three content sections", path.name)
        first = heads[0] if heads else ""
        if first:
            m = re.search(rf"^##\s+{re.escape(first)}\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
            section = m.group(1) if m else ""
            fence = re.search(r"```[^\n]*\n(.*?)```", section, re.S)
            if not fence:
                report.must_fix("install-prompt", "Install section lacks a fenced agent prompt", path.name)
            else:
                body = fence.group(1)
                if repo_key not in body or steps_key not in body:
                    report.must_fix("install-prompt", f"prompt must contain {repo_key!r} and {steps_key!r}", path.name)
            if "git clone" in section:
                report.must_fix("install-prompt", "no human git clone command in Install", path.name)


def check_skill(root: Path, depth: str) -> Report:
    report = Report(root)
    skill_md = root / "SKILL.md"
    if not skill_md.is_file():
        report.must_fix("structure", "SKILL.md missing")
        return report
    text = skill_md.read_text(encoding="utf-8")
    name = frontmatter_field(text, "name")
    if name != root.name:
        report.must_fix("id", f"frontmatter name {name!r} != folder {root.name!r}", "SKILL.md")
    if not frontmatter_field(text, "description"):
        report.must_fix("structure", "frontmatter description missing", "SKILL.md")
    if not re.fullmatch(r"jeffrey-[a-z0-9]+(?:-[a-z0-9]+)*-skill|stride-[a-z0-9]+(?:-[a-z0-9]+)*", root.name):
        report.must_fix("id", f"global skill id pattern broken: {root.name}")
    try:
        url = subprocess.run(
            ["git", "-C", str(root), "remote", "get-url", "origin"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        if url:
            repo = url.rstrip("/").rsplit("/", 1)[-1].removesuffix(".git")
            if repo != root.name:
                report.must_fix("id", f"origin repo {repo!r} != folder {root.name!r}")
    except (OSError, subprocess.TimeoutExpired):
        pass
    kind = root / "kind.txt"
    if not kind.is_file() or kind.read_text(encoding="utf-8").strip() not in {"演进", "底本"}:
        report.must_fix("structure", "kind.txt missing or not one line 演进 / 底本", "kind.txt")
    xref = root / "references" / "cross-reference.md" if (root / "references").is_dir() else root / "cross-reference.md"
    if not xref.is_file():
        report.must_fix("structure", "cross-reference.md missing", str(xref.relative_to(root)))
    examples = root / "examples"
    if not examples.is_dir() or not any(examples.iterdir()):
        report.must_fix("structure", "examples/ missing or empty (layer 3)", "examples/")
    check_readme_pair(report, root, depth)
    if depth == "full":
        body = strip_frontmatter(text)
        if len(body.splitlines()) > 100 or len(body) > 4000:
            report.review("thin-hub", f"hub body {len(body.splitlines())} lines / {len(body)} chars — keep routing-only", "SKILL.md")
    for path in iter_text_files(root):
        rel = path.relative_to(root).as_posix()
        if path.suffix == ".md":
            check_links(report, root, path, rel)
            if rel not in {"README.md", "README-EN.md"}:
                check_language(report, path, rel, "en")
        if path.suffix in {".md", ".py", ".ps1", ".sh", ".json", ".txt"}:
            check_hygiene(report, path, rel)
    return report


def check_project(root: Path, depth: str) -> Report:
    report = Report(root)
    for required in ("README.md", "README-EN.md", "DEVLOG.md", "AGENTS.md"):
        if not (root / required).is_file():
            report.must_fix("structure", f"{required} missing", required)
    check_readme_pair(report, root, "quick")
    for name in ("AGENTS.md",):
        path = root / name
        if path.is_file():
            check_language(report, path, name, "en")
            check_links(report, root, path, name)
            check_hygiene(report, path, name)
    return report


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("targets", nargs="*", help="skill folder names or absolute paths")
    parser.add_argument("--skills-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--depth", choices=["quick", "full"], default="quick")
    parser.add_argument("--project", action="store_true", help="treat targets as project repos")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.project:
        roots = [Path(t).resolve() for t in args.targets]
        if not roots:
            parser.error("--project needs at least one target path")
        reports = [check_project(r, args.depth) for r in roots]
    else:
        if args.targets:
            roots = []
            for t in args.targets:
                p = Path(t)
                roots.append(p.resolve() if p.is_absolute() or p.exists() else args.skills_root / t)
        else:
            roots = sorted(
                d for d in args.skills_root.iterdir()
                if d.is_dir() and (d / "SKILL.md").is_file() and not d.name.startswith(".")
            )
        reports = [check_skill(r, args.depth) for r in roots]

    must_fix = sum(1 for r in reports for f in r.findings if f["severity"] == "must-fix")
    if args.json:
        print(json.dumps(
            {"depth": args.depth, "must_fix": must_fix,
             "results": [{"target": str(r.target), "findings": r.findings} for r in reports]},
            ensure_ascii=False, indent=2,
        ))
    else:
        for r in reports:
            fixes = [f for f in r.findings if f["severity"] == "must-fix"]
            reviews = [f for f in r.findings if f["severity"] == "review"]
            print(f"{r.target.name}: {'PASS' if not fixes else f'{len(fixes)} must-fix'}"
                  f"{f', {len(reviews)} review' if reviews else ''}")
            for f in r.findings:
                loc = f"{f['file']}:{f['line']}" if f["line"] else f["file"]
                print(f"  [{f['severity']}] {f['check']}: {f['detail']}" + (f"  ({loc})" if loc else ""))
        print(f"total must-fix: {must_fix}")
    return 1 if must_fix else 0


if __name__ == "__main__":
    sys.exit(main())