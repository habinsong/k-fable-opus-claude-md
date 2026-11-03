# Gemini 3.8 Flash · 한국어 윤문 — 조사 기록
> 제공자: Google · 모델 ID: `gemini-3.8-flash` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`ko-academic`](../../../md/gemini/gemini-3.8-flash/ko-academic.md) · [`ko-everyday`](../../../md/gemini/gemini-3.8-flash/ko-everyday.md) · [`ko-literary`](../../../md/gemini/gemini-3.8-flash/ko-literary.md)
> 공통 조사(AI 말투 도구, 실측, 한국어 원리): [`docs/_common/korean-writing/`](../../_common/korean-writing/README.md)
> 이 모델의 일반 조사 기록: [`README.md`](README.md)

## 1. 이 모델에서 확인한 것 (글쓰기 제어 관점)
- 2026-09-02 GA. 입력 $0.75 / 출력 $3.75(2026-12-31까지), 이후 $1.50 / $7.50이라는 2차 정리가 있다 [부분]. 추론을 끌 수 없고 생각 토큰이 출력 요금으로 청구된다.
- Artificial Analysis에서 3.7 Flash 대비 같은 평가에 출력 토큰을 약 1.77배 냈다 [부분].

## 2. 한국어 문체에 대해 알려진 것과 모르는 것
- Gemini 3.8 Flash의 한국어 문체 독립 평가를 찾지 못했다 [미확인].
- 이 문서가 모델 간 한국어 문체의 우열을 말하지 않는 이유: 사람이 평가한 독립 자료가 없고, 공개된 실측(`empirical-validation.md`)은 다른 모델 버전으로 한 것이다.

## 3. 모델 지침(md)의 근거

`md/gemini/gemini-3.8-flash/ko-*.md`의 '이 모델에서 지킬 점 (한국어 윤문)' 각 줄이 왜 그렇게 쓰였는지다. 순서가 같다.

1. 지침: 페르소나나 역할이 주어져도 결과물의 문체 규칙(이 문서의 분야 규칙)이 우선이다. 감탄, 칭찬, 이모지를 기본값으로 쓰지 않고 사용자가 보인 말투만 따른다.
   - 근거: Gemini 3 가이드는 persona를 진지하게 따라 때로는 지시를 무시하고, 기본 응답은 덜 장황하다고 한다 [부분: 검색 요약]. Gemini 4·3.8 Flash에 그대로 적용되는지는 확인하지 못했다 [추정].
2. 지침: 답은 직접적이고 간결하게 쓴다.
   - 근거: Gemini 3 가이드의 기본 응답 특성 [부분]. 3.8 Flash는 3세대라 가이드가 더 직접 적용될 가능성이 있다 [추정].
3. 지침: 숫자, 고유명사, 인용, 약어, 날짜는 원문 그대로 둔다.
   - 근거: 윤문의 보존 원칙이다. 사실, 수치, 고유명사를 바꾸는 실패를 막는다. 공개 윤문 도구들도 같은 보존 규칙을 둔다(`ai-tell-projects.md` §3).
4. 지침: 긴 문학 원고 전체의 일관성 점검처럼 이 모델에 버거운 작업이면 더 큰 모델이 필요하다고 보고한다.
   - 근거: 티어 위치(가격·용도 설명)에서 끌어낸 운용 권고다. 한국어 윤문 품질의 독립 측정은 없다 [추정].

## 4. 근거와 한계
- [Gemini 3 프롬프트 가이드](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide) [부분: 검색 요약, 호스트 미열람]
- [Gemini 3.8 Flash 모델 페이지](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash) [부분: 호스트 미열람, 같은 폴더 `overview.md`에서 확인]
- 이 모델 문서의 사양·가격은 같은 폴더의 [`README.md`](README.md)가 안내하는 문서와 [`sources.md`](sources.md)를 따른다.
- 한계: 지침을 적용한 실제 출력을 사람이 읽고 평가한 적이 없다. 위 근거는 대부분 공식 가이드의 영어 기준 서술이거나 검색 요약이다.
