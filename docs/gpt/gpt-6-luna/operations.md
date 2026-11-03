# GPT-6 Luna — 운용
> 제공자: OpenAI · 모델 ID: `gpt-6-luna` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-luna/general.md`](../../../md/gpt/gpt-6-luna/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API를 쓸 때
- 도구 호출은 **Responses API**로 한다. Chat Completions에서는 `reasoning_effort: "none"`일 때만 함수 호출이 된다. 추론과 도구를 함께 쓰려면 Responses를 쓴다. [확인]
- effort가 `none`이 아니면 `temperature`, `top_p`, `top_logprobs`를 보내지 않는다. [확인]
- 대화 중 effort 변경은 `configuration_update` 항목으로 하고 요청 수준 `reasoning.effort`는 고정한다. 모델 문자열만 바꾸지 말고 같은 effort로 이전 모델과 먼저 비교한다. [확인]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- OpenAI는 "Sol이나 Luna에 도움이 되는 지침이 Astra에는 과할 수 있다"고 언급했다. Luna에는 구체적인 절차, 출력 형식, 예시, 검증 명령을 모두 적어 주는 편이 맞다. [부분]
- **출력 형식을 스키마로 강제하고 코드로 검증한다.** Structured Outputs 같은 형식 강제와 스키마 검증 코드를 붙이고, 형식을 벗어난 응답은 자동으로 재시도하거나 폐기한다.
- 지침 문서의 승인 필요 동작은 §1.6 목록뿐이다. 최종 보고는 5항목, 항목당 1~2줄.
