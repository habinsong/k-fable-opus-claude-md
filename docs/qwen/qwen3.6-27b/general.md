# Qwen3.6-27B · 범용 (로컬) — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.6-27B`(검색 결과의 Hugging Face 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.6-27b/general.md`](../../../md/qwen/qwen3.6-27b/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Qwen3.6-27B (밀집 27B, 공개 가중치)
이 환경에서는 Hugging Face와 Alibaba 공식 문서가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 후속은 `qwen3.8-27b`, 같은 세대의 MoE는 `qwen3.6-35b-a3b` 문서에 둔다.

### 2.1 위치와 사양
- 2026-04-22에 나온 **밀집 27B 모델**로 같은 세대의 `qwen3.6-35b-a3b`(4월 중순), 클로즈드 미리보기 `Max-Preview`(4월 20일)와 함께 나왔다. 네이티브 컨텍스트 262,144 토큰(확장 시 약 101만 토큰), 비전 언어 입력을 네이티브로 지원하고 추론/비추론 모드가 한 체크포인트에 있다고 서술된다. 라이선스는 여러 목록에서 Apache 2.0이다(Unsloth GGUF 저장소 태그 포함). [부분]
- **서빙 안내**: 공식 카드의 서빙 예시는 `qwen3` 추론 파서와 `qwen3_coder` 도구 호출 파서(자동 도구 선택)를 쓴다. 기본 모드가 추론인지는 확인하지 못했다. [부분/미확인]
- **메모리**: 이번 조사에서 확인한 VRAM 수치는 없다. 같은 급인 후속 `qwen3.8-27b`는 BF16 가중치 약 55.6 GB, 4비트로 24 GB GPU라는 서술이 있으나 이 모델에 그대로 적용하지 않는다. 대상 기기에서 양자화·컨텍스트별로 실측한다. [미확인]

### 2.2 성능 근거를 읽는 법
- **벤더 보고**: SWE-bench Verified가 35B-A3B 73.4, 27B 밀집 최대 77.2라는 한 안내 글의 서술이 있다. 벤더 수치를 옮긴 것으로 보이며 하네스 조건은 확인하지 못했다. [부분: 벤더 주장]
- **독립 후기가 비교적 풍부하다(개인 후기).** 한 후기는 벤치마크와 일반 여론 모두 27B 쪽이 크게 앞선다고 했다. 어떤 후기는 소규모 ggml-org 유지보수 작업에 쓸 만하되 PR 검토가 병목이라고 했다. 에이전트·도구 호출 작업에서는 이 계열을 쓴다는 후기가 많았고, Gemma 4 26B A4B의 도구 호출 문제와 대비됐다. 반면 한 사용자는 박사 논문용 코드 시험에서 Gemma 4 31B가 Qwen 3.6(27B와 35B A3B)을 크게 앞섰다고 했다. 서로 엎치락뒤치락이라는 후기도 있다. [부분: 개인 후기]
- **속도 보고**: 9070 XT에서 27B가 초당 약 13~15 토큰, 35B-A3B가 약 35 토큰. 다른 보고는 RTX 3090에서 35B-A3B가 초당 약 101 토큰이었다. 기기·양자화에 따라 크게 달라진다. [부분: 개인 후기]
- **독립 평가 수치(AA 지수 등)와 환각 값은 이 모델에 대해 찾지 못했다.** [미확인]

### 2.3 로컬로 돌릴 때
- 서빙에는 vLLM, llama.cpp(`llama-server --jinja`로 네이티브 도구 호출), Ollama, LM Studio, Unsloth GGUF 등을 쓴다. Unsloth 페이지는 중첩 객체 파싱을 개선한 도구 호출 수정을 언급한다. 열린 도구 호출 버그의 현재 상태는 확인하지 못했다. 사용하는 런타임·템플릿 버전에서 작은 시험으로 확인한다. [부분]
- 로컬 모델에는 제공자 쪽 안전장치와 사용량 제한이 없다. 입력 필터, 출력 검증, 권한 제한을 직접 설계한다.

### 2.4 이 문서를 쓰는 법
- **지침은 짧게.** 이 문서는 한국어로 수천 토큰이다. §0과 §1.2·§1.3·§1.6의 핵심을 발췌해 쓰고 분야 규칙은 필요한 작업에 붙인다. 준수율을 측정한다.
- **출력은 스키마로 강제하고 코드로 검증한다.** 한국어 존댓말 준수를 직접 측정한다. [미확인]

### 2.5 비판적 평가
- 강점 후보: 로컬 코딩·에이전트 기준선으로 거론됨, 도구 호출 후기가 비교적 좋음, Apache 2.0, 비전 입력. 약점 후보: 독립 지수·환각 값 부재, 후기가 개인 경험이고 Gemma 4 31B와 결과가 갈림, 벤더 수치의 조건 불명, 후속(`qwen3.8-27b`)이 이미 나옴.
- 막히면 `qwen3.8-27b`와 비교하거나 상위 모델 문서(`claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon`)의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 사양·라이선스·파서·서빙 | [SiliconFlow: Qwen3.6-27B](https://siliconflow.com/models/qwen3-6-27b), [Unsloth: Qwen3.6-27B GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF), [Roboflow: 27B 대 35B-A3B](https://playground.roboflow.com/models/compare/qwen3-6-27b-vs-qwen3-6-35b-a3b) (스니펫만) | [부분] |
| 출시 순서·벤더 수치 | [InsiderLLM: Qwen 3.6 완전 가이드](https://insiderllm.com/guides/qwen-3-6-local-ai-guide/), [Towards AI: Qwen 3.6 리뷰](https://pub.towardsai.net/qwen-3-6-reviewed-the-open-weight-coder-that-just-crashed-the-frontier-party-3b2e3e37ba34) (스니펫만) | [부분: 벤더 주장 포함] |
| 로컬 후기·속도 | [Quesma: Qwen 3.6 is awesome](https://quesma.com/blog/qwen-36-is-awesome/), [Brian Lovin HN](https://brianlovin.com/hn/47960507), [ToolHalla: Qwen3.6-27B 로컬 코딩 리뷰](https://toolhalla.ai/blog/qwen3-6-27b-local-coding-review-bottleneck) (스니펫만, quesma.com은 이 환경에서 열리지 않음) | [부분: 개인 후기] |
- 공식 모델 카드·LICENSE 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
