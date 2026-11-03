# Claude Opus 5.5 · 한국어 윤문 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-opus-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`ko-academic`](../../../md/claude/opus-5.5/ko-academic.md) · [`ko-everyday`](../../../md/claude/opus-5.5/ko-everyday.md) · [`ko-literary`](../../../md/claude/opus-5.5/ko-literary.md)
> 공통 조사(AI 말투 도구, 실측, 한국어 원리): [`docs/_common/korean-writing/`](../../_common/korean-writing/README.md)
> 이 모델의 일반 조사 기록: [`general.md`](general.md)

## 1. 이 모델에서 확인한 것 (글쓰기 제어 관점)
- 입력 $4 / 출력 $20, 기본 effort `medium`(Opus 5는 `high`) [확인]. 가이드에 문체 절은 없다 [확인].
- 영어 창작 평가에서 LMArena Creative Writing 상단 근처, EQ-Bench Creative Writing 약 8위라는 블로그 서술이 있다. 영어 기준이며 한국어가 아니다 [부분]. 제작사 한국어 소개 페이지는 더 명확하고 자연스러운 문체를 홍보한다 [부분: 제작사 홍보].

## 2. 한국어 문체에 대해 알려진 것과 모르는 것
- Opus 5.5의 한국어 문체를 사람이 평가한 독립 자료를 찾지 못했다 [미확인].
- 이 문서가 모델 간 한국어 문체의 우열을 말하지 않는 이유: 사람이 평가한 독립 자료가 없고, 공개된 실측(`empirical-validation.md`)은 다른 모델 버전으로 한 것이다.

## 3. 모델 지침(md)의 근거

`md/claude/opus-5.5/ko-*.md`의 '이 모델에서 지킬 점 (한국어 윤문)' 각 줄이 왜 그렇게 쓰였는지다. 순서가 같다.

1. 지침: 긴 글에서 이미 합의된 설정(인물, 시제, 용어)은 사용자가 바꾸자고 하기 전에는 다시 뒤집지 않는다. 앞선 부분의 오류를 발견하면 즉시 알린다.
   - 근거: 가이드는 '이미 답한 것은 끝난 것으로 다룬다'는 문구가 생각과 지연을 줄이지만 앞선 답의 오류를 스스로 짚을 가능성도 낮출 수 있다고 경고한다 [확인]. 그래서 오류 발견 시 즉시 알린다는 조건을 붙였다.
2. 지침: 표와 문서를 윤문할 때 숫자와 날짜, 표와 본문이 서로 맞는지 직접 대조한다.
   - 근거: 가이드 *Knowledge work*: 큰 입력에서 요일 불일치나 차트와 수치 불일치를 잡는다는 서술이 있다 [확인: 벤더 주장].
3. 지침: 숫자, 고유명사, 인용, 약어, 날짜는 원문 그대로 둔다.
   - 근거: 윤문의 보존 원칙이다. 사실, 수치, 고유명사를 바꾸는 실패를 막는다. 공개 윤문 도구들도 같은 보존 규칙을 둔다(`ai-tell-projects.md` §3).

## 4. 근거와 한계
- [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) [확인]
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) [확인]
- 이 모델 문서의 사양·가격은 같은 폴더의 `general.md`와 그 출처를 따른다.
- 한계: 지침을 적용한 실제 출력을 사람이 읽고 평가한 적이 없다. 위 근거는 대부분 공식 가이드의 영어 기준 서술이거나 검색 요약이다.
