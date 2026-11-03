# Claude Haiku 5.5 · 하드웨어 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-haiku-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/haiku-5.5/hardware.md`](../../../md/claude/haiku-5.5/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: AA-Omniscience 정답 비율 36%, 멀티모달 코딩이 약점이라는 후기, 검증 가능한 대량 작업용.

- **설계 판단에 쓰지 않는다.** 핀 배치, 정격, 타이밍, 수식은 틀리면 보드가 망가지거나 위험해진다. 이 모델의 지식 평가 정답 비율은 36%(GPT-6 Luna 44%, Gemini 3.8 Flash 55%)다. [부분] 아는 게 적은 대신 추측도 적다는 해석이 있으나 전용 환각률은 찾지 못했다. [미확인] 설계는 `sonnet-5.5` 이상 문서를 따르고, 그 결과도 데이터시트 원문과 도구 계산으로 확인한다.
- **써도 되는 좁은 일.** BOM 행의 표기 정규화(단위, 제조사명 철자), 부품 번호 목록의 형식 변환, 시험 로그의 분류, 데이터시트 텍스트에서 정해진 필드(패키지, 핀 수) 추출. 추출값은 원본과 한 건씩 대조할 수 있는 일로 한정하고, "원문에 없으면 null"을 명시한다.
- **부품 사양을 모델에게 채우게 하지 않는다.** 데이터시트에 없는 값을 그럴듯하게 채울 수 있다. 값은 PDF의 개정판·페이지에서 가져오고 없으면 비운다(§3.1).
- **계산은 도구로 한다.** 모델이 낸 숫자는 스크립트나 시뮬레이터 출력과 대조한다. 몇 단계 계산이 필요한 JSON 답은 추론 없이 답하면 틀리기 쉬우니 적응형 추론을 쓴다. [확인: Sonnet 5.5 지침 기준, Haiku 5.5도 JSON·도구 조합에서 같은 위험을 문서화]
- **이미지(회로도 스크린샷) 해석을 근거로 쓰지 않는다.** 이미지가 포함된 이슈를 다루는 멀티모달 코딩이 약점이라는 후기가 있다. [부분] 넷리스트·ERC 보고서와 대조한다.
- **인체·화재 위험 설계는 "안전하다"고 단정하지 않는다.**

## 4. 근거와 한계
- 정답 비율·멀티모달 약점: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review), [Beam](https://beam.ai/agentic-insights/claude-haiku-5-5-subagents), [Miraflow](https://miraflow.ai/blog/claude-haiku-5-5-benchmarks-pricing-explained-2026) [부분]
- JSON·도구 조합 지침: [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) [확인]
- 한계: 하드웨어 설계에 대한 Haiku 5.5 평가가 없다. "쓰지 않는다"는 지식 평가 지표에서 도출한 보수적 권고이며 일반 지식 질의가 회로 설계 오류율을 대표한다는 보장은 없다.
