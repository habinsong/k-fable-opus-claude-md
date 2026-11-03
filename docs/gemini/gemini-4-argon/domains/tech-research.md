# Gemini 4 Argon · 기술 연구 — 조사 기록
> 제공자: Google · 모델 ID: `gemini-4-argon` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-argon/tech-research.md`](../../../../md/gemini/gemini-4-argon/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 2026-11-30 이후 가격 2배, 독립 평가 점수는 Opus 5.5보다 낮음, 토큰 사용이 큼, 누락 기능이 있음, 벤더 수치가 페이지마다 다름.

**이 모델에게 기술 조사를 시킬 때**
- 비교표의 모든 칸에 출처와 확인 수준을 붙이게 하고, 직접 열지 않은 출처의 칸은 비워 두게 한다. 환각을 모델 카드가 인정하므로 출처를 직접 연다. [부분]
- 라이선스·특허 판단은 단정하지 않는다. SPDX 식별자, 원문 링크, 공개 DB 검색 조건과 날짜만 받아 사람이 판단한다(§3.2).
- 자기 검증이 약하다는 후기가 있으므로 [부분] 결과를 쓰기 전에 반대 근거와 약한 근거를 따로 적게 한다.

**Argon을 도입 후보로 평가할 때**
- **가격은 도입가가 아니라 인상 후 가격으로 본다.** 입력 $2 / 출력 $10(캐시 입력 $0.10)이 2026-11-30 이후 $4 / $20이 된다는 Google 발표의 각주가 있다. 무료 티어가 없다. [부분]
- **독립 평가 점수와 벤더 수치를 나눠 본다.** Artificial Analysis v5.0에서 Argon 50, Opus 5.5 58, Google이 소개한 Carbon 59라는 2차 정리가 있다. Terminal-Bench 4.0은 Google 수치 57.4%(발표 글 57.1%)이고 같은 정리에서 Opus 5.5는 66.4%다. Vals Index 1위, DeepSWE v1.1 77.9%는 Google 자체 보고다. [부분]
- **토큰 사용.** 지수 평가에서 출력 약 1.1억 토큰을 썼고 중앙값은 8,200만이라는 리뷰가 있다. 작업당 총비용을 같은 과제·같은 `thinking_level`로 비교한다. [부분]
- **누락 기능과 제약.** Live API, 명시적 캐싱, 이미지·오디오 생성이 없다고 지적된다. 입출력·생각이 통합 한도를 나눠 쓴다. 최대 출력 한도는 출처가 엇갈린다. [부분/미확인]
- **도구 호환.** Gemini CLI는 Gemini 4에 최적화돼 있지 않아 Antigravity CLI를 써야 한다. Antigravity 접근 등급(Ultra만 / Pro 포함)이 글마다 다르다. [확인/부분]
- **이행 비용.** 함수 호출 시 thought signature를 돌려주지 않으면 검증 오류이고, `MINIMAL`과 `thinking_budget`은 400이다. [부분]
- **사이버 능력과 제한.** 모델 카드는 사이버 임계 능력 도달 가능성을 배제하지 못한다고 한다. 이중 용도 작업은 Fairwind 승인 파트너에 한한다는 안내가 있다. 상위 모델 Carbon은 제한 공개 단계다(`gemini-4-carbon` 문서 참고). [부분]
- **데이터·규제.** Argon의 데이터 보관·학습 사용 조건과 규제 인증은 이 조사에서 확인하지 못했다. [미확인]

## 4. 근거와 한계
- 가격 인상·벤더 수치: [Gemini 4 Argon: Built to solve your hardest problems](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/), [Now available for developers](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/) (스니펫만) [부분]
- 지수·토큰·누락 기능: [Layer3 Labs 리뷰](https://www.layer3labs.io/guides/gemini-4-argon-review), [eesel.ai 리뷰](https://www.eesel.ai/blog/gemini-4-argon-review), [BenchLM](https://benchlm.ai/models/gemini-4-argon) [부분]
- 한계: Google 공식 가격·모델 페이지를 직접 열지 못했다. 도입 결정 전에 공식 페이지로 다시 확인한다.
