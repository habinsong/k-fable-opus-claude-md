# Qwen3.6-35B-A3B · 범용 (로컬) — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.6-35B-A3B`(검색 결과의 Hugging Face 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.6-35b-a3b/general.md`](../../../md/qwen/qwen3.6-35b-a3b/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Qwen3.6-35B-A3B (MoE, 총 35B·활성 약 3B, 공개 가중치)
이 환경에서는 Hugging Face와 Alibaba 공식 문서가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 같은 세대의 밀집 모델은 `qwen3.6-27b` 문서에 둔다.

### 2.1 위치와 사양
- 2026-04 중순에 나온 **희소 MoE 모델**로 총 약 35B 파라미터에 활성 약 3B다. 네이티브 컨텍스트 262K 토큰, 비전 언어 입력을 네이티브로 지원하고 라이선스는 여러 목록에서 Apache 2.0이다. 같은 세대에서 밀집 `qwen3.6-27b`(4월 22일)가 뒤따랐다. [부분]
- **MoE의 메모리 함정.** 활성 파라미터가 적어 빠르지만 35B 전체를 메모리에 올려야 한다. 4비트 GGUF가 Unsloth Studio에서 돈다는 서술은 있으나 이 조사에서 확인한 VRAM 수치는 없다. 대상 기기에서 양자화·컨텍스트별로 실측한다. [미확인]

### 2.2 성능 근거를 읽는 법
- **벤더 수치**: SWE-bench Verified 73.4(밀집 27B는 최대 77.2)라는 안내 글의 인용이 있다. 하네스 조건을 확인하지 못했고 독립 재현이 없다. [부분: 벤더 주장]
- **속도**: 한 보고에서 9070 XT 기준 초당 약 35 토큰(27B는 13~15), 다른 보고는 RTX 3090에서 약 101 토큰이었다. 기기·양자화·런타임에 따라 크게 달라진다. [부분: 개인 후기]
- **품질 후기가 갈린다.** 한 후기는 "3배 빠르지만 27B를 선호한다"고 했고, 다른 후기는 A3B의 Q4 양자화가 같은 자리를 돌며(루프) Q6 27B가 끝낸 작업보다 오래 걸렸다고 했다. Q4 대 Q6 비교라 모델 차이와 양자화 차이가 섞인다. 다른 보고에서는 도구 호출 문제가 Gemma 4 26B A4B에서 주로 나왔다는 서술도 있다. [부분: 개인 후기]
- **독립 지수·환각 값은 찾지 못했다.** [미확인]

### 2.3 로컬로 돌릴 때
- 서빙에는 vLLM, llama.cpp(`--jinja`), Ollama, LM Studio, Unsloth GGUF 등을 쓴다. 서빙 예시는 `qwen3` 추론 파서와 `qwen3_coder` 도구 호출 파서를 쓴다. 열린 도구 호출 버그의 현재 상태는 확인하지 못했으므로 런타임·템플릿 버전에서 작은 시험으로 확인한다. [부분]
- 로컬 모델에는 제공자 쪽 안전장치와 사용량 제한이 없다. 입력 필터, 출력 검증, 권한 제한을 직접 설계한다.

### 2.4 이 문서를 쓰는 법
- **지침은 짧게.** 활성 약 3B 모델은 긴 지침이 컨텍스트를 압박할 수 있다. §0과 §1.2·§1.3·§1.6의 핵심을 발췌해 쓰고 분야 규칙은 필요한 작업에 붙인다. 준수율을 측정한다. [추정]
- **출력은 스키마로 강제하고 코드로 검증한다.** 한국어 존댓말 준수를 직접 측정한다. [미확인]
- **같은 실패가 3번 반복되면 멈추게 한다.** 루프 후기가 있으므로 하네스에 반복 한도를 둔다(§1.2). [부분: 개인 후기]

### 2.5 비판적 평가
- 강점 후보: 속도(초당 35~101 토큰 보고), Apache 2.0, 비전 입력, 단발·소규모 작업. 약점 후보: Q4에서 루프를 돈다는 후기, 독립 평가 부재, 메모리는 35B 전체, 후속 세대(`qwen3.8-27b`)가 나옴.
- 막히면 `qwen3.6-27b`로 올리거나 상위 모델 문서(`claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon`)의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 사양·라이선스·파서 | [SiliconFlow: Qwen3.6-35B-A3B](https://www.siliconflow.com/models/qwen3-6-35b-a3b), [Roboflow: 27B 대 35B-A3B](https://playground.roboflow.com/models/compare/qwen3-6-27b-vs-qwen3-6-35b-a3b), [Unsloth: Qwen3.6-27B GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF) (스니펫만) | [부분] |
| 벤더 수치·속도·출시 순서 | [InsiderLLM: Qwen 3.6 완전 가이드](https://insiderllm.com/guides/qwen-3-6-local-ai-guide/), [Towards AI: Qwen 3.6 리뷰](https://pub.towardsai.net/qwen-3-6-reviewed-the-open-weight-coder-that-just-crashed-the-frontier-party-3b2e3e37ba34) (스니펫만) | [부분: 벤더 주장·개인 후기] |
| 로컬 후기(루프·속도) | [Brian Lovin HN](https://brianlovin.com/hn/47960507), [ToolHalla: Qwen3.6-27B 로컬 코딩 리뷰](https://toolhalla.ai/blog/qwen3-6-27b-local-coding-review-bottleneck) (스니펫만) | [부분: 개인 후기] |
- 공식 모델 카드·LICENSE 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
