# GPT-6.1 Sol · 기술 연구 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.1-sol` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6.1-sol/tech-research.md`](../../../../md/gpt/gpt-6.1-sol/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Astra의 5분의 1 가격, 보안 통과율이 낮게 측정됨, 벤더 주장과 독립 측정이 어긋남.

**이 모델에게 기술 조사를 시킬 때**
- 비교표의 모든 칸에 출처와 확인 수준을 붙이게 하고, 열어 보지 않은 출처의 칸은 비워 두게 한다.
- 라이선스·특허 판단은 단정하지 않는다. SPDX 식별자, 원문 링크, 공개 DB 검색 조건과 날짜만 받아 사람이 판단한다(§3.2).
- 어려운 비교·설계 판단은 Astra와 결과를 맞춰 본다. Sol은 가장 어려운 평가에서 Astra에 못 미친다는 정리가 있다. [부분]

**Sol을 도입 후보로 평가할 때**
- **비용.** 입력 $2 / 출력 $10(100만 토큰당)으로 대부분의 집계가 같다. 입력 272K 초과 요청은 요청 전체에 장문 요금(입력·캐시 2배, 출력 1.5배)이 붙는다는 보고가 있다. 공식 가격 페이지는 열지 못했다. [부분] 총비용은 같은 과제·같은 effort에서 실제 토큰으로 비교한다. OpenAI도 Astra와 Sol을 자기 과제로 비교하라고 권한다. [확인: 마이그레이션 가이드]
- **벤더 주장과 독립 측정을 분리한다.** "Astra에 거의 근접, 5분의 1 가격"은 OpenAI의 주장이다. 독립 측정(Endor Labs, Codex 하네스)은 기능 통과율이 Astra보다 몇 점 낮고, 보안 통과율은 34.1%였다. 아레나 순위는 보드마다 달라 종합은 Sol, 코딩은 Astra가 앞선다. [부분]
- **코딩 기만 평가가 엇갈린다.** DataCamp는 Astra보다 나쁘다고, Endor Labs는 0건이라고 했다. 도입 전 자체 과제에서 테스트 조작 여부를 확인한다. [부분, 충돌]
- **데이터 요건.** Fast 모드는 EU 데이터 레지던시에서 쓸 수 없고 Ultrafast는 미국·글로벌 처리만 지원한다. [확인] 규제 인증(HIPAA, SOC 2 등)은 이 모델에 대해 확인하지 못했다. [미확인]
- **모델 라인업 혼선.** "GPT-6 Sol"과 "GPT-6.1 Sol"이 공존하고 6.1 Astra 보류설이 있다. 문서와 계정에서 실제로 선택 가능한 ID를 먼저 확인한다. [부분/미확인]

## 4. 근거와 한계
- 가격·비교: [lmspedia](https://lmspedia.org/gpt-6-1-sol/), [nocode.mba](https://www.nocode.mba/articles/gpt-6-1-sol-vs-gpt-6-astra), [Hugging Face 블로그 비교](https://huggingface.co/blog/karmen-beatapi/gpt-6-1-sol-vs-sol-vs-astra-coding-agent-cost) [부분: 집계·후기]
- 독립 측정: [Endor Labs](https://www.endorlabs.com/learn/gpt-6-1-sol-on-codex-astra-level-security-a-third-faster-zero-cheating), [DataCamp](https://www.datacamp.com/blog/gpt-6-1-sol) [부분]
- 한계: 공식 가격·모델 페이지를 직접 열지 못했다. 도입 결정 전에 공식 페이지로 다시 확인한다.
