# Muse Spark · 기술 연구 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: 최신 버전 1.3의 API ID는 확인 필요(`muse-spark-1.3` 형태로 보이나 미확인), 오픈 가중치 변형은 "Muse Spark Open" · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-spark/tech-research.md`](../../../../md/muse/muse-spark/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 폐쇄형 API 모델(오픈 변형은 별도 제한 라이선스), 한두 달마다 갱신, 단가는 낮지만 과제당 비용 상승 보고, 독립 지수 충돌, 데이터 약관 불분명, 상위 모델 Muse Wonder 병행.

**이 모델에게 기술 조사를 시킬 때**
- 분류·정리 단계에만 쓴다. 후보를 정해진 기준(라이선스 유형, 지원 언어, 릴리스 날짜)으로 분류해 표로 만들 때, 값은 사람이 확보한 1차 자료 텍스트에서 추출하게 하고 원문에 없으면 null로 둔다.
- 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2, §3.5). 후보를 지나치게 높게 평가하는 경향(아첨)은 측정된 바 없으므로 사람이나 상위 모델이 근거를 보고 판단한다.
- 환각 수치가 벤더 보고뿐이므로 모델이 말하는 버전·날짜·가격·라이선스는 모두 1차 출처로 다시 확인한다.

**Muse Spark를 도입 후보로 평가할 때**
- **Spark와 Spark Open과 Wonder를 구분한다.** 폐쇄형 Spark(API), Spark Open(오픈 가중치, 별도 라이선스), 상위 모델 Muse Wonder / Wonder Full(`muse-wonder` 문서)은 서로 다른 모델이다. 집계 사이트가 변형을 섞어 점수를 싣는 사례가 있다. 인용 전에 정확한 모델명과 버전, 노력 단계를 확인한다. [부분]
- **벤더 수치로 결정하지 않는다.** 대표 수치(DeepSWE 75.4%, MRCR 98.1%)는 일반 제공 최고(`xhigh`)보다 높은 `max` 단계의 결과이고, 독립 지수는 61과 48로 충돌한다. 후보 비교는 같은 과제, 같은 노력 단계, 같은 예산의 자체 실측으로 한다. [부분, 충돌]
- **총비용은 과제당 비용이다.** 단가(입력 $1.25 / 출력 $4.25, 캐시 입력 $0.15)는 1.1부터 같다는 서술이지만, AA는 1.3이 에이전트 평가에서 입력 토큰을 약 57% 더 써서 작업당 비용이 $0.40에서 $0.55로 올랐다고 했다. Meta의 "토큰 약 25%·도구 호출 약 20% 감소"는 내부 비교다. 가격 경쟁(오픈AI·Anthropic보다 싸다는 서술)은 단가 비교일 뿐 과제당 비용이 아니다. [부분, 충돌]
- **"Contributor" 등급은 가격이 아니라 데이터 계약이다.** 입력 $0.10 / 출력 $0.20은 Meta가 트래픽을 학습에 쓸 수 있는 조건이라는 서술이 있다. 조건 원문을 확인하기 전에는 기업·연구·고객 데이터에 쓰지 않는다. [부분/미확인]
- **데이터 거버넌스.** 처리 서술이 충돌한다(프롬프트·응답을 학습에 쓰지 않는다는 전언 대 약관상 사용 데이터로 API를 개선할 수 있고 무료 서비스 콘텐츠는 분리 후 학습에 쓸 수 있다는 서술). 보관 기간과 영 보관 등급이 공개돼 있지 않고, 정책 위반 검토 중 콘텐츠는 오래 보관될 수 있다는 서술이 있다. 데이터 저장 위치(지역)도 확인하지 못했다. [미확인, 충돌] 약관과 개인정보 처리방침을 원문으로 읽고 법무·보안 검토를 거친다.
- **오픈 변형의 라이선스.** Spark Open은 "Muse Model License"를 따른다. 상업 이용 조건이 제한적이고, 대형 클라우드·AI 제공자의 재판매는 Meta 승인이 필요하며, 모델이나 파생 모델을 쓰는 제품·서비스에 "Built with Muse Spark Open"을 눈에 띄게 표시해야 한다는 서술이 있다. 오픈소스(OSI 정의)와 다르다. 임계값·정의·파생 모델 범위를 LICENSE 원문으로 확인한다(§3.2). 전체 안전 평가 보고서는 보도 시점에 대기 중이었다. [부분/미확인]
- **공급 연속성과 버전 관리.** 1.1(7월)·1.2(8월)·1.3(9월)·Spark Open(10월)·Wonder(10월)가 석 달 사이에 나왔다. 구버전 폐기 일정, 모델 교체 절차, 폴백 모델, 회귀 시험을 도입 조건으로 둔다. 일반 제공 최고 노력 단계(`xhigh`)와 `max`의 일반 제공 시점도 추적한다. [부분]
- **접근 경로.** Meta Model API(공개 프리뷰로 시작)와 Muse Code 구독 경로가 다르다. 제3자 호스트(Together AI, Fireworks, Groq, OpenRouter)는 Spark Open만 제공하고 가격은 호스트가 정한다. 사용하려는 경로의 SLA, 한도, 약관을 확인한다. [부분]
- **제공자 안전장치와 규정.** 규제 적합성은 모델이 아니라 시스템 전체에 대해 판단하고, 모델 카드나 라이선스를 규정 준수의 근거로 쓰지 않는다.

## 4. 근거와 한계
- 가격·버전·Contributor 등급: [The Decoder: Muse Spark 1.1 API 가격](https://the-decoder.com/metas-muse-spark-1-1-api-pricing-squeezes-openai-and-anthropic-as-the-ai-price-war-heats-up/), [DataLearner: Muse Spark 1.3](https://www.datalearner.com/en/ai-models/pretrained-models/muse-spark-1-3), [DataNorth: 1.3 출시](https://datanorth.ai/news/meta-launches-muse-spark-1-3) (스니펫만) [부분, 충돌]
- AA의 작업당 비용·지수: [The New Stack: Muse Spark 1.3 대 Gemini](https://thenewstack.io/muse-spark-1-3-gemini/) (스니펫만) [부분, 충돌]
- Spark Open 라이선스·배포·호스트: [The New Stack: Muse Spark Open](https://thenewstack.io/meta-muse-spark-open/), [Trending Topics: 라이선스](https://www.trendingtopics.eu/muse-spark-open-meta-open-weight-license/), [Mind-verse: Muse Spark Open](https://www.mind-verse.de/news/meta-muse-spark-open-modellgewichte-api-18c6e4e853de) (스니펫만) [부분]
- 데이터 약관: [ConductAtlas: Llama API 약관](https://conductatlas.com/platform/meta/llama-api-terms-of-service/provision/CA-P-060472/meta-may-use-usage-data-to-improve-api/), [Standard Compute: Meta](https://standardcompute.com/providers/meta) (스니펫만) [미확인, 충돌]
- 한계: Meta 공식 문서·모델 카드·약관·Muse Model License 본문을 읽지 못했다. 도입 전에 공식 문서와 라이선스 원문에서 확인한다.
