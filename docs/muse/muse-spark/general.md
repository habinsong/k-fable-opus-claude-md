# Muse Spark · 범용 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: 최신 버전 1.3의 API ID는 확인 필요(`muse-spark-1.3` 형태로 보이나 미확인), 오픈 가중치 변형은 "Muse Spark Open" · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-spark/general.md`](../../../md/muse/muse-spark/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Muse Spark (폐쇄형 API 모델, 버전이 계속 갱신됨)
이 환경에서는 Meta 공식 문서가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 상위 모델 Muse Wonder는 `muse-wonder` 문서에 둔다.

### 2.1 연혁과 버전 — 이름이 같아도 다른 모델이다
- **2026-04**: Meta가 처음 낸 폐쇄형 Muse 모델로 보도됨(Spark). **1.1(2026-07-09)**: Meta Model API 공개 프리뷰와 함께 나온 첫 유료 API 모델. **1.2(2026-08-05)**. **1.3(2026-09-02)**: 1.2를 장시간 에이전트·코딩에 맞게 조정한 갱신이라는 서술이 있다. 이 날짜는 집계 사이트(DataLearner 등) 값이고 Meta 공식 공지는 확인하지 못했다.
- **버전을 명시하지 않은 자료를 조심한다.** 가격·벤치마크·점수가 버전별로 다르게 섞여 있다(예: 1.1의 독립 지수 53.2라는 집계와 1.3의 48이라는 서술은 지수 버전이 달라 비교할 수 없다). 인용할 때 버전과 지수 버전을 같이 쓴다. [부분, 충돌]
- **Muse Spark Open(2026-10-15)**: 별도의 오픈 웨이트 변형이다(§2.5). 폐쇄형 Spark와 같은 모델이 아니다.

### 2.2 사양 (1.3 기준, 출처마다 다름)
- 컨텍스트 100만 토큰(능동 압축이 있다는 서술), OpenAI·Anthropic SDK 형식 호환. 최대 출력은 Meta가 공개하지 않았다는 지적이 있고 한 집계는 13.1만 토큰이라고 적었다. [부분, 충돌]
- **가격**: 입력 $1.25 / 출력 $4.25 (100만 토큰당, 1.1부터 이어진 가격이고 1.3도 같다는 서술), 캐시 입력 $0.15. 신규 계정에 $20 무료 크레딧이 있었다고 한다. 한 페이지의 $12/$60은 다른 출처와 모순돼 신뢰하지 않는다. [부분, 충돌]
- **"Contributor" 등급**: 입력 $0.10 / 출력 $0.20으로 매우 싸지만 Meta가 사용자 트래픽을 학습에 쓸 수 있는 조건이라는 서술이 있다. 가격만 보고 선택하지 말고 약관을 원문으로 확인한다(§2.4). [부분/미확인]
- **추론 노력 단계**: 1.3에서 `xhigh`까지 제공되고 `max`는 안전 시험 때문에 보류됐다는 서술이 있다. [부분]
- **"1.3이 1.2보다 토큰 약 25%, 도구 호출 약 20% 적다"는 것은 Meta 엔지니어의 내부 비교이고, 독립 측정은 반대로 나왔다.** Artificial Analysis는 1.3이 에이전트 평가에서 입력 토큰을 약 57% 더 써서 작업당 비용이 1.2의 $0.40에서 $0.55로 올랐다고 보고했다. 가격표(토큰당 단가)가 같아도 과제당 비용은 올랐을 수 있다는 뜻이다. 우리 과제로 과제당 비용을 직접 잰다. [부분, 충돌]
- **Meta의 대표 수치는 일반 제공 수준보다 높은 노력 단계로 잰 것이다.** 1.3의 DeepSWE 75.4%, 긴 컨텍스트 MRCR(512K~1M) 98.1%는 `max` 단계의 결과이고 개발자가 쓸 수 있는 최고 단계는 `xhigh`다. 공개 수치를 읽을 때 어느 노력 단계의 값인지 확인한다. [부분: 벤더 주장]
- **Muse Code**(Meta의 터미널 코딩 에이전트)가 1.2와 함께 8월 초 베타로 나왔고 1.3도 Muse Code와 Meta Model API에서 쓸 수 있다. [부분]

### 2.3 성능 근거를 읽는 법
- **벤더 주장.** 1.1은 Meta가 공개한 두 벤치마크에서 Claude Opus 4.8과 GPT-5.5를 이겼다는 서술이 있으나, 이는 Meta가 고른 지표이고 에이전트 도구 사용 강점은 독립 벤치마크로도 확인됐지만 Meta 자체 점수는 회의적 시각을 받는다는 평도 있다. [부분]
- **독립 지수(Artificial Analysis)가 두 값으로 갈린다.** 한 검색 결과는 AA가 일반 제공 최고 단계(`xhigh`)의 1.3에 지능 지수 61을 매겼고 1.2보다 4점 높다고 서술한다. 다른 곳은 지수 v4.3에서 Spark 1.3이 48이고 Muse Wonder 52, Wonder Full 56, Claude Opus 5.5 58이라고 인용한다. 61이 Opus 5.5의 58보다 높아 두 값은 같은 지수 버전일 수 없다. 어느 지수 버전의 값인지 확인되기 전에는 다른 모델과의 순위 비교에 쓰지 않는다. 1.1의 53.2라는 집계값도 또 다른 버전일 수 있다. [부분, 충돌]
- **1.3 코딩 향상은 "역대 최대 코딩 도약"이라는 홍보성 서술이다.** AA는 1.3이 Gemini 3.8 Flash보다 작업당 비용과 점수 모두 우세하다고 했으나 코딩 한 분야의 독립 평가나 프런트엔드·시스템 코드 평가는 찾지 못했다. [부분/미확인]
- **환각(벤더 보고).** Meta의 안전·대비 보고서는 환각·보정 벤치마크에서 비교 모델과 경쟁력이 있다고 하며, 이미지가 빠진 CharXiv 질문에서 환각률 35.0%(비교 모델 GPT-5.4 48.8%, Gemini 3.1 Pro 86.8%)를 최고로 제시한다. 이는 Meta 자체 보고이고 특정 시험 한 가지다. 오픈 변형은 AA-Omniscience 지수 25로 집계됐다(자체 출시 표 8개 모델 중 최고라는 서술, 지수가 사실 회상과 답변 보류를 함께 재므로 환각률로 읽지 않는다). [부분: 벤더·집계]

### 2.4 운용 시 알아둘 것
- **버전 고정.** 버전이 한두 달 간격으로 갱신되고 같은 이름 아래 동작이 바뀔 수 있다. API 모델 ID에 버전이 포함되는지(예: `-1.3`)와 구버전 폐기 일정을 공식 문서로 확인하고, 업데이트 전후 자체 회귀 시험을 돌린다. [추정]
- **데이터 처리 조건이 불분명하고 서술이 충돌한다.** 한 추적 사이트는 Meta가 프롬프트와 응답을 AI 모델 학습에 쓰지 않는다고 밝혔다고 전하고, 다른 곳은 Meta Model API 약관(Llama API 약관 기반)이 사용 데이터로 API를 개선할 수 있고 무료 서비스의 콘텐츠를 계정·키에서 분리한 뒤 학습에 쓸 수 있다고 한다. 프롬프트 보관 기간은 공개돼 있지 않고 영 보관(ZDR) 등급도 공개되지 않았으며, 정책 위반 검토 중인 콘텐츠는 오래 보관될 수 있다는 서술도 있다. [미확인, 충돌] 개인정보·영업비밀은 약관을 원문으로 읽기 전에 보내지 않고, Contributor 등급은 쓰지 않는다.
- **지침은 짧게.** 이 문서의 §0과 §1.2·§1.3·§1.6을 시스템 프롬프트에 두고 분야 규칙은 필요한 작업에 붙인다. 한국어 존댓말 준수는 직접 측정한다. [미확인]

### 2.5 Muse Spark Open (오픈 웨이트 변형)
- 2026-10-15에 공개된 다운로드 가능한 가중치다. 라이선스는 Meta의 자체 "Muse Model License"로, 상업 이용 조건이 제한적이다. 많은 개발자는 무료로 쓸 수 있으나 대형 클라우드·AI 제공자가 재판매하려면 Meta의 승인이 필요하고, 모델이나 파생 모델을 쓰는 제품·서비스에 "Built with Muse Spark Open"을 눈에 띄게 표시해야 한다는 서술이 있다. 원문 조항은 확인하지 못했다. [부분/미확인]
- 가중치는 Hugging Face, Amazon SageMaker AI, Google Cloud Model Garden, Microsoft Foundry Models에서 받을 수 있고, M5 Ultra 맥 스튜디오 두 대로 로컬 실행이 가능하다는 서술이 있다. Meta Model API에서는 제공되지 않고 Together AI, Fireworks, Groq, OpenRouter 등 제3자가 호스팅하며 가격은 호스트가 정한다. 전체 안전 평가 보고서는 보도 시점에 대기 중이었고, Artificial Analysis의 공개 가중치 순위에도 아직 없었다. [부분]
- 이 문서의 운용 규칙은 폐쇄형 Spark를 기준으로 하며, 오픈 가중치를 쓰면 라이선스 원문 확인, 공식 저장소에서만 받기, 호스트별 약관 확인을 추가로 한다(§1.5).

### 2.6 비판적 평가
- 강점 후보: 낮은 단가, 100만 토큰 컨텍스트, SDK 호환, 도구 사용 강점(독립 확인된 부분). 약점 후보: 폐쇄형이라 구조·학습 정보가 없고, 버전 갱신이 잦으며, 벤더 수치가 회의적으로 평가되고, 데이터 약관이 불분명하다.
- 최고 성능이 필요하면 상위 모델 Muse Wonder(`muse-wonder` 문서)나 `claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 1.1 출시·가격·무료 크레딧·SDK 호환 | [The Decoder: Muse Spark 1.1 API 가격](https://the-decoder.com/metas-muse-spark-1-1-api-pricing-squeezes-openai-and-anthropic-as-the-ai-price-war-heats-up/), [AI Weekly: 1.1 가격](https://aiweekly.co/node/5972), [Implicator: 첫 유료 API](https://www.implicator.ai/meta-prices-its-first-paid-ai-model-api-at-4-25-per-million-output-tokens/) (스니펫만) | [부분] |
| 1.2·1.3 출시일·가격·Contributor 등급·변화 | [DataLearner: Muse Spark 1.3](https://www.datalearner.com/en/ai-models/pretrained-models/muse-spark-1-3), [DataNorth: 1.3 출시](https://datanorth.ai/news/meta-launches-muse-spark-1-3), [MindStudio: 1.3 가격](https://www.mindstudio.ai/blog/muse-spark-1-3-pricing), [eesel: Muse Spark 1.3](https://www.eesel.ai/blog/muse-spark-1-3) (스니펫만) | [부분, 충돌] |
| Spark Open 라이선스·배포 | [The New Stack: Muse Spark Open](https://thenewstack.io/meta-muse-spark-open/), [Trending Topics: 라이선스](https://www.trendingtopics.eu/muse-spark-open-meta-open-weight-license/), [Itdaily](https://itdaily.com/news/innovation/meta-muse-spark-open-weigh/) (스니펫만) | [부분] |
| 독립 지수·작업당 비용·Meta 대표 수치의 노력 단계 | [The New Stack: Muse Spark 1.3 대 Gemini](https://thenewstack.io/muse-spark-1-3-gemini/), [ProPakistani: 1.3 출시](https://propakistani.pk/2026/09/03/meta-launches-muse-spark-1-3-with-faster-coding-and-smarter-agents/) (스니펫만) | [부분, 충돌] |
| 환각 보고(벤더)·오픈 변형 AA-Omniscience | [Muse Spark Safety & Preparedness Report](https://arxiv.org/pdf/2606.12429), [BenchmarkList: Muse Spark Open](https://benchmarklist.com/models/meta-muse-spark-open/) (스니펫만, arxiv.org는 이 환경에서 열리지 않음) | [부분: 벤더·집계] |
| 데이터 약관(Llama API 약관 기반) | [ConductAtlas: Llama API 약관](https://conductatlas.com/platform/meta/llama-api-terms-of-service/provision/CA-P-060472/meta-may-use-usage-data-to-improve-api/), [Standard Compute: Meta](https://standardcompute.com/providers/meta) (스니펫만) | [미확인, 충돌] |
- Meta 공식 문서·모델 카드·Muse Model License 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
- 최신 버전이 1.3 이후로 갱신됐는지는 확인하지 못했다.
