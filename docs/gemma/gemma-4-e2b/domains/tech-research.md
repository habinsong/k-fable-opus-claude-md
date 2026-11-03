# Gemma 4 E2B · 기술 연구 (로컬·온디바이스) — 조사 기록
> 제공자: Google · 모델 ID: `google/gemma-4-E2B` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemma/gemma-4-e2b/tech-research.md`](../../../../md/gemma/gemma-4-e2b/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Apache 2.0 가중치, 4비트 약 2.9 GB, 온디바이스 후보, 독립 평가 없음, 런타임 버그 이력.

**이 모델에게 기술 조사를 시킬 때**
- 분류·정리 단계에만 쓴다. 후보를 정해진 기준(라이선스 유형, 지원 언어, 릴리스 날짜)으로 분류해 표로 만들 때, 값은 사람이 확보한 1차 자료 텍스트에서 추출하게 하고 원문에 없으면 null로 둔다. 모델의 기억으로 채우지 않는다.
- 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2). 사람이나 상위 모델이 근거를 보고 판단한다.

**Gemma 4 E2B를 도입 후보로 평가할 때**
- **용도 적합성.** 온디바이스·오프라인·데이터 외부 반출 금지 요건이 있을 때의 후보다. 메모리 4비트 약 2.9 GB, BF16 약 11.4 GB, 컨텍스트 128K, 오디오 입력 지원이다. [부분] 정확도 요건이 높은 업무에는 맞지 않는다.
- **라이선스.** Google 모델 카드는 Apache 2.0이라고 적었다. 호스팅 플랫폼을 거치면 그쪽 약관(예: NVIDIA Open Model License)이 붙는다는 지적이 있다. 가중치를 받는 경로와 재배포 계획에 따라 LICENSE와 약관을 직접 확인한다. 상표(Gemma 명칭 사용), 사용 정책, 파생 모델 조건은 원문으로 확인한다. [부분]
- **총소유비용.** API 비용이 없는 대신 기기·전력·유지보수와 평가 비용이 든다. 대상 기기에서 메모리·속도·발열을 실측한다. 같은 용도의 다른 소형 모델(Qwen3.6 계열, Gemma 4 E4B)과 같은 과제로 비교한다.
- **독립 평가가 없다.** 벤더 서술 외에 E2B의 독립 평가는 찾지 못했다. [미확인] 자체 과제와 라벨로 정확도를 측정한다.
- **런타임 성숙도.** 출시 직후 Ollama·llama.cpp에서 도구 호출·토크나이저·스트리밍 버그가 보고됐고 현재 수정 여부를 확인하지 못했다. 사용할 런타임 버전에서 시험한다. [부분]
- **제공자 안전장치 부재.** 입력 필터, 출력 검증, 권한 제한을 직접 구축한다. 규제 인증(데이터 보호, AI 규정) 적합성은 이 모델이 아니라 시스템 전체에 대해 판단한다.
- **12B가 후속 추가 모델이다.** 공식 문서에 5개 크기(E2B, E4B, 12B, 26B A4B, 31B)가 있고 출시 블로그는 4개만 적었다는 불일치가 있어, 크기 선택 시 현재 모델 카드를 확인한다. [부분]

## 4. 근거와 한계
- 크기·메모리·라이선스: [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4), [Gemma 4: Byte for byte, the most capable open models](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) (스니펫만) [부분]
- 호스팅 약관 지적·런타임 버그: [gemma-4-31b-it (NVIDIA)](https://build.nvidia.com/google/gemma-4-31b-it/modelcard), [Run Gemma 4 Locally](https://www.danilchenko.dev/posts/2026-04-07-run-gemma-4-locally-ollama-llama-cpp-vllm/) [부분]
- 한계: 공식 LICENSE 본문과 사용 정책을 직접 읽지 못했다. 도입 전에 모델 저장소에서 확인한다.
