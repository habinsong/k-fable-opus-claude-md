# GPT-6 Astra · 기술 연구 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6-astra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-astra/tech-research.md`](../../../../md/gpt/gpt-6-astra/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델 자체를 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 비용이 높고, 벤더 수치는 독립 검증이 아니며, 지침 충돌에 민감하다.

**이 모델에게 기술 조사를 시킬 때**
- 비교표의 모든 칸에 출처와 확인 수준을 붙이게 하고, 출처를 열어 보지 않은 칸은 비워 두게 한다. 이 모델은 자기 평가가 틀릴 수 있으므로 "충분히 조사했다"는 말을 근거로 삼지 않는다.
- 라이선스·특허 판단은 모델이 단정하지 않는다. SPDX 식별자와 원문 링크, 공개 DB 검색 조건과 날짜만 받아 사람이 판단한다(§3.2).

**Astra를 도입 후보로 평가할 때**
- **비용.** 입력 $10 / 출력 $50(100만 토큰당)으로 보도됐고 GPT-5.6 Sol의 약 2.5배, Fable 5.1과 같은 수준이다. 272K 초과 입력은 장문 요금이 적용된다는 집계가 있다. Fast 모드 배수와 Ultrafast 요금은 확인하지 못했다. [부분] 비용은 같은 과제·같은 effort에서 실제 토큰 사용량으로 비교한다. OpenAI도 Astra와 6.1 Sol을 자기 과제로 비교하라고 권한다. [확인: 마이그레이션 가이드]
- **벤더 수치를 걸러서 읽는다.** 종합 지수(Artificial Analysis 약 61)에서는 GPT-5.6 Sol과 거의 같고 Fable 5.1·Muse Spark 1.3에 뒤진다는 보도가 있고, ARC Prize는 컴퓨터 사용·추론 수치가 하네스에 크게 좌우된다고 지적했다. [부분]
- **규제·데이터 요건.** HIPAA·SOC 2 같은 특정 규정 준수 인증은 확인되지 않았다는 보도가 있다. Fast 모드는 EU 데이터 레지던시에서 쓸 수 없고 Ultrafast는 미국·글로벌 처리만 지원한다. [부분/확인] 규제 데이터를 다루려면 계약·인증 문서를 직접 확인한다.
- **미출시·예정 정보는 쓰지 않는다.** 이 폴더는 2026-11-03 기준 출시된 모델만 다룬다.

## 4. 근거와 한계
- 비용·종합 지수: [eesel.ai 리뷰](https://www.eesel.ai/blog/gpt-6-astra-review), [CloudZero](https://www.cloudzero.com/blog/gpt-6-pricing/), [GPT-6 Astra Benchmarks: Is It Really Better Than Fable 5.1?](https://www.mindstudio.ai/blog/gpt-6-astra-benchmarks-analysis) [부분]
- 데이터 레지던시·마이그레이션 원칙: [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) [확인]
- 한계: OpenAI 공식 가격·모델 페이지를 직접 열지 못해 가격과 컨텍스트는 집계 사이트 기준이다. 도입 결정 전에 공식 페이지로 다시 확인한다.
