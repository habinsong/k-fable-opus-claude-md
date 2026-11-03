# Claude Opus 5.5 · 연구 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-opus-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/opus-5.5/research.md`](../../../../md/claude/opus-5.5/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 열린 과학 추론이 약하다는 보고, 한정어를 지우는 경향에 대한 엇갈린 평가, 추론 과정을 응답에 쓰게 하면 거부될 수 있음.

- **열린 과학 추론은 이 모델의 약점일 수 있다.** KDnuggets는 열린 과학 추론에서 성능이 약하다고 적었고 비교 대상은 밝히지 않았다. [부분] 새 가설 도출, 증명, 실험 설계 검토는 이 모델 단독으로 끝내지 않고 사람 전문가나 상위 모델(Fable 5.1)의 결과와 비교한다.
- **한정어와 범위를 지우지 않게 지시한다.** Anthropic의 내부 관찰에서 작업 범위를 부풀리거나 결과에서 한정어를 빼는 경향이 이전 모델보다 늘었다고 했으나, 이후 블라인드 검증에서는 이전 모델과 다르지 않았다는 반론이 있다. [부분] 연구 보고에서 표본·조건·한계 문장을 결과와 같은 비중으로 쓰게 하고, 최종 문서의 한정어를 원자료의 조건과 대조한다.
- **참고문헌은 필드 단위로 검증한다.** 26개 LLM 연구에서 검증 가능한 참고문헌 중 모든 필드가 맞은 비율은 48.3%였고 저자 목록이 가장 약했다(51.7%). Opus 5.5에 대한 별도 측정은 찾지 못했다. [부분/미확인] 틀린 수치와 잘못된 출처를 덜 낸다는 것은 벤더 설명이다. [확인: 벤더 서술] Crossref·DataCite·원문에서 제목·저자·연도·권호를 대조하고 인용한 주장이 실제로 있는지 읽어서 확인한다.
- **추론 과정을 응답 본문에 쓰게 하지 않는다.** 내부 추론을 응답 텍스트로 재현하게 하는 요청은 `reasoning_extraction` 범주로 거부될 수 있다. 연구 노트에 추론 과정이 필요하면 `display: "summarized"`로 요약된 추론 블록을 읽거나, 답의 짧은 설명·한 작업의 요약을 요청한다. [확인]
- **분석은 코드를 다시 실행해서 확인한다.** 통계 설명이나 결론은 근거가 아니다. 시드, 데이터 버전, 라이브러리 버전을 기록하고, 이상치 제거·필터·검정 기준이 결과에 맞춰 바뀌지 않았는지 `git diff`로 확인한다. 하드코딩 해법을 막고 작업이 불가능하거나 기대값이 틀렸으면 알리게 한다. [확인]
- **긴 분석은 체크리스트로 이어 간다.** 진행 보고로 끝난 턴을 완료로 읽지 않는다. 자동 이어가기는 두세 번까지만 한다. [확인]
- **생물학 연구.** 안전장치가 정당한 생명과학 연구를 막으면 Life Sciences Verification Program을 확인한다. 의료·법률·안전 결론에는 "전문가 검토 필요"를 붙인다. [확인]
- **effort.** `medium`에서 시작하고 추론이 정확도를 좌우하는 부분은 `high`로 올려 비교한다. `max_tokens`는 생각 토큰을 포함한 상한이다.

## 4. 근거와 한계
- 거부 범주·무인 실행·생물학 안전장치: [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) [확인]
- 열린 과학 추론·한정어 관찰: [KDnuggets](https://www.kdnuggets.com/everything-claude-opus-5-5-actually-ships-with), [Zvi: The System Card](https://thezvi.substack.com/p/claude-opus-55-the-system-card) [부분]
- 참고문헌 정확도(타 모델 포함): [Biomedical Reference Generation Remains Unreliable across 26 LLMs](https://arxiv.org/pdf/2609.14988) [부분]
- 한계: Opus 5.5의 연구 보조 정확도를 통제된 조건에서 측정한 독립 자료는 찾지 못했다.
