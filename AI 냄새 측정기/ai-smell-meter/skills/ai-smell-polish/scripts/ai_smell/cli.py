"""명령줄. analyze, polish, verify, prompt, rules, selftest, doctor, install, version."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from typing import List, Optional

from . import report
from .detect import analyze
from .fix import polish
from .model import GENRES, VERSION
from .prompt import build as build_prompt
from .rules import load_rules
from .textutil import read_input
from .verify import verify


def _common(p: argparse.ArgumentParser, with_input: bool = True) -> None:
    if with_input:
        p.add_argument("path", nargs="?", help="파일 경로. 생략하거나 '-'면 표준 입력")
        p.add_argument("--text", help="파일 대신 문자열을 직접 넘긴다")
    p.add_argument("--genre", choices=GENRES, default="general", help="장르: 일부 규칙의 가중치가 달라진다")
    p.add_argument("--lang", choices=("auto", "ko", "en"), default="auto", help="규칙 언어를 제한한다")
    p.add_argument("--ui", choices=("ko", "en"), default="ko", help="보고서 언어")
    p.add_argument("--ban", action="append", default=[], metavar="구절", help="작성자 금지어(여러 번 가능)")
    p.add_argument("--ban-file", help="금지어 목록 파일(한 줄에 하나)")


def _ban(args) -> List[str]:
    words = list(args.ban)
    if getattr(args, "ban_file", None):
        with open(args.ban_file, encoding="utf-8") as fh:
            words += [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    return words


def _out(s: str, stream=None) -> None:
    (stream or sys.stdout).write(s if s.endswith("\n") else s + "\n")


def cmd_analyze(args) -> int:
    text = read_input(args.path, args.text)
    a = analyze(text, genre=args.genre, lang=args.lang, ban=_ban(args), quotes=args.protect_quotes)
    if args.format == "json":
        _out(json.dumps(report.analysis_dict(a, text), ensure_ascii=False, indent=2))
    else:
        _out(report.render_analysis(a, text, args.ui, args.top, args.all))
    return 1 if args.fail_above is not None and a.score > args.fail_above else 0


def cmd_polish(args) -> int:
    text = read_input(args.path, args.text)
    res = polish(text, tier=args.tier, genre=args.genre, lang=args.lang, ban=_ban(args))
    ver = verify(res.original, res.text, genre=args.genre, lang=args.lang)
    summary = report.render_polish_summary(res, ver, args.ui)
    if args.format == "json":
        _out(json.dumps(report.polish_dict(res, ver), ensure_ascii=False, indent=2))
        return 1 if ver.status == "FAIL" else 0
    if args.in_place:
        if not args.path or args.path == "-":
            _out("오류: --in-place는 파일 경로가 필요합니다.", sys.stderr)
            return 2
        shutil.copyfile(args.path, args.path + ".bak")
        with open(args.path, "w", encoding="utf-8", newline="") as fh:
            fh.write(res.output)
        _out(summary + f"\n  원본은 {args.path}.bak 으로 보관했습니다.")
    elif args.out:
        with open(args.out, "w", encoding="utf-8", newline="") as fh:
            fh.write(res.output)
        _out(summary + f"\n  교정문을 {args.out} 에 썼습니다.")
    else:
        sys.stdout.write(report.unified_diff(res.original, res.text) if args.diff else res.output)
        if not res.output.endswith("\n"):
            sys.stdout.write("\n")
        if not args.text_only:
            _out("\n" + summary, sys.stderr)
    return 1 if ver.status == "FAIL" else 0


def cmd_verify(args) -> int:
    a, b = read_input(args.original, None), read_input(args.revised, None)
    v = verify(a, b, genre=args.genre, lang=args.lang)
    if args.format == "json":
        from .verify import to_dict
        _out(json.dumps(to_dict(v), ensure_ascii=False, indent=2))
    else:
        _out(report.render_verify(v, args.ui))
    return 1 if v.status == "FAIL" else 0


def cmd_prompt(args) -> int:
    if args.chat:
        from .prompt import chat_prompt
        _out(chat_prompt(args.chat))
        return 0
    text = read_input(args.path, args.text)
    base = text
    if not args.no_polish:
        base = polish(text, tier=args.tier, genre=args.genre, lang=args.lang, ban=_ban(args)).text
    a = analyze(base, genre=args.genre, lang=args.lang, ban=_ban(args))
    _out(build_prompt(base, a, ui=args.prompt_lang, target=args.target))
    return 0


def cmd_rules(args) -> int:
    rules = [r for r in load_rules(args.lang) if not args.category or r.category == args.category]
    if args.format == "md":
        _out(report.rules_markdown(rules))
    elif args.format == "json":
        _out(json.dumps([{"id": r.id, "lang": r.lang, "category": r.category, "grade": r.grade,
                          "weight": r.weight, "tier": r.tier, "note": r.note} for r in rules],
                        ensure_ascii=False, indent=2))
    else:
        _out(report.render_rules(rules, args.ui))
    return 0


def cmd_selftest(args) -> int:
    from .selftest import run
    return run(args.format)


def cmd_doctor(args) -> int:
    from .installer import doctor
    return doctor(args.format)


def cmd_install(args) -> int:
    from .installer import install
    return install(args)


def cmd_version(args) -> int:
    _out(f"ai-smell {VERSION}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ai-smell", description="AI 냄새 측정기: 한국어·영어 윤문 엔진 (측정 + 교정문 출력)")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("analyze", help="AI 냄새 점수와 검출 항목 목록을 출력한다")
    _common(a)
    a.add_argument("--format", choices=("text", "json"), default="text")
    a.add_argument("--top", type=int, default=12, help="보여 줄 신호 수")
    a.add_argument("--all", action="store_true", help="검출 항목을 모두 보인다")
    a.add_argument("--protect-quotes", action="store_true", help="긴 따옴표 안의 글을 건드리지 않는다")
    a.add_argument("--fail-above", type=int, metavar="N", help="점수가 N보다 크면 종료 코드 1")
    a.set_defaults(fn=cmd_analyze)

    c = sub.add_parser("polish", help="교정문을 출력한다(표준 출력). 요약은 표준 오류로 나간다")
    _common(c)
    c.add_argument("--tier", choices=("safe", "standard", "strong"), default="standard",
                   help="safe: 글자만 정리, standard: 군더더기·잔재 삭제, strong: 뜻이 조금 달라질 수 있는 교정 포함")
    c.add_argument("--out", help="교정문을 파일로 쓴다(요약은 표준 출력)")
    c.add_argument("--in-place", action="store_true", help="입력 파일을 덮어쓴다(.bak 백업)")
    c.add_argument("--diff", action="store_true", help="교정문 대신 통합 diff를 출력한다")
    c.add_argument("--text-only", action="store_true", help="요약 없이 교정문만")
    c.add_argument("--format", choices=("text", "json"), default="text")
    c.set_defaults(fn=cmd_polish)

    v = sub.add_parser("verify", help="원문과 윤문본을 대조한다(사실 보존, 변경률, 새 결함)")
    v.add_argument("original")
    v.add_argument("revised")
    v.add_argument("--genre", choices=GENRES, default="general")
    v.add_argument("--lang", choices=("auto", "ko", "en"), default="auto")
    v.add_argument("--ui", choices=("ko", "en"), default="ko")
    v.add_argument("--format", choices=("text", "json"), default="text")
    v.set_defaults(fn=cmd_verify)

    r = sub.add_parser("prompt", help="LLM에게 맡길 윤문 프롬프트를 출력한다")
    _common(r)
    r.add_argument("--tier", choices=("safe", "standard", "strong"), default="standard")
    r.add_argument("--target", choices=("generic", "claude", "gpt", "gemini"), default="generic")
    r.add_argument("--prompt-lang", choices=("", "ko", "en"), default="", help="프롬프트 언어(기본: 글의 언어)")
    r.add_argument("--no-polish", action="store_true", help="자동 교정 없이 원문 그대로 프롬프트에 싣는다")
    r.add_argument("--chat", choices=("ko", "en"), help="셸 없는 채팅 환경용 일반 프롬프트를 출력한다(입력 불필요)")
    r.set_defaults(fn=cmd_prompt)

    u = sub.add_parser("rules", help="규칙 목록")
    u.add_argument("--lang", choices=("auto", "ko", "en"), default="auto")
    u.add_argument("--category")
    u.add_argument("--ui", choices=("ko", "en"), default="ko")
    u.add_argument("--format", choices=("text", "json", "md"), default="text")
    u.set_defaults(fn=cmd_rules)

    s = sub.add_parser("selftest", help="내장 시험을 돌린다(설치 확인용)")
    s.add_argument("--format", choices=("text", "json"), default="text")
    s.set_defaults(fn=cmd_selftest)

    d = sub.add_parser("doctor", help="실행 환경과 설치 위치를 점검한다")
    d.add_argument("--format", choices=("text", "json"), default="text")
    d.set_defaults(fn=cmd_doctor)

    i = sub.add_parser("install", help="스킬과 에이전트 정의를 각 AI 도구의 폴더에 설치한다")
    i.add_argument("--scope", choices=("user", "project", "both"), default="user")
    i.add_argument("--agents", default="auto", help="auto 또는 claude,codex,gemini,agents (쉼표)")
    i.add_argument("--project", default=".", help="project 범위의 기준 폴더")
    i.add_argument("--home", help="user 범위의 기준 폴더(시험용). 기본은 홈 디렉터리")
    i.add_argument("--dry-run", action="store_true")
    i.add_argument("--uninstall", action="store_true")
    i.add_argument("--force", action="store_true", help="표지가 없는 같은 이름 폴더도 덮어쓴다")
    i.add_argument("--append-instructions", action="store_true",
                   help="project 범위에서 AGENTS.md, GEMINI.md 끝에 사용 안내를 덧붙인다")
    i.add_argument("--format", choices=("text", "json"), default="text")
    i.set_defaults(fn=cmd_install)

    ver = sub.add_parser("version")
    ver.set_defaults(fn=cmd_version)
    return p


def main(argv: Optional[List[str]] = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    args = build_parser().parse_args(argv)
    try:
        return args.fn(args)
    except (OSError, ValueError) as e:
        _out(f"오류: {e}", sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
