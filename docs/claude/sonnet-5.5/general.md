# Claude Sonnet 5.5 · 범용 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/sonnet-5.5/general.md`](../../../md/claude/sonnet-5.5/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Claude Sonnet 5.5
Anthropic 공식 문서(models overview, What's new, Prompting Claude Sonnet 5.5, Effort)를 직접 읽고 쓴 내용이다. 별도 표기가 없으면 [확인]이다.

### 2.1 위치와 사양
- "속도와 지능의 가장 좋은 조합"으로 안내된다. Anthropic은 가장 어려운 장시간 작업에는 Opus를 권한다.
- 가격은 입력 $2 / 출력 $10(100만 토큰당), 캐시 읽기 $0.10(Sonnet 5의 절반). 컨텍스트 1M, 최대 출력 128K, 지식 컷오프 2026-06. 토크나이저는 Sonnet 5와 같다. 기본 effort는 Claude API에서 **`high`**이고 `low` / `medium` / `high` / `xhigh` / `max`를 지원한다. 레벨이 재조정돼 Sonnet 5의 같은 레벨과 생각량이 다르다.
- 추론은 적응형이 기본이고, 끄려면 `thinking: {"type":"between_tools"}`를 쓴다(`low`·`medium`·`high`에서만, `xhigh`·`max`에서는 400). `disabled`는 400이다.

### 2.2 API·하네스를 직접 만들 때 (Claude Code·Agent SDK 사용자는 자동 처리됨)
- **강제 도구 호출이 없다.** `tool_choice`의 `any`·`tool`은 400이다. `strict: true`나 structured outputs를 쓴다.
- **`between_tools`는 다른 필드와 같이 보낼 수 없다.** `display`·`budget_tokens`·`block_binding`을 함께 보내면 400이다. `between_tools`에서는 도구 사이 진행 알림이 요약 텍스트로 돌아오고, 도구가 없는 요청에서는 추론 없이 바로 답한다. 이때 effort를 대화 중 바꾸면 400이므로 턴마다 effort를 바꾸려면 적응형을 쓴다.
- **추론 블록은 모델·대화·계정에 묶인다.** Sonnet 5.5는 Sonnet 5, Opus 4.8, Haiku 4.5 이하와 Haiku 5.5(Claude API)의 블록을 읽지만 Opus 5/5.5와 Fable·Mythos의 블록은 읽지 못한다. Opus 5.5는 Sonnet 5.5의 블록을 읽는다. 이력은 append-only로 유지하고, 계정이 2026-08-31 이후 만들어졌고 `prefix_mismatch_behavior`를 설정하지 않으면 무효 블록에 400 오류다.
- **도구 사이 설명이 `thinking` 블록으로 온다.** 사용자에게 보이려면 `display: "updates"`(베타)를 켜거나 `between_tools`를 쓴다.
- 컴퓨터 사용은 `computer_toolset_20260801`을 쓴다. 어드바이저 도구는 허용된 짝만 된다(Opus 4.8·4.7, Sonnet 5, Haiku 5.5는 어드바이저로 거부).
- 거부는 `stop_reason: "refusal"`의 5개 범주(`cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`)로 온다. 서버 쪽 대체는 `cyber`·`frontier_llm`만 Sonnet 5로 재시도한다.

### 2.3 행동 특성과 이 문서를 쓰는 법 (Anthropic 지침 기준)
- **effort를 새로 훑는다.** 기본 `high`에서 시작하되 에이전트·지연에 민감한 작업은 `medium`부터 시작한다. 채팅은 `medium`이나 `low`다. `medium` 이상에서는 인사에도 짧게 생각해 첫 토큰이 늦다. 생각을 줄이려면 프롬프트가 아니라 effort를 낮춘다. `xhigh`·`max`는 측정된 이득이 있을 때만 쓰고 `max_tokens`를 크게(128K) 잡고 스트리밍한다.
- **`low`에서는 검증을 건너뛴다.** 코드를 바꾸고 테스트·빌드를 돌리지 않은 채 완료라고 보고하는 일이 있다. 그래서 "실행 가능한 코드를 바꿨으면 변경을 실제로 시험하는 검사(프로젝트 테스트, 타입 체커, 빌드, 바뀐 명령 자체)를 돌린 뒤에 완료를 보고하라. 문법 검사만으로는 인정되지 않는다. 의존성이 없을 뿐이면 프로젝트의 패키지 관리자로 설치하고 `sudo`나 시스템 패키지 관리자는 쓰지 말라. 시험이 불가능하면 어떤 검사를 왜 못 했는지 말하고 완료로 보고하지 말라"를 시스템 프롬프트에 넣는다. §1.2·§1.3과 같은 방향이다.
- **`low`·`medium`에서는 중간에 확인을 구하며 멈춘다.** 계획 확인, 스스로 답할 수 있는 질문, 여러 부분 중 하나를 끝낸 뒤의 계속 여부를 묻는다. "사용자가 요청한 일이 끝날 때까지 계속하고, 사용자 없이는 진행할 수 없거나 위험한 단계 앞에서만 멈춰라. 요청한 일이 끝나 확인되면 멈추고 보고하라. 요청하지 않은 기능·테스트·파일·문서·리팩터링은 하지 말고 끝에서 제안만 하라"를 쓴다. 이 문서의 승인 필요 동작은 §1.6 목록뿐이다.
- **요청하지 않은 테스트·문서·보조 파일을 덧붙인다.** 모든 effort에서 나타나고 높을수록 많다. 원치 않으면 위 지시의 둘째 문단을 쓴다. `xhigh`·`max`에서 이 문단이 추가 점검을 줄여 준다.
- **`xhigh`·`max`는 요청하지 않은 점검 라운드를 시작한다.** 완료 후 스스로 리뷰·강화 라운드를 돌리고, 하위 에이전트를 띄우기도 하고, 관련 수정을 덧붙인다. "요청한 일이 끝나고 검사가 통과하면 멈추고 보고하라. 스스로 추가 리뷰나 강화를 시작하지 말고, 요청이 없으면 리뷰어 하위 에이전트를 띄우지 말라"는 지시가 `max`에서 세션 비용을 약 3분의 1 줄였다고 한다.
- **열린 요청에 만들기부터 시작한다.** "무엇을 할 수 있는지 보여 줘"에 발표 자료나 영상을 만들기 시작한다. "아이디어·선택지·계획을 요청하면 그것을 주고 멈춰라"를 쓴다.
- **JSON을 요구하는 추론 과제는 적응형으로 한다.** 몇 단계 계산이 필요한 JSON 답은 추론 없이 답하면 틀리기 쉽다(`low`·`medium`에서 특히). structured outputs에서는 "답하기 전에 문제를 끝까지 생각하라"를 시스템 프롬프트 끝에 넣거나 `xhigh`를 쓴다. `between_tools`에서는 효과가 없다. `stop_reason`이 `max_tokens`인 응답은 JSON이 유효해도 실패로 보고 재시도한다. [확인]
- **채팅·지식 작업에서 검색을 덜 부른다.** 허용·요구·요금처럼 바뀐 세부를 학습 지식으로 답할 수 있다. 도구 사용을 억제하는 문구를 지우고 "바뀌었을 수 있는 세부는 확신이 있어도 검색으로 확인하라"를 넣는다.
- **사용자가 작업 중 보낸 메시지를 주입으로 오해할 수 있다.** 사용자 글을 `tool_result` 안에 넣지 말고, `tool_result` 뒤 같은 사용자 메시지의 텍스트 블록으로 보낸다. 토큰 카운트다운 같은 하네스 문구를 매 도구 결과 뒤에 붙이지 않는다.
- **도구 이름 대소문자나 매개변수 이름이 조금 어긋난 호출을 낼 수 있다.** 명확하면 받아 주거나, 기대한 정확한 이름을 담은 `is_error: true` 결과로 돌려준다.
- **복잡한 차트·도면은 자르기·확대 도구를 준다.** 차트는 모든 effort에서, 기술 도면은 `high` 이상에서 효과가 있다.
- **진행 알림은 직접 요구한다.** 시작 한 줄과 독립적으로 읽히는 마지막 요약은 §0이 요구한다.

### 2.4 비판적 평가 (독립 측정은 2차 출처)
- **`max`가 비싸고 점수가 떨어졌다는 보고.** Artificial Analysis에서 작업당 비용이 Sonnet 5.5(`max`) $7.60, Opus 5.5 $5.98로 보고됐다(토큰을 더 씀). 한 평가에서 점수도 `xhigh` 52.1%에서 `max` 46.2%로 낮아졌다. → `max`를 기본으로 쓰지 않는다. [부분]
- **지식·사실 회상이 약하다.** Artificial Analysis 지식 평가에서 Sonnet 5.5 54%, Opus 5.5 66%. 시스템 카드는 Sonnet 5보다 오답을 낼 가능성이 약간 높은 대신 맞히는 문제도 더 늘었다고 한다는 보도가 있다. → 사실 질의는 검색으로 확인한다. [부분]
- **종합 지수는 높다.** Artificial Analysis 지능 지수 56으로 Opus 5.5(58) 다음이라는 보도가 있다. Terminal-Bench 수치는 출처마다 70.6% 대 66.4%, 64% 대 60%로 다르고 독립 초기 결과는 Anthropic 수치보다 낮다. Opus 5.5에 대한 우위는 한 벤치마크에 의존한다. [부분]
- **글쓰기에서 Opus 5.5와 격차가 있다는 평가.** 미적·인문적 글쓰기에서 격차가 크고 명료성에서는 비슷하다고 한다. 개별 후기다. [부분]
- **끈기가 약하다는 사용자 보고.** 답을 얻으려고 계속 시도하는 데 소극적이라 점수가 낮아진 사례가 있다. 개별 후기다. [부분]
- **이행 비용.** Sonnet 5에서 올 때 깨지는 변경이 5가지다(`between_tools`, 강제 도구 호출, 추론 블록, 컴퓨터 사용 도구, 어드바이저 짝). 높은 위험의 사이버 요청은 눈에 띄게 Sonnet 5로 넘어간다는 보고가 있다. [확인/부분]
- 한 코딩 후기(체스 엔진 구현)에서는 Opus 5.5와 같은 정확도를 약간 더 빠르게, 절반 가격으로 냈다는 사례가 있다. 단일 사례다. 같은 후기는 검토 없이 받아들일 수 있던 실행은 Opus 5.5뿐이었다고 적었다. [부분]

### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 대부분의 구현·수정·리뷰, 속도가 중요한 에이전트 작업, 채팅·지식 작업, 비용에 민감한 반복 루프.
- 올린다: 가장 어려운 장시간 작업은 Opus 5.5(Anthropic 권고).
- 내린다: 단순 대량 작업은 Haiku 5.5.
- 시작은 `high`(에이전트는 `medium`). 코드 변경 후 검증을 강제하는 지시를 항상 넣는다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 모델 ID·가격·컨텍스트 | [Models overview](https://platform.claude.com/docs/en/models/overview) | [확인] |
| API 변경·thinking 모드·거부·가용성 | [What's new in Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5) | [확인] |
| 행동 특성과 권장 프롬프트 | [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) | [확인] |
| effort | [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) | [확인] |
| 비용·지식·지수 | [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-sonnet-5-5-review), [Claude 5.5 is brilliant, confusing, and very hungry](https://dreasays.substack.com/p/claude-55-is-brilliant-confusing), [Kingy.ai](https://kingy.ai/blog/claude-sonnet-5-5-specs-benchmarks-pricing/), [Thomas Wiegold 비교](https://thomas-wiegold.com/blog/claude-sonnet-5-5-review/) | [부분] |
- 시스템 카드 원문은 열어 보지 않았다. 오답 가능성에 대한 서술은 2차 보도 기준이다.
- 위 비용·점수는 Artificial Analysis를 인용한 후기들이며 값이 출처마다 다르다. 원본 데이터로 다시 확인한다.
