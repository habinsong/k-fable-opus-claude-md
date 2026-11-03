"""문서와 구조 점검: 스킬 형식, 생성 문서의 최신성, 파일 크기, 소스의 보이지 않는 문자."""
import pathlib
import re
import subprocess
import sys
import unicodedata
import unittest

import _path
from ai_smell.prompt import chat_prompt

ROOT = _path.ROOT
SKILL_DIR = ROOT / "skills" / "ai-smell-polish"


def cli(*argv):
    return subprocess.run([sys.executable, "-I", str(_path.LAUNCHER), *argv], capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout


def frontmatter(path):
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    assert m, f"frontmatter 없음: {path}"
    out = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip('"')
    return out


class SkillFormat(unittest.TestCase):
    def test_skill_md_follows_the_agent_skills_spec(self):
        fm = frontmatter(SKILL_DIR / "SKILL.md")
        self.assertEqual(fm["name"], SKILL_DIR.name)
        self.assertRegex(fm["name"], r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertLessEqual(len(fm["name"]), 64)
        self.assertTrue(1 <= len(fm["description"]) <= 1024, len(fm["description"]))
        self.assertLessEqual(len(fm.get("compatibility", "")), 500)
        self.assertLessEqual(set(fm), {"name", "description", "license", "compatibility", "metadata", "allowed-tools"})

    def test_skill_body_is_short(self):
        body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertLess(len(body.splitlines()), 120)
        self.assertLess(len(body) / 2, 5000)          # 한국어는 글자 하나가 토큰 1~2개: 보수적으로 절반

    def test_referenced_files_exist(self):
        body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        for ref in re.findall(r"`(references/[\w.-]+)`", body):
            self.assertTrue((SKILL_DIR / ref).is_file(), ref)

    def test_claude_subagent_frontmatter(self):
        fm = frontmatter(ROOT / "agents" / "claude" / "ai-smell-polisher.md")
        self.assertEqual(fm["name"], "ai-smell-polisher")
        self.assertTrue(fm["description"])
        self.assertIn("Bash", fm["tools"])
        self.assertIn("managed-by: ai-smell-meter", (ROOT / "agents" / "claude" / "ai-smell-polisher.md").read_text(encoding="utf-8"))

    def test_instruction_snippets_have_markers(self):
        for rel in ("codex/AGENTS.snippet.md", "gemini/GEMINI.snippet.md"):
            t = (ROOT / "agents" / rel).read_text(encoding="utf-8")
            self.assertIn("<!-- ai-smell-meter:begin -->", t)
            self.assertIn("<!-- ai-smell-meter:end -->", t)


class GeneratedDocs(unittest.TestCase):
    def test_rules_md_is_current(self):
        self.assertEqual((ROOT / "docs" / "rules.md").read_text(encoding="utf-8"), cli("rules", "--format", "md"))

    def test_chat_prompts_are_current(self):
        text = (SKILL_DIR / "references" / "chat-prompts.md").read_text(encoding="utf-8")
        self.assertIn(chat_prompt("ko").rstrip("\n"), text)
        self.assertIn(chat_prompt("en").rstrip("\n"), text)


class Hygiene(unittest.TestCase):
    def test_files_stay_under_500_lines(self):
        for p in ROOT.rglob("*"):
            if p.is_file() and p.suffix in (".py", ".md") and "__pycache__" not in p.parts:
                n = len(p.read_text(encoding="utf-8").splitlines())
                if p.name == "rules.md":
                    continue                       # 자동 생성 표
                self.assertLessEqual(n, 500, f"{p.relative_to(ROOT)}: {n}줄")

    def test_source_has_no_invisible_characters(self):
        for p in (SKILL_DIR / "scripts").rglob("*.py"):
            for ch in p.read_text(encoding="utf-8"):
                if ch in " \n\t":
                    continue
                self.assertNotIn(unicodedata.category(ch), ("Cf", "Co", "Zs", "Cc"), f"{p.name}: U+{ord(ch):04X}")

    @unittest.skipUnless(hasattr(sys, "stdlib_module_names"), "Python 3.10 이상에서만 목록을 제공한다")
    def test_engine_is_stdlib_only(self):
        stdlib = set(sys.stdlib_module_names)
        for p in (SKILL_DIR / "scripts").rglob("*.py"):
            for m in re.finditer(r"^\s*(?:from|import)\s+([a-zA-Z_][\w]*)", p.read_text(encoding="utf-8"), re.M):
                name = m.group(1)
                self.assertTrue(name in stdlib or name in ("ai_smell", "_path"), f"{p.name}: {name}")

    def test_no_network_calls_in_engine(self):
        for p in (SKILL_DIR / "scripts").rglob("*.py"):
            t = p.read_text(encoding="utf-8")
            for banned in ("urllib", "requests", "socket", "http.client"):
                self.assertNotIn(banned, t, f"{p.name}: {banned}")

    def test_no_claude_attribution_in_tool_files(self):
        for p in ROOT.rglob("*"):
            if p.is_file() and p.suffix in (".py", ".md") and "tests" not in p.parts:
                t = p.read_text(encoding="utf-8")
                for banned in ("Co-Authored-By", "Generated with Claude Code", "claude.ai/code/session"):
                    self.assertNotIn(banned, t, f"{p.relative_to(ROOT)}: {banned}")

    def test_launchers_are_executable(self):
        for rel in ("install.py", "bin/ai-smell", "skills/ai-smell-polish/scripts/ai-smell"):
            self.assertTrue((ROOT / rel).stat().st_mode & 0o111, rel)

    def test_license_present(self):
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
