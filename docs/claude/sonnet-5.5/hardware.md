# Claude Sonnet 5.5 · 하드웨어 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/sonnet-5.5/hardware.md`](../../../md/claude/sonnet-5.5/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 지식 평가 54%(Opus 5.5는 66%), 몇 단계 계산이 필요한 JSON 답이 추론 없이 틀리기 쉬움, 기술 도면은 `high` 이상과 도구가 있어야 정확해짐.

- **하드웨어 설계에 대한 Sonnet 5.5 전용 독립 평가는 찾지 못했다.** [미확인] 아래는 공개된 특성에서 끌어온 운용 권고다.
- **부품 사양을 기억에서 가져오지 않는다.** 지식 평가에서 Sonnet 5.5는 54%, Opus 5.5는 66%였고, 시스템 카드는 Sonnet 5보다 오답을 낼 가능성이 약간 높다고 서술했다는 보도가 있다. [부분] 핀 배치, 절대 최대 정격, 타이밍은 데이터시트의 개정판·페이지에서 가져오고, 확인하지 못한 값은 숫자를 쓰지 않는다(§3.1). 학습 지식으로 답하는 경향이 있어 최신 정보는 검색으로 확인하게 한다. [확인]
- **몇 단계 계산이 필요한 JSON 답은 적응형 추론으로.** 합계, 규칙 적용, 순위 같은 계산을 JSON으로 답하게 하면 추론 없이 답해 틀리기 쉽다. 특히 `low`·`medium`에서. BOM 합산이나 전류 예산을 structured outputs로 받을 때 "답하기 전에 문제를 끝까지 생각하라"를 시스템 프롬프트 끝에 넣거나 `xhigh`를 쓴다. `between_tools`에서는 도구가 없는 요청이 추론 없이 답하므로 이 용도로 쓰지 않는다. `stop_reason`이 `max_tokens`인 응답은 JSON이 유효해도 실패로 보고 재시도한다. [확인]
- **도면·차트는 도구를 주고 effort를 올린다.** 밀도 높은 차트와 기술 도면은 자르기·확대·코드 실행 도구를 주면 정확도가 오른다. 기술 도면은 `high` 이상에서만 효과가 있고 `xhigh`·`max`에서 가장 크다. 차트는 도구를 주는 편이 effort를 올리는 것보다 낫다. 읽은 값은 원문 PDF의 같은 페이지와 한 건씩 대조한다. [확인]
- **계산은 도구로 다시 한다.** 전류 예산, 분압, 필터, 열 계산은 스크립트·시뮬레이터 출력으로 확인하고 식과 가정을 남긴다.
- **`max`는 쓰지 않는다.** 한 평가에서 `max`가 `xhigh`보다 낮았고 작업당 비용이 Opus 5.5보다 높았다. [부분]
- **인체·화재 위험 설계(고전압, 대전류, 배터리, 모터)는 "안전하다"고 단정하지 않고 필요한 안전 검토를 적는다. 인증 통과 여부는 시험 결과로만 말한다.**

## 4. 근거와 한계
- JSON 추론 과제·시각 도구·검색 경향: [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) [확인]
- 지식 평가·`max` 비용: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-sonnet-5-5-review), [Claude 5.5 is brilliant, confusing, and very hungry](https://dreasays.substack.com/p/claude-55-is-brilliant-confusing) [부분]
- 한계: 회로·PCB·HDL 능력을 측정한 독립 자료가 없다. 알려진 정답이 있는 레퍼런스 회로로 이 모델의 계산·핀 배치 답을 먼저 점검해 본다.
