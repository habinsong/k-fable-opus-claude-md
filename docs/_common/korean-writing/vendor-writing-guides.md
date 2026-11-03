# 모델 제공자의 프롬프트 가이드 중 글쓰기 관련 내용

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 가이드는 영어 기준이고 한국어 효과는 검증되지 않았다 [미확인]. 모델별 지침(`md/<계열>/<모델>/ko-*.md`)은 이 내용을 한국어 윤문에 맞게 다시 쓴 것이다.

## 1. Anthropic — 모델별 프롬프트 가이드 (직접 읽음 [확인])

| 모델 | 글쓰기·문체 관련 절 | 요지 |
|---|---|---|
| [Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) | *Writing density* | 상투구와 설명 없는 전문용어가 적지만 Fable 5보다 문장이 길고 문단 나눔이 적을 수 있다. 직접 말하지 않고 비유·수사로 돌려 말하는 "허세 문체(mannered prose)"를 정의해 주면 도움이 된다고 한다 |
| 같은 문서 | *Formatting in chat* | 이전 모델과 반대로 굵은 글씨·제목·목록을 덜 쓴다. 반(反)서식 지시는 지우고 "언제 서식을 써도 되는지"로 바꾸라고 한다. 대화·개인·감정 교환은 줄글을 권한다 |
| 같은 문서 | *Quoting retrieved sources* | 출처 글을 요약할 때 원문 구절을 인용 표시 없이 옮기는 경향이 Fable 5보다 늘었다. 완전한 응답 예시 하나를 넣으라고 한다 |
| 같은 문서 | *Leave room for long outputs at xhigh and max* | 긴 산출물을 생각 속에서 초안으로 쓰고 다시 쓰는 일이 있다. `high`를 권하고, 전체 출력이 한 번의 한도에 들어간다는 점을 알려 주라고 한다 |
| [Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) | 문체 절 없음 | 에이전트 작업 중심. 채팅 시스템 프롬프트에서 "신중히 생각하라"를 지우라는 권고, 이전 답을 다시 파고드는 경향을 줄이는 문구, "다중 앱 작업은 행동 전에 넓게 탐색하라" |
| [Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) | 문체 절 없음 | 요청하지 않은 추가(테스트·문서·보조 파일)를 하는 경향, `xhigh`·`max`의 추가 리뷰 라운드, 열린 요청에 만들기부터 시작하는 경향. 범위를 제한하는 문구를 제공한다 |
| [Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) | *Keep reasoning out of user-facing text* | 사용자에게 보이는 답에 추론처럼 보이는 글이 섞이는 일이 있고 사고를 끄거나 `low`일 때 더 잦다. 적응형 사고와 `medium`을 권한다 |

세 모델(Opus·Sonnet·Haiku 5.5)의 가이드는 글쓰기 문체를 직접 다루지 않는다. 그래서 이 세 모델의 한국어 지침은 범위 제한, 결과물 분리, 사고 메모 분리처럼 가이드가 확인해 준 행동에만 근거한다.

## 2. OpenAI (검색 요약 [부분], developers.openai.com은 이 환경에서 열리지 않음)

- GPT-5.1 가이드: 길이는 `verbosity` 매개변수로 조절하고 어조·리듬은 프롬프트로 조절할 수 있다. 과도한 길이는 매개변수를 조정한 뒤 프롬프트로 더 줄인다. ([GPT-5.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide))
- 성격(personality)은 시스템·개발자 지시에서 정의하며 이모지 금지 같은 예시가 있다. ([Shaping your agent's personality](https://developers.openai.com/cookbook/examples/gpt-5/prompt_personalities))
- GPT-5.5 가이드는 성격(어조·따뜻함·직접성·격식·유머·공감)과 협업 방식을 분리하고, 3자 요약에 따르면 `text.verbosity` 기본값은 medium이다. ([GPT-5.5 prompting guide](https://developers.openai.com/api/docs/guides/prompt-guidance.md))
- GPT-6 계열에서 `verbosity`가 지원되는지는 확인하지 못했다 [미확인].
- 2025년 GPT-4o의 아첨 문제와 이후 "더 따뜻한" 성격 조정에 대한 보도가 있다 [부분: 보도].

## 3. Google (검색 요약 [부분], docs.cloud.google.com은 열리지 않음)

[Gemini 3 프롬프트 가이드](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide) 요약:
- 기본 응답은 덜 장황하고 직접적이다. 수다스러운 persona는 프롬프트에서 명시적으로 요청해야 한다.
- persona를 진지하게 따르고 때로는 지시를 무시하면서까지 유지한다.
- 복잡한 요청에서 앞쪽에 둔 부정 제약("~하지 마라")을 놓칠 수 있다. 긴 자료는 지시를 자료 뒤에 두라고 한다.
- temperature는 기본값 1.0을 권한다.

Gemini 4 Argon·3.8 Flash에 이 가이드가 그대로 적용되는지는 확인하지 못했다 [추정].

[Gemma 4 프롬프트 형식](https://ai.google.dev/gemma/docs/core/prompt-formatting-gemma4) 요약: 시스템 턴을 지원하고, 시스템 지시에 `<|think|>` 토큰을 넣어 생각 모드를 켜며, 다중 턴에서는 이전 턴의 생각을 제거해야 한다 [부분: 검색 요약].

## 4. 번역투·프롬프트 언어 연구 (한국어 직접 검증 아님)

- [Lost in Literalism](https://arxiv.org/pdf/2503.04369)(ACL 2025): 영-중, 독-영 번역 실험에서 프롬프트에 자연스러움 요구를 넣어도 번역투 비율이 일관되게 줄지 않았고, 모델이 자기 출력을 다듬게 하면 GPT-4의 번역투 비율이 43%에서 25%로 줄었다 [부분: 검색 요약]. → 지침을 "규칙 나열"이 아니라 "초안→점검→수정 순환"으로 설계한 근거.
- [KRETA](https://arxiv.org/pdf/2508.19944): 프롬프트를 영어로 번역하고 한국어 출력을 요구하면 QA 품질이 하락했다. 저자의 가설이고 문체 자연스러움이 아니라 QA 품질이다 [부분]. → "지시는 한국어로"의 근거.
- 영어권에서 "not X, but Y"는 가장 안 지워지는 AI 습관으로 보도됐다([Atlantic 요약](https://aiweekly.co/alerts/atlantic-ais-its-not-x-its-y-tic-proves-hardest-to-shake)). 금지하면 "rather than X" 같은 변종으로 옮겨 간다는 후기가 있다. 수치(Washington Post 데이터셋 약 6%, Fortune 500 공시 50→200여 건)는 원문을 열람하지 못했다 [부분].
- 옥스퍼드 인터넷 연구소 연구 보도: 더 따뜻하게 조율한 챗봇일수록 답변 질과 정확도가 낮았다 [부분: 보도]. → 공감 문구를 줄이는 근거의 하나.
