"""한국어: 챗봇 잔재와 아첨, 빈 자리표시자. 글의 내용이 아니라 대화의 껍데기를 잡는다."""
from __future__ import annotations

from .. import fixers as fx
from .build import R

T = r"[^.!?\n]*[.!?]"

RULES = [
    R("ko.residue.opener", "ko", "residue", "A",
      r"^[ \t]*(?:물론(?:입니다|이죠|이지요|이에요)[!.]|(?:알겠습니다|그럼요|당연하죠|좋습니다)!)[ \t]+(?=\S)",
      "챗봇식 수락 서두.", tier="standard", repl="", sugg="서두를 지우고 내용으로 시작한다."),
    R("ko.residue.hope-helps", "ko", "residue", "A",
      r"도움이\s*(?:되|됐)(?:셨|었)?(?:기를|길|으면|면)\s*(?:바랍니다|바라요|바랄게요|좋겠습니다|좋겠어요)" + T,
      "챗봇식 맺음 인사.", tier="standard", repl="", scope="sentence", guard=fx.in_tail,
      sugg="맺음 인사를 지운다."),
    R("ko.residue.ask-more", "ko", "residue", "A",
      r"(?:추가(?:로)?|더|다른)?\s*(?:궁금하신|궁금한|필요하신|필요한|수정이\s*필요한|알고\s*싶은)\s*"
      r"(?:점|부분|사항|내용|것)(?:이|은)?\s*(?:있으시면|있으면|있다면|있으신\s*경우|있으실\s*경우)" + T,
      "더 도울 일을 묻는 맺음.", tier="standard", repl="", scope="sentence", guard=fx.in_tail),
    R("ko.residue.anytime", "ko", "residue", "A",
      r"언제든(?:지)?\s*(?:편하게\s*)?(?:말씀해|물어봐|문의해|연락해|질문해|알려|연락|문의|말씀)\s*(?:주세요|주십시오|주시기\s*바랍니다|줘요)"
      + T, "'언제든 말씀하세요' 맺음.", tier="standard", repl="", scope="sentence", guard=fx.in_tail),
    R("ko.residue.lead-in", "ko", "residue", "B",
      r"(?:아래|다음)(?:와|과)\s*같이\s*(?:정리|작성|수정|요약|안내|설명|개선)(?:해\s*)?"
      r"(?:드리겠습니다|드립니다|드릴게요|했습니다|하였습니다|해\s*보겠습니다)[^.!?\n:]*[:.]",
      "결과물 앞의 안내 문장.", tier="standard", repl="", scope="sentence"),
    R("ko.residue.revised-label", "ko", "residue", "A",
      r"^[ \t]*(?:수정|윤문|교정|개선|정리)(?:된|한)\s*(?:버전|문장|글|내용|본)[^\n]{0,30}[:：][ \t]*\n+",
      "결과물 앞의 이름표 줄.", tier="standard", repl=""),
    R("ko.residue.as-ai", "ko", "residue", "A",
      r"(?:AI로서|인공지능으로서|AI\s*언어\s*모델로서|언어\s*모델로서|저는\s*(?:AI|인공지능)(?:이기\s*때문에|라서|입니다)|"
      r"인공지능\s*언어\s*모델)" + T, "모델 자기소개.", sugg="지우고, 그 문장이 막고 있던 주장이 아직 유효한지 본다."),
    R("ko.residue.confusion", "ko", "residue", "A",
      r"(?:혼란|불편)을\s*드려\s*(?:죄송합니다|죄송해요|사과드립니다)" + T,
      "판에 박힌 사과.", tier="standard", repl="", scope="sentence"),
    R("ko.sycophancy.praise", "ko", "sycophancy", "A",
      r"(?:정말\s*|아주\s*)?(?:좋은|훌륭한|흥미로운|멋진|날카로운|중요한)\s*(?:질문|지적|생각|관점|접근)"
      r"(?:이에요|입니다|이네요|이군요|이십니다|이시네요)[!.]?",
      "질문을 칭찬하며 시작한다.", tier="standard", repl="", scope="sentence", sugg="지우고 바로 답한다."),
    R("ko.sycophancy.right", "ko", "sycophancy", "B",
      r"(?:정확(?:합니다|해요)|맞는\s*말씀(?:입니다|이에요)|정확히\s*맞습니다)!",
      "확인하기 전에 먼저 동의한다."),
    R("ko.sycophancy.apology-thanks", "ko", "sycophancy", "B",
      r"(?:정말|진심으로|너무)?\s*(?:죄송합니다|죄송해요|미안합니다|미안해요|감사합니다|감사해요|고맙습니다|고마워요)",
      "사과와 감사가 한 글에 여러 번 겹친다.", w=0.3, min_count=3, sugg="사과와 감사는 한 번, 짧게."),
    R("ko.placeholder.bracket", "ko", "placeholder", "A",
      r"\[(?:이름|회사명|담당자|날짜|제목|링크|URL|연락처|주소|전화번호|이메일|내용|여기에)[^\]\n]{0,20}\]",
      "채우지 않은 자리표시자.", sugg="채우거나 줄을 지운다."),
]
