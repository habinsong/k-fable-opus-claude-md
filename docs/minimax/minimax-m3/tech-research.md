# MiniMax-M3 · 기술 연구 — 조사 기록
> 제공자: MiniMax · 모델 ID: API `MiniMax-M3`, 가중치 저장소 `MiniMaxAI/MiniMax-M3`(검색 결과 표기를 따른 추정, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/minimax/minimax-m3/tech-research.md`](../../../md/minimax/minimax-m3/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 428B MoE(활성 약 23B), 공개 가중치(MiniMax Community License, 용도 금지 조항), 입력 $0.30 / 출력 $1.20, 독립 지수 버전 혼재, 후속 `minimax-m3.1-flash` 존재, 제공자(호스트) 주장과 독립 측정의 구분 필요.

**이 모델에게 기술 조사를 시킬 때**
- 분류·정리 단계에만 쓴다. 후보를 정해진 기준(라이선스 유형, 지원 언어, 릴리스 날짜)으로 분류해 표로 만들 때, 값은 사람이 확보한 1차 자료 텍스트에서 추출하게 하고 원문에 없으면 null로 둔다.
- 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2, §3.5). 후보를 지나치게 높게 평가하는 경향(아첨)은 측정된 바 없으므로 사람이나 상위 모델이 근거를 보고 판단한다.

**MiniMax-M3를 도입 후보로 평가할 때**
- **라이선스를 원문으로 확인한다 — 이 모델 도입의 최우선 항목이다.** "MINIMAX COMMUNITY LICENSE"는 Apache 2.0·MIT와 같지 않다는 평가가 있고, 군사 용도, 미성년자 착취, 유해한 허위 정보, 혐오 표현을 금지한다는 요약이 있다. 상업 이용 임계값, 표시 의무, 파생 모델·증류 조건, 금지 용도 조항의 하위 전달 의무는 확인하지 못했다. 출시 전 한 보도가 라이선스 미공표라고 했던 만큼 요약은 시점에 따라 어긋난다. LICENSE 원문(공식 저장소)을 읽고 SPDX 식별자가 없으면 "사용자 정의 라이선스"로 기록한다(§3.2). "가중치 공개"를 "오픈소스"나 "자유로운 상업 이용"으로 읽지 않는다. [부분: 2차 요약/미확인]
- **제공자 홍보와 독립 측정을 분리한다.** "GPT-5.5와 Gemini 3.1 Pro를 일부 벤치마크에서 앞서면서 비용은 5~10%", "공개 모델 중 종합 지능 최고"는 호스팅 제공자(Fireworks)와 언론의 서술이다. 독립 지수는 44, 29, 55로 보이고 지수 버전(v4.1, v4.3.2, v5)이 달라 순위 근거로 쓸 수 없다. SWE-Bench Pro 59.0%는 Opus 4.8의 69.2%에 못 미쳤다. 후보 비교는 같은 과제, 같은 조건의 자체 실측으로 한다. [부분, 충돌]
- **총비용은 과제당 비용이다.** 단가(입력 $0.30 / 출력 $1.20)는 낮지만 호스트마다 가격과 컨텍스트 한도가 다르다(Fireworks는 출시 시점 50만 토큰, 512K 초과 입력은 더 높은 요율). 지수 실행 비용은 약 $203.86이라는 서술이 있다(버전 불명). 우리 과제의 토큰·도구 호출 수로 비교한다. [부분, 충돌]
- **후속 모델과의 관계를 확인한다.** `minimax-m3.1-flash`가 약 4개월 뒤 같은 계열로 나왔고 독립 측정에서 작업당 비용이 M3보다 낮다는 서술이 있다. M3를 선택하는 이유(가중치 공개, 더 큰 모델)가 후속에 없는지 비교한다. [부분]
- **데이터 거버넌스.** 싱가포르 법인 Nanonoble Pte. Ltd.가 정책을 발행하고 데이터가 미국에 저장된다는 독립 안내와, 중국을 가리키는 오래된 정책이 충돌한다. 보관 기간은 고정값이 없고 포괄적 학습 제외 약속이나 ZDR은 공개 문서로 확인되지 않는다. 소비자 제품 정책은 따로다. 약관·개인정보 정책을 원문으로 읽고 법무·보안 검토를 거친다. [부분, 충돌]
- **자체 호스팅.** 총 428B라 다중 GPU 노드가 필요하다. 필요한 하드웨어와 운영비를 계산하고, 직접 호스팅이 호스트 서비스보다 타당한 경우(데이터를 외부로 보낼 수 없는 경우)로 제한한다. 공식 조직 저장소에서만 받고 커밋 해시를 고정하며 제3자 재업로드와 양자화 변환본은 출처를 확인하기 전에는 쓰지 않는다. [추정]
- **제공자 안전장치와 규정.** 공개 가중치에는 제공자 쪽 안전장치가 없다. 입력 필터, 출력 검증, 권한 제한을 직접 구축하고 규제 적합성은 시스템 전체에 대해 판단한다. 라이선스의 용도 금지 조항을 규제 준수의 근거로 쓰지 않는다.

## 4. 근거와 한계
- 출시·사양·가격·라이선스 요약: [Artificial Analysis: MiniMax-M3](https://artificialanalysis.ai/models/releases/minimax-m3), [DataNorth: MiniMax M3 출시](https://datanorth.ai/news/minimax-launches-m3), [HowAIWorks: MiniMax M3](https://howaiworks.ai/models/minimax-m3) (스니펫만) [부분]
- 제공자·언론 서술: [Fireworks: MiniMax M3 출시](https://fireworks.ai/blog/minimax-m3-launch), [VentureBeat: MiniMax M3](https://venturebeat.com/technology/minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost) (스니펫만) [부분: 제공자·언론]
- 독립 지수(버전 혼재): [Artificial Analysis: MiniMax-M3](https://artificialanalysis.ai/models/minimax-m3), [AA 기사: MiniMax-M3](https://artificialanalysis.ai/articles/minimax-m3) (스니펫만) [부분, 충돌]
- 데이터 정책(2차): [Flowith: MiniMax 데이터 안전 FAQ](https://flowith.io/blog/minimax-faq-data-safety), [Opper: MiniMax](https://opper.ai/provider/minimax) (스니펫만) [부분, 충돌]
- 한계: MiniMax 공식 모델 카드·LICENSE·약관 본문을 읽지 못했다. 도입 전에 공식 저장소와 문서에서 확인한다.
