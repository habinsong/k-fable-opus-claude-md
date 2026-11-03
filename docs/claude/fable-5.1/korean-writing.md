# Claude Fable 5.1 · 한국어 윤문 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-fable-5-1` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`ko-academic`](../../../md/claude/fable-5.1/ko-academic.md) · [`ko-everyday`](../../../md/claude/fable-5.1/ko-everyday.md) · [`ko-literary`](../../../md/claude/fable-5.1/ko-literary.md)
> 공통 조사(AI 말투 도구, 실측, 한국어 원리): [`docs/_common/korean-writing/`](../../_common/korean-writing/README.md)
> 이 모델의 일반 조사 기록: [`README.md`](README.md)

## 1. 이 모델에서 확인한 것 (글쓰기 제어 관점)
- 입력 $10 / 출력 $50, 컨텍스트 1M, 가장 느린 티어. 기본 effort `high`. Anthropic은 대부분 Opus 5.5로 시작하라고 안내한다 [확인].
- 공식 가이드가 문체를 직접 다룬다: 문장 밀도, 허세 문체, 서식, 인용 표시 [확인]. 영어 기준이며 한국어 효과는 검증되지 않았다 [미확인].

## 2. 한국어 문체에 대해 알려진 것과 모르는 것
- Fable 5.1의 한국어 문체 독립 평가를 찾지 못했다 [미확인].
- 이 문서가 모델 간 한국어 문체의 우열을 말하지 않는 이유: 사람이 평가한 독립 자료가 없고, 공개된 실측(`empirical-validation.md`)은 다른 모델 버전으로 한 것이다.

## 3. 모델 지침(md)의 근거

`md/claude/fable-5.1/ko-*.md`의 '이 모델에서 지킬 점 (한국어 윤문)' 각 줄이 왜 그렇게 쓰였는지다. 순서가 같다.

1. 지침: 비유와 수사를 늘리지 않는다. 말하려는 바를 직접 쓰고, 문자 그대로의 표현이 있으면 그것을 쓴다.
   - 근거: 가이드 *Writing density*: 비유·수사로 돌려 말하는 문체를 정의해 주면 도움이 된다 [확인]. 한국어에 맞게 다시 썼다 [추정].
2. 지침: 긴 문장을 이어 붙이기만 하고 문단을 나누지 않는 것을 피한다. 한 문단은 한 주제다.
   - 근거: 같은 절: 문장이 길고 문단 나눔이 적을 수 있다 [확인]. 한국어 적용은 [추정].
3. 지침: 출처 글을 요약할 때 원문 구절을 따옴표 없이 옮기지 않는다. 직접 인용은 짧게 표시하고 나머지는 자기 말로 다시 쓴다.
   - 근거: 가이드 *Quoting retrieved sources*: 인용 표시 없이 원문을 옮기는 경향 [확인]. 저작권·출처 규칙(§1.5)과 이어진다.
4. 지침: 목록, 제목, 굵은 글씨는 요청받았을 때만 쓴다. 대화, 개인적인 글, 감정이 담긴 글은 줄글로 쓴다.
   - 근거: 가이드 *Formatting in chat*: 서식을 덜 쓰는 경향이며 대화·감정 교환은 줄글을 권한다 [확인].

## 4. 근거와 한계
- [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) [확인]
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) [확인]
- 이 모델 문서의 사양·가격은 같은 폴더의 [`README.md`](README.md)가 안내하는 문서와 [`sources.md`](sources.md)를 따른다.
- 한계: 지침을 적용한 실제 출력을 사람이 읽고 평가한 적이 없다. 위 근거는 대부분 공식 가이드의 영어 기준 서술이거나 검색 요약이다.
