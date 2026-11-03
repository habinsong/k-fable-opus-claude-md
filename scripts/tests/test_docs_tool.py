"""scripts/docs_tool.py 시험. 임시 저장소를 만들어 sync와 check, 위반 검출을 확인한다.

실행: python3 -I -m unittest discover -s scripts/tests -v
"""
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "docs_tool.py"


def load():
    spec = importlib.util.spec_from_file_location("docs_tool_under_test", TOOL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def make_repo(tool, root):
    """검사를 통과하는 최소 저장소: 계열 gpt 아래 모델 m1 하나."""
    u = root / "universal"
    write(u / "contract.md", "# 범용 · 계약\n> 기준일\n\n## 0. 응답 계약\n" + " ".join(tool.CONTRACT_KEYWORDS) + "\n")
    write(u / "ko-core.md", "# 범용 · 한국어 공통\n> 기준일\n\n### 3.1 목표\n" + " ".join(tool.KO_CORE_KEYWORDS) + "\n")
    for d in tool.ALL_DOMAINS:
        ko = d in tool.KO_DOMAINS
        write(u / f"{d}.md",
              f"# 범용 · {d}\n> 기준일\n\n<!-- BEGIN:contract -->\n<!-- END:contract -->\n\n"
              f"## 3. 분야 규칙 — {d}\n본문 {d}\n"
              + ("\n<!-- BEGIN:ko-core -->\n<!-- END:ko-core -->\n" if ko else ""))
    for d in tool.ALL_DOMAINS:
        block = ""
        if d in ("general", "ko-academic"):
            block = "## 2. 이 모델에서 지킬 점\n- 지시를 지킨다.\n"
        write(root / "md" / "gpt" / "m1" / f"{d}.md",
              f"# M1 · {d}\n> 제공자: X · 모델 ID: `m1` · 기준일: 2026-11-03\n\n"
              "<!-- BEGIN:contract -->\n<!-- END:contract -->\n\n"
              f"<!-- BEGIN:model -->\n{block}<!-- END:model -->\n\n"
              "<!-- BEGIN:domain -->\n<!-- END:domain -->\n")
    write(root / "docs" / "README.md", "# docs\n")
    m = root / "docs" / "gpt" / "m1"
    write(m / "README.md", "# M1 색인\n")
    write(m / "sources.md", "# 출처\nhttps://example.com\n")
    write(m / "korean-writing.md", "# 한국어\nhttps://example.com\n")
    for d in tool.DOMAINS:
        if d != "general":
            write(m / "domains" / f"{d}.md", "# 분야\nhttps://example.com\n")


class Base(unittest.TestCase):
    def setUp(self):
        self.tool = load()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.root = root
        make_repo(self.tool, root)
        self.tool.ROOT, self.tool.UNIV = root, root / "universal"
        self.tool.MD, self.tool.DOCS = root / "md", root / "docs"

    def run_tool(self, fn, *args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = fn(*args)
        return code, buf.getvalue()

    def synced(self):
        code, out = self.run_tool(self.tool.sync)
        self.assertEqual(code, 0, out)


class ResearchMarkerTest(unittest.TestCase):
    def setUp(self):
        self.tool = load()

    def labels(self, text, skip_tags=False):
        return " ".join(self.tool.research_hits(text, skip_tags))

    def test_url(self):
        self.assertIn("출처 URL", self.labels("참고 https://a.b"))

    def test_tag(self):
        self.assertIn("근거 수준 태그", self.labels("사실이다 [부분]"))
        self.assertNotIn("근거 수준 태그", self.labels("사실이다 [부분]", skip_tags=True))

    def test_price(self):
        self.assertIn("가격", self.labels("입력 $4"))

    def test_clean_text(self):
        self.assertEqual(self.tool.research_hits("그냥 지침 문장이다."), [])


class InjectTest(unittest.TestCase):
    def test_inject_replaces_block(self):
        tool = load()
        text = "a\n<!-- BEGIN:x -->\nold\n<!-- END:x -->\nb\n"
        self.assertEqual(tool.inject(text, "x", "new"), "a\n<!-- BEGIN:x -->\nnew\n<!-- END:x -->\nb\n")

    def test_inject_missing_marker(self):
        self.assertIsNone(load().inject("no markers", "x", "new"))

    def test_fact_rows(self):
        tool = load()
        text = "### 3.2 시점에 민감한 사실\n문장\n\n| 항목 | 내용 |\n|---|---|\n| A | 내용A |\n| B | 내용B |\n\n### 3.3 다음\n| C | 무시 |\n"
        rows = tool.fact_rows(text)
        self.assertEqual(sorted(rows), ["A", "B"])
        self.assertEqual(rows["A"][1], "내용A")


class SyncCheckTest(Base):
    def test_sync_then_check_passes(self):
        self.synced()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 0, out)

    def test_sync_propagates_model_block_to_siblings(self):
        self.synced()
        web = (self.root / "md/gpt/m1/web.md").read_text(encoding="utf-8")
        self.assertIn("지시를 지킨다.", web)
        ko = (self.root / "md/gpt/m1/ko-literary.md").read_text(encoding="utf-8")
        self.assertIn("지시를 지킨다.", ko)

    def test_domain_part_expands_ko_core_without_markers(self):
        self.synced()
        text = (self.root / "md/gpt/m1/ko-everyday.md").read_text(encoding="utf-8")
        self.assertIn("### 3.1 목표", text)
        self.assertNotIn("BEGIN:ko-core", text)

    def test_url_in_md_is_rejected(self):
        self.synced()
        p = self.root / "md/gpt/m1/web.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n참고 https://example.com\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("출처 URL", out)

    def test_price_and_tag_in_md_are_rejected(self):
        self.synced()
        p = self.root / "md/gpt/m1/app.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n가격 $4 [부분]\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("가격", out)
        self.assertIn("근거 수준 태그", out)

    def test_out_of_sync_block_is_rejected(self):
        self.synced()
        p = self.root / "md/gpt/m1/web.md"
        p.write_text(p.read_text(encoding="utf-8").replace("지시를 지킨다.", "다른 지시."), encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("model 블록이 원본과 다름", out)

    def test_missing_domain_doc_is_error_when_complete(self):
        self.synced()
        (self.root / "md/gpt/m1/ko-everyday.md").unlink()
        self.assertEqual(self.run_tool(self.tool.check, True, False)[0], 1)
        self.assertEqual(self.run_tool(self.tool.check, False, False)[0], 0)

    def test_missing_docs_pair_is_error_when_complete(self):
        self.synced()
        (self.root / "docs/gpt/m1/sources.md").unlink()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("sources.md", out)

    def test_korean_domain_only_for_ko_families(self):
        self.synced()
        extra = self.root / "md" / "claude" / "x"
        write(extra / "ko-academic.md",
              "# X\n> 제공자: Y · 모델 ID: `x` · 기준일: 2026-11-03\n\n"
              "<!-- BEGIN:contract -->\n<!-- END:contract -->\n<!-- BEGIN:model -->\n<!-- END:model -->\n<!-- BEGIN:domain -->\n<!-- END:domain -->\n")
        # claude는 KO_FAMILIES에 있으므로 허용, deepseek 같은 계열은 거부
        bad = self.root / "md" / "deepseek" / "x"
        write(bad / "ko-academic.md", (extra / "ko-academic.md").read_text(encoding="utf-8"))
        code, out = self.run_tool(self.tool.check, False, True)
        self.assertEqual(code, 1)
        self.assertIn("한국어 윤문 분야는", out)

    def test_shared_dir_is_rejected(self):
        self.synced()
        (self.root / "_shared").mkdir()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("_shared", out)

    def test_old_family_root_is_rejected(self):
        self.synced()
        (self.root / "gpt").mkdir()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("옛 위치", out)


class FactTableTest(Base):
    def add_table(self, level="부분", docs_content="내용A"):
        u = self.root / "universal" / "web.md"
        text = u.read_text(encoding="utf-8")
        text += ("\n### 3.2 시점에 민감한 사실\n아래 표는 확정된 사실이 아니라 확인의 출발점이다.\n\n"
                 "| 항목 | 내용 |\n|---|---|\n| A | 내용A |\n")
        u.write_text(text, encoding="utf-8")
        write(self.root / "docs/_common/domain-rules/web.md",
              f"# x\n\n| 항목 | 근거 수준 | 내용 |\n|---|---|---|\n| A | {level} | {docs_content} |\n")

    def errors(self):
        errs = []
        self.tool.check_fact_tables(errs)
        return errs

    def test_matching_tables_pass(self):
        self.add_table()
        self.assertEqual(self.errors(), [])

    def test_content_mismatch(self):
        self.add_table(docs_content="다른 내용")
        self.assertTrue(any("내용이" in e for e in self.errors()))

    def test_invalid_level(self):
        self.add_table(level="아마도")
        self.assertTrue(any("허용값" in e for e in self.errors()))

    def test_missing_hedge_sentence(self):
        self.add_table()
        u = self.root / "universal" / "web.md"
        u.write_text(u.read_text(encoding="utf-8").replace("확정된 사실이 아니라", "사실이다"), encoding="utf-8")
        self.assertTrue(any("명령문이 없음" in e for e in self.errors()))

    def test_row_missing_in_docs(self):
        self.add_table()
        write(self.root / "docs/_common/domain-rules/web.md", "# x\n\n| 항목 | 근거 수준 | 내용 |\n|---|---|---|\n")
        self.assertTrue(any("근거 수준 행 없음" in e for e in self.errors()))


if __name__ == "__main__":
    unittest.main()
