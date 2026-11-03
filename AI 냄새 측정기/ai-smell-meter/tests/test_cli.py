"""명령줄: 실제로 프로세스를 띄워 출력 분리, 종료 코드, 파일 쓰기를 확인한다."""
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

import _path
from ai_smell.samples import AI_STRONG

LAUNCHER = str(_path.LAUNCHER)


def run(*argv, stdin=None):
    return subprocess.run([sys.executable, "-I", LAUNCHER, *argv], input=stdin, capture_output=True,
                          text=True, encoding="utf-8", timeout=120)


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name)
        self.src = self.dir / "한글 이름.md"
        self.src.write_text(AI_STRONG["en"], encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_analyze_text_and_json(self):
        p = run("analyze", str(self.src))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("AI 냄새 점수", p.stdout)
        self.assertIn("저자 판정에 쓰지 마세요", p.stdout)
        j = json.loads(run("analyze", str(self.src), "--format", "json").stdout)
        self.assertGreaterEqual(j["score"], 60)
        self.assertIn("disclaimer", j)
        self.assertTrue(j["findings"])

    def test_analyze_english_ui_and_stdin(self):
        p = run("analyze", "-", "--ui", "en", stdin="Certainly! Done.")
        self.assertIn("AI smell index", p.stdout)

    def test_fail_above(self):
        self.assertEqual(run("analyze", str(self.src), "--fail-above", "10").returncode, 1)
        self.assertEqual(run("analyze", str(self.src), "--fail-above", "100").returncode, 0)

    def test_polish_separates_text_and_summary(self):
        p = run("polish", str(self.src))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertNotIn("Certainly", p.stdout)
        self.assertNotIn("교정 요약", p.stdout)
        self.assertIn("교정 요약", p.stderr)

    def test_polish_text_only_and_diff(self):
        p = run("polish", str(self.src), "--text-only")
        self.assertEqual(p.stderr, "")
        d = run("polish", str(self.src), "--diff")
        self.assertIn("--- original", d.stdout)

    def test_polish_out_and_in_place(self):
        out = self.dir / "out.md"
        p = run("polish", str(self.src), "--out", str(out))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("교정 요약", p.stdout)
        self.assertNotIn("Certainly", out.read_text(encoding="utf-8"))
        before = self.src.read_text(encoding="utf-8")
        run("polish", str(self.src), "--in-place")
        self.assertEqual(pathlib.Path(str(self.src) + ".bak").read_text(encoding="utf-8"), before)
        self.assertNotEqual(self.src.read_text(encoding="utf-8"), before)

    def test_polish_json(self):
        j = json.loads(run("polish", str(self.src), "--format", "json", "--tier", "strong").stdout)
        self.assertLess(j["after"]["score"], j["before"]["score"])
        self.assertNotIn("Certainly", j["corrected"])
        self.assertIn(j["verify"]["status"], ("PASS", "WARN", "CONFIRM"))

    def test_verify_exit_codes(self):
        a = self.dir / "a.txt"
        b = self.dir / "b.txt"
        a.write_text("Revenue grew 38%.", encoding="utf-8")
        b.write_text("Revenue grew 83%.", encoding="utf-8")
        p = run("verify", str(a), str(b))
        self.assertEqual(p.returncode, 1)
        self.assertIn("FAIL", p.stdout)
        b.write_text("Revenue grew 38%.", encoding="utf-8")
        self.assertEqual(run("verify", str(a), str(b)).returncode, 0)

    def test_prompt_targets_and_chat(self):
        self.assertIn("<flagged_signals>", run("prompt", str(self.src), "--target", "claude").stdout)
        self.assertIn("# Flagged signals", run("prompt", str(self.src), "--target", "gpt").stdout)
        self.assertIn("{{paste the text here}}", run("prompt", "--chat", "en").stdout)
        self.assertIn("{{여기에 글을 붙여 넣는다}}", run("prompt", "--chat", "ko").stdout)

    def test_rules_formats(self):
        self.assertIn("en.structure.neg-parallel", run("rules").stdout)
        self.assertIn("| id |", run("rules", "--format", "md").stdout)
        data = json.loads(run("rules", "--format", "json", "--lang", "ko").stdout)
        self.assertTrue(all(r["lang"] in ("ko", "any") for r in data))

    def test_selftest_and_version(self):
        p = run("selftest", "--format", "json")
        self.assertEqual(p.returncode, 0, p.stdout)
        self.assertTrue(json.loads(p.stdout)["ok"])
        self.assertIn("ai-smell", run("version").stdout)

    def test_missing_file_is_exit_2(self):
        p = run("analyze", str(self.dir / "nope.md"))
        self.assertEqual(p.returncode, 2)
        self.assertIn("오류", p.stderr)

    def test_in_place_needs_a_path(self):
        self.assertEqual(run("polish", "-", "--in-place", stdin="x").returncode, 2)

    def test_ban_file(self):
        ban = self.dir / "ban.txt"
        ban.write_text("# 내 말버릇\ncircle back\n", encoding="utf-8")
        p = run("analyze", "--text", "We will circle back later.", "--ban-file", str(ban), "--format", "json")
        self.assertIn("user.ban.1", [f["rule"] for f in json.loads(p.stdout)["findings"]])

    def test_oversize_input_is_rejected(self):
        big = self.dir / "big.txt"
        big.write_bytes(b"a" * 2_000_100)
        self.assertEqual(run("analyze", str(big)).returncode, 2)

    def test_utf8_output_without_locale(self):
        env = {k: v for k, v in os.environ.items() if k not in ("LANG", "LC_ALL", "PYTHONUTF8", "PYTHONIOENCODING")}
        env["LC_ALL"] = "C"
        p = subprocess.run([sys.executable, "-I", LAUNCHER, "analyze", "--text", "물론입니다! 도움이 되었기를 바랍니다."],
                           capture_output=True, env=env, timeout=60)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("AI 냄새 점수".encode("utf-8"), p.stdout)


if __name__ == "__main__":
    unittest.main()
