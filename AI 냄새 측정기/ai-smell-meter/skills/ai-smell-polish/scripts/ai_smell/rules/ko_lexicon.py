"""한국어: 번역투, 과다 어휘. 가중치는 실측이 있는 것만 높다.

im-not-ai의 자체 보고(사람 60편 대 AI 60편)에서 '~를 통해'와 '~것이다'는 사람이 더 많이 썼다.
그래서 이 둘은 점수에 넣지 않고 참고(info)로만 보여 준다(docs/research.md 4절).
"""
from __future__ import annotations

from .. import fixers as fx
from .build import KB, R

PASSIVE_STEM = r"(?P<stem>보여|쓰여|불리워|불려|잊혀|읽혀|닫혀|열려|놓여|나뉘어|섞여|바뀌어|쌓여|묶여)"
PASSIVE_END = r"(?P<end>진다|지는|진|졌|지며|지고|지면|질|짐|지게|지도록|지기|져)"
SINO_B = r"(?:시사|규명|기여)"
SINO_C = r"(?:도모|제고|모색|극대화|고도화|견인|선도|조명|야기|초래|담보|천명|영위|체계화|내재화|활성화)"
END = r"(?:하|한|했|합|함|할|해)[가-힣]*"
EVAL_B = (r"혁신적(?:인|으로)?|획기적(?:인|으로)?|비약적(?:인|으로)?|괄목할\s*만한|괄목할\s*성장|독보적(?:인)?|"
          r"무궁무진|지대한|무한한\s*가능성")
EVAL_C = r"압도적(?:인|으로)?|탁월(?:한|하게)|눈부신|놀라운|방대한|심오한|다채로운"

RULES = [
    R("ko.trans.daehan", "ko", "translationese", "C", r"에\s*대(?:해서?|하여|한)(?![가-힣])",
      "'~에 대해/대한' 번역투.", w=0.25, min_count=4, sugg="을/를로 바꾼다."),
    R("ko.trans.isseo", "ko", "translationese", "C", r"에\s*있어(?:서의|서는|서도|서)?(?![가-힣])",
      "'~에 있어서' 번역투.", w=0.4, min_count=2, sugg="'~에서'로 바꾼다."),
    R("ko.trans.euihae", "ko", "translationese", "C", r"에\s*의(?:해서?|하여|한)(?![가-힣])",
      "'~에 의해' 번역투.", w=0.3, min_count=3, sugg="행위자를 주어로 세운다."),
    R("ko.trans.inhae", "ko", "translationese", "C", r"(?:으로|로)\s*인(?:해서?|하여|한)(?![가-힣])",
      "'~로 인해' 번역투.", w=0.3, min_count=3, sugg="'~해서', '~때문에'로 푼다."),
    R("ko.trans.tonghae", "ko", "info", "C", r"[을를]\s*통(?:해서?|하여)(?![가-힣])",
      "'~를 통해'. 사람 글에서 오히려 더 많이 나와 점수에 넣지 않는다.", w=0.0),
    R("ko.trans.geosida", "ko", "info", "C", r"것(?:이다|입니다)(?![가-힣])",
      "'~것이다'. 사람 글에서 오히려 더 많이 나와 점수에 넣지 않는다.", w=0.0),
    R("ko.trans.double-passive-doe", "ko", "translationese", "C", r"(?P<stem>되어)" + PASSIVE_END,
      "'되어지다'. 비문으로 단정하지는 않지만 '되다'가 읽기 쉽다.", w=0.4, tier="standard",
      repl=fx.double_passive, genre={"academic": 0.6}),
    R("ko.trans.double-passive", "ko", "translationese", "C",
      KB + PASSIVE_STEM + PASSIVE_END,
      "'-어지다'가 겹친 피동. 비문으로 단정하지는 않지만 단순형이 읽기 쉽다.", w=0.4, tier="standard",
      repl=fx.double_passive, genre={"academic": 0.6}),
    R("ko.trans.such-as", "ko", "translationese", "C", r"[와과]\s*같은(?![가-힣])", "'~와 같은' (such as) 번역투.",
      w=0.25, min_count=2),
    R("ko.trans.in-order", "ko", "translationese", "C", r"(?:하기|하는\s*데)\s*(?:위해서는|있어서?)(?![가-힣])",
      "'~하기 위해서는', '~하는 데 있어' 번역투.", w=0.3, min_count=2),
    R("ko.trans.demonstrative", "ko", "info", "C", r"(?<![가-힣])(?:이러한|이와\s*같은|그러한)(?![가-힣])",
      "'이러한' 지시어 반복. 참고용이다.", w=0.0),
    R("ko.trans.gajigo", "ko", "translationese", "C", r"(?:가지고|갖고)\s*있(?:다|는|습니다|으며|고|어)",
      "'가지고 있다' 번역투.", w=0.3, min_count=2, sugg="'있다', '갖췄다'로."),
    R("ko.trans.one-of", "ko", "translationese", "C", r"중\s*하나(?:이다|입니다|다|로|이며)",
      "'~중 하나' 번역투.", w=0.3, min_count=2),
    R("ko.trans.case", "ko", "translationese", "C", r"의\s*경우(?:에는|에도|에)?", "'~의 경우' 반복.", w=0.2,
      min_count=4),
    R("ko.trans.jeok", "ko", "translationese", "C", r"(?<![목표과지사])적(?:인|으로|이다|이며)(?![가-힣])",
      "'~적' 체인.", w=0.12, min_count=10),
    R("ko.trans.jaeda", "ko", "translationese", "B",
      r"(?P<lead>(?:신호|비용|격차|오류율|성능|정확도|전후|지연|수치|효과|차이|역량|품질|가치|확률|영향|밀도|결과)[을를]?\s*(?:직접|먼저|다시|실제로)?\s*|(?<=전후를\s)|(?<=차이를\s)|(?<=격차를\s))(?P<v>재(?:다|고|며|면|지|어|어서|어야|어도|는)|잰(?:다|다는|다면)?|쟀(?:다|으며|고|지만)?|잽(?:니다|니까)?|잴\s*(?:수)?)",
      "'재다': 물리적 길이가 아닌 추상적 격차·비용·오류율·수치를 '재다'로 표현한 번역투.",
      w=0.7, tier="standard", repl=fx.jaeda,
      sugg="'재다' 대신 '비교하다', '측정하다', '확인하다'로 바꾼다."),
    R("ko.trans.jeonpa", "ko", "translationese", "B",
      r"(?P<lead>(?:영향|가치|지식|정보|문화|소식|기술|효과|메시지|사상|소문)[이가은는을를]?\s*(?:빠르게|널리|쉽게|직접)?\s*)전파(?P<end>한다|했다|하며|하고|하여|되는|된다|되었다|되었으며|되었고|되면서|할|자|이|는)",
      "'전파하다/전파되다': 확산·전달·공유를 기계적으로 '전파(propagate/disseminate)'로 쓴 번역투.",
      w=0.6, tier="standard", repl=fx.jeonpa,
      sugg="'전파하다' 대신 '전달하다', '알리다', '퍼지다'로 바꾼다."),
    R("ko.trans.jadong", "ko", "translationese", "B",
      r"자동으로\s*(?P<v>[가-힣]+(?:한다|했다|된다|됐다|생성|반영|처리|완성|실행|적용|갱신|저장|전환|분류|감지)[가-힣]*)",
      "'자동으로': '스스로'나 '알아서'로 충분한 자리에 'automatically'를 직역한 표현.",
      w=0.5, tier="standard", repl=fx.jadong,
      sugg="'자동으로' 대신 '스스로', '알아서'로 바꾸거나 뺀다."),

    R("ko.vocab.sino-b", "ko", "vocab", "B", KB + SINO_B + END,
      "한자어 학술 동사. 2018→2026년 논문 초록에서 급증한 계열(arXiv 2609.07447).", w=0.5,
      genre={"academic": 0.6}, sugg="'보여 준다', '밝히다', '도움이 된다'처럼 풀어 쓸 수 있는지 본다."),
    R("ko.vocab.sino-c", "ko", "vocab", "C", KB + SINO_C + END, "한자어 동사 묶음.", w=0.4, cluster=1,
      genre={"academic": 0.6}),
    R("ko.vocab.eval-b", "ko", "vocab", "B", KB + r"(?:" + EVAL_B + r")",
      "평가 형용사. 숫자와 비교 대상 없이 칭찬만 한다.", w=0.7, sugg="수치와 비교 대상으로 바꾼다."),
    R("ko.vocab.eval-c", "ko", "vocab", "C", KB + r"(?:" + EVAL_C + r")", "평가 형용사.", w=0.4, cluster=1),
    R("ko.vocab.jjak", "ko", "vocab", "B",
      r"(?P<w>짝\s*지(?:어(?:서)?|은|며|고)|짝\s*짓(?:는다|기|는|고|어)|짝(?:을|이)?\s*(?:이루(?:어(?:서)?|뤄|는|고|며)|이룬)|짝\s*(?:모델|문서|항목|요소)|짝이\s*되는)",
      "'짝'/'짝짓다': 둘의 대응이나 연계를 인위적으로 '짝'으로 표현한 번역투.",
      w=0.7, tier="standard", repl=fx.jjak,
      sugg="'짝' 대신 '맞추다', '연결하다', '대응', '연계'로 바꾼다."),
    R("ko.vocab.ssang", "ko", "vocab", "B",
      r"(?P<w>쌍(?:을|이)?\s*(?:이루(?:어(?:서)?|뤄|는|고|며)|이룬)|쌍으로(?![가-힣]))",
      "'쌍을 이루다': 둘의 병렬·대응을 상투적으로 표현한 어구.",
      w=0.6, tier="standard", repl=fx.ssang,
      sugg="'쌍을 이루다' 대신 '함께', '나란히', '둘씩'으로 바꾼다."),
    R("ko.vocab.sinho", "ko", "vocab", "B",
      r"(?P<w>(?P<target>(?:AI|인공지능|문체|위험|경고|이상|품질)\s*신호|신호\s*밀도)(?P<part>[이가은는을를])?|신호(?:로|가)\s*작용(?:한다|했다|하며|하고|해|하므로)?|신호가\s*된다|신호가\s*되나|신호가\s*되며|신호를\s*감지(?:한다|했다|하며|하고)?|신호를\s*포착(?:한다|했다|하며|하고)?)",
      "'신호': 징후·단서·특징을 '신호(signal)'로 직역한 번역투.",
      w=0.6, tier="standard", repl=fx.sinho,
      sugg="'신호' 대신 '특징', '단서', '징후'로 바꾼다."),
    R("ko.vocab.bakda", "ko", "vocab", "B",
      r"(?<!못을\s)(?<!못이\s)(?<!못은\s)(?<!못\s)(?<!못)(?P<w>박아\s*넣(?:는다|고|었다|은|어|으며)|박아\s*(?:두(?:고|었다|면|어)|둔다)|박아\s*(?:놓(?:는다|고|은|았다)|놨다)|박(?:는다|았다|았고|아서))",
      "'박다/박아 넣다': 거칠거나 비격식적인 삽입·하드코딩 표현 상투구.",
      w=0.6, tier="standard", repl=fx.bakda,
      sugg="'박아 넣다/박다' 대신 '직접 넣다', '적어 두다', '지정하다'로 바꾼다."),
]
