# GPT-6.1 Terra · 한국어 윤문 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.1-terra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`ko-academic`](../../../md/gpt/gpt-6.1-terra/ko-academic.md) · [`ko-everyday`](../../../md/gpt/gpt-6.1-terra/ko-everyday.md) · [`ko-literary`](../../../md/gpt/gpt-6.1-terra/ko-literary.md)
> 공통 조사(AI 말투 도구, 실측, 한국어 원리): [`docs/_common/korean-writing/`](../../_common/korean-writing/README.md)
> 이 모델의 일반 조사 기록: [`README.md`](README.md)

## 1. 이 모델에서 확인한 것 (글쓰기 제어 관점)
- 입력 $1 / 출력 $5. '시각 추론, 컴퓨터 사용, 명료한 글쓰기에 맞춘 중간 티어'라는 서술이 있다(2026-10-26 출시 보도) [부분].
- 세션당 비용은 Terra $0.24 대 Sol $0.98로 보고됐지만 Sol이 성공률이 높아 재시도가 줄면 더 쌀 수 있다는 반론이 있다 [부분].

## 2. 한국어 문체에 대해 알려진 것과 모르는 것
- '명료한 글쓰기'가 한국어에서도 성립하는지 독립 측정이 없다 [미확인].
- 이 문서가 모델 간 한국어 문체의 우열을 말하지 않는 이유: 사람이 평가한 독립 자료가 없고, 공개된 실측(`empirical-validation.md`)은 다른 모델 버전으로 한 것이다.

## 3. 모델 지침(md)의 근거

`md/gpt/gpt-6.1-terra/ko-*.md`의 '이 모델에서 지킬 점 (한국어 윤문)' 각 줄이 왜 그렇게 쓰였는지다. 순서가 같다.

1. 지침: 결과물은 짧고 명료한 평서문으로 쓴다. 꾸미는 말을 덜어낸다.
   - 근거: 티어 설명을 근거로 한 운용 권고다. 독립 측정이 없다 [추정].
2. 지침: 숫자, 고유명사, 인용, 약어, 날짜는 원문 그대로 둔다.
   - 근거: 윤문의 보존 원칙이다. 사실, 수치, 고유명사를 바꾸는 실패를 막는다. 공개 윤문 도구들도 같은 보존 규칙을 둔다(`ai-tell-projects.md` §3).
3. 지침: 결과물의 말투(존대, 평어)는 원문의 것을 끝까지 유지하고 중간에 바꾸지 않는다.
   - 근거: 경어법 일관성을 AI 문체 특징으로 보는 도구가 있고(humanizer-ko, im-not-ai E-7), 필자의 격식을 바꾸지 않는 것이 윤문의 기본 원칙이다.

## 4. 근거와 한계
- [GPT-5.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide) [부분: 검색 요약]
- [Shaping your agent's personality](https://developers.openai.com/cookbook/examples/gpt-5/prompt_personalities) [부분: 검색 요약]
- [Using the latest model](https://developers.openai.com/api/docs/guides/latest-model) [부분: 같은 폴더 `overview.md`에서 확인한 모델 사양]
- 이 모델 문서의 사양·가격은 같은 폴더의 [`README.md`](README.md)가 안내하는 문서와 [`sources.md`](sources.md)를 따른다.
- 한계: 지침을 적용한 실제 출력을 사람이 읽고 평가한 적이 없다. 위 근거는 대부분 공식 가이드의 영어 기준 서술이거나 검색 요약이다.
