# Gemini 4 Argon · 범용 — 조사 기록
> 제공자: Google · 모델 ID: `gemini-4-argon` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-argon/general.md`](../../../md/gemini/gemini-4-argon/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Gemini 4 Argon
이 환경에서는 `ai.google.dev`, `docs.cloud.google.com`, `blog.google`, `deepmind.google` 본문이 열리지 않아 Google 공식 도메인의 검색 스니펫과 2차 출처로 썼다. GitHub의 Gemini CLI README만 직접 읽었다. 별도 표기가 없으면 [부분]이다.

### 2.1 위치와 사양
- Google의 플래그십 모델이다. 2026-10-13에 정식 출시(GA)됐고 Gemini API에서는 유료 티어로만 쓸 수 있다고 한다. 모델 ID는 `gemini-4-argon`이다.
- **가격이 곧 오른다.** 도입가는 입력 $2 / 출력 $10(100만 토큰당), 캐시 입력 $0.10이다. Google 발표의 각주는 **2026-11-30 이후 $4 / $20**이 적용된다고 적었다. 이 저장소의 기준일에서 4주도 안 남았다. 비용 계획은 인상된 가격으로 세운다.
- **컨텍스트는 입력·출력 통합 한도 1,048,576 토큰**이고 생각 토큰도 같은 예산을 쓴다. 최대 출력은 출처가 엇갈린다. Google 발표는 출력 한도가 이전 64K에서 1M으로 늘었다고 하지만, 집계 사이트는 API 모델 항목에 65,536(Vertex 비스트리밍은 32,768)으로 적었다. 실제 한도는 모델 페이지로 확인하기 전에 단정하지 않는다. [미확인]
- **추론 강도는 `thinking_level`**: `LOW` / `MEDIUM`(기본) / `HIGH`. `MINIMAL`이나 `thinking_budget`을 지정하면 HTTP 400이다(`thinking_budget`은 Gemini 4에서 deprecated). 사이버 변종 `gemini-4-argon-cyber-permissive`의 기본은 `HIGH`다.
- **함수 호출에는 thought signature를 되돌려줘야 한다.** Gemini 4와 3은 함수 호출 시 thought signature를 돌려주지 않으면 검증 오류다. 병렬 호출은 첫 함수 호출 파트에 서명이 붙고, 순차 호출은 호출마다 서명이 붙으며 모두 돌려줘야 한다. 응답의 모든 파트를 그대로 다음 턴에 넣는다.
- 지원 도구: 함수 호출, structured outputs, 코드 실행, Google 검색·지도 grounding, URL 컨텍스트, 파일 검색, 컴퓨터 사용(프리뷰). 없는 기능으로 지적된 것: Live API, 명시적 캐싱(암묵적 캐싱만), 이미지·오디오 생성. 초기에 일부 사용자가 `404 NOT_FOUND`를 겪었다는 보고가 있다.

### 2.2 도구·하네스
- **Gemini CLI는 Gemini 4 이후에 최적화돼 있지 않다.** README가 직접 그렇게 적고 Gemini 4 Argon 이후는 Antigravity CLI를 쓰라고 안내한다. [확인] Antigravity CLI는 `AGENTS.md`를 읽고 `GEMINI.md`는 하위 호환으로만 읽으며 `AGENTS.md`로 바꾸길 권한다는 안내가 있다. 두 파일이 충돌할 때의 우선순위는 출처마다 다르다. [부분]
- 이 문서를 Antigravity CLI에서 쓰려면 `AGENTS.md`로 복사하고, `GEMINI.md`와 둘 다 두지 않는다(충돌 방지).

### 2.3 행동 특성과 이 문서를 쓰는 법
- **effort를 명시한다.** `thinking_level`은 항상 지정한다. 기본 `MEDIUM`에서 시작하고, 어려운 문제에서만 `HIGH`로 올린다. `MINIMAL` 용도(빠른 단순 응답)는 `LOW`로 대체한다.
- **지침과 오래된 명세에 휘둘린다는 후기가 있다.** 개발자 포럼의 한 글은 코딩이 기대에 못 미치고 정확성보다 규칙을 우선하며 레거시 명세·코드에 주의가 흐트러진다고 적었다. 개별 후기다. → 컨텍스트에 낡은 문서·충돌하는 지침 파일을 두지 않고, 규칙과 정확성이 부딪히는 경우 어느 쪽이 우선인지 지시한다(이 문서는 사용자의 현재 지시가 우선).
- **스스로 검증하고 되돌아가 검토하는 일이 약하다는 평가가 있다.** 한 후기는 좋은 코더지만 Claude만큼 자기 검증과 코드 재검토로 돌아가는 데는 약하다고 했다. → §1.2 루프를 문장으로 지시한다: "변경 후 실제 검사를 돌리고, 출력을 읽고, 실패하면 원인을 고쳐 다시 돌려라. 검사를 못 돌렸으면 못 했다고 말하라."
- **구조 편집에 강점이 있다는 후기.** 한 평론가는 이 모델을 구조 편집기로서 가장 좋았다고 평가했다. 단일 후기다.
- **샘플링 파라미터의 권장값은 Gemini 4 문서에서 확인하지 못했다.** [미확인] 이전 세대(Gemini 3) 문서가 기본 temperature를 바꾸지 말라고 권한 것으로 알려져 있으나 Gemini 4에 적용되는지 확인하지 못했다.
- **최종 보고는 5항목, 항목당 1~2줄.**

### 2.4 비판적 평가 (벤더 수치와 2차 평가를 구분)
- **독립 지수는 Opus 5.5보다 낮다.** Artificial Analysis Intelligence Index v5.0에서 Argon 50, Claude Opus 5.5 58, Google이 소개한 Gemini 4 Carbon 59로 정리한 2차 보도가 있다. Terminal-Bench 4.0은 Google 수치 57.4%(발표 글은 57.1%, 페이지마다 다름)이고 같은 정리에서 Opus 5.5는 66.4%다. 이 수치는 2차 출처가 옮긴 것이다. [부분]
- **벤더 수치.** Vals Index 1위(모델 카드 68.9%), DeepSWE v1.1 77.9% 신기록, Gray Swan 간접 프롬프트 인젝션 평가 선두는 모두 Google 자체 보고다. Google 자신의 비교표도 FrontierSWE, Terminal-Bench-Science 등에서 일부 경쟁 모델에 뒤진다고 보인다. Antigravity에서 에이전트 코드 제출이 35% 넘게 늘고 롤백이 거의 3분의 1 줄었다는 것도 Google 내부 서술이다. [부분]
- **토큰을 많이 쓴다.** 한 리뷰에 따르면 지수 평가를 돌리며 출력 약 1.1억 토큰을 생성했고 중앙값은 8,200만이다. 가격 인상(2026-11-30)과 겹치면 비용 부담이 커진다. [부분]
- **환각.** 모델 카드가 기반 모델의 일반적인 한계로 환각을 인정한다. 한 리뷰는 출시 요약에서 근거 없는 문장을 발견했다. 환각률 수치는 찾지 못했다. [부분/미확인]
- **사이버 임계 능력.** 모델 카드는 사이버 보안의 임계 능력 수준에 도달했을 가능성을 배제할 수 없다고 하며 안전장치를 적용한다고 한다. 정당한 보안 작업이 제한될 수 있다. [부분]
- 리뷰들이 서로 엇갈리고 방법론이 불분명한 블로그가 많다.

### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 어려운 문제의 구조 설계·문서 편집, 긴 컨텍스트 종합, Google 생태계(검색·지도 grounding, URL 컨텍스트)를 쓰는 작업.
- 쓰지 않는다: 자기 검증이 핵심인 자율 코딩(Claude 계열이나 GPT-6.1 Sol과 비교), 비용이 중요한 대량 작업(Gemini 3.8 Flash), 가격 인상 이후 예산이 빠듯한 반복 루프.
- 시작은 `MEDIUM`, 막히면 `HIGH`. 비용은 2026-11-30 이후 가격으로 계산한다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 출시·가격·컨텍스트·벤더 벤치마크 | [Gemini 4 Argon: Built to solve your hardest problems](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/), [Now available for developers](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/), [모델 카드](https://deepmind.google/models/model-cards/gemini-4-argon/) (검색 스니펫만) | [부분] |
| thinking 레벨·thought signature | [Thinking (Google Cloud)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking), [Thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures) (스니펫만) | [부분] |
| Gemini CLI와 Gemini 4 | [google-gemini/gemini-cli README](https://github.com/google-gemini/gemini-cli) (직접 읽음) | [확인] |
| 독립 평가·결함 지적 | [eesel.ai 리뷰](https://www.eesel.ai/blog/gemini-4-argon-review), [Layer3 Labs 리뷰](https://www.layer3labs.io/guides/gemini-4-argon-review), [Google AI 개발자 포럼](https://discuss.ai.google.dev/t/how-bad-is-gemini-4-argon/190009) | [부분] |
- Google 공식 본문을 열지 못해 최대 출력, 기본 샘플링 값, 정확한 요금 규칙은 확인하지 못했다. 도입 전에 공식 모델 페이지로 다시 확인한다.
- Antigravity 접근 등급(Ultra만 / Pro 포함)이 글마다 달라 현재 요건을 확인한다.
