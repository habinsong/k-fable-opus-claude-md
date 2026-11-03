"""scripts/ko_style_probe.py 회귀 시험.

실행: python3 -I -m unittest discover -s scripts/tests -v
"""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "ko_style_probe.py"


def load():
    spec = importlib.util.spec_from_file_location("ko_style_probe", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


kp = load()


def neg(text):
    return kp.measure(text)["근거 있는 신호(1천자당)"]["부정 대구 후보"]["횟수"]


class RegisterTest(unittest.TestCase):
    def test_aninda_is_not_formal(self):
        # 회귀: '아니다'가 '니다'로 끝나 합쇼체로 분류되던 버그
        self.assertEqual(kp.register("재능이 아니다."), "평서(한다체)")

    def test_registers(self):
        self.assertEqual(kp.register("회의는 세 시입니다."), "합쇼체")
        self.assertEqual(kp.register("자료는 읽어 와요."), "해요체")
        self.assertEqual(kp.register("그는 문을 열었다."), "평서(한다체)")
        self.assertEqual(kp.register("늦지 마."), "반말")

    def test_mixed_paragraph_detected(self):
        out = kp.measure("안녕하세요. 늦지 마. 자료는 읽어 와요.")
        self.assertGreaterEqual(out["말투"]["존대와 평어가 섞인 문단"], 1)

    def test_plain_paragraph_not_mixed(self):
        out = kp.measure("그는 문을 열었다. 방은 조용했다.")
        self.assertEqual(out["말투"]["존대와 평어가 섞인 문단"], 0)


class NegativeContrastTest(unittest.TestCase):
    def test_counts_a_not_b(self):
        self.assertEqual(neg("이것은 도구가 아니라 습관이다."), 1)

    def test_excludes_ordinary_conjunction(self):
        self.assertEqual(neg("이 방법은 좋을 뿐만 아니라 값도 싸다."), 0)
        self.assertEqual(neg("값이 싼 것뿐 아니라 맛도 좋다."), 0)

    def test_consecutive_negation_run(self):
        out = kp.measure("재능이 아니다. 운도 아니다. 노력이다.")
        self.assertEqual(out["연속 부정 뒤 결론 후보"]["'~아니다' 문장 연속 최대"], 2)

    def test_no_negation_run(self):
        out = kp.measure("노력이다. 시간이 걸린다.")
        self.assertEqual(out["연속 부정 뒤 결론 후보"]["'~아니다' 문장 연속 최대"], 0)


class StructureTest(unittest.TestCase):
    def test_triple_list(self):
        self.assertEqual(kp.triple_lists(["사과, 배, 포도를 샀다."]), 1)
        self.assertEqual(kp.triple_lists(["사과와 배를 샀다."]), 0)
        self.assertEqual(kp.triple_lists(["사과, 배를 샀다."]), 0)

    def test_duty_includes_passive_form(self):
        # 회귀: '확보되어야 한다'를 놓치던 누락
        out = kp.measure("효율과 정확성이 확보되어야 한다. 점검을 해야 한다.")
        self.assertEqual(out["근거 있는 신호(1천자당)"]["당위 서술"]["횟수"], 2)

    def test_triple_list_with_long_last_part(self):
        self.assertEqual(kp.triple_lists(["효율성, 정확성, 그리고 확장성이 모두 확보되어야 한다."]), 1)
        self.assertEqual(kp.triple_lists(["사과, 배, 아주 길고 복잡하게 이어지는 마지막 덩어리라서 나열이 아니다."]), 0)

    def test_code_fence_ignored(self):
        text = "평범한 문장이다.\n```\n이것은 도구가 아니라 코드다\n```\n"
        self.assertEqual(neg(text), 0)

    def test_markdown_markers_counted_as_format(self):
        out = kp.measure("# 제목\n- 항목 하나\n**굵게** 쓴다.\n")
        self.assertEqual(out["서식 신호"]["제목 줄"], 1)
        self.assertEqual(out["서식 신호"]["불릿/번호 줄"], 1)
        self.assertEqual(out["서식 신호"]["굵은 글씨 쌍"], 1)

    def test_emotion_words(self):
        out = kp.measure("그날 그녀는 가슴이 먹먹해졌다. 정말 외로웠다.")
        self.assertGreaterEqual(out["감정 직접 서술 후보(AI 특유 근거 없음)"]["횟수"], 2)

    def test_empty_text_does_not_crash(self):
        out = kp.measure("")
        self.assertEqual(out["문장수"], 0)


class CliTest(unittest.TestCase):
    def run_cli(self, *args, stdin=None):
        return subprocess.run([sys.executable, "-I", str(SCRIPT), *args], input=stdin,
                              capture_output=True, text=True)

    def test_no_args_is_usage_error(self):
        self.assertEqual(self.run_cli().returncode, 2)

    def test_missing_file(self):
        self.assertEqual(self.run_cli("/no/such/file.txt").returncode, 1)

    def test_json_from_stdin(self):
        r = self.run_cli("-", "--json", stdin="이것은 도구가 아니라 습관이다.")
        self.assertEqual(r.returncode, 0)
        self.assertEqual(json.loads(r.stdout)["문장수"], 1)

    def test_file_input(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "a.txt"
            p.write_text("그는 문을 열었다. 방은 조용했다.", encoding="utf-8")
            r = self.run_cli(str(p))
            self.assertEqual(r.returncode, 0)
            self.assertIn("문장수: 2", r.stdout)


if __name__ == "__main__":
    unittest.main()
