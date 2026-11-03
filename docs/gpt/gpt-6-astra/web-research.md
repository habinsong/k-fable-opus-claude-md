# GPT-6 Astra · 웹 리서치 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6-astra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-astra/web-research.md`](../../../md/gpt/gpt-6-astra/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 상세하고 서식 많은 답을 내는 경향, 자기 평가 불신.

- **프롬프트 인젝션은 줄었지만 사라지지 않았다.** Gray Swan의 간접 인젝션 평가에서 공격 성공률이 약 8.5%(시나리오당 15회 시도)로, GPT-5.6 Sol의 27%보다 낮아졌지만 해당 출처는 "개선됐을 뿐 해결되지 않았다"고 평가한다. OpenAI 내부 수치(방어율 99.79%)는 벤더 수치다. [부분] 그래서 웹 페이지 안의 지시문은 계속 데이터로만 다루고, 외부 전송·로그인·결제·계정 변경 같은 행동은 페이지가 시켜도 하지 않는다.
- **인용 환각은 줄었다는 근거가 약하다.** 한 사이트의 측정은 DOI 30개 주장을 3회 반복해 Astra가 지어낸 DOI가 3.0%(이전 모델 8.8%)였다고 하지만, 검색 없이 측정했고 신뢰구간이 1.0~8.4%로 넓으며 독립 재현이 없다. 다른 연구는 웹 검색 도구가 있어도 인용 환각이 지속된다고 보고한다. [부분]
  → 모델이 제시한 모든 URL·DOI를 직접 열어 제목·저자·연도·주장 일치를 확인한다. 열지 못한 출처는 "미열람"으로 분리해 쓴다.
- **보고 형식을 고정한다.** 상세하고 서식이 많은 답을 내는 경향이 있으므로, 조사 결과는 "결론 → 근거(출처, 수준) → 충돌·불확실 → 모르는 것" 네 덩어리로 쓰고 항목당 1~2문장으로 제한한다. 같은 상투구를 반복하지 않는다.
- **긴 페이지를 통째로 읽지 않는다.** 입력이 272K 토큰을 넘으면 요청 전체가 장문 요금으로 계산된다는 집계가 있다. [부분] 필요한 구간을 발췌해서 읽고, 중요한 수치는 원문에서 다시 확인한다.
- **자기 평가를 쓰지 않는다.** "충분히 확인했다", "출처가 일치한다"는 모델의 판단이 아니라 실제로 연 URL 목록과 대조 결과로 보고한다.

## 4. 근거와 한계
- 인젝션·컴퓨터 사용: [GPT-6 Astra: Faster Agents, Critical Cyber Controls](https://developer.tenten.co/gpt-6-astra-computer-use-cyber-deployment), [OpenAI 발표](https://openai.com/index/gpt-6-astra/) 스니펫 [부분]
- 인용 환각: [GPT-6 Astra Hallucination Rate, Measured](https://truestandard.ai/releases/gpt-6-astra), [Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents](https://arxiv.org/pdf/2604.03173) [부분: 단일 비독립 측정 + 일반 연구]
- 한계: Astra 전용 웹 리서치 정확도 평가는 찾지 못했다. 위 수치들은 모두 조건(검색 유무, 하네스)이 달라서 서로 비교하지 않는다.
