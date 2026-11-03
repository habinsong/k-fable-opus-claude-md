"""규칙 데이터의 무결성과, 규칙마다 맞는 문장 하나와 안 맞는 문장 하나."""
import unittest

import _path  # noqa: F401
from ai_smell.detect import analyze
from ai_smell.model import CATEGORIES, GRADES, TIER_RANK
from ai_smell.rules import load_rules

# (규칙 id, 걸려야 하는 글, 걸리면 안 되는 글)
CASES = [
    ("en.residue.opener", "Certainly! Here is the plan for today.", "Certainly the plan is sound."),
    ("en.residue.hope-helps", "That is the fix. I hope this helps!", "We hope this approach helps teams."),
    ("en.residue.let-me-know", "Done. Let me know if you have any questions.", "She never let me know."),
    ("en.residue.as-an-ai", "As an AI language model, I cannot browse.", "As an engineer, I can browse."),
    ("en.residue.cutoff", "As of my last knowledge cutoff, the API was v2.", "As of Monday, the API is v3."),
    ("en.sycophancy.praise", "Great question! The answer is yes.", "The question was great fun to answer."),
    ("en.sycophancy.right", "You're absolutely right, I missed that.", "You are right about the date only."),
    ("en.placeholder.bracket", "Dear [Your Name], thanks.", "Dear Ana, see [1] for details."),
    ("any.markup.oaicite", "The study found this.:contentReference[oaicite:0]{index=0}", "The study found this."),
    ("any.markup.utm", "See https://a.example/x?utm_source=chatgpt.com now.", "See https://a.example/x?ref=1 now."),
    ("en.puffery.testament", "The bridge stands as a testament to the city.", "He gave his testament in court."),
    ("en.puffery.vital-role", "Water plays a vital role in cooking.", "Water boils at 100 degrees."),
    ("en.puffery.todays-world", "In today's fast-paced digital world, apps matter.", "Today we shipped the app."),
    ("en.puffery.paving", "This paves the way for new tools.", "He paved the driveway."),
    ("en.structure.neg-parallel", "It's not just a tool, it's a platform.", "It's not a tool. It's slow."),
    ("en.structure.neg-parallel-about", "This isn't about speed, it's about trust.", "This isn't about money."),
    ("en.structure.participial-tail", "Sales rose, highlighting the need for growth.", "Sales rose, and growth followed."),
    ("en.structure.copula", "The park serves as a hub for the town.", "The server serves requests."),
    ("en.structure.boasts", "The hotel boasts a pool and a bar.", "He boasts about nothing."),
    ("en.hedging.note-that", "It is important to note that the test failed.", "It is important to the test."),
    ("en.hedging.potentially", "This could potentially break the build.", "This could break the build."),
    ("en.hedging.wordy", "We did it in order to save time.", "We did it to save time."),
    ("en.signpost.lets-pure", "Let's dive in. The first step is setup.", "We dove in last week."),
    ("en.signpost.heres-the-thing", "Here's the thing: it failed.", "Here is a thing I found."),
    ("en.attribution.vague", "Experts say the market will grow.", "Experts at Acme (Kim, 2020) say it grew."),
    ("en.vocab.delve", "We delve into the data.", "We dig into the data."),
    ("en.vocab.pivotal", "A pivotal moment in the match.", "A key moment in the match."),
    ("en.vocab.utilize", "We utilize the cache.", "We use the cache."),
    ("ko.residue.opener", "물론입니다! 계획은 다음과 같습니다.", "물론 계획은 있다."),
    ("ko.residue.hope-helps", "이상입니다. 도움이 되었기를 바랍니다.", "그 책은 도움이 되었다."),
    ("ko.residue.ask-more", "이상입니다. 궁금한 점이 있으시면 말씀해 주세요.", "궁금한 점이 있었지만 묻지 않았다."),
    ("ko.sycophancy.praise", "좋은 질문입니다! 답은 그렇다.", "질문이 좋았다."),
    ("ko.puffery.implication", "이 결과는 시사하는 바가 크다.", "이 결과는 표 2에 있다."),
    ("ko.puffery.noteworthy", "이 점은 주목할 만하다.", "그는 주목을 받았다."),
    ("ko.puffery.new-horizon", "연구는 새로운 지평을 열었다.", "새 길을 걸었다."),
    ("ko.puffery.grand-background", "급변하는 시대에 기업은 적응해야 한다.", "시대는 바뀌었다."),
    ("ko.structure.neg-simple", "그것은 단순한 슬픔이 아니라 그리움이었다.", "그것은 슬픔이었다."),
    ("ko.structure.neg-general", "문제는 속도가 아니라 신뢰다.", "문제는 속도다."),
    ("ko.structure.beyond", "도구를 넘어 문화로 자리 잡았다.", "도구를 샀다."),
    ("ko.hedging.rago", "이것은 핵심 요소라고 할 수 있다.", "이것은 핵심 요소다."),
    ("ko.hedging.dago", "성공은 균형에 달려 있다고 할 수 있다.", "성공은 균형에 달려 있다."),
    ("ko.hedging.can-do", "이 도구를 사용하는 것이 가능하다.", "이 도구를 쓸 수 있다."),
    ("ko.hedging.nominal-verb", "검토를 진행한다.", "검토한다."),
    ("ko.trans.double-passive", "결과가 보여진다.", "결과가 보인다."),
    ("ko.trans.double-passive-doe", "비용이 감소되어진다.", "비용이 감소된다."),
    ("ko.vocab.eval-b", "혁신적인 방법을 썼다.", "새로운 방법을 썼다."),
    ("ko.structure.postposed", "그는 떠났다, 조용히.", "그는 떠났다. 조용히 문을 닫았다."),
    ("ko.sycophancy.apology-thanks",
     "죄송합니다. 감사합니다. 정말 감사합니다. 죄송합니다.", "죄송합니다. 늦었습니다."),
    ("ko.puffery.deohada", "이 소스는 요리에 깊이를 더한다.", "숫자 2에 3을 더한다."),
    ("ko.vocab.jjak", "이 둘은 완벽한 짝을 이룬다.", "신발 한 짝을 잃어버렸다."),
    ("ko.vocab.ssang", "두 단어가 쌍을 이루어 나타난다.", "쌍안경으로 먼 곳을 보았다."),
    ("ko.trans.jaeda", "우리는 시스템의 가치를 잰다.", "줄자로 방의 길이를 잰다."),
    ("ko.vocab.sinho", "문체 신호를 감지하여 분석한다.", "신호등 파란불에 건넜다."),
    ("ko.trans.jeonpa", "소식이 빠르게 전파되었다.", "라디오 전파를 수신했다."),
    ("ko.trans.jadong", "모든 설정은 자동으로 반영된다.", "자동차가 지나갔다."),
    ("ko.puffery.jisu", "팀원들의 행복 지수가 올라갔다.", "지수 함수를 배웠다."),
    ("ko.puffery.mildo", "그의 글은 높은 정보 밀도를 자랑한다.", "인구 밀도를 조사했다."),
    ("ko.vocab.bakda", "코드에 값을 박아 넣는다.", "벽에 못을 박았다."),
    ("en.puffery.adds-depth", "The backstory adds depth to the narrative.", "He adds milk to his morning tea."),
    ("en.structure.paired-with", "Speed, paired with accuracy, is crucial.", "They worked in pairs on the assignment."),
    ("en.vocab.gauge", "We need to gauge the impact of this change.", "The technician checked the oil gauge."),
    ("en.puffery.signal", "The statement sends a clear signal that policy is changing.", "The antenna picked up a weak radio signal."),
    ("en.vocab.propagate", "The error will propagate across the nodes.", "Sound cannot propagate without matter."),
    ("en.vocab.seamless-action", "The plugin seamlessly integrates with the editor.", "The dress had a seamless design."),
    ("en.puffery.abstract-index", "The happiness index reached a new peak.", "The Dow Jones stock index reached a new peak."),
    ("en.puffery.density", "The summary has high information density.", "Lead has high physical density."),
    ("en.vocab.hardcode", "The secret key was hardcoded directly into the script.", "She baked cookies directly on the tray."),
    ("en.puffery.paradigm-shift", "This represents a paradigm shift in computing.", "The night shift started at eight."),
    ("en.vocab.automatically", "The tool automatically generates the summary.", "The automatic watch kept good time."),
]


class RuleIntegrity(unittest.TestCase):
    def test_load_and_unique(self):
        rules = load_rules()
        self.assertGreaterEqual(len(rules), 150)
        self.assertEqual(len({r.id for r in rules}), len(rules))

    def test_fields_are_valid(self):
        for r in load_rules():
            self.assertIn(r.category, CATEGORIES, r.id)
            self.assertIn(r.grade, GRADES, r.id)
            self.assertIn(r.tier, TIER_RANK, r.id)
            self.assertTrue(r.note.strip(), r.id)
            self.assertIn(r.lang, ("ko", "en", "any"), r.id)
            self.assertTrue(r.id.startswith(("en.", "ko.", "any.")), r.id)

    def test_fix_rules_have_replacement(self):
        for r in load_rules():
            if r.tier != "none":
                self.assertIsNotNone(r.repl, f"{r.id}: tier가 있는데 repl이 없다")
            if r.scope == "sentence":
                self.assertEqual(r.repl, "", f"{r.id}: 문장 삭제는 repl이 빈 문자열이어야 한다")

    def test_no_pattern_matches_empty_string(self):
        for r in load_rules():
            self.assertIsNone(r.pattern.fullmatch(""), r.id)

    def test_language_split_is_reasonable(self):
        rules = load_rules()
        self.assertGreaterEqual(sum(r.lang == "ko" for r in rules), 40)
        self.assertGreaterEqual(sum(r.lang == "en" for r in rules), 80)

    def test_lang_filter(self):
        self.assertTrue(all(r.lang in ("ko", "any") for r in load_rules("ko")))
        self.assertTrue(all(r.lang in ("en", "any") for r in load_rules("en")))


class RulePositiveNegative(unittest.TestCase):
    def test_cases(self):
        ids = {r.id for r in load_rules()}
        for rid, pos, neg in CASES:
            self.assertIn(rid, ids, f"규칙이 없다: {rid}")
            hit = {f.rule_id for f in analyze(pos).findings}
            miss = {f.rule_id for f in analyze(neg).findings}
            with self.subTest(rule=rid):
                self.assertIn(rid, hit, f"걸려야 한다: {pos!r}")
                self.assertNotIn(rid, miss, f"걸리면 안 된다: {neg!r}")


class MinCountAndCluster(unittest.TestCase):
    def test_min_count_gates_translationese(self):
        one = analyze("그는 도시에 대해 말했다.")
        four = analyze("도시에 대해 말했다. 강에 대해 썼다. 길에 대해 물었다. 집에 대한 이야기를 했다.")
        self.assertNotIn("ko.trans.daehan", {f.rule_id for f in one.findings})
        self.assertIn("ko.trans.daehan", {f.rule_id for f in four.findings})

    def test_cluster_gates_common_words(self):
        alone = analyze("The design is robust.")
        pair = analyze("The design is robust and seamless in practice.")
        self.assertNotIn("en.vocab.robust", {f.rule_id for f in alone.findings})
        self.assertIn("en.vocab.robust", {f.rule_id for f in pair.findings})

    def test_info_rules_are_not_scored(self):
        a = analyze("자료를 통해 확인했다. 방법을 통해 얻었다. 이것이다. 저것이다.")
        info = [f for f in a.findings if f.rule_id in ("ko.trans.tonghae", "ko.trans.geosida")]
        self.assertTrue(info)
        self.assertTrue(all(f.weight == 0 for f in info))
        self.assertEqual(a.score, 0)


if __name__ == "__main__":
    unittest.main()
