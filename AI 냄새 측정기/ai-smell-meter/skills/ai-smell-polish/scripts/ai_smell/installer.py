"""스킬과 에이전트 정의를 각 AI 도구의 폴더에 설치하고, 설치본이 도는지 확인한다. 표준 라이브러리만 쓴다.

설치 위치는 Agent Skills 규격을 따른다(근거와 불확실한 점은 docs/design.md 6절):
  Claude Code : .claude/skills/<이름>/SKILL.md, ~/.claude/skills/   (서브에이전트: .claude/agents/*.md)
  공통(Codex, Gemini CLI 등): .agents/skills/<이름>/, ~/.agents/skills/
  Gemini CLI  : .gemini/skills/<이름>/, ~/.gemini/skills/
  Codex(구 경로): ~/.codex/skills/<이름>/
"""
from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from .model import VERSION

SKILL = "ai-smell-polish"
MARK = ".ai-smell-installed"
AGENT_FILE = "ai-smell-polisher.md"
OWNER_TAG = "managed-by: ai-smell-meter"
TOOLS = ("claude", "agents", "gemini", "codex")


def skill_source() -> Path:
    return Path(__file__).resolve().parents[2]


def agents_source() -> Optional[Path]:
    for cand in (skill_source() / "agents", skill_source().parents[1] / "agents"):
        if cand.is_dir():
            return cand
    return None


def _bases(scope: str, home: Optional[str], project: str) -> Dict[str, Path]:
    out = {}
    if scope in ("user", "both"):
        out["user"] = Path(home).expanduser() if home else Path.home()
    if scope in ("project", "both"):
        out["project"] = Path(project).expanduser().resolve()
    return out


def _detect(scope: str, base: Path) -> List[str]:
    found = ["agents"]
    if (base / ".claude").exists() or (scope == "project" and (base / "CLAUDE.md").exists()):
        found.append("claude")
    if (base / ".gemini").exists() or (scope == "project" and (base / "GEMINI.md").exists()):
        found.append("gemini")
    if scope == "user" and (base / ".codex").exists():
        found.append("codex")
    if found == ["agents"]:
        found.append("claude")            # 아무것도 못 찾으면 가장 흔한 Claude Code도 함께 둔다
    return found


def plan(args) -> List[Dict[str, Any]]:
    actions: List[Dict[str, Any]] = []
    for scope, base in _bases(args.scope, args.home, args.project).items():
        names = _detect(scope, base) if args.agents == "auto" else [x.strip() for x in args.agents.split(",") if x.strip()]
        for name in names:
            if name not in TOOLS:
                raise ValueError(f"알 수 없는 대상: {name} (가능: {', '.join(TOOLS)})")
            if name == "codex" and scope == "project":
                continue                    # 프로젝트의 Codex는 .agents/skills가 맡는다
            actions.append({"tool": name, "scope": scope, "kind": "skill", "dest": base / f".{name}" / "skills" / SKILL})
            if name == "claude":
                actions.append({"tool": name, "scope": scope, "kind": "subagent",
                                "dest": base / ".claude" / "agents" / AGENT_FILE})
    return actions


def _ours(dest: Path) -> bool:
    if dest.is_dir():
        return (dest / MARK).exists()
    if dest.is_file():
        try:
            return OWNER_TAG in dest.read_text(encoding="utf-8")
        except OSError:
            return False
    return False


def _install_skill(dest: Path, force: bool) -> str:
    src = skill_source()
    if src in dest.parents or src == dest:
        raise ValueError("설치 위치가 원본 폴더 안이다")
    if dest.exists() and not _ours(dest) and not force:
        return "건너뜀: 같은 이름의 다른 폴더가 있다(--force로 덮어씀)"
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.parent / f".{SKILL}.tmp-{os.getpid()}"
    if tmp.exists():
        shutil.rmtree(tmp)
    shutil.copytree(src, tmp, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"))
    ag = agents_source()
    if ag is not None and not (tmp / "agents").exists():
        shutil.copytree(ag, tmp / "agents", ignore=shutil.ignore_patterns("__pycache__"))
    (tmp / MARK).write_text(json.dumps({"version": VERSION, "installed": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                        "source": str(src)}, ensure_ascii=False), encoding="utf-8")
    existed = dest.exists()
    if existed:
        old = dest.parent / f".{SKILL}.old-{os.getpid()}"
        os.replace(dest, old)
    os.replace(tmp, dest)
    if existed:
        shutil.rmtree(old, ignore_errors=True)
    return "갱신됨" if existed else "설치됨"


def _install_agent(dest: Path, force: bool) -> str:
    ag = agents_source()
    src = (ag / "claude" / AGENT_FILE) if ag else None
    if src is None or not src.is_file():
        return "건너뜀: 에이전트 정의 원본을 찾지 못했다"
    if dest.exists() and not _ours(dest) and not force:
        return "건너뜀: 같은 이름의 다른 파일이 있다(--force로 덮어씀)"
    dest.parent.mkdir(parents=True, exist_ok=True)
    existed = dest.exists()
    shutil.copyfile(src, dest)
    return "갱신됨" if existed else "설치됨"


def _remove(dest: Path) -> str:
    if not dest.exists():
        return "없음"
    if not _ours(dest):
        return "건너뜀: 이 도구가 설치한 것이 아니다"
    shutil.rmtree(dest) if dest.is_dir() else dest.unlink()
    return "제거됨"


def _check(dest: Path) -> str:
    launcher = dest / "scripts" / "ai-smell"
    if not launcher.exists():
        return "검증 못 함: 실행 파일이 없다"
    try:
        proc = subprocess.run([sys.executable, "-I", str(launcher), "selftest", "--format", "json"],
                              capture_output=True, text=True, encoding="utf-8", timeout=180)
        data = json.loads(proc.stdout or "{}")
        return f"selftest {data.get('passed', 0)}/{data.get('total', 0)}" + ("" if data.get("ok") else " 실패")
    except (OSError, ValueError, subprocess.SubprocessError) as e:
        return f"검증 실패: {e}"


SNIPPETS = {"AGENTS.md": ("codex", "AGENTS.snippet.md"), "GEMINI.md": ("gemini", "GEMINI.snippet.md")}
BEGIN = "<!-- ai-smell-meter:begin -->"


def _append_instructions(project: Path, dry: bool) -> List[Dict[str, Any]]:
    """프로젝트의 AGENTS.md, GEMINI.md 끝에 사용 안내를 덧붙인다. 이미 있으면 건드리지 않는다."""
    out: List[Dict[str, Any]] = []
    ag = agents_source()
    for fname, (folder, snippet) in SNIPPETS.items():
        target = project / fname
        src = (ag / folder / snippet) if ag else None
        if src is None or not src.is_file():
            out.append({"tool": folder, "scope": "project", "kind": "instructions", "path": str(target),
                        "status": "건너뜀: 원본 없음", "check": ""})
            continue
        if target.exists() and BEGIN in target.read_text(encoding="utf-8"):
            status = "이미 있음"
        elif dry:
            status = "덧붙일 예정"
        else:
            body = src.read_text(encoding="utf-8")
            old = target.read_text(encoding="utf-8") if target.exists() else ""
            target.write_text(old + ("\n" if old and not old.endswith("\n\n") else "") + body, encoding="utf-8")
            status = "덧붙임"
        out.append({"tool": folder, "scope": "project", "kind": "instructions", "path": str(target),
                    "status": status, "check": ""})
    return out


def install(args) -> int:
    results: List[Dict[str, Any]] = []
    try:
        actions = plan(args)
    except ValueError as e:
        sys.stderr.write(f"오류: {e}\n")
        return 2
    failed = False
    for a in actions:
        dest: Path = a["dest"]
        try:
            if args.dry_run:
                status = "제거 예정" if args.uninstall else "설치 예정"
            elif args.uninstall:
                status = _remove(dest)
            elif a["kind"] == "skill":
                status = _install_skill(dest, args.force)
            else:
                status = _install_agent(dest, args.force)
            check = ""
            if not args.dry_run and not args.uninstall and a["kind"] == "skill" and status in ("설치됨", "갱신됨"):
                check = _check(dest)
                failed |= check.endswith("실패")
        except (OSError, ValueError) as e:
            status, check, failed = f"실패: {e}", "", True
        results.append({"tool": a["tool"], "scope": a["scope"], "kind": a["kind"], "path": str(a["dest"]),
                        "status": status, "check": check})
    if getattr(args, "append_instructions", False) and not args.uninstall and args.scope in ("project", "both"):
        results += _append_instructions(Path(args.project).expanduser().resolve(), args.dry_run)
    if args.format == "json":
        sys.stdout.write(json.dumps({"ok": not failed, "version": VERSION, "results": results},
                                    ensure_ascii=False, indent=2) + "\n")
    else:
        for r in results:
            sys.stdout.write(f"{r['status']:<8} [{r['tool']}/{r['scope']}/{r['kind']}] {r['path']}"
                             + (f"  ({r['check']})" if r["check"] else "") + "\n")
        if not args.dry_run and not args.uninstall:
            sys.stdout.write("\nAI 에이전트를 새로 시작하면 스킬 목록에 `ai-smell-polish`가 보입니다.\n"
                             "바로 쓰기: python3 <설치 경로>/scripts/ai-smell polish 글.md\n")
    return 1 if failed or any(r["status"].startswith("실패") for r in results) else 0


def doctor(fmt: str = "text") -> int:
    from .selftest import collect
    checks = collect()
    bad = [c for c in checks if not c[1]]
    home = Path.home()
    installs = []
    for tool in TOOLS:
        p = home / f".{tool}" / "skills" / SKILL
        if p.exists():
            installs.append(str(p))
    info = {"ok": sys.version_info >= (3, 9) and not bad, "version": VERSION, "python": platform.python_version(),
            "executable": sys.executable, "platform": platform.platform(),
            "stdout_encoding": getattr(sys.stdout, "encoding", None), "skill_source": str(skill_source()),
            "agents_source": str(agents_source()) if agents_source() else None,
            "selftest": f"{len(checks) - len(bad)}/{len(checks)}", "user_installs": installs,
            "tool_dirs": {t: (home / f".{t}").exists() for t in TOOLS}}
    if fmt == "json":
        sys.stdout.write(json.dumps(info, ensure_ascii=False, indent=2) + "\n")
    else:
        for k, v in info.items():
            sys.stdout.write(f"{k}: {v}\n")
        if sys.version_info < (3, 9):
            sys.stdout.write("Python 3.9 이상이 필요합니다.\n")
    return 0 if info["ok"] else 1
