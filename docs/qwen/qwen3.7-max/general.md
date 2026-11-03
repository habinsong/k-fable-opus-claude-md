# Qwen3.7-Max · 범용 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: API `qwen3.7-max`(5월 17일·6월 8일 빌드 ID가 따로 표기됨, 정확한 ID는 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.7-max/general.md`](../../../md/qwen/qwen3.7-max/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Qwen3.7-Max (API 전용, 후속 3.8-Max에 앞선 세대)
이 환경에서는 Alibaba 공식 문서가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 후속은 `qwen3.8-max` 문서에 둔다.

### 2.1 위치와 사양
- **2026-05-19에 나온 것으로 집계 사이트가 적고**(빌드 ID는 5월 17일과 6월 8일이 따로 있어 이후 스냅샷이 있었을 수 있음) Alibaba는 이를 "독점(proprietary) 모델, API 전용"이라 부른다. 약 석 달 뒤 `qwen3.8-max`(8월 3일)가 나왔으므로 이 모델은 한 세대 전이다. 폐기 일정은 확인하지 못했다. [부분]
- 컨텍스트 100만 토큰. 가격(100만 토큰당)은 Alibaba 직접이 입력 $2.50 / 출력 $7.50이고 OpenRouter·Vercel 같은 경로는 $1.25 / $3.75로 다르다. 경로마다 가격·한도·데이터 조건이 다르므로 공식 가격표와 경로별 약관을 확인한다. [부분, 충돌]
- **장시간 자율 실행을 내세운다.** 에이전트 런타임이 최대 35시간 자율 작업을 지원하고 Anthropic의 Claude Code 같은 외부 하네스와 함께 쓸 수 있다고 VentureBeat가 보도했다. 벤더 설명이며 독립 확인은 없다. [부분: 벤더 주장]

### 2.2 성능 근거를 읽는 법
- **독립 지수가 둘로 갈린다.** Artificial Analysis 기반 페이지가 지능 지수 46.0과 56.6을 각각 싣는다. 스냅샷·지수 버전이 다른 것으로 보이며 어느 쪽도 이 문서에서 원 페이지를 확인하지 못했다. 다른 모델과의 비교에는 같은 지수 버전의 값만 쓴다. [부분, 충돌]
- **벤더 보고**: Humanity's Last Exam 41.4, MCP-Atlas 76.4(VentureBeat 인용). 독립 확인이 없고 도구 포함 여부와 조건은 확인하지 못했다. [부분: 벤더 주장]
- **환각 값은 찾지 못했다.** [미확인]

### 2.3 데이터·정책
- Alibaba Cloud Model Studio는 데이터를 모델 학습에 쓰지 않는다고 밝히고, 리전이 저장 위치를 정하며(추론 위치는 별도 설정), ZDR은 국제 사이트 기업 고객 전용이다. 보관 최대 30일은 제3자 서술이다. 모기업이 중국 본사라는 위험 분석이 있다(`qwen3.8-max` 문서 §2.3). [부분, 충돌]

### 2.4 운용
- **후속 모델과 비교해 이 모델을 유지할 이유를 따진다.** 3.8-Max가 같은 가격대에서 나왔다. 이 모델을 쓰는 이유가 안정성이나 이미 검증한 회귀 시험뿐이라면 폐기 일정을 확인하고 이행 계획을 세운다. [추정]
- **빌드를 고정한다.** 5월과 6월 빌드가 따로 있었으므로 재현성이 필요한 작업에서 빌드 ID를 지정한다.
- **지침은 짧게.** 이 문서의 §0과 §1.2·§1.3·§1.6을 시스템 프롬프트에 두고 분야 규칙은 필요한 작업에 붙인다. 한국어 존댓말 준수는 직접 측정한다. [미확인]

### 2.5 비판적 평가
- 강점 후보: 100만 토큰, 외부 하네스 호환, 경로별로 낮은 가격. 약점 후보: 독립 지수 값이 둘로 갈림, 벤더 수치 조건 불명, 한 세대 뒤처짐, 경로별 가격 차이, 데이터 정책 일부는 2차 출처.
- 새 도입이면 `qwen3.8-max` 문서를, 막히면 `claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델을 본다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 출시·API 전용·35시간 자율 실행·벤더 수치 | [VentureBeat: Qwen3.7-Max 35시간 자율 실행](https://venturebeat.com/ai/alibabas-proprietary-qwen3-7-max-can-run-for-35-hours-autonomously-and-supports-external-harnesses-like-anthropics-claude-code) (스니펫만) | [부분: 벤더 주장] |
| 출시일·가격·지수 | [Cloudprice: Qwen3.7-Max](https://cloudprice.net/models/alibaba-qwen3-7-max), [LLM Reference: Qwen3.7-Max](https://www.llmreference.com/model/qwen3-7-max), [LLMBase: Qwen3.7-Max](https://llmbase.ai/models/qwen/qwen3-7-max/) (스니펫만) | [부분, 충돌] |
| 데이터 정책 | [Alibaba Cloud Model Studio: 데이터 보관 정책](https://www.alibabacloud.com/help/en/model-studio/data-retention-policy), [Security Scientist: Qwen 위험 평가](https://www.securityscientist.net/blog/qwen-risk-assessment-template/) (스니펫만) | [부분, 충돌] |
- Alibaba 공식 모델 카드·약관 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
