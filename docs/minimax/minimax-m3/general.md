# MiniMax-M3 · 범용 — 조사 기록
> 제공자: MiniMax · 모델 ID: API `MiniMax-M3`, 가중치 저장소 `MiniMaxAI/MiniMax-M3`(검색 결과 표기를 따른 추정, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/minimax/minimax-m3/general.md`](../../../md/minimax/minimax-m3/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — MiniMax-M3 (공개 가중치 MoE, 제한적 커뮤니티 라이선스)
이 환경에서는 MiniMax 공식 문서와 Hugging Face가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 후속 경량 모델은 `minimax-m3.1-flash` 문서에 둔다.

### 2.1 위치와 사양
- **2026-06-01 출시**(Artificial Analysis 기준). **MoE, 총 428B 파라미터에 활성 약 23B**(NVIDIA 배포 글은 22B라고 적었다는 서술). 컨텍스트 100만 토큰이나 Fireworks는 출시 시점에 50만 토큰까지 지원하고 전체 100만은 며칠 뒤로 약속했다. 호스트마다 지원 컨텍스트가 다를 수 있다. [부분, 충돌]
- **가격**(100만 토큰당, 공식 API): 입력 $0.30 / 출력 $1.20. 제공자마다 다르다(Fireworks는 입력 512K 이하는 표준 요율, 초과는 더 높은 요율). 공식 가격표는 확인하지 못했다. [부분]
- **출력 속도**: 페이지에 따라 초당 약 73~108 토큰. 호스트와 부하에 따라 달라진다. [부분, 충돌]

### 2.2 라이선스 — 가중치는 공개돼 있으나 MIT·Apache가 아니다
- 출시 시점에 **MINIMAX COMMUNITY LICENSE**로 가중치가 공개됐다(출시 전 한 보도는 라이선스가 미공표라고 했으나 오래된 정보다). Apache 2.0이나 MIT와 같지 않다는 평가가 있고, 군사 용도, 미성년자 착취, 유해한 허위 정보, 혐오 표현을 금지하는 용도 제한이 있다고 한다. 상업 이용 조건, 규모 임계값, 표시 의무, 파생·증류 조건은 확인하지 못했다. [부분: 2차 요약, 원문 미확인]
- → 제품·서비스에 쓰기 전에 LICENSE 원문(공식 저장소)으로 상업 이용 조건과 용도 제한을 읽는다. 사용자 콘텐츠가 이 금지 용도에 해당할 수 있는 서비스는 약관 전달(flow-down) 조항을 확인한다(§1.5).

### 2.3 성능 근거를 읽는 법 — 독립 지수가 버전마다 다르다
- **Artificial Analysis 지능 지수**가 페이지에 따라 44, 29, 55로 보인다. 44는 여러 페이지에서 MiniMax 모델 중 최고로, 29는 더 오래된 페이지, 55는 가중치 공개 전 6월 8일 기사에서 나왔다. 지수 버전(v4.1, v4.3.2, 그리고 10월에 v5 발표)이 달라 직접 비교할 수 없다. 다른 모델과 비교하려면 같은 지수 버전의 값을 확인한다. 지수 실행 비용은 약 $203.86이었다. [부분, 충돌]
- **벤더·제공자 주장**: "GPT-5.5와 Gemini 3.1 Pro를 일부 주요 벤치마크에서 앞서면서 비용은 5~10%"(VentureBeat 제목), "공개 모델 중 종합 지능 최고"(Fireworks, AA 인용). 반면 SWE-Bench Pro에서는 59.0%로 Opus 4.8의 69.2%에 못 미쳤다는 보도가 있다. 제공자(Fireworks 등)는 이 모델을 호스팅하는 이해당사자이므로 홍보 성격을 감안한다. [부분: 벤더·제공자 주장]
- **환각 값(AA-Omniscience)은 이 모델에 대해 찾지 못했다.** 후속 M3.1 Flash는 독립 측정에서 환각률 93%라는 보도가 있어 같은 계열의 사실성 위험을 의심할 이유가 있다(`minimax-m3.1-flash` 문서). [미확인/추정]
- **독립 코딩 에이전트 후기는 찾지 못했다.** [미확인]

### 2.4 데이터·정책
- API 개인정보 정책은 싱가포르 주소의 Nanonoble Pte. Ltd.가 발행하고 개인 데이터가 미국 데이터센터에 저장된다는 한 독립 안내가 있다. 더 오래된 MiniMax.io 정책은 중국을 가리켜 서술이 충돌한다. 보관 기간은 고정값이 없고(필요한 기간 또는 법이 허용하는 기간), 모든 API 입력이 학습에서 제외된다는 포괄적 약속이나 ZDR은 공개 문서로 확인되지 않는다는 평가가 있다. 소비자 제품(음성, 에이전트, Talkie)은 정책이 따로다. 모두 2차 출처다. [부분, 충돌]

### 2.5 운용
- **직접 호스팅은 대규모 노드가 필요하다.** 총 428B라 다중 GPU 서버가 필요하다. 공식 저장소에서만 가중치를 받고 해시를 확인하며 제3자 재업로드와 양자화 변환본은 출처를 확인하기 전에는 쓰지 않는다. [추정]
- **호스트(제3자 호스팅)를 쓰면 호스트 약관이 적용된다.** 호스트마다 컨텍스트 한도, 가격, 데이터 조건이 다르다. [부분]
- **지침은 짧게.** 이 문서의 §0과 §1.2·§1.3·§1.6을 시스템 프롬프트에 두고 분야 규칙은 필요한 작업에 붙인다. 한국어 존댓말 준수는 직접 측정한다. [미확인]

### 2.6 비판적 평가
- 강점 후보: 매우 낮은 단가, 공개 가중치, 100만 토큰급 컨텍스트, 활성 약 23B. 약점 후보: 제한적 라이선스(용도 금지 조항), 독립 지수가 버전마다 갈림, 환각 값 부재, SWE-Bench Pro에서 상위 모델에 뒤짐, 호스트마다 컨텍스트 차이.
- 막히면 `claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 출시일·사양·가격·라이선스 요약 | [Artificial Analysis: MiniMax-M3](https://artificialanalysis.ai/models/releases/minimax-m3), [DataNorth: MiniMax M3 출시](https://datanorth.ai/news/minimax-launches-m3), [HowAIWorks: MiniMax M3](https://howaiworks.ai/models/minimax-m3) (스니펫만) | [부분] |
| 호스트 컨텍스트·주장 | [Fireworks: MiniMax M3 출시](https://fireworks.ai/blog/minimax-m3-launch), [VentureBeat: MiniMax M3](https://venturebeat.com/technology/minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost) (스니펫만) | [부분: 제공자·언론] |
| 독립 지수(버전 혼재) | [Artificial Analysis: MiniMax-M3](https://artificialanalysis.ai/models/minimax-m3), [AA 기사: MiniMax-M3](https://artificialanalysis.ai/articles/minimax-m3), [Beam: MiniMax 모델 목록](https://beam.ai/llm/minimax/) (스니펫만) | [부분, 충돌] |
| 데이터 정책(2차) | [Flowith: MiniMax 데이터 안전 FAQ](https://flowith.io/blog/minimax-faq-data-safety), [Opper: MiniMax](https://opper.ai/provider/minimax), [MiniMax 개인정보 정책(비공식 미러)](https://minimax-ai.chat/privacy-security/minimax-privacy-policy/) (스니펫만) | [부분, 충돌] |
- MiniMax 공식 모델 카드·LICENSE·약관 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
