"""대조 검증: 사실 보존, 변경률, 새 신호, 프롬프트."""
import unittest

import _path  # noqa: F401
from ai_smell.detect import analyze
from ai_smell.prompt import build, chat_prompt
from ai_smell.verify import change_rate, facts_for_prompt, names, numbers, verify


class Facts(unittest.TestCase):
    def test_numbers_normalized(self):
        self.assertEqual(numbers("12,481 and 3.50 and 007"), numbers("12481 3.5 7"))

    def test_changed_number_fails(self):
        v = verify("Revenue grew 38% in 2025.", "Revenue grew 83% in 2025.")
        self.assertEqual(v.status, "FAIL")
        self.assertIn("38", v.numbers_missing)

    def test_missing_url_code_quote_fail(self):
        base = 'Run `make all` then open https://a.example/x and read "the exact words here".'
        self.assertEqual(verify(base, base.replace("`make all`", "make")).status, "FAIL")
        self.assertEqual(verify(base, base.replace("https://a.example/x", "the site")).status, "FAIL")
        self.assertEqual(verify(base, base.replace("the exact words here", "other words")).status, "FAIL")

    def test_same_text_passes(self):
        v = verify("A plain sentence about nothing in particular.", "A plain sentence about nothing in particular.")
        self.assertEqual(v.status, "PASS")
        self.assertEqual(v.change_rate, 0.0)

    def test_names_detection(self):
        n = names("We tested GPT-6 and Claude with PyTorch. Then Anna left.")
        self.assertTrue({"GPT-6", "PyTorch"} <= n)

    def test_added_name_warns(self):
        v = verify("We tested the tool on Monday and it worked.", "We tested the tool with Kubernetes on Monday and it worked.")
        self.assertIn("Kubernetes", v.names_added)
        self.assertEqual(v.status, "WARN")


class Rates(unittest.TestCase):
    def test_bounds(self):
        self.assertEqual(change_rate("a b c", "a b c"), 0.0)
        self.assertEqual(change_rate("a b c", "x y z"), 1.0)
        self.assertEqual(change_rate("", "x"), 0.0)

    def test_deletion_only(self):
        self.assertAlmostEqual(change_rate("a b c d", "a b"), 0.5)

    def test_thresholds(self):
        src = " ".join(f"w{i}" for i in range(10))
        warn = verify(src, " ".join(f"w{i}" for i in range(6)) + " x y z").status   # 30% 초과
        confirm = verify(src, "w0 w1 w2 q q q q q q q").status                     # 50% 초과
        self.assertIn(warn, ("WARN", "CONFIRM"))
        self.assertEqual(confirm, "CONFIRM")

    def test_new_signal_warns(self):
        v = verify("The cache is per-process and expires after a minute.",
                   "Certainly! The cache is per-process and expires after a minute.")
        self.assertIn("en.residue.opener", v.new_signals)
        self.assertNotEqual(v.status, "PASS")

    def test_polish_result_passes_verify(self):
        from ai_smell.fix import polish
        from ai_smell.samples import AI_STRONG
        for t in AI_STRONG.values():
            r = polish(t, tier="standard")
            self.assertNotEqual(verify(t, r.text).status, "FAIL")


class Prompts(unittest.TestCase):
    TEXT = "Certainly! It's not just a tool, it's a platform. Sales rose 12% in 2025 (see https://a.example/r)."

    def test_generic_has_sections_and_facts(self):
        p = build(self.TEXT, analyze(self.TEXT), target="generic")
        for h in ("# Role", "# Rules", "# How to fix", "# Do not change", "# Flagged signals", "# Output format", "# Text"):
            self.assertIn(h, p)
        self.assertIn("12", p)
        self.assertIn("https://a.example/r", p)
        self.assertIn("evading AI detectors", p)

    def test_claude_uses_xml_tags(self):
        p = build(self.TEXT, analyze(self.TEXT), target="claude")
        self.assertIn("<flagged_signals>", p)
        self.assertIn("</text>", p)
        self.assertNotIn("# Role", p)

    def test_korean_prompt(self):
        t = "물론입니다! 이는 시사하는 바가 크다. 비용이 38% 줄었다."
        p = build(t, analyze(t))
        self.assertIn("# 바꾸지 말 것", p)
        self.assertIn("38", p)

    def test_prompt_forbids_evasion(self):
        for lang in ("ko", "en"):
            self.assertTrue("탐지기" in chat_prompt(lang) or "detector" in chat_prompt(lang))

    def test_facts_for_prompt(self):
        f = facts_for_prompt(self.TEXT)
        self.assertIn("12", f["numbers"])
        self.assertEqual(f["urls"], ["https://a.example/r"])


if __name__ == "__main__":
    unittest.main()
