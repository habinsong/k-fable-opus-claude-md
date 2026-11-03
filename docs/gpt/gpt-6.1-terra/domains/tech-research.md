# GPT-6.1 Terra · 기술 연구 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.1-terra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6.1-terra/tech-research.md`](../../../../md/gpt/gpt-6.1-terra/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Sol의 절반 가격, 환각률 38%, 벤치마크 수치가 출처마다 어긋남.

**이 모델에게 기술 조사를 시킬 때**
- 사실 정확도가 낮을 수 있다(환각률 38%). [부분] 비교표 작성은 맡기더라도 각 칸의 출처를 직접 열어 확인하고, 열지 못한 칸은 비워 둔다. 라이선스·특허 판단은 단정하지 않는다(§3.2).
- 설계 판단과 트레이드오프 평가는 `gpt-6.1-sol`이나 `gpt-6-astra` 문서를 따른다.

**Terra를 도입 후보로 평가할 때**
- **비용.** 입력 $1 / 출력 $5(100만 토큰당), 캐시 입력 $0.05로 Sol의 절반이다. 세션당 비용은 Terra $0.24 대 Sol $0.98로 보고됐다. 그러나 성공률이 낮아 재시도가 늘면 Sol이 더 쌀 수 있다는 반론이 있다. [부분] 비용은 "성공한 작업당"으로, 같은 과제·같은 effort에서 실제 토큰으로 비교한다.
- **수치를 걸러서 읽는다.** 같은 지표의 값이 출처마다 다르다. Terra의 지능 지수는 48과 51로 갈리고, Sol의 작업당 비용도 $0.72와 $1.27로 갈린다. Terminal-Bench 4.0의 OpenAI 자체 수치(`max` 50.3%)와 Artificial Analysis 수치(55.6%)도 설정이 달라 다르다. [부분] 원본 데이터를 확인하기 전에는 순위를 확정하지 않는다.
- **`max`는 비용만 늘 수 있다.** 한 저장소 테스트에서 `max`가 `medium`보다 낮았다. [부분] 도입 평가는 `medium` 기준으로 하고, 올릴 때는 개선을 측정한다.
- **컴퓨터 사용 주장.** OpenAI의 74.2%(OSWorld 2.1 오프라인, 82개 작업)는 소규모 세트다. 검증된 최고 점수는 Claude Opus 5.5의 87.2%로 보고된다. [부분] 자체 과제로 비교한다.
- **데이터 요건.** Fast·Ultrafast 지원과 EU 데이터 레지던시 제약은 Terra에 대해 확인하지 못했다. 규제 인증도 확인하지 못했다. [미확인]
- **출시 직후 정보.** 2026-10-26 출시로 보도됐고 평가 대부분이 첫 주 블로그다. 몇 주 후 업데이트를 확인한다.

## 4. 근거와 한계
- 가격·비교: [Lindy](https://www.lindy.ai/blog/gpt-6-1-terra), [eesel.ai](https://www.eesel.ai/blog/gpt-6-1-terra), [TrueFoundry](https://www.truefoundry.com/blog/gpt-6-1-sol-terra-luna) [부분]
- 벤치마크 불일치: [BenchLM](https://benchlm.ai/models/gpt-6-1-terra), [Bito 비교](https://bito.ai/blog/gpt-6-1-terra-vs-gpt-6-1-sol-vs-gpt-6-luna/) [부분]
- 한계: 공식 가격·모델 페이지를 직접 열지 못했다. 도입 결정 전에 공식 페이지로 다시 확인한다.
