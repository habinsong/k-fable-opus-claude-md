# Gemma 4 31B · 웹 (로컬) — 조사 기록
> 제공자: Google · 모델 ID: `google/gemma-4-31B-it` (Hugging Face 토론 URL에서 확인한 표기, 본문은 열지 못함) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemma/gemma-4-31b/web.md`](../../../../md/gemma/gemma-4-31b/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 밀집 약 31B, 4비트 약 17.5~20 GB + KV 캐시, 속도 느림(약 3.4 토큰/초, DGX Spark), 코딩 비교 후기가 갈림, 집계 벤치마크 값은 불일치.

- **웹 UI 코드 생성에 쓸 만하다는 후기가 있으나 표본이 작다.** 한 개발자는 단순 레이아웃, 복잡한 대시보드, 긴 출력에서 31B가 더 작은 Gemma 4 변형보다 구조를 일관되게 유지했다고 했고, 31B로 구조화된 UI를 만들어 렌더링한 사례, 자연어를 HTML/CSS/JS로 바꾸는 템플릿 도구에 쓴 사례가 있다. 모두 제작자 본인의 보고다. [부분: 개인 후기]
- **프런트엔드 품질은 Qwen 계열과 의견이 갈린다.** 한 Reddit 스레드에서 한 사용자는 프런트엔드 생성은 Qwen 3.5가 낫다고 했고 다른 사용자는 31B가 단발 게임과 긴 컨텍스트 코딩에서 매우 강하다고 했다. 시각 품질은 주관적이라는 단서도 붙었다. [부분: 개인 후기] → 기존 UI 체계가 우선이므로(§3.1) 스크린샷과 린터·타입체크로 직접 대조하고, 두 모델을 같은 과제로 비교한 뒤 선택한다.
- **CSS·React 시각 버그 수정에서 자체 10건 중 10건을 해결했다는 보고는 근거로 약하다.** 작고 선별된 자체 테스트 모음이다. [부분: 개인 후기] 시각 회귀는 직접 스크린샷 비교로 확인한다.
- **표준화된 프런트엔드 벤치마크의 독립 결과는 찾지 못했다.** [미확인] LiveCodeBench 약 80 같은 집계 수치는 알고리즘 문제이고 UI 품질을 말해 주지 않는다. SWE-bench 값은 집계 사이트마다 18~68%로 달라 인용하지 않는다(README.md가 안내하는 개요·운용 문서.2).
- **느림을 설계에 반영한다.** 밀집 31B는 같은 계열의 26B A4B보다 훨씬 느리다(약 3.4 대 12.5 토큰/초, 한 기기 측정). 컴포넌트 하나를 고치는 대화형 흐름에서는 지연이 크다. 자동완성·실시간 보조에는 맞지 않고, 어려운 단발 요청에 쓴다. [부분]
- **긴 컨텍스트의 메모리 비용.** 4비트 가중치가 들어가도 전체 컨텍스트의 KV 캐시가 약 20 GiB(bf16 추정)까지 갈 수 있다. 저장소 전체를 넣지 말고 관련 파일만 준다. [부분]
- **보안·접근성 판단을 맡기지 않는다.** 인가, 입력 검증, 비밀 노출, 접근성 "충족" 여부는 도구 출력과 §3.1 기준으로 사람이 점검한다. API·CSS·브라우저 지원은 공식 문서와 린터·컴파일러 출력으로 확인한다.
- **로컬 실행의 이점과 책임.** 미공개 소스를 외부로 보내지 않는다. 대신 제공자 쪽 안전장치가 없으므로 모델이 만든 코드는 격리된 환경에서 실행하고, 의존성 추가는 라이선스·유지 상태를 확인한 뒤에 한다(§1.5).
- **도구 호출 하네스는 사용 중인 런타임 버전에서 작은 시험으로 확인한다.** Gemma 4 계열에서 출시 직후 파서·스트리밍 오류가 보고됐고 31B에서의 현재 상태는 확인하지 못했다. [부분] 샘플링은 권장값(1.0 / 0.95 / 64)에서 시작한다.

## 4. 근거와 한계
- UI 생성 후기: [Gemma 4 on 16GB RAM (DEV)](https://dev.to/shogun444/gemma-4-on-16gb-ram-what-actually-works-for-structured-ai-workflows-3kmb), [Gemma 4 needs more than a chat box (DEV)](https://dev.to/aj0070/gemma-4-needs-more-than-a-chat-box-why-local-ai-needs-generative-ui-4fjk), [Caretaker Sandbox (DEV)](https://dev.to/brixtonmavu/the-caretaker-sandbox-an-offline-first-visual-playground-template-engine-powered-by-gemma-4-2bgl) [부분: 개인 후기]
- Qwen 3.5와의 의견 대립: [Reddit 스냅샷](https://reddit.sentinel-team.org/posts/1sapl6k/snapshots/2026-04-03T21%3A20%3A24.375333Z) [부분: 개인 후기]
- 시각 버그 수정 자체 평가: [Evaluation benchmark results (DEV)](https://dev.to/pinaksh_patel_7c884a18b06/evaluation-benchmark-results-4nc0) [부분: 자체 평가]
- 한계: 독립적인 웹 UI 벤치마크가 없다. 후기는 Qwen 3.5와의 비교이며 Qwen3.6과는 다를 수 있다. 모델 ID 표기는 저장소 URL에서 가져왔다.
