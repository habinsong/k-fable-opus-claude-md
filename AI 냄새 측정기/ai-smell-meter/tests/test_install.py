"""설치기: 임시 홈과 프로젝트에만 쓴다. 실제 홈 디렉터리는 건드리지 않는다."""
import contextlib
import io
import json
import pathlib
import tempfile
import unittest

import _path  # noqa: F401
from ai_smell import installer
from ai_smell.cli import build_parser


def run_install(*argv):
    args = build_parser().parse_args(["install", *argv])
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        rc = installer.install(args)
    return rc, buf.getvalue()


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.home = pathlib.Path(self.tmp.name) / "home"
        self.proj = pathlib.Path(self.tmp.name) / "proj"
        self.home.mkdir()
        self.proj.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def skill(self, base, tool):
        return base / f".{tool}" / "skills" / "ai-smell-polish"

    def test_user_install_auto_detects_and_verifies(self):
        (self.home / ".gemini").mkdir()
        rc, out = run_install("--home", str(self.home), "--format", "json")
        data = json.loads(out)
        self.assertEqual(rc, 0, out)
        tools = {r["tool"] for r in data["results"] if r["kind"] == "skill"}
        self.assertEqual(tools, {"agents", "gemini"})
        for tool in tools:
            d = self.skill(self.home, tool)
            self.assertTrue((d / "SKILL.md").is_file())
            self.assertTrue((d / installer.MARK).is_file())
            self.assertTrue((d / "scripts" / "ai_smell" / "cli.py").is_file())
            self.assertTrue((d / "agents" / "claude" / installer.AGENT_FILE).is_file())
        self.assertTrue(all(r["check"].startswith("selftest 26/26") for r in data["results"] if r["kind"] == "skill"))

    def test_no_tool_found_adds_claude_and_subagent(self):
        rc, _ = run_install("--home", str(self.home))
        self.assertEqual(rc, 0)
        self.assertTrue((self.skill(self.home, "claude") / "SKILL.md").is_file())
        self.assertTrue((self.home / ".claude" / "agents" / installer.AGENT_FILE).is_file())

    def test_update_and_uninstall(self):
        run_install("--home", str(self.home), "--agents", "agents")
        d = self.skill(self.home, "agents")
        (d / "stale.txt").write_text("x", encoding="utf-8")
        rc, out = run_install("--home", str(self.home), "--agents", "agents")
        self.assertEqual(rc, 0)
        self.assertIn("갱신됨", out)
        self.assertFalse((d / "stale.txt").exists())
        rc, out = run_install("--home", str(self.home), "--agents", "agents", "--uninstall")
        self.assertEqual(rc, 0)
        self.assertFalse(d.exists())

    def test_foreign_folder_is_not_overwritten_without_force(self):
        d = self.skill(self.home, "agents")
        d.mkdir(parents=True)
        (d / "mine.txt").write_text("keep", encoding="utf-8")
        rc, out = run_install("--home", str(self.home), "--agents", "agents")
        self.assertIn("건너뜀", out)
        self.assertTrue((d / "mine.txt").exists())
        rc, out = run_install("--home", str(self.home), "--agents", "agents", "--uninstall")
        self.assertIn("건너뜀", out)
        self.assertTrue((d / "mine.txt").exists())
        rc, _ = run_install("--home", str(self.home), "--agents", "agents", "--force")
        self.assertEqual(rc, 0)
        self.assertTrue((d / "SKILL.md").is_file())

    def test_dry_run_writes_nothing(self):
        rc, out = run_install("--home", str(self.home), "--dry-run")
        self.assertEqual(rc, 0)
        self.assertIn("설치 예정", out)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_project_scope_and_instructions_are_idempotent(self):
        for _ in range(2):
            rc, _ = run_install("--scope", "project", "--project", str(self.proj), "--agents", "claude,agents",
                                "--append-instructions")
            self.assertEqual(rc, 0)
        self.assertTrue((self.skill(self.proj, "claude") / "SKILL.md").is_file())
        text = (self.proj / "AGENTS.md").read_text(encoding="utf-8")
        self.assertEqual(text.count(installer.BEGIN), 1)
        self.assertTrue((self.proj / "GEMINI.md").is_file())

    def test_unknown_agent_is_an_error(self):
        rc, _ = run_install("--home", str(self.home), "--agents", "vim")
        self.assertEqual(rc, 2)

    def test_existing_user_instructions_are_kept(self):
        (self.proj / "AGENTS.md").write_text("# mine\n", encoding="utf-8")
        run_install("--scope", "project", "--project", str(self.proj), "--agents", "agents", "--append-instructions")
        text = (self.proj / "AGENTS.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# mine\n"))
        self.assertIn(installer.BEGIN, text)

    def test_installed_copy_runs_standalone(self):
        import subprocess
        import sys
        run_install("--home", str(self.home), "--agents", "agents")
        launcher = self.skill(self.home, "agents") / "scripts" / "ai-smell"
        p = subprocess.run([sys.executable, "-I", str(launcher), "analyze", "--text", "Certainly! Done."],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("AI 냄새 점수", p.stdout)


if __name__ == "__main__":
    unittest.main()
