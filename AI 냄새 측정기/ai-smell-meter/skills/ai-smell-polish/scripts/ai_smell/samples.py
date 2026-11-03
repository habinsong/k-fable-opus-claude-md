"""내장 표본. selftest와 시험이 함께 쓴다.

모두 이 저장소에서 새로 쓴 글이다. 실제 AI 출력이나 사람 글의 분포를 대표하지 않는다.
점수 기준선을 잡는 용도일 뿐이며, 이 표본으로 맞춘 임계값이 일반화된다는 근거는 없다.
"""
from __future__ import annotations

ZW = chr(0x200B)
NB = chr(0x00A0)

# 뚜렷한 AI풍 (점수 60 이상이어야 한다)
AI_STRONG = {
    "en": (
        "Certainly! Here is a revised version of your text.\n\n"
        "In today's fast-paced digital world, artificial intelligence plays a crucial role in shaping the future. "
        "It's not just a tool, it's a game-changer that stands as a testament to human ingenuity. Moreover, "
        "organizations can leverage the robust, seamless, and innovative solutions to unlock their full potential. "
        "Furthermore, it is important to note that the landscape is ever-evolving, highlighting the need for "
        "adaptability.\n\n"
        "Experts agree that this transformative technology will delve into every aspect of life. Additionally, the "
        "intricate tapestry of data-driven insights underscores its pivotal importance.\n\n"
        "In conclusion, the future looks bright. I hope this helps! Let me know if you have any questions."
    ),
    "ko": (
        "물론입니다! 아래와 같이 정리해 드리겠습니다.\n\n"
        "급변하는 AI 시대에 인공지능 기술은 단순한 도구가 아니라 패러다임의 전환을 의미한다. 이는 다양한 측면에서 "
        "시사하는 바가 크다. 또한 기업은 혁신적인 솔루션을 활용하여 생산성을 극대화할 수 있다. 아울러 데이터 품질을 "
        "확보하는 것이 중요하다.\n\n"
        "결론적으로 인공지능은 우리의 삶을 새로운 지평으로 이끌 것이다. 도움이 되었기를 바랍니다. 궁금한 점이 "
        "있으시면 언제든지 말씀해 주세요."
    ),
}

# 중간 정도 (점수 30 이상)
AI_MID = {
    "en": (
        "Remote work has transformed how teams collaborate. By leveraging digital tools, organizations can foster a "
        "culture of flexibility and trust. However, it is important to note that remote work also presents unique "
        "challenges, such as communication barriers and feelings of isolation. To address these challenges, companies "
        "should invest in robust onboarding, regular check-ins, and clear expectations. Ultimately, the success of "
        "remote work depends on balancing autonomy with accountability."
    ),
    "ko": (
        "원격 근무는 팀의 협업 방식을 크게 변화시켰다. 디지털 도구를 활용함으로써 기업은 유연성과 신뢰의 문화를 조성할 "
        "수 있다. 그러나 원격 근무는 소통의 어려움과 고립감과 같은 문제도 안고 있다는 점에 주목할 필요가 있다. 이러한 "
        "문제를 해결하기 위해서는 체계적인 온보딩, 정기적인 점검, 명확한 기대치 설정이 필요하다. 결국 원격 근무의 "
        "성공은 자율성과 책임성의 균형에 달려 있다고 할 수 있다."
    ),
}

# 사람이 쓴 글 (점수 15 이하여야 한다)
HUMAN = {
    "en-blog": (
        "I spent most of last weekend trying to fix the leak under our kitchen sink. The first plumber I called "
        "quoted me $340 and said he couldn't come until Thursday, so I watched three videos, bought a $12 washer and "
        "a bucket, and got it wrong twice. The third time worked. The cabinet floor is still warped, and my wife has "
        "opinions about the towels."
    ),
    "en-docs": (
        "The cache stores responses for 60 seconds by default. If you need fresh data on every request, pass "
        "`no_cache=True`. Note that the cache is per-process, so two workers can return different values for the "
        "same key until their entries expire."
    ),
    "en-science": (
        "We trained the model for 40 epochs on the filtered corpus (n = 12,481). Accuracy on the held-out set rose "
        "from 71.2% to 78.9%, although the improvement vanished on the out-of-domain test. We suspect the filter "
        "removed rare dialect forms, but we did not test this."
    ),
    "en-classic": (
        "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in "
        "Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great "
        "civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure."
    ),
    "ko-daily": (
        "어제 퇴근길에 비가 와서 우산을 사려고 편의점에 들렀다. 만 원짜리 투명 우산밖에 없어서 그냥 샀다. 집에 "
        "도착하니까 현관에 같은 우산이 벌써 세 개나 있었다."
    ),
    "ko-news": (
        "서울시는 3일 내년 1월부터 시내버스 요금을 300원 올린다고 발표했다. 인상 폭은 2015년 이후 가장 크다. 시는 "
        "연료비와 인건비가 올라 적자가 커졌다고 설명했다."
    ),
    "ko-academic": (
        "본 연구는 초등학교 3학년 학생 84명을 대상으로 읽기 유창성 훈련의 효과를 살펴보았다. 12주 동안 주 3회 "
        "훈련한 결과 분당 읽은 단어 수가 평균 18.4개 늘었다. 다만 통제집단이 없어 효과를 훈련 때문이라고 단정하기는 "
        "어렵다."
    ),
    "ko-literary": (
        "아버지는 말이 없는 사람이었다. 밥상머리에서도 숟가락 소리만 났다. 그날 저녁에도 아버지는 신문을 접어 놓고 "
        "한참 창밖을 보았다. 나는 무슨 말이든 해야 할 것 같아서 물을 따라 드렸다."
    ),
}

# 교정 결과가 글자 단위로 정해진 경우: (이름, 입력, 단계, 기대 출력)
GOLDEN = [
    ("en-standard",
     "Certainly! In order to save time, utilize the cache. I hope this helps!", "standard",
     "To save time, use the cache."),
    ("ko-standard",
     "물론입니다! 분석을 진행한 결과, 비용이 감소되어진 것으로 보여진다. 도움이 되었기를 바랍니다.", "standard",
     "분석한 결과, 비용이 감소된 것으로 보인다."),
    ("hygiene-safe", "Hello" + ZW + " world" + NB + "again", "safe", "Hello world again"),
    ("code-url-protected",
     "In order to run it, call `utilize(x)` and visit https://example.com/in-order-to?utm_source=chatgpt.com now.",
     "standard", "To run it, call `utilize(x)` and visit https://example.com/in-order-to now."),
    ("en-strong-neg-parallel", "It's not just a tool, it's a platform.", "strong", "It's a platform."),
    ("ko-strong-neg-simple", "그것은 단순한 슬픔이 아니라 오래된 그리움이었다.", "strong", "그것은 오래된 그리움이었다."),
]
