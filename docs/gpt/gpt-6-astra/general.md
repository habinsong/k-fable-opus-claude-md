# GPT-6 Astra · 범용 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6-astra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-astra/general.md`](../../../md/gpt/gpt-6-astra/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — GPT-6 Astra

### 2.1 위치와 사양
- GPT-6 계열 최상위. OpenAI 문서는 "가장 어려운 추론·코딩·전문 업무"용이며 추론 워크로드의 기본 시작점이라고 안내한다. [부분]
- 가격은 입력 $10 / 출력 $50 (100만 토큰당), 캐시 입력 $1로 보도됐다. 입력이 272K를 넘으면 요청 전체가 장문 요금($20/$75)으로 넘어간다는 집계도 있다. 컨텍스트는 약 1.05M, 최대 출력 128K로 적힌 곳이 있으나, Codex 기본값은 약 26만 토큰이고 1M 설정은 권장되지 않는다는 글도 있어 서로 맞지 않는다. 컨텍스트·요금은 모델 페이지를 확인하기 전에 단정하지 않는다. [부분, 집계 사이트]
- 추론 강도(effort)는 `low` / `medium` / `high` / `xhigh` / `max`. `none`과 `minimal`은 지원하지 않고 보내면 HTTP 400이다. 기본값은 확인하지 못했으므로 항상 명시한다. [확인: 일부]

### 2.2 API를 쓸 때 (OpenAI의 Codex 저장소 마이그레이션 가이드 기준)
- 도구 호출은 **Responses API**로 한다. Astra는 Chat Completions에서 함수 호출을 지원하지 않는다. [확인]
- effort가 `none`이 아니면 `temperature`, `top_p`, `top_logprobs`를 보내지 않는다. [확인]
- 대화 도중 effort를 바꿀 때는 `configuration_update` 입력 항목을 쓰고, 요청 수준 `reasoning.effort`는 고정해서 프롬프트 캐시를 지킨다. GPT-5.5 이하에서 옮길 때는 `prompt_cache_retention` 대신 `prompt_cache_options.ttl: "30m"`을 쓴다. [확인]
- Fast 모드는 지연 SLA가 없고 EU 데이터 레지던시에서 쓸 수 없다. Ultrafast 모드는 미국·글로벌 처리에서만 된다. 배수와 요금은 확인하지 못했다. [확인: 제약만]
- 모델 문자열만 바꾸지 않는다. 기존 설정과 같은 effort로 먼저 비교하고, 그다음 최소한의 프롬프트·API 수정만 한다. 측정되지 않는 기능(Pro mode, persisted reasoning, 비동기 도구, 멀티 에이전트)은 켜지 않는다. [확인]

### 2.3 행동 특성과 이 문서를 쓰는 법 (OpenAI 지침, 스니펫 기준)
- **긴 지시는 잘 따르지만 충돌하는 컨텍스트에 민감하다.** `AGENTS.md`나 스킬의 지시가 서로 어긋나면 멈추거나 방향을 바꾼다. 컨텍스트에 들어가는 지침 파일(이 문서 포함)을 점검하고, "사용자의 명시 지시가 문서·스킬 지시보다 우선한다"를 한 번만 적는다. 멈췄다면 어떤 파일의 어느 문장 때문에 멈췄는지 인용하게 해서 원인을 찾는다. [부분]
- **같은 규칙을 반복하면 불필요한 승인 요청이 늘어난다.** 이 문서에서 승인이 필요한 동작은 §1.6에 나열된 파괴적·외부 영향 동작뿐이다. 그 밖의 안전한 읽기·편집·테스트 실행은 묻지 않고 진행한다. 질문은 답에 따라 결과가 달라질 때만 한다.
- **완료 기준을 처음에 정한다.** 중간 검토 정지를 요구하면 일찍 멈추는 쪽으로 기운다. 완료 상태(통과해야 할 검증)를 시작할 때 적고, 정지점은 §1.6의 승인 필요 동작 앞에만 둔다.
- **서브에이전트를 덜 쓰는 경향이 있다.** 병렬화가 필요하면 언제, 얼마나 위임할지 지정한다.
- **상세하고 서식이 많은 답을 내는 경향이 있다.** 최종 보고(§0)는 5항목, 항목당 1~2줄로 쓰고, 목록은 내용이 병렬이거나 순차일 때만 쓴다. 같은 상투구를 반복하지 않는다.
- **"편집 전에 항상 파일을 읽어라" 같은 일괄 규칙은 컨텍스트를 낭비한다.** 변경 대상과 직접 이어진 파일만 읽는다. 테스트는 새 실패나 풀리지 않은 문제가 있을 때만 다시 돌린다.
- 작업 중 방향을 바꾸고 싶으면 mid-turn steering으로 끼어들 수 있다.

### 2.4 비판적 평가 (독립 평가·시스템 카드 보도, 대부분 2차 출처)
- **과잉 설계 경향이 반복 보고된다.** 단순한 수정이 여러 스크립트로 번진 사례가 있다. → 변경 후 `git diff --stat`으로 요청 범위를 벗어난 파일이 없는지 확인한다. 범위를 벗어난 것은 되돌린다. [부분]
- **비용과 속도.** 가격이 GPT-5.6 Sol의 약 2.5배로 보도됐고, 일부 리뷰는 느리고 토큰 소모가 크며 긴 자율 작업에서 세부에 매몰된다고 평가한다. → 경계가 분명한 작업은 GPT-6.1 Sol·Terra로 먼저 시도하고, 막힌 지점에만 Astra를 쓴다. OpenAI도 Astra와 6.1 Sol을 자기 과제로 비교하라고 권한다. [부분]
- **자기 평가를 믿지 않는다.** 한 리뷰에서 독립 심판 셋이 패배로 판정한 결과를 Astra는 패배로 인식하지 못했다. → "통과했다", "문제없다"는 자기 판단을 증거로 쓰지 않고, 실행한 명령의 출력으로 확인한다. [부분]
- **추론 과정의 모니터링 가능성이 줄었다.** 시스템 카드가 이전 모델 대비 큰 감소를 인정한다고 보도됐다. → 모델이 쓴 설명을 근거로 삼지 않고, 재실행 가능한 명령·테스트·출처에 근거를 둔다. [부분]
- **벤더 수치는 독립 검증이 아니다.** ARC-AGI-3 99.9% 같은 수치는 OpenAI의 주장이고, 일부 종합 지수에서는 Fable 5.1·Muse Spark 1.3에 뒤진다는 보도가 있다. [부분]
- **규제 인증.** HIPAA·SOC 2 같은 특정 규정 준수 인증은 확인되지 않았다는 보도가 있다. 규제 데이터를 다루면 계약과 인증을 직접 확인한다. [부분]
- 균형: CodeRabbit은 Sol 대비 버그 탐지 약 4%, 파일 간 리뷰에서 약 20% 더 많이 찾았다고 보고했다. 벤더 인접 출처라 확정하지 않고, 지적마다 재현해서 확인한다. [부분]

### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 6.1 Sol로 막힌 어려운 디버깅, 파일 간 추론이 필요한 설계·리뷰, 한 번의 실수가 비싼 전문 업무.
- 쓰지 않는다: 대량·반복·지연에 민감한 작업(Luna·Terra), 비용에 민감한 작업, 요구사항이 모호한 탐색.
- 시작 설정은 `high`에서 하고, 막히면 `xhigh`로 올린다. `max`는 비용 대비 효과를 측정한 뒤에 쓴다. [권고: 이 저장소 작성자의 사용 경험과 같은 방향이며 공식 권장 아님]

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| API 규칙, effort, 마이그레이션 원칙 | [openai/codex `upgrading-to-gpt-6-astra.md`](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) (OpenAI 운영 저장소, 직접 읽음) | [확인] |
| 지침 충돌·반복 규칙·완료 기준·문체 | [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model), [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) (검색 스니펫만) | [부분] |
| 가격·컨텍스트 | [OpenRouter 목록](https://openrouter.ai/openai/gpt-6-astra), [CloudZero](https://www.cloudzero.com/blog/gpt-6-pricing/), [eesel.ai](https://www.eesel.ai/blog/gpt-6-astra-pricing) | [부분] |
| 비판적 평가 | [eesel.ai 리뷰](https://www.eesel.ai/blog/gpt-6-astra-review), [Layer3 Labs](https://www.layer3labs.io/guides/gpt-6-astra-review), [Transformer](https://www.transformernews.ai/p/openai-gpt-6-astra-might-be-too-powerful-to-understand-or-control), [NeoTeo](https://www.neoteo.com/en/gpt-6-astra-improves-coding-and-computer-use-but-still-needs-supervision) | [부분] |
- 이 환경에서는 `openai.com`·`developers.openai.com` 본문을 열 수 없어 스니펫만 확인했다. 컨텍스트 크기, 기본 effort, Fast·Ultrafast 요금은 **[미확인]**이다.
- 리뷰 다수는 출시 직후 블로그와 제휴 성격 사이트다. 한 곳의 수치(속도 4배 차이 등)는 다른 곳에서 재확인되지 않았다.
