# GPT-6.1 Terra · 범용 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.1-terra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6.1-terra/general.md`](../../../md/gpt/gpt-6.1-terra/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — GPT-6.1 Terra

### 2.1 위치와 사양
- 시각 추론, 컴퓨터 사용, 명료한 글쓰기에 맞춘 중간 티어. OpenAI는 복잡한 코딩에는 Sol이나 Astra를 권한다. 텍스트와 이미지를 입력받는다. 2026-10-26 출시로 보도됐다. [부분]
- 가격은 입력 $1 / 출력 $5(100만 토큰당), 캐시 입력 $0.05로 Sol의 절반이다. 컨텍스트 1.05M(입력 최대 922K, 출력 128K). 큰 티어에는 272K 초과 요청의 장문 요금이 붙는다는 보고가 있어 Terra에 같은 규칙이 적용되는지는 확인하지 못했다. [부분, 집계 사이트]
- 추론 강도는 `none` / `low` / `medium`(기본) / `high` / `xhigh` / `max`. Astra·Sol과 달리 `none`을 지원한다. [부분: 공식 도메인 스니펫]
- 도구 호출은 **Responses API**로 한다. Chat Completions에서 `none`일 때만 함수 호출이 되는지는 Terra에 대해 확인하지 못했다. [미확인]

### 2.2 API를 쓸 때 (OpenAI의 GPT-6 마이그레이션 가이드 기준)
- effort가 `none`이 아니면 `temperature`, `top_p`, `top_logprobs`를 보내지 않는다. `none`이면 보낼 수 있다. [확인: Sol·Luna 기준 문서, Terra 적용은 추정]
- 대화 중 effort 변경은 `configuration_update` 항목을 쓰고 요청 수준 `reasoning.effort`는 고정해 캐시를 보존한다. 모델 문자열만 바꾸지 말고 같은 effort로 기존 설정과 먼저 비교한다. [확인]
- Fast 모드는 EU 데이터 레지던시에서 쓸 수 없고, Ultrafast는 미국·글로벌 처리만 지원한다(Astra·Sol·Luna 기준 문서). Terra는 문서에서 별도로 확인하지 못했다. [미확인]

### 2.3 행동 특성과 이 문서를 쓰는 법
- Sol과 마찬가지로 구체적인 절차·제약·검증 명령을 적어 주는 편이 낫다고 본다. OpenAI가 Sol·Luna에 도움이 되는 지침이 Astra에는 과할 수 있다고 언급한 데서 온 추정이다. [부분/추정]
- 이 문서의 승인 필요 동작은 §1.6 목록뿐이다. 그 밖의 안전한 읽기·편집·테스트는 묻지 않고 진행한다.
- 작성·요약 작업에서는 "원문에 없는 사실을 추가하지 않는다"를 명시한다(아래 2.4의 max 사례).
- 최종 보고는 5항목, 항목당 1~2줄.

### 2.4 비판적 평가 (대부분 2차 출처, 독립 재현 없음)
- **`max`가 `medium`보다 나쁜 사례가 있다.** 한 저장소 테스트에서 Terra는 `medium` 43.7%, `max` 36.0%였고 Sol `max`는 49.1%였다. 뉴스 작성 테스트에서는 `max`가 가장 나빴고, 원문에 없는 외부 정보를 찾아 사실을 덧붙였다. 한 리뷰는 `max`에서 첫 토큰까지 131.81초, 약 1.3억 토큰을 썼다고 한다. [부분]
  → effort를 올리기 전에 같은 과제로 `medium`과 비교해서 실제로 나아지는지 측정한다. 기본은 `medium`이다.
- **코딩은 Sol보다 낮고, 숫자는 설정에 좌우된다.** 한 비교에서 Sol 74%, Terra 69%. Artificial Analysis의 Terminal-Bench 4.0은 Terra `max` 55.6%, Sol `max` 56.1%로 거의 같고, OpenAI 자체 수치(Terra `max` 50.3%)와 다르다. 하네스와 설정이 다르면 숫자가 달라진다. [부분]
- **가격이 싸다고 총비용이 싼 것은 아니다.** 세션당 비용은 Terra $0.24 대 Sol $0.98로 보고됐지만, Sol의 성공률이 높아 재시도가 줄면 Sol이 더 쌀 수 있다는 반론이 있다. [부분]
- **환각률이 개선됐으나 여전히 높다.** 한 독립 테스트에서 GPT-5.6 Terra `max`의 환각률 88%·정확도 47%가 GPT-6.1 Terra에서 환각률 38%·정확도 49%가 됐다. 38%는 낮은 수치가 아니다. [부분]
  → 사실 조회를 모델의 기억에 맡기지 않는다. 사실·수치·출처는 문서와 검색 결과로 확인한다.
- **컴퓨터 사용 수치를 그대로 믿지 않는다.** OpenAI의 OSWorld 2.1(오프라인) 74.2%는 82개 작업의 소규모 하위 집합 기준이고, BenchLM 리더보드의 검증된 최고 점수는 Claude Opus 5.5의 87.2%로 보고된다. 프로토콜(OSWorld-Verified, 2.1 오프라인, Agents' Last Exam)마다 측정하는 행동이 다르다. [부분]
  → GUI 자동화 모델은 자체 과제로 비교해서 고른다.
- 한 블로그는 시험 날짜와 모델 스냅샷이 공개되지 않았다고 지적한다. 모든 수치는 잠정이다.

### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 스크린샷·UI 이해, 컴퓨터 사용 보조, 명료한 설명·문서 작성, 중간 난도의 에이전트 작업, 비용에 민감한 반복 작업.
- 쓰지 않는다: 복잡한 코딩(Sol·Astra), 사실 회상 중심 질의, 오류가 비싼 판단, `max` 기본 사용.
- 막히면 같은 재현 절차를 Sol로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 가격·컨텍스트·위치 | [Lindy](https://www.lindy.ai/blog/gpt-6-1-terra), [eesel.ai](https://www.eesel.ai/blog/gpt-6-1-terra), [DataCamp](https://www.datacamp.com/blog/gpt-6-1-terra) | [부분] |
| 코딩·`max` 역효과·환각률·OSWorld | [BenchLM](https://benchlm.ai/models/gpt-6-1-terra), [MyClaw 리뷰](https://myclaw.ai/blog/gpt-6-1-terra-review), [Puter 리뷰](https://developer.puter.com/blog/gpt-6-1-terra-review/), [Bito 비교](https://bito.ai/blog/gpt-6-1-terra-vs-gpt-6-1-sol-vs-gpt-6-luna/) | [부분] |
| effort 범위, API 규칙 | [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model) 스니펫, [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) | [부분/확인] |
- OpenAI 공식 Terra 모델 페이지는 열지 못했다. 가격, 장문 요금 적용 여부, Fast·Ultrafast 지원은 공식 페이지로 다시 확인한다.
- 위 수치는 대부분 블로그·집계 사이트가 벤더 수치와 Artificial Analysis 수치를 섞어 인용한 것이다. 같은 지표의 값이 출처마다 다르다(예: 지수 48 대 51).
