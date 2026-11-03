# Claude Sonnet 5.5 · 한국어 윤문 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`ko-academic`](../../../md/claude/sonnet-5.5/ko-academic.md) · [`ko-everyday`](../../../md/claude/sonnet-5.5/ko-everyday.md) · [`ko-literary`](../../../md/claude/sonnet-5.5/ko-literary.md)
> 공통 조사(AI 말투 도구, 실측, 한국어 원리): [`docs/_common/korean-writing/`](../../_common/korean-writing/README.md)
> 이 모델의 일반 조사 기록: [`general.md`](general.md)

## 1. 이 모델에서 확인한 것 (글쓰기 제어 관점)
- 입력 $2 / 출력 $10, 기본 effort `high`. 가이드에 문체 절은 없고 범위·완료 보고·검증 안내가 중심이다 [확인].
- 지식 평가 54%(Opus 5.5 66%) [부분]. 미적·인문적 글쓰기에서 Opus 5.5와 격차가 크다는 개별 후기가 있다 [부분: 개인 후기].

## 2. 한국어 문체에 대해 알려진 것과 모르는 것
- 한국어 문체의 독립 평가를 찾지 못했다 [미확인].
- 이 문서가 모델 간 한국어 문체의 우열을 말하지 않는 이유: 사람이 평가한 독립 자료가 없고, 공개된 실측(`empirical-validation.md`)은 다른 모델 버전으로 한 것이다.

## 3. 모델 지침(md)의 근거

`md/claude/sonnet-5.5/ko-*.md`의 '이 모델에서 지킬 점 (한국어 윤문)' 각 줄이 왜 그렇게 쓰였는지다. 순서가 같다.

1. 지침: 요청한 범위의 문장만 고친다. 요청하지 않은 문장 추가, 구조 변경, 대안 버전 여러 개를 덧붙이지 않는다. 더 나은 안이 있으면 끝에서 한 줄로 제안만 한다.
   - 근거: Sonnet 5.5 가이드 *Steer initiative and scope*가 요청하지 않은 추가를 하는 경향과 이를 막는 문구를 제공한다 [확인]. 윤문에 맞게 '요청한 범위만'으로 옮겼다 [추정].
2. 지침: 숫자, 고유명사, 인용, 약어, 날짜는 원문 그대로 둔다.
   - 근거: 윤문의 보존 원칙이다. 사실, 수치, 고유명사를 바꾸는 실패를 막는다. 공개 윤문 도구들도 같은 보존 규칙을 둔다(`ai-tell-projects.md` §3).
3. 지침: 결과물의 말투(존대, 평어)는 원문의 것을 끝까지 유지하고 중간에 바꾸지 않는다.
   - 근거: 경어법 일관성을 AI 신호로 보는 도구가 있고(humanizer-ko, im-not-ai E-7), 필자의 격식을 바꾸지 않는 것이 윤문의 기본 원칙이다.

## 4. 근거와 한계
- [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) [확인]
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) [확인]
- 이 모델 문서의 사양·가격은 같은 폴더의 `general.md`와 그 출처를 따른다.
- 한계: 지침을 적용한 실제 출력을 사람이 읽고 평가한 적이 없다. 위 근거는 대부분 공식 가이드의 영어 기준 서술이거나 검색 요약이다.
