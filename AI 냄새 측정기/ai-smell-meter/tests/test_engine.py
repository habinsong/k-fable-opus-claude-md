"""측정과 교정의 핵심 동작: 보호 구간, 문장 나누기, 점수, 겹침, 분석기, 교정 성질."""
import unittest

import _path  # noqa: F401
from ai_smell.detect import analyze
from ai_smell.fix import polish
from ai_smell.samples import AI_MID, AI_STRONG, GOLDEN, HUMAN, NB, ZW
from ai_smell.textutil import (count_units, detect_lang, mask, protected_spans, sentence_spans)


def ids(a):
    return {f.rule_id for f in a.findings if f.weight > 0 and not f.shadowed}


class Protection(unittest.TestCase):
    def test_spans_cover_code_url_quote_ignore(self):
        t = ("a `x` b\n```\nIn order to\n```\nsee https://e.com/in-order-to c\n> Certainly! quoted\n"
             "<!-- ai-smell:ignore-start -->Certainly! hi<!-- ai-smell:ignore-end -->\nplain")
        m = mask(t, protected_spans(t))
        for needle in ("In order to", "in-order-to", "quoted", "Certainly! hi"):
            self.assertNotIn(needle, m)
        self.assertIn("plain", m)
        self.assertEqual(len(m), len(t))

    def test_findings_skip_protected_text(self):
        t = "```\nCertainly! In order to utilize it.\n```\n\n> Certainly! quoted.\n\nWe read `utilize` today."
        self.assertEqual(analyze(t).findings, [])

    def test_polish_leaves_protected_text_alone(self):
        t = "Certainly! Run `utilize(x)` in order to test.\n\n```\nin order to\n```\n"
        out = polish(t, tier="strong").text
        self.assertIn("`utilize(x)`", out)
        self.assertIn("```\nin order to\n```", out)
        self.assertNotIn("Certainly", out)

    def test_ignore_markers_exclude_ai_specimens(self):
        t = "Plain words. <!-- ai-smell:ignore-start -->Certainly! I hope this helps!<!-- ai-smell:ignore-end -->"
        self.assertEqual(analyze(t).score, 0)

    def test_front_matter_and_markdown_link_target(self):
        t = "---\ntitle: In order to utilize\n---\nSee [docs](https://a.example/utilize-in-order-to) now."
        self.assertEqual(analyze(t).findings, [])


class Sentences(unittest.TestCase):
    def spans(self, t):
        m = mask(t, protected_spans(t))
        return [t[a:b] for a, b in sentence_spans(m)]

    def test_abbreviations_and_decimals(self):
        s = self.spans("Dr. Smith paid 3.5 dollars. He left. Then it ended.")
        self.assertEqual(s[0], "Dr. Smith paid 3.5 dollars.")
        self.assertEqual(len(s), 3)
        self.assertEqual(len(self.spans("Mr. Lee met Dr. Kim at 5 p.m. yesterday.")), 1)

    def test_korean(self):
        self.assertEqual(self.spans("첫 문장이다. 둘째 문장이다! 셋째인가?"), ["첫 문장이다.", "둘째 문장이다!", "셋째인가?"])

    def test_lists_and_colon_lines_split(self):
        s = self.spans("Here are items:\n- one item\n- two items\n\nAfter.")
        self.assertEqual(len(s), 4)

    def test_units_and_lang(self):
        self.assertEqual(count_units("a b `c`"), 3)
        self.assertEqual(detect_lang("안녕하세요 여러분"), "ko")
        self.assertEqual(detect_lang("hello world"), "en")
        self.assertEqual(detect_lang("hello 안녕하세요 world 여러분 반갑습니다 hi"), "mixed")


class Scoring(unittest.TestCase):
    def test_bands(self):
        for lang, t in AI_STRONG.items():
            self.assertGreaterEqual(analyze(t).score, 60, lang)
        for lang, t in AI_MID.items():
            self.assertGreaterEqual(analyze(t).score, 30, lang)
        for name, t in HUMAN.items():
            self.assertLessEqual(analyze(t).score, 15, name)

    def test_more_signals_never_lower_the_score(self):
        base = "The plan is simple and the team knows the steps well enough to start on Monday."
        s0 = analyze(base).score
        s1 = analyze(base + " Certainly! I hope this helps!").score
        s2 = analyze(base + " Certainly! I hope this helps! Let me know if you have any questions.").score
        self.assertLessEqual(s0, s1)
        self.assertLessEqual(s1, s2)

    def test_score_is_bounded(self):
        a = analyze(("Certainly! " + "It's not just a tool, it's a platform. ") * 100)
        self.assertTrue(0 <= a.score <= 100)

    def test_empty_and_whitespace(self):
        for t in ("", "   \n\n ", "!!! ... ???"):
            a = analyze(t)
            self.assertEqual(a.score, 0)
            self.assertEqual(a.findings, [])

    def test_short_text_note(self):
        self.assertTrue(any("불안정" in n for n in analyze("Certainly! Done.").notes))

    def test_overlapping_signals_count_once(self):
        a = analyze("The bridge plays a crucial role in the region today and always.")
        scored = [f for f in a.findings if not f.shadowed and f.weight > 0]
        spans = sorted((f.start, f.end) for f in scored)
        for (s1, e1), (s2, e2) in zip(spans, spans[1:]):
            self.assertLessEqual(e1, s2)

    def test_genre_changes_weight(self):
        t = "이번 글에서는 방법을 살펴보겠습니다. 다음 절에서는 결과를 정리하겠습니다."
        g = analyze(t, genre="general")
        ac = analyze(t, genre="academic")
        self.assertGreater(g.score, ac.score)

    def test_ban_words(self):
        a = analyze("We will circle back on the synergy deck.", ban=["circle back"])
        self.assertIn("user.ban.1", ids(a))

    def test_paragraph_scores_locate_the_problem(self):
        t = "The release went out on Tuesday after two tests.\n\nCertainly! I hope this helps! Let me know if you have questions."
        ps = analyze(t).paragraph_scores
        self.assertEqual(len(ps), 2)
        self.assertGreater(ps[1]["score"], ps[0]["score"])


class Analyzers(unittest.TestCase):
    def test_em_dash_needs_three(self):
        two = "The tool — which is new — works well."
        three = "The tool — which is new — works well. It is fast — really fast."
        self.assertNotIn("any.format.em-dash", ids(analyze(two)))
        self.assertIn("any.format.em-dash", ids(analyze(three)))

    def test_em_dash_pair_becomes_commas(self):
        t = "The tool — which is new — works well. It is fast — really fast. Done — truly."
        out = polish(t, tier="standard").text
        self.assertIn("The tool, which is new, works well.", out)
        self.assertIn("It is fast — really fast.", out)           # 한 줄표는 standard에서 그대로
        self.assertIn("fast, really fast", polish(t, tier="strong").text)

    def test_transition_stack(self):
        t = "Moreover, a is true. Furthermore, b is true. Additionally, c is true. Also d."
        self.assertIn("en.transition.stack", ids(analyze(t)))
        out = polish(t, tier="strong").text
        self.assertNotIn("Furthermore", out)
        self.assertIn("Moreover", out)

    def test_ko_transition_stack(self):
        t = "또한 가가 맞다. 아울러 나나가 맞다. 나아가 다다가 맞다."
        self.assertIn("ko.transition.stack", ids(analyze(t)))

    def test_triples_need_repetition(self):
        one = "We value speed, quality, and trust."
        many = "We value speed, quality, and trust. They offer reach, depth, and scale. It brings focus, clarity, and calm."
        self.assertNotIn("en.structure.triple", ids(analyze(one)))
        self.assertIn("en.structure.triple", ids(analyze(many)))

    def test_same_ending_run(self):
        t = "그는 밥을 먹었다. 그는 길을 걸었다. 그는 문을 열었다. 그는 책을 읽었다. 그는 손을 씻었다."
        self.assertIn("ko.rhythm.same-ending", ids(analyze(t)))

    def test_emotion_pile_in_one_paragraph(self):
        t = "그날 가슴이 먹먹해졌다. 눈시울이 붉어졌고 마음이 무거웠다."
        self.assertIn("ko.emotion.told", ids(analyze(t, genre="literary")))
        self.assertNotIn("ko.emotion.told", ids(analyze("그날 가슴이 먹먹해졌다.")))

    def test_register_mix(self):
        mixed = "안녕하세요. 어제 보내 주신 자료 잘 받았습니다. 내일 회의에서 보자. 그럼 수고해."
        clean = "안녕하세요. 어제 보내 주신 자료 잘 받았습니다. 내일 회의에서 뵙겠습니다."
        self.assertIn("ko.register.mixed", ids(analyze(mixed)))
        self.assertNotIn("ko.register.mixed", ids(analyze(clean)))
        quoted = '그는 "내일 보자."라고 말했다. 나는 "알겠습니다."라고 답했습니다. 우리는 웃었다.'
        self.assertNotIn("ko.register.mixed", ids(analyze(quoted)))

    def test_exclamations(self):
        self.assertIn("any.format.exclaim", ids(analyze("좋아요! 최고예요! 정말 멋져요! 가요!")))
        self.assertNotIn("any.format.exclaim", ids(analyze("좋아요! 오늘은 비가 옵니다. 우산을 챙기세요.")))

    def test_summary_closer(self):
        t = "The test failed on Monday. The fix shipped on Tuesday. Ultimately, the process worked."
        self.assertIn("en.structure.summary-closer", ids(analyze(t)))


class Polish(unittest.TestCase):
    def test_golden(self):
        for name, src, tier, want in GOLDEN:
            with self.subTest(name):
                self.assertEqual(polish(src, tier=tier).text, want)

    def test_idempotent_and_non_increasing(self):
        for tier in ("safe", "standard", "strong"):
            for key, t in {**AI_STRONG, **{f"m{k}": v for k, v in AI_MID.items()}}.items():
                once = polish(t, tier=tier)
                twice = polish(once.text, tier=tier)
                with self.subTest(tier=tier, key=key):
                    self.assertEqual(twice.text, once.text)
                    self.assertLessEqual(once.after.score, once.before.score)

    def test_tiers_nest(self):
        for t in AI_STRONG.values():
            n = [len(polish(t, tier=x).edits) for x in ("safe", "standard", "strong")]
            self.assertLessEqual(n[0], n[1])
            self.assertLessEqual(n[1], n[2])

    def test_human_text_is_untouched_at_standard(self):
        for name, t in HUMAN.items():
            self.assertEqual(polish(t, tier="standard").text, t, name)

    def test_invalid_tier(self):
        with self.assertRaises(ValueError):
            polish("x", tier="none")

    def test_crlf_is_preserved(self):
        t = "Certainly! In order to run it.\r\n\r\nLet me know if you have questions.\r\n"
        r = polish(t, tier="standard")
        self.assertEqual(r.output, "To run it.\r\n")

    def test_never_returns_empty_for_nonempty_input(self):
        r = polish("\U0001F680\U0001F680\U0001F680", tier="strong")
        self.assertEqual(r.text, "\U0001F680\U0001F680\U0001F680")
        self.assertTrue(r.notes)

    def test_recapitalization_only_at_sentence_start(self):
        out = polish("It works. In today's fast-paced digital world, apps matter.", tier="standard").text
        self.assertEqual(out, "It works. Apps matter.")
        mid = polish("We think that it is important to note that apps matter.", tier="standard").text
        self.assertIn("apps matter", mid)

    def test_hygiene_characters(self):
        self.assertEqual(polish("a" + ZW + "b" + NB + "c", tier="safe").text, "ab c")

    def test_utm_variants(self):
        cases = {
            "See https://a.example/x?utm_source=chatgpt.com&k=1 now.": "See https://a.example/x?k=1 now.",
            "See https://a.example/x?k=1&utm_source=openai now.": "See https://a.example/x?k=1 now.",
            "See https://a.example/x?utm_source=chatgpt.com now.": "See https://a.example/x now.",
        }
        for src, want in cases.items():
            self.assertEqual(polish(src, tier="safe").text, want)

    def test_double_passive_table(self):
        cases = {"보여진다": "보인다", "보여지는": "보이는", "쓰여진": "쓰인", "불리워진다": "불린다", "잊혀졌다": "잊혔다",
                 "열려진다": "열린다", "놓여진": "놓인", "되어진다": "된다", "되어졌다": "되었다", "되어질": "될"}
        for src, want in cases.items():
            self.assertEqual(polish(f"결과가 {src}", tier="standard").text, f"결과가 {want}", src)

    def test_double_passive_ignores_look_alikes(self):
        for t in ("돼지는 풀을 먹는다", "주어진 시간이 짧다", "이루어진 일이다", "만들어진 물건이다"):
            self.assertEqual(polish(t, tier="standard").text, t)

    def test_nominal_verb(self):
        self.assertEqual(polish("분석을 진행한다.", tier="standard").text, "분석한다.")
        self.assertEqual(polish("회의를 진행한다.", tier="standard").text, "회의를 진행한다.")

    def test_neg_parallel_fix_variants(self):
        cases = {
            "It isn't just a phone but a camera.": "It is a camera.",
            "This is not only fast but also cheap.": "This is not only fast but also cheap.",
            "It's not just a tool, it's a platform.": "It's a platform.",
            "It's not just 3 tools, it's a platform.": "It's not just 3 tools, it's a platform.",
        }
        for src, want in cases.items():
            self.assertEqual(polish(src, tier="strong").text, want, src)

    def test_participial_tail_keeps_facts(self):
        keep = "Sales rose, demonstrating a 12% gain."
        self.assertEqual(polish(keep, tier="strong").text, keep)
        self.assertEqual(polish("Sales rose 12%, demonstrating strong growth.", tier="strong").text, "Sales rose 12%.")
        self.assertEqual(polish("Sales rose, highlighting the need for growth.", tier="strong").text, "Sales rose.")

    def test_empty_bullet_is_removed(self):
        t = "- Certainly! Let me know if you have any questions.\n- Real item here.\n"
        self.assertEqual(polish(t, tier="standard").text, "- Real item here.\n")

    def test_korean_ai_smell_fixes(self):
        cases = {
            "이 작품은 서사에 깊이를 더한다.": "이 작품은 서사에 더 깊게 한다.",
            "팀원들의 행복 지수가 올라갔다.": "팀원들의 행복도가 올라갔다.",
            "밀도 있는 구성을 보여준다.": "짜임새 있는 구성을 보여준다.",
            "우리 과제로 오류율을 잰다.": "우리 과제로 오류율을 비교한다.",
            "새로운 기술을 전파한다.": "새로운 기술을 전달한다.",
            "파일이 자동으로 생성된다.": "파일이 알아서 생성된다.",
            "두 모델을 짝지어 비교한다.": "두 모델을 맞추어 비교한다.",
            "두 요소가 쌍을 이루어 나타난다.": "두 요소가 함께 나타난다.",
            "문체 신호를 감지하여 분석한다.": "문체 특징을 감지하여 분석한다.",
            "코드에 값을 박아 넣는다.": "코드에 값을 직접 넣는다.",
        }
        for src, want in cases.items():
            self.assertEqual(polish(src, tier="standard").text, want, src)

    def test_english_ai_smell_fixes(self):
        cases = {
            "The update adds depth to our workflow.": "The update deepens our workflow.",
            "Speed, paired with accuracy, is crucial.": "Speed, with accuracy, is crucial.",
            "We should gauge the impact of the rollout.": "We should assess the impact of the rollout.",
            "The announcement sends a clear signal that change is coming.": "The announcement indicates that change is coming.",
            "The updates propagate across the cluster.": "The updates spread across the cluster.",
            "The pipeline automatically generates the report.": "The pipeline generates the report.",
            "The employee happiness index improved this quarter.": "The employee happiness level improved this quarter.",
            "The article has high information density.": "The article has rich detail.",
            "The key is hardcoded directly into the script.": "The key is written directly into the script.",
            "This discovery represents a paradigm shift.": "This discovery represents a major shift.",
            "The design seamlessly integrates with existing apps.": "The design integrates with existing apps.",
        }
        for src, want in cases.items():
            self.assertEqual(polish(src, tier="standard").text, want, src)


if __name__ == "__main__":
    unittest.main()
