# GPT-6.1 Sol · 한국어 윤문 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.1-sol` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`ko-academic`](../../../md/gpt/gpt-6.1-sol/ko-academic.md) · [`ko-everyday`](../../../md/gpt/gpt-6.1-sol/ko-everyday.md) · [`ko-literary`](../../../md/gpt/gpt-6.1-sol/ko-literary.md)
> 공통 조사(AI 말투 도구, 실측, 한국어 원리): [`docs/_common/korean-writing/`](../../_common/korean-writing/README.md)
> 이 모델의 일반 조사 기록: [`general.md`](general.md)

## 1. 이 모델에서 확인한 것 (글쓰기 제어 관점)
- 입력 $2 / 출력 $10, 컨텍스트 1.05M. 추론 강도 `low`~`max`, 기본 `medium` [확인/부분].
- OpenAI는 사실 오류율이 11.4%에서 7.7%로 줄었다고 주장한다. 개선돼도 약 13건 중 1건은 틀릴 수 있다는 뜻이다 [부분: 벤더 주장].

## 2. 한국어 문체에 대해 알려진 것과 모르는 것
- GPT-6.1 계열의 한국어 문체 독립 평가를 찾지 못했다 [미확인].
- 이 문서가 모델 간 한국어 문체의 우열을 말하지 않는 이유: 사람이 평가한 독립 자료가 없고, 공개된 실측(`empirical-validation.md`)은 다른 모델 버전으로 한 것이다.

## 3. 모델 지침(md)의 근거

`md/gpt/gpt-6.1-sol/ko-*.md`의 '이 모델에서 지킬 점 (한국어 윤문)' 각 줄이 왜 그렇게 쓰였는지다. 순서가 같다.

1. 지침: 윤문 전후로 수치와 고유명사를 원문과 대조한다. 자기 설명만 믿지 않는다.
   - 근거: 벤더 오류율 주장이 완전하지 않으므로 윤문 후 수치와 고유명사를 원문과 대조한다 [부분].
2. 지침: 숫자, 고유명사, 인용, 약어, 날짜는 원문 그대로 둔다.
   - 근거: 윤문의 보존 원칙이다. 사실, 수치, 고유명사를 바꾸는 실패를 막는다. 공개 윤문 도구들도 같은 보존 규칙을 둔다(`ai-tell-projects.md` §3).
3. 지침: 결과물의 말투(존대, 평어)는 원문의 것을 끝까지 유지하고 중간에 바꾸지 않는다.
   - 근거: 경어법 일관성을 AI 신호로 보는 도구가 있고(humanizer-ko, im-not-ai E-7), 필자의 격식을 바꾸지 않는 것이 윤문의 기본 원칙이다.

## 4. 근거와 한계
- [GPT-5.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide) [부분: 검색 요약]
- [Shaping your agent's personality](https://developers.openai.com/cookbook/examples/gpt-5/prompt_personalities) [부분: 검색 요약]
- [Using the latest model](https://developers.openai.com/api/docs/guides/latest-model) [부분: 기존 `general.md`에서 확인한 모델 사양]
- 이 모델 문서의 사양·가격은 같은 폴더의 `general.md`와 그 출처를 따른다.
- 한계: 지침을 적용한 실제 출력을 사람이 읽고 평가한 적이 없다. 위 근거는 대부분 공식 가이드의 영어 기준 서술이거나 검색 요약이다.
