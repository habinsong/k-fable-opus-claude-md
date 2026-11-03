# Claude Fable 5.1 · 범용 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-fable-5-1` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.1/general.md`](../../../md/claude/fable-5.1/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Claude Fable 5.1
Anthropic 공식 문서(models overview, What's new, Prompting Claude Fable 5.1, Effort)를 직접 읽고 쓴 내용이다. 별도 표기가 없으면 [확인]이다. Claude Mythos 5.1은 검증된 조직 전용이라 이 폴더에서 다루지 않는다.

### 2.1 위치와 사양
- Anthropic은 대부분의 워크로드는 **Opus 5.5로 시작**하고, 어려운 추론·장시간 에이전트 작업이거나 Opus 5.5의 높은 effort로도 평가 기준에 못 미칠 때 Fable 5.1을 쓰라고 안내한다.
- 가격은 입력 $10 / 출력 $50(100만 토큰당), 캐시 읽기 $0.25(입력가의 2.5%), 배치 $5/$25. 컨텍스트 1M(전 구간 표준 요금), 최대 출력 128K. 지식 컷오프 2026-06. 응답 속도는 현재 라인업에서 가장 느린 쪽(Anthropic 상대 지연 등급 "Slower").
- 토크나이저는 Opus 4.7 이전 모델보다 같은 글에서 토큰이 약 30% 더 나온다.
- 30일 데이터 보관, ZDR(보관 없음) 비대상, 모든 출력 텍스트에 통계적 워터마크가 들어간다(C2PA 자격 증명은 파일 출력에 한함).

### 2.2 API·하네스를 직접 만들 때 (Claude Code·Agent SDK 사용자는 자동 처리됨)
- **적응형 추론이 항상 켜져 있다.** `thinking: {"type":"disabled"}`와 `budget_tokens` 방식은 400 오류다. `temperature`·`top_p`·`top_k` 지정과 어시스턴트 프리필도 400이다.
- **강제 도구 호출이 없다.** `tool_choice`의 `any`·`tool`은 400이다. 스키마 보장은 `strict: true` 도구 사용이나 structured outputs로 하고, 도구를 쓰게 하려면 프롬프트에 언제 쓰는지 적는다.
- **대화 이력은 append-only로 유지한다.** thinking 블록은 앞의 시스템 프롬프트·도구·이전 메시지가 하나도 바뀌지 않았을 때만 유효하다. 이전 턴을 고치거나, 요청마다 넣었다 지우는 알림을 쓰거나, `system`·`tools`를 중간에 다시 만들면 뒤의 thinking이 무효가 되고 캐시도 깨진다. 턴 단위 알림은 turn-scoped system message(베타)로 보낸다. 2026-08-31 이후 만든 계정은 무효 블록에 400 오류가 기본이다.
- **thinking 블록은 같은 모델만 읽는다.** Fable 5.1 → 다른 모델로 바꾸면 그 턴들의 추론이 사라진다.
- **진행 알림은 기본으로 비어 온다.** `thinking.display`의 기본은 `omitted`다. 사용자에게 보이려면 `display: "updates"`(베타 헤더 `thinking-display-updates-2026-08-18`)를 켠다.
- 대화 중 effort 변경은 per-message `output_config`(베타 헤더 `mid-conversation-output-config-2026-07-01`)로 캐시를 지킨다. 최상위 `effort` 값을 바꾸면 캐시가 무효가 된다.
- 거부(`stop_reason: "refusal"`)를 클라이언트에서 처리한다. 대체 모델은 Opus 4.8·Opus 5다. 출력이 나오기 전의 일부 범주 거부는 2026-09-24부터 과금된다.

### 2.3 행동 특성과 이 문서를 쓰는 법 (Anthropic 지침 기준)
- **effort는 `high`(기본)에서 시작해 직접 비교한다.** `medium`은 Fable 5와 비슷한 결과를 더 싸게, `low`는 Opus·Sonnet과 비슷한 작업당 비용에 더 높은 점수를 낸다고 한다. `xhigh`·`max`는 측정으로 이득을 확인한 뒤에만 쓴다. `high` 이상에서는 `max_tokens`를 크게 잡는다(생각 토큰 포함 상한). `xhigh`·`max`는 긴 산출물을 생각 속에서 초안으로 쓰고 다시 쓰는 일이 있어 시간과 토큰이 늘어난다.
- **작업 중 말이 적다.** 도구 호출 사이의 사용자용 설명이 Fable 5보다 적다. 이 문서의 §0이 시작 한 줄(복명복창)과 독립적으로 읽히는 마지막 요약(5항목)을 요구하므로 Anthropic의 권장 방식과 맞는다. "결과를 마지막에만 말하라"는 식의 지침은 넣지 않는다.
- **독립 호출을 묶어 보내지 않을 때가 있다.** 코딩·컴퓨터 사용 루프에서 암시된 독립 호출을 턴마다 하나씩 보낸다. 시간과 토큰이 늘 뿐 정확도는 영향이 없다. 하네스에서 "먼저 필요한 것을 모두 나열하고, 서로 의존하지 않는 호출은 한 번에 요청하라"를 덧붙인다.
- **끝까지 하게 만들되 승인 규칙은 §1.6이 우선한다.** Anthropic은 장시간 비동기 작업에서 "다음에 ~하겠습니다"라고 쓰고 멈추거나 이미 요청된 단계의 허락을 묻는 문제를 막으려면 "되돌릴 수 있는 일은 묻지 말고 진행, 파괴적 동작과 범위 변경에서만 멈춤"을 쓰라고 한다. 이 저장소에서는 파괴적·외부 영향 동작의 승인 규칙(§1.6)을 그대로 두고, 그 밖의 되돌릴 수 있는 단계에서는 묻지 않고 진행한다.
- **범위 밖 변경을 억제한다.** 열린 요청에서 근처 코드를 고치거나 테스트 파일을 필요 이상 추가하는 경향이 있다. "발견한 기존 버그·성능 문제는 이 변경에서 고치지 말고 후속으로 보고하라, 테스트는 요청이 있거나 저장소가 같은 종류의 변경에 테스트를 두는 경우에만 커밋하라"는 지침이 효과가 있었다고 한다. §1.6과 같은 방향이다.
- **작은 수정에도 파일 전체를 다시 쓰려는 경향이 있다.** "가능하면 파일을 통째로 다시 쓰지 말고 필요한 부분만 고쳐라"를 명시한다. 출력 토큰과 시간이 줄어든다.
- **낮은 effort에서는 검색을 덜 한다.** `low`에서는 기억으로 답하는 일이 늘어난다. 최신 정보가 필요한 턴은 effort를 올리거나, 이름을 사용자가 쓴 그대로 검색해 확인하게 한다.
- **요약에서 출처 문장을 따옴표 없이 옮길 수 있다.** 요약은 간접 화법으로 쓰고, 인용은 짧게 표시한다(§1.5).
- **채팅에서 서식이 줄고 문장이 길고 촘촘하다.** 목록·표가 필요한 내용에는 필요하다고 명시한다.

### 2.4 비판적 평가 (독립 측정·리뷰는 2차 출처)
- **비용 대비 토큰 사용이 크다.** Artificial Analysis 기사에 따르면 Astra는 같은 점수에 작업당 출력 약 27k 토큰, Fable 5.1(`max`)은 약 78k 토큰이다. 같은 기사에서 Terminal-Bench v4.0은 Astra 59%, Fable 5.1 52%다. 반면 같은 기관의 코딩 에이전트 지수에서는 Claude Code 기준 Fable 5.1이 70으로 가장 높고 Codex 기준 Astra가 67이다. 지표와 하네스에 따라 순위가 바뀐다. [부분]
- **벤더 수치는 독립 확인 전이다.** SWE-Bench Pro 81.2%는 Anthropic 자체 보고다. 일부 안전장치가 개입한 평가는 0점 처리돼 측정 점수가 낮아졌을 수 있다는 리뷰가 있다. [부분]
- **안전장치의 거짓 양성.** 거짓 양성이 Fable 5보다 줄었다고 하지만 남아 있다. "이 프로그램이 컴파일되는가?" 같은 표현, 덜 알려진 언어, 도구 출력의 base64가 원인이 되기 쉽다. 질문을 "이 프로그램에 버그가 있는가?"로 바꾸거나 언어 문서를 주고, base64를 컨텍스트에 넣지 않는다. [확인]
- **쓸 수 있는 곳이 좁다.** 가장 높은 사이버 기능은 검증된 조직 전용 Mythos 5.1에만 있고, 리뷰들은 일상 작업에는 과하다고 평가한다. [부분]
- **ZDR 불가.** 데이터 보관 요건이 엄격한 조직은 사용할 수 없다. [확인]

### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 몇 시간 단위의 대규모 리팩터링·이전, 여러 문서를 가로지르는 조사, Opus 5.5의 `high`·`xhigh`로도 막히는 어려운 문제.
- 쓰지 않는다: 일상적인 구현·리뷰(Opus 5.5나 Sonnet 5.5), 대량·저지연 작업(Haiku 5.5), ZDR이 필요한 업무, 비용에 민감한 반복 루프.
- 시작은 `high`, 반복 작업은 `medium`, 가볍지만 어려운 질문은 `low`도 비교한다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 모델 ID·가격·컨텍스트·지연 등급 | [Models overview](https://platform.claude.com/docs/en/models/overview) | [확인] |
| API 변경·제약·거부·과금·가용성 | [What's new in Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) | [확인] |
| 행동 특성과 권장 프롬프트 | [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) | [확인] |
| effort 권장 | [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) | [확인] |
| 독립 측정·리뷰 | [Artificial Analysis: Benchmarking GPT-6 Astra](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra), [Layer3 Labs 리뷰](https://www.layer3labs.io/guides/claude-fable-5-1-review), [Tabbit 리뷰](https://go.tabbit.ai/blog/claude-fable-5-1-review) | [부분] |
- 위 1차 문서는 Anthropic 자신의 서술이다. 성능 비교(순위, 토큰 사용)는 2차 출처이며, 지표와 하네스에 따라 결과가 달라진다.
- 시스템 카드(2026-09-01)는 열어 보지 않았다. 안전·평가 세부는 시스템 카드로 다시 확인한다.
