# Gemini 4 Carbon · 기술 연구 (제한 공개 대비) — 조사 기록
> 제공자: Google · 모델 ID: 미공개 [미확인] · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-carbon/tech-research.md`](../../../../md/gemini/gemini-4-carbon/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때 (잠정)
2026-11-03 기준 Carbon은 사이버 방어 조직 일부에게만 제한 공개돼 있고 일반 개발자는 쓸 수 없다. 모델 상태와 일반 공개 시 체크리스트는 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 일반 접근에서는 `gemini/gemini-4-argon/tech-research.md`를 적용한다.

**도입 후보로 평가할 때**
- **지금은 도입 후보가 될 수 없다.** 일반 개발자·기업·소비자에게 공개되지 않았고 모델 ID, 가격, 컨텍스트, 데이터 보관이 공개되지 않았다. [부분/미확인] 조달 문서에 Carbon을 전제로 쓰지 않는다.
- **접근 경로를 확인한다.** 접근은 사이버 방어 담당자 일부에서 시작해 Fairwind 프로그램을 통한 신뢰 파트너로 단계적으로 확대된다. Fairwind는 승인된 파트너 전용이며 허용 범위는 승인된 위협 시뮬레이션, 리버스 엔지니어링, 방어·학술 연구 목적의 악성코드 분석이다. 승인 조건, 심사 기준, 약관은 프로그램 페이지에서 직접 확인한다. [부분]
- **벤더 1위 주장을 구분한다.** 지수 59(Artificial Analysis v5.0)는 Google이 인용한 값이고, 같은 정리에서 Opus 5.5는 58, Argon은 50이다. 사이버 벤치마크(SEC-bench Pro 88.2% 등)는 안전장치 없이 측정한 값이다. [부분]
- **정부 사전 시험.** Google은 미국 정부의 자발적 사전 시험 절차에 참여 중이라고 밝혔다. 시험 결과가 공개되는지, 일정이 어떻게 되는지는 확인하지 못했다. [부분/미확인]
- **이행 비용 예상.** Argon에서 이미 thought signature 요건, `MINIMAL`과 `thinking_budget` 거부가 있다. Carbon의 이행 가이드가 나오면 깨지는 변경 목록을 먼저 읽는다. [추정]
- **Fairwind 파트너가 받는 모델이 글마다 다르다**(Argon 또는 Gemini 3.8 Flash Cyber). 파트너 계약 전에 실제 제공 모델을 서면으로 확인한다. [부분]

**라이선스·규정**
- 이중 용도 능력의 사용 조건(약관, 수출 통제, 책임 있는 공개 의무)은 계약 문서로 확인하고, 규정 준수 여부를 모델이나 이 문서가 단정하지 않는다. 법무·보안 책임자의 검토를 거친다.

## 4. 근거와 한계
- 접근 단계·벤더 수치: [Gemini 4 Carbon: our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [Fairwind Program](https://deepmind.google/fairwind-program/), [Google 블로그: Fairwind](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/) (검색 스니펫만) [부분]
- 지수 비교: [Layer3 Labs: Gemini 4 Argon 리뷰](https://www.layer3labs.io/guides/gemini-4-argon-review) [부분: 2차]
- 한계: Google 공식 본문을 열지 못했다. 이 문서는 확인 항목 목록이며 모델 특성이 아니다.
