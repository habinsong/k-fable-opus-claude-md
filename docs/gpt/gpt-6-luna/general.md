# GPT-6 Luna · 범용 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6-luna` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-luna/general.md`](../../../md/gpt/gpt-6-luna/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — GPT-6 Luna

### 2.1 위치와 사양
- GPT-6 계열에서 가장 싸고 빠른 티어. OpenAI는 "집중된 대량 작업"용이라고 안내한다. 텍스트와 이미지를 입력받는다. 2026-09-22 출시, 지식 컷오프는 2026-05-18로 한 리뷰가 적었다. [부분]
- 가격은 입력 $0.10 / 출력 $0.50(100만 토큰당), 캐시 읽기 $0.01. 컨텍스트 1.05M(입력 최대 922K, 출력 128K). 입력이 272K를 넘으면 입력 요금이 2배라는 보고가 있다. [부분, 집계 사이트]
- 추론 강도는 `none` / `low` / `medium`(기본) / `high` / `xhigh` / `max`. [확인: 마이그레이션 가이드]

### 2.2 API를 쓸 때
- 도구 호출은 **Responses API**로 한다. Chat Completions에서는 `reasoning_effort: "none"`일 때만 함수 호출이 된다. 추론과 도구를 함께 쓰려면 Responses를 쓴다. [확인]
- effort가 `none`이 아니면 `temperature`, `top_p`, `top_logprobs`를 보내지 않는다. [확인]
- 대화 중 effort 변경은 `configuration_update` 항목으로 하고 요청 수준 `reasoning.effort`는 고정한다. 모델 문자열만 바꾸지 말고 같은 effort로 이전 모델과 먼저 비교한다. [확인]

### 2.3 행동 특성과 이 문서를 쓰는 법
- OpenAI는 "Sol이나 Luna에 도움이 되는 지침이 Astra에는 과할 수 있다"고 언급했다. Luna에는 구체적인 절차, 출력 형식, 예시, 검증 명령을 모두 적어 주는 편이 맞다. [부분]
- **출력 형식을 스키마로 강제하고 코드로 검증한다.** Structured Outputs 같은 형식 강제와 스키마 검증 코드를 붙이고, 형식을 벗어난 응답은 자동으로 재시도하거나 폐기한다.
- 이 문서의 승인 필요 동작은 §1.6 목록뿐이다. 최종 보고는 5항목, 항목당 1~2줄.

### 2.4 비판적 평가 (Artificial Analysis 등 2차 출처 중심)
- **모르는 것을 모른다고 하지 않는다.** AA-Omniscience에서 Luna(`max`)의 환각률은 93%에서 77%로 줄었지만 정확도는 44%로 거의 그대로(이전 43%)다. 77%는 답하지 말았어야 할 질문의 대부분에 틀린 답을 낸다는 뜻이다. [부분]
  → 사실, 수치, 날짜, API 이름, 출처를 모델의 기억에서 가져오지 않는다. 사실 질의는 검색 결과나 문서를 입력으로 주고 거기서만 답하게 한다.
- **코딩은 이전 세대보다 낮아졌다.** 코딩 지수는 41로 GPT-5.6 Luna(`max`)보다 2점 낮고, SWE-Atlas-QnA 44%(이전 49%), DeepSWE v1.1 64%(이전 66%)다. OpenAI 자체 수치(DeepSWE 66.6%)와 독립 수치가 다르다. [부분]
  → 독립 평가자들은 문법은 맞지만 동작이 불완전한 코드를 냈다고 보고했다. 생성된 코드는 항상 컴파일과 테스트로 확인한다.
- **종합 지수는 GPT-5.6과 비슷하고, 개선과 후퇴가 섞였다.** 비용이 절반으로 줄어든 대신 일부 평가는 나빠졌다. [부분]
- **코딩 기만 비율이 2.8%라는 시스템 카드 수치가 보도됐다.** 2차 출처 인용이라 확정하지 않는다. 테스트 통과를 위해 테스트·기대값을 바꾸지 않았는지 `git diff`로 확인한다. [부분/미확인]
- `none`·`low` effort에서의 정확도, 도구 호출 실패율은 독립 측정을 찾지 못했다. [미확인]
- 대부분의 수치가 `max` effort 기준이다. 비용 때문에 낮은 effort로 쓰면 결과가 더 나쁠 수 있다. 자체 과제로 측정한다.

### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 분류, 라벨링, 필드 추출, 라우팅, 짧은 요약처럼 **정답을 코드로 검증할 수 있는** 대량 작업. 템플릿 채우기, 로그 분류, 형식 변환.
- 쓰지 않는다: 여러 단계의 코딩·에이전트 작업(Sol 이상), 사실 회상, 설계·보안 판단, 오류가 비싼 작업.
- 대량 작업은 일부(예: 5~10%)를 무작위로 뽑아 사람이 정답과 대조하는 표본 점검을 붙인다. 오류율이 기준을 넘으면 Terra나 Sol로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 환각률·코딩 지수·SWE 수치 | [Artificial Analysis: GPT-6 Sol and Luna push the cost efficiency frontier](https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier), [Luna 모델 페이지](https://artificialanalysis.ai/models/releases/gpt-6-luna) | [부분] |
| 가격·컨텍스트·출시일 | [OpenRouter](https://openrouter.ai/openai/gpt-6-luna), [Apidog](https://apidog.com/blog/what-is-gpt-6-luna/), [Hokai 리뷰](https://hokai.io/hub/models/gpt-6-luna) | [부분] |
| 위치·API 규칙 | [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) | [확인] |
- OpenAI 공식 Luna 페이지는 열지 못했다. 컨텍스트와 장문 요금 임계값은 공식 페이지로 다시 확인한다.
- 일부 출처는 위키·개인 블로그라서 코딩 기만 2.8% 같은 수치는 확정하지 않았다.
