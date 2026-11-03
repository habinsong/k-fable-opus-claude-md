# Qwen3.7-Max · 기술 연구 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: API `qwen3.7-max`(5월 17일·6월 8일 빌드 ID가 따로 표기됨, 정확한 ID는 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.7-max/tech-research.md`](../../../../md/qwen/qwen3.7-max/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: API 전용, 한 세대 전(후속 `qwen3.8-max`가 석 달 뒤 출시), 경로별 가격 두 배 차이, 독립 지수 46.0 또는 56.6(충돌), 벤더 수치는 조건 불명, 데이터 정책 일부는 2차 출처.

**이 모델에게 기술 조사를 시킬 때**
- 분류·정리 단계에만 쓴다. 후보를 정해진 기준(라이선스 유형, 지원 언어, 릴리스 날짜)으로 분류해 표로 만들 때, 값은 사람이 확보한 1차 자료 텍스트에서 추출하게 하고 원문에 없으면 null로 둔다.
- 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2, §3.5). 후보를 지나치게 높게 평가하는 경향(아첨)은 측정된 바 없으므로 사람이나 상위 모델이 근거를 보고 판단한다.

**Qwen3.7-Max를 도입 후보로 평가할 때**
- **신규 도입 후보로는 후속 세대가 우선이다.** 이 모델은 한 세대 전이고 `qwen3.8-max`가 같은 세대 가격대에서 나왔다. 이 모델을 고려하는 이유가 기존 검증이나 특정 경로의 가격이라면 그 이유를 기록하고 폐기 일정과 이행 비용(회귀 시험, 프롬프트 재조정)을 함께 평가한다. [추정]
- **경로마다 가격과 데이터 조건이 다르다.** Alibaba 직접 입력 $2.50 / 출력 $7.50, OpenRouter·Vercel $1.25 / $3.75다. 싼 경로가 같은 품질을 제공하는지(양자화, 컨텍스트 제한, 빌드 차이), 데이터 처리 조건이 같은지 확인한다. 과제당 비용은 우리 과제의 토큰·도구 호출 수로 계산한다. [부분, 충돌]
- **벤더 수치로 결정하지 않는다.** HLE 41.4, MCP-Atlas 76.4는 벤더 보고이고 조건 불명이다. 독립 지수는 46.0과 56.6으로 갈려 스냅샷·지수 버전을 알기 전에는 순위 근거로 쓰지 않는다. 후보 비교는 같은 과제, 같은 조건의 자체 실측으로 한다. [부분, 충돌]
- **"독점 모델, API 전용"의 의미.** 가중치가 공개되지 않아 자체 호스팅, 오프라인 사용, 구조·학습 데이터 검증이 불가능하다. 학습 데이터의 저작권 문제는 확인할 수 없다(§1.5). 자체 호스팅이 필요하면 공개 가중치 모델(`qwen3.6-27b`, `qwen3.6-35b-a3b`, `qwen3.8-27b`)을 본다. [부분]
- **데이터 거버넌스.** Alibaba는 데이터를 모델 학습에 쓰지 않는다고 밝히고, 리전이 저장 위치를 정하며(추론 위치는 별도 설정), ZDR은 국제 사이트 기업 고객 전용이고, 최대 30일 보관은 제3자 서술이다. 싱가포르 리전이어도 모기업은 중국 본사이고 중국 법령이 그룹사에 미칠 수 있다는 위험 분석이 있다. 약관·개인정보 처리방침·ZDR 조건을 원문으로 읽고 법무·보안 검토를 거친다. [부분, 충돌]
- **공급 연속성.** 5월 출시, 6월 새 빌드, 8월 후속 출시로 석 달 안에 세대가 바뀌었다. 빌드 폐기 일정, 모델 교체 절차, 폴백 모델, 회귀 시험을 도입 조건으로 둔다. [부분]
- **제공자 안전장치와 규정.** 규제 적합성은 모델이 아니라 시스템 전체에 대해 판단하고, 모델 카드를 규정 준수의 근거로 쓰지 않는다.

## 4. 근거와 한계
- 출시·가격·지수: [Cloudprice: Qwen3.7-Max](https://cloudprice.net/models/alibaba-qwen3-7-max), [LLM Reference: Qwen3.7-Max](https://www.llmreference.com/model/qwen3-7-max), [LLMBase: Qwen3.7-Max](https://llmbase.ai/models/qwen/qwen3-7-max/) (스니펫만) [부분, 충돌]
- 벤더 설명: [VentureBeat: Qwen3.7-Max 35시간 자율 실행](https://venturebeat.com/ai/alibabas-proprietary-qwen3-7-max-can-run-for-35-hours-autonomously-and-supports-external-harnesses-like-anthropics-claude-code) (스니펫만) [부분: 벤더 주장]
- 데이터 정책: [Alibaba Cloud Model Studio: 데이터 보관 정책](https://www.alibabacloud.com/help/en/model-studio/data-retention-policy), [Security Scientist: Qwen 위험 평가](https://www.securityscientist.net/blog/qwen-risk-assessment-template/) (스니펫만) [부분, 충돌]
- 한계: Alibaba 공식 모델 카드·약관 본문을 읽지 못했다. 도입 전에 공식 문서에서 확인한다.
