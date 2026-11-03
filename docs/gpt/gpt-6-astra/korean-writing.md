# GPT-6 Astra · 한국어 윤문 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6-astra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`ko-academic`](../../../md/gpt/gpt-6-astra/ko-academic.md) · [`ko-everyday`](../../../md/gpt/gpt-6-astra/ko-everyday.md) · [`ko-literary`](../../../md/gpt/gpt-6-astra/ko-literary.md)
> 공통 조사(AI 말투 도구, 실측, 한국어 원리): [`docs/_common/korean-writing/`](../../_common/korean-writing/README.md)
> 이 모델의 일반 조사 기록: [`general.md`](general.md)

## 1. 이 모델에서 확인한 것 (글쓰기 제어 관점)
- OpenAI 플래그십 티어. 입력 $10 / 출력 $50(100만 토큰당)으로 보도됐고 6.1 Sol의 5배다 [부분: 집계 사이트].
- 추론 강도 `low`~`max`, `none`·`minimal`은 400. 기본값은 확인하지 못했다. effort가 `none`이 아니면 `temperature`·`top_p`를 보낼 수 없으므로 샘플링으로 문체를 조절하지 못하고 프롬프트와 점검 순환으로만 조절한다 [확인: 일부].
- 작업당 중앙값이 6.1 Sol보다 느리다(약 11.5분 대 8분) [부분]. 충돌하는 지침 파일에 민감하다는 보고가 있다 [부분].

## 2. 한국어 문체에 대해 알려진 것과 모르는 것
- GPT-6 한국어 문체를 사람이 평가한 독립 자료를 찾지 못했다 [미확인].
- 한국어 모어 화자 글 20편과 GPT-5 글 20편을 비교한 연구에서 복잡성·정확성·유창성에 유의한 차이가 없었고 GPT-5의 어휘 다양성이 더 높았다는 검색 요약이 있다. GPT-6이 아니다 [부분].
- 이 문서가 모델 간 한국어 문체의 우열을 말하지 않는 이유: 사람이 평가한 독립 자료가 없고, 공개된 실측(`empirical-validation.md`)은 다른 모델 버전으로 한 것이다.

## 3. 모델 지침(md)의 근거

`md/gpt/gpt-6-astra/ko-*.md`의 '이 모델에서 지킬 점 (한국어 윤문)' 각 줄이 왜 그렇게 쓰였는지다. 순서가 같다.

1. 지침: 장문 원고는 마지막에 용어, 시제, 인물 이름, 수치가 처음부터 끝까지 일치하는지 한 번 대조한다.
   - 근거: 티어 위치(가격·용도 설명)에서 끌어낸 운용 권고다. 한국어 윤문 품질의 독립 측정은 없다 [추정]. 장문 원고의 일관성 점검은 긴 컨텍스트 티어의 용도다.
2. 지침: 지침이 서로 충돌하면 임의로 고르지 않는다. 충돌을 한 줄로 알리고 사용자 요청과 장르를 따른다.
   - 근거: 기존 `general.md`: 충돌하는 지침이 있으면 멈추거나 방향을 바꾼다는 보고 [부분].
3. 지침: 숫자, 고유명사, 인용, 약어, 날짜는 원문 그대로 둔다.
   - 근거: 윤문의 보존 원칙이다. 사실, 수치, 고유명사를 바꾸는 실패를 막는다. 공개 윤문 도구들도 같은 보존 규칙을 둔다(`ai-tell-projects.md` §3).

## 4. 근거와 한계
- [GPT-5.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide) [부분: 검색 요약]
- [Shaping your agent's personality](https://developers.openai.com/cookbook/examples/gpt-5/prompt_personalities) [부분: 검색 요약]
- [Using the latest model](https://developers.openai.com/api/docs/guides/latest-model) [부분: 기존 `general.md`에서 확인한 모델 사양]
- 이 모델 문서의 사양·가격은 같은 폴더의 `general.md`와 그 출처를 따른다.
- 한계: 지침을 적용한 실제 출력을 사람이 읽고 평가한 적이 없다. 위 근거는 대부분 공식 가이드의 영어 기준 서술이거나 검색 요약이다.
