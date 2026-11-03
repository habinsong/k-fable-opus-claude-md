# Claude Sonnet 5.5 · 연구 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/sonnet-5.5/research.md`](../../../md/claude/sonnet-5.5/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 지식 평가 54%, 오답 가능성이 Sonnet 5보다 약간 높다는 보도, 글쓰기는 수정자에 가깝다는 개별 후기, 추론을 응답에 쓰게 하면 거부될 수 있음.

- **연구의 사실 회상과 인용을 이 모델에 맡기지 않는다.** 지식 평가에서 Sonnet 5.5는 54%, Opus 5.5는 66%였다. [부분] 26개 LLM을 비교한 2026년 연구에서 검증 가능한 참고문헌 중 모든 필드가 맞은 비율은 48.3%였고 저자 목록이 가장 약했다(51.7%). Sonnet 5.5에 대한 별도 측정은 찾지 못했다. [부분/미확인] 모든 인용은 Crossref·DataCite·원문에서 제목·저자·연도·권호와 주장의 실제 존재를 확인한다. 확인하지 못한 항목은 목록에서 분리한다.
- **가설 도출과 열린 추론은 상위 모델로.** Anthropic은 가장 어려운 장시간 작업에 Opus를 권한다. [확인] 새 가설, 증명, 실험 설계 검토는 Sonnet 5.5 단독으로 끝내지 않고 Opus 5.5나 사람 전문가의 결과와 비교한다.
- **글쓰기에 쓸 때.** 한 후기는 이 모델을 창작자보다 수정자에 가깝다고 평가했고, Opus 5.5와의 격차가 미적·인문적 글쓰기에서 크고 명료성에서는 비슷하다고 했다. 개별 후기다. [부분] 초안 생성보다 이미 쓴 글의 명료화·구조 점검에 쓰고, 논지와 인용은 사람이 책임진다.
- **몇 단계 계산이 필요한 JSON 답은 적응형 추론으로.** 통계 요약이나 표 집계를 JSON으로 받을 때 추론 없이 답하면 틀리기 쉽다(`low`·`medium`에서 특히). "답하기 전에 문제를 끝까지 생각하라"를 넣거나 `xhigh`를 쓴다. `max_tokens`로 끊긴 응답은 실패로 본다. [확인]
- **추론 과정을 응답 본문에 쓰게 하지 않는다.** 내부 추론을 응답 텍스트로 재현하게 하는 요청은 `reasoning_extraction` 범주로 거부될 수 있고, 이 거부는 서버 쪽 대체로 재시도되지 않는다. `display: "summarized"`로 요약된 추론 블록을 읽거나 답의 짧은 설명을 요청한다. [확인]
- **분석은 코드를 다시 실행해서 확인한다.** 통계 설명이나 결론은 근거가 아니다. 시드, 데이터 버전, 라이브러리 버전을 기록하고, 이상치 제거·필터·검정 기준이 결과에 맞춰 바뀌지 않았는지 `git diff`로 확인한다. `low`에서는 변경을 검사 없이 완료로 보고할 수 있어 재실행을 요구한다. [확인]
- **생물학 연구.** `bio` 분류기가 정당한 생명과학 연구를 막으면 Life Sciences Verification Program을 확인한다. `bio` 거부는 서버 쪽 대체로 재시도되지 않는다. 의료·법률·안전 결론에는 "전문가 검토 필요"를 붙인다. [확인]
- **`max`는 쓰지 않는다.** 한 평가에서 `max`가 `xhigh`보다 낮았다. [부분]

## 4. 근거와 한계
- 거부 범주·JSON 추론·검증 강제: [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5), [What's new in Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5) [확인]
- 지식 평가·글쓰기: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-sonnet-5-5-review), [I Tested Claude Sonnet 5.5's Writing](https://vocal.media/01/i-tested-claude-sonnet-55s-writing-its-a-reviser-not-a-creator) [부분: 개별 후기]
- 참고문헌 정확도(타 모델 포함): [Biomedical Reference Generation Remains Unreliable across 26 LLMs](https://arxiv.org/pdf/2609.14988) [부분]
- 한계: Sonnet 5.5의 연구 보조 정확도를 통제된 조건에서 측정한 독립 자료는 찾지 못했다.
