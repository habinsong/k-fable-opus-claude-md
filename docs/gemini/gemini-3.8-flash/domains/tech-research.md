# Gemini 3.8 Flash · 기술 연구 — 조사 기록
> 제공자: Google · 모델 ID: `gemini-3.8-flash` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-3.8-flash/tech-research.md`](../../../../md/gemini/gemini-3.8-flash/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 2027-01-01 이후 가격 2배 예상, 이전 Flash보다 작업당 비용이 높음, 첫 토큰 지연이 큼, 사이버 변종은 제한 제공.

**이 모델에게 기술 조사를 시킬 때**
- **분류·정리 단계에 쓴다.** 후보 수십~수백 개를 정해진 기준(라이선스 유형, 지원 언어, 최근 릴리스 날짜)으로 분류해 표로 만드는 일에 맞다. 값은 사람이 확보한 1차 자료 텍스트에서 추출하게 하고 원문에 없으면 null로 둔다. 지식 정답 비율 55%라도 기억으로 채우게 하지 않는다. [부분]
- **판단은 맡기지 않는다.** 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2). SPDX 식별자, 원문 링크, 공개 DB 검색 조건과 날짜만 받아 사람이 판단한다.

**3.8 Flash를 도입 후보로 평가할 때**
- **가격은 인상 후로 본다.** 입력 $0.75 / 출력 $3.75(100만 토큰당)가 2026-12-31까지 도입가이고 2027-01-01부터 $1.50 / $7.50이라는 2차 정리가 있다. 생각 토큰은 출력 요금이다. [부분] Google 공식 가격 페이지로 확인하기 전에는 확정하지 않는다.
- **작업당 총비용으로 비교한다.** 이전 Flash(3.7)보다 같은 평가에서 출력 토큰을 약 1.77배 내고 작업당 비용이 $0.74로 $0.55보다 높았다. 같은 과제·같은 `thinking_level`에서 GPT-6 Luna·Terra, Claude Haiku·Sonnet 5.5와 비교한다. [부분]
- **성능 지표를 구분한다.** 독립 지수는 지능 40.9, 코딩 76.3, 에이전트 40.2다. Google 비교표에서 Terminal-Bench 4.0이 Claude Opus 5보다 32.7점 낮다. DeepSWE v1.1 73.7%는 벤더 수치다. [부분]
- **지연 특성.** 첫 토큰까지 13.30초(중앙값 2.99초), 출력 속도는 196개 중 3위, 장황함 74위라는 측정이 있다. 대화형 제품에는 불리하고 배치·비동기에는 유리하다. [부분]
- **제한과 접근.** 사이버 변종 `Gemini 3.8 Flash Cyber`는 Fairwind 승인 파트너 전용이고 가격과 일반 공개 일정이 없다. 상위 모델 Argon(2026-11-30 이후 $4/$20)과 Carbon(제한 공개)은 별도 문서를 따른다. [부분]
- **도구 호환.** Gemini CLI는 Gemini 4 이후에 비최적화이고 3.8 Flash는 3.x 세대라 Gemini CLI와 `GEMINI.md`에 맞는다. [확인]
- **데이터·규제.** 3.8 Flash의 데이터 보관·학습 사용 조건과 규제 인증은 이 조사에서 확인하지 못했다. [미확인]

## 4. 근거와 한계
- 가격·사양: [Gemini 3.8 Flash (Google Cloud 문서)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash), [9to5Google](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/) (스니펫만) [부분]
- 비용·지수·지연·격차: [eesel.ai 리뷰](https://www.eesel.ai/blog/gemini-3-8-flash), [Gemini 3.8 Flash Review: The Token Bill](https://truestandard.ai/blog/gemini-3-8-flash-review), [DataNorth](https://datanorth.ai/news/google-launches-gemini-3-8-flash-gemini-3-8-flash-cyber) [부분]
- Gemini CLI: [google-gemini/gemini-cli README](https://github.com/google-gemini/gemini-cli) [확인]
- 한계: Google 공식 가격 페이지를 열지 못했다. 도입 결정 전에 다시 확인한다.
