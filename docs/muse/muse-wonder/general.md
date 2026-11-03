# Muse Wonder · 범용 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-wonder-1.0`(한 출처의 표기, 확인 필요), 상위 변형 Wonder Full은 `muse-wonder-full-1.0`(카탈로그 전용, 한 출처의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-wonder/general.md`](../../../md/muse/muse-wonder/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Muse Wonder / Muse Wonder Full (폐쇄형)
이 환경에서는 Meta 공식 문서와 모델 카드가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 하위 모델 Muse Spark는 `muse-spark` 문서에 둔다.

### 2.1 위치와 접근 경로
- **2026-10-12**에 Meta가 공개한 Muse 계열 최상위 모델이다. 개인·전문 업무용 에이전트를 내세운다. 2026-04 Muse Spark, 2026-09 개인용 Muse 에이전트에 이어 나왔다.
- **두 모델이 있고 접근 경로가 다르다.** Muse Wonder는 Meta Model API와 Muse Code(Meta의 터미널 코딩 에이전트)에서 쓰고, **Wonder Full은 Muse Code 구독자(Power Usage 또는 Maximum Usage 요금제)만** 쓴다. 공개 API는 Wonder만 제공한다. 따라서 Wonder Full의 벤치마크 헤드라인은 지금 호출할 수 없는 모델을 설명할 수 있다. Muse 앱에도 순차 적용된다고 하나 일정은 없다. [부분]
- 모델은 폐쇄형이며 가중치를 받을 수 없다. 모델 카드가 구조·학습에 관해 알려 주는 정보가 거의 없다는 지적이 있다. [부분]

### 2.2 사양 (출처마다 다를 수 있음)
- 컨텍스트 100만 토큰, 장시간 에이전트·컴퓨터 사용을 겨냥. 가격은 Meta Model API에서 입력 $4 / 출력 $20 (100만 토큰당)이다. 한 매체는 Opus 5.5와 비슷한 가격대인데 벤치마크에서는 뒤처진다고 보도했다. [부분]
- **Active Memory**(대화를 넘어 맥락을 유지하고 관련 정보를 다시 꺼냄)와 **Active Focus**(긴 작업에서 대안을 시도하고, 막히면 우회하고, 중대한 행동 전에 확인 질문을 함)가 Meta가 내세운 두 기능이다. 두 기능이 API에서 어떻게 노출되는지, Active Memory가 데이터를 어디에 얼마나 보관하는지는 찾지 못했다. [미확인]
- 노력 단계: 벤치마크 대부분이 `max` 단계의 값이다(Wonder Full의 SWE-Marathon만 `xhigh`). 일반 제공 단계와 다를 수 있다. [부분]

### 2.3 성능 근거를 읽는 법 — Meta의 표와 독립 측정이 어긋난다
- **독립 지수(Artificial Analysis v4.3, 최대 노력)**: Wonder 52, Wonder Full 56, 비교로 Claude Opus 5.5 58, Muse Spark 1.3 48(Spark 1.3은 다른 서술에서 61이라 지수 버전 충돌이 있다, `muse-spark` 문서 참조). 즉 독립 지수에서 Wonder 계열은 Opus 5.5에 못 미친다. [부분, 충돌]
- **Meta 자체 표가 독립 값보다 높다.** Meta 모델 카드는 Wonder Full을 AA 지수 항목으로 59.0이라 적었고 AA는 56을 게시한다(지수 버전·실행 시점·Meta 하네스 차이일 수 있다). AutomationBench도 Meta 표 45.4/39.1에 대해 AA는 71%/68%로 달라 시험 버전이 다르다는 서술이 있다. 같은 이름의 지표라도 값을 섞어 비교하지 않는다. [부분, 충돌]
- **터미널·코딩 지표**: Terminal-Bench 4.0에서 Wonder Full 57%, Wonder 52%, 같은 값으로 Gemini 4 Argon 57%라는 한 독일어 글의 서술이 있고, Meta 자체 표에서도 Opus 5.5가 TB 4.0에서 앞선다고 한다. 집계 사이트의 코딩 점수(예: Haiku 5.5와의 비교에서 69.8 대 51.3)는 표 수치일 뿐 개발자 경험이 아니다. [부분]
- **Meta의 헤드라인 수치는 상당수가 내부 평가다.** 예컨대 MemoryBench는 LLM 심사위원이 채점하고 결과 출처가 Meta 내부다. 독립 재현 가능성이 낮다는 평가가 있다. [부분]
- **비용**: AA 페이지(독일어)는 지수 실행에서 출력 토큰 1.3억 개(비교 추론 모델 중앙값 8,500만)를 썼고 평균 비용이 과제당 $4.52라고 한다. 단가가 같은 가격대여도 토큰을 많이 쓰면 과제당 비용이 올라간다. [부분]
- **환각·사실성 평가는 찾지 못했다.** [미확인]

### 2.4 안전과 데이터
- **안전**: 모델 카드는 완화 조치가 없다면 Wonder Full이 화학·생물 위협의 고위험 기준에 도달할 가능성을 배제하지 못한다고 밝히고, 안전 후처리와 시스템 수준 분류기를 적용하면 잔여 위험이 중간 이하라고 평가한다. 추가 안전 평가를 담은 전체 보고서를 약속했으나 출시 시점에 공개되지 않았다. 사이버 위험 평가의 세부는 찾지 못했다. [부분] 분류기가 정당한 보안·생명과학 업무를 거부할 수 있으므로 거부율을 우리 과제로 시험한다. [추정]
- **데이터 처리**: Meta Model API 약관은 Llama API 약관에 기반한 것으로 보이며, 사용 데이터로 API를 개선할 수 있다는 조항과 학습 불사용 전언이 충돌한다(`muse-spark` 문서 §2.4). Active Memory의 저장 위치·기간·삭제 방법은 찾지 못했다. Meta 소비자 제품의 개인정보 처리방침은 AI 상호작용을 광고 개인화에 쓸 수 있다고 알려졌으나 이것이 API에 적용되는지는 확인하지 못했다. [미확인, 충돌] 개인정보·영업비밀은 약관을 원문으로 읽기 전에 보내지 않는다.
- **사람에 대한 기억을 쌓는 기능은 위험하다.** 별개 제품인 개인용 Muse 에이전트가 기억으로 연락처 프로필을 만든다는 보도와 프라이버시 우려가 있다. 이것이 API의 Active Memory와 같은지는 확인하지 못했다. 제3자 개인정보를 기억에 넣는 용도로 쓰지 않는다. [부분/미확인]

### 2.5 이 모델을 운용하는 법
- **에이전트 자율성을 제한한다.** Active Focus가 "중대한 행동 전에 확인한다"고 하나 이는 Meta의 설명이다. 파괴적·외부 영향 동작은 도구 권한·훅으로 차단하고 사용자 승인 후에만 한다(§1.6). [부분: 벤더 주장]
- **버전 고정.** 모델 ID에 버전이 포함돼 보이나(`-1.0`) 구버전 폐기 일정과 갱신 방식은 공식 문서로 확인한다. Muse 계열은 석 달 사이에 여러 번 갱신됐다. 회귀 시험을 업데이트 전후에 돌린다. [부분/추정]
- **지침은 짧게.** 이 문서의 §0과 §1.2·§1.3·§1.6을 시스템 프롬프트에 두고 분야 규칙은 필요한 작업에 붙인다. 한국어 존댓말 준수는 직접 측정한다. [미확인]

### 2.6 비판적 평가
- 강점 후보: 100만 토큰 컨텍스트, 장시간 에이전트 기능, Muse Code 연계, 일부 지표에서 Gemini 4 Argon과 비슷. 약점 후보: 독립 지수에서 Opus 5.5에 못 미침, Meta 자체 표와 독립 값 불일치, 토큰 소비가 많음, 폐쇄형이라 구조 정보가 없음, 안전 보고서·데이터 약관·Active Memory 정보 부족, Wonder Full은 구독 전용.
- 최고 성능이 필요하면 `claude/opus-5.5`, `claude/fable-5.1`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델과 같은 과제로 비교한다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 출시일·접근 경로·가격·ID·기능 | [Free Press Journal: Muse Wonder 출시](https://www.freepressjournal.in/tech/meta-launches-muse-wonder-muse-wonder-full-advanced-ai-models-key-features-pricing), [Let's Data Science](https://letsdatascience.com/news/meta-launches-muse-wonder-and-muse-wonder-full-for-agentic-t-41113cca), [Digit: Active Memory·Active Focus](https://www.digit.in/features/general/meta-muse-wonder-explained-what-active-memory-and-active-focus-do.html), [MindStudio: 출시](https://www.mindstudio.ai/blog/meta-muse-wonder-launch) (스니펫만) | [부분] |
| 독립 지수·평가 조건·Meta 표와의 불일치 | [Braindetox: 점수보다 평가 조건을 먼저 읽어라](https://braindetox.kr/en/posts/meta_muse_wonder_agent_models_release_2026.html), [MindStudio: Wonder 벤치마크](https://www.mindstudio.ai/blog/muse-wonder-benchmarks-vs-opus-gpt6), [Implicator: Opus 아래 순위](https://implicator.ai/meta-muse-wonder-ranks-below-claude-opus) (스니펫만) | [부분, 충돌] |
| AA 토큰·비용(독일어 페이지) | [Artificial Analysis: Muse Wonder (Max)](https://artificialanalysis.ai/de/models/muse-wonder) (스니펫만) | [부분] |
| 안전 모델 카드 서술 | [BetaNews: Muse Wonder](https://betanews.com/article/muse-wonder-frontier-model-developers/), [Pasquale Pillitteri: Opus 5.5 가격·벤치마크](https://pasqualepillitteri.it/en/news/23176/muse-wonder-launches-opus-5-5-prices-trails-benchmarks) (스니펫만) | [부분] |
| Active Memory 관련 프라이버시 우려(별개 제품 포함) | [Let's Data Science: 연락처 프로필](https://letsdatascience.com/news/meta-muse-creates-profiles-of-users-contacts-15585c25), [Atlanta News First: 프라이버시 우려](https://www.atlantanewsfirst.com/2026/10/09/metas-new-muse-ai-agent-raises-privacy-concerns/) (스니펫만) | [부분: 별개 제품, API 적용 미확인] |
- Meta 공식 문서·모델 카드·약관 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
- Wonder Full은 공개 API로 호출할 수 없으므로 Full 관련 수치는 직접 시험할 수 없다.
