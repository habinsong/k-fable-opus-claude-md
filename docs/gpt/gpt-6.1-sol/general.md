# GPT-6.1 Sol · 범용 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.1-sol` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6.1-sol/general.md`](../../../md/gpt/gpt-6.1-sol/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — GPT-6.1 Sol

### 2.1 위치와 사양
- GPT-6 계열의 균형형. OpenAI는 "복잡한 작업에서 Astra에 근접한 성능을 더 낮은 비용으로" 제공하는 모델로 안내한다. 출시일은 2026-09-29로 보도됐다. [확인: 위치 / 부분: 날짜]
- 가격은 입력 $2 / 출력 $10(100만 토큰당)으로 대부분의 집계가 같고, Astra($10/$50)의 5분의 1이다. GPT-6 Sol과 표준 가격은 같고 캐시 읽기만 절반($0.10)이라는 리뷰가 있다. 한 사이트는 $2.11/$10.55로 적었는데 이상치로 본다. [부분, 집계 사이트]
- 컨텍스트 1.05M, 최대 출력 128K로 집계가 일치한다. 입력이 272K를 넘으면 요청 **전체**에 입력·캐시 2배, 출력 1.5배 요금이 붙는다는 보고가 있다. [부분]
- 추론 강도는 `low` / `medium`(기본) / `high` / `xhigh` / `max`. `none`·`minimal`은 지원하지 않는다(400). 문서는 `medium`에서 시작하고 품질 향상이 시간·토큰 비용을 정당화할 때만 올리라고 안내한다. `reasoning.context: all_turns`도 지원한다. [확인/부분]
- "GPT-6.1 Astra"는 가정하지 않는다. 한 정리 글은 OpenAI가 안전 문제로 6.1 Astra를 보류했다고 적었지만 확인되지 않았다. 이 폴더의 Astra는 `gpt-6-astra`다. [미확인]

### 2.2 API를 쓸 때
- 도구 호출은 **Responses API**로 한다. Chat Completions는 도구 호출을 지원하지 않는다. [확인]
- effort가 `none`이 아니면 `temperature`, `top_p`, `top_logprobs`를 보내지 않는다. 옛 코드의 `none`·`minimal`은 `low`로 바꿔 비교한다. 이 세 가지(effort `none`, 샘플링 파라미터, Chat Completions의 도구)가 이전 때 가장 흔한 오류 원인이라는 개발자 커뮤니티 정리가 있다. [확인/부분]
- 대화 중 effort 변경은 `configuration_update` 항목으로 하고 요청 수준 `reasoning.effort`는 고정한다(캐시 보존). 모델 문자열만 바꾸지 말고, 같은 effort로 기존 설정과 먼저 비교한다. [확인]
- Fast 모드는 EU 데이터 레지던시에서 쓸 수 없고, Ultrafast는 미국·글로벌 처리만 지원한다. [확인]

### 2.3 행동 특성과 이 문서를 쓰는 법
- OpenAI는 "Sol이나 Luna에 도움이 되는 지침이 Astra에는 과할 수 있다"고 언급했다. 거꾸로 말하면 Sol에는 구체적인 절차, 제약, 검증 명령을 적어 주는 것이 Astra보다 더 도움이 된다. [부분]
  → 이 문서의 §1.2 루프와 §3의 검증 순서를 따르게 하고, 작업 시작 때 통과해야 할 검증 명령을 직접 적어 준다.
- "끝까지 완료하라"는 initiative-and-follow-through 지침 블록이 "Using GPT-6" 가이드에 있다. 승인 요청이 지나치게 잦을 때만 쓰고, 승인이 필요한 동작은 §1.6 목록으로 한정한다. [부분]
- 같은 규칙을 반복해서 적지 않는다. 충돌하는 지침 파일이 있으면 사용자 지시가 우선한다고 한 번만 적는다.
- 최종 보고는 5항목, 항목당 1~2줄로 쓴다.

### 2.4 비판적 평가 (독립 테스트·보도, 대부분 2차 출처)
- **동작하는 코드가 안전한 코드는 아니다.** Endor Labs가 Codex 하네스로 측정했을 때 기능 통과율은 77.7%(Astra보다 낮음), 보안 통과율은 34.1%였다. 제목은 "Astra 수준의 보안"이라고 하지만 절대 수치는 낮다. 한 업체의 단일 테스트다. [부분]
  → 생성된 코드는 기능 테스트와 별도로 보안 검토 단계를 거친다(입력 검증, 인가, 비밀 처리, 의존성). 테스트 통과를 안전하다는 뜻으로 보고하지 않는다.
- **속도와 토큰은 장점이다.** 같은 테스트에서 작업당 중앙값 8분(GPT-6 Sol·Astra는 약 11.5분), 시간 초과 9건(12~13건), 토큰 사용도 더 적었다. 해석은 "Astra와의 차이는 몇 점의 기능 통과율 대 약 5배 가격"이다. [부분]
- **어려운 문제에서는 Astra에 못 미친다.** 가장 어려운 사이버·생물·과학 평가에서 Astra보다 낮다는 정리가 있다. [부분]
- **코딩 기만에 대한 평가가 엇갈린다.** DataCamp는 코딩 기만과 불필요한 지속에서 Astra보다 나쁜 점수라고 정리했고, Endor Labs는 "속임수 0건"이라고 했다. 측정 방식이 다르다. [부분, 충돌]
  → 테스트를 통과시키려고 테스트·기대값·검증 스크립트를 고치지 않았는지 `git diff`로 매번 확인한다(§1.2, §1.6).
- **`max` effort는 비용이 크다.** GPT-5.6 Sol의 `max`보다 훨씬 느리고 추론 토큰이 많다는 개발자 포럼 보고가 있다(공식 문서 아님). `max`를 기본값으로 쓰지 않고 측정한 뒤 쓴다. [부분]
- **벤더 수치.** 사실 오류율이 낮은 effort에서 11.4%에서 7.7%로 줄었다는 보도는 OpenAI의 주장이다. 개선돼도 약 13건 중 1건은 틀릴 수 있다는 뜻이다. [부분]
- 아레나 순위는 보드마다 다르다(종합은 Sol, 코딩은 Astra 우세). 단일 순위로 결론내지 않는다. [부분]

### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 일상적인 구현·수정·리뷰·디버깅의 기본 모델, 반복 루프가 많은 에이전트 작업, 비용에 민감한 장시간 작업.
- 올린다: 같은 문제에서 두 번 이상 막히면 Astra로 올린다. 시작은 `medium`, 어려우면 `high`.
- 쓰지 않는다: 가장 어려운 연구·보안 분석(Astra), 대량·저지연 단순 작업(Luna·Terra).

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| API 규칙, effort, 이전 원칙 | [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) | [확인] |
| 모델 페이지·기본 effort·`all_turns` | [GPT-6.1 Sol Model](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model) (스니펫만) | [부분] |
| 이전 시 오류, `max` 지연 | [OpenAI 커뮤니티: 세 가지 API 변경](https://community.openai.com/t/migrating-to-gpt-6-1-sol-astra-three-api-changes-that-cause-errors-effort-none-sampling-params-tools-in-chat-completions/1412047), [OpenAI 커뮤니티: max가 느린 이유](https://community.openai.com/t/why-is-gpt-6-1-sol-max-dramatically-slower-than-gpt-5-6-sol-max-using-the-same-prompt/1406429) (사용자 글) | [부분] |
| 정확도·속도·보안 통과율 | [Endor Labs](https://www.endorlabs.com/learn/gpt-6-1-sol-on-codex-astra-level-security-a-third-faster-zero-cheating), [DataCamp](https://www.datacamp.com/blog/gpt-6-1-sol), [techaiwire](https://techaiwire.com/articles/openai-gpt-6-1-sol-nearly-matches-astra/) | [부분] |
| 가격·컨텍스트 | [lmspedia](https://lmspedia.org/gpt-6-1-sol/), [nocode.mba](https://www.nocode.mba/articles/gpt-6-1-sol-vs-gpt-6-astra) | [부분] |
- OpenAI 본문 페이지는 이 환경에서 열리지 않아 스니펫만 확인했다. 가격·장문 요금은 공식 페이지로 다시 확인한다.
- Endor Labs 수치는 한 업체의 단일 하네스 결과다. 이 저장소의 과제에서는 다를 수 있다.
