# Qwen3.8-27B · 범용 (로컬) — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-27B`(검색 결과의 Hugging Face 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.8-27b/general.md`](../../../md/qwen/qwen3.8-27b/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Qwen3.8-27B (밀집 비전 언어 모델, 공개 가중치)
이 환경에서는 Hugging Face와 Alibaba 공식 문서가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. API 전용 `qwen3.8-max`, 텍스트 전용 대형 `qwen3.8-2.4t-a95b`와 별개 모델이다.

### 2.1 위치와 사양
- 2026-08-14 Qwen 조직이 Hugging Face에 공개한 **밀집 27B 비전 언어 모델**이다. 네이티브 컨텍스트 262,144 토큰(YaRN으로 약 100만까지 확장), 스택의 4분의 3에 선형 어텐션을 써서 긴 컨텍스트 비용을 줄였다는 서술이 있다. 입력은 이미지를 포함한다. [부분]
- **라이선스는 Apache 2.0이라는 서술이 두 곳(저장소가 표준 Apache License 2.0을 싣는다는 서술 포함)에 있다.** 반면 출시 전후의 다른 글은 Apache 2.0이 확실하지 않고 과거 일부 Qwen 릴리스가 월간 활성 사용자 1억 명 임계값이 있는 "Tongyi Qianwen" 라이선스를 썼다고 지적했다. 같은 세대의 2.4T 체크포인트는 자체 라이선스다. 근거가 소수 출처라 저장소의 LICENSE 원문으로 확인하기 전에는 단정하지 않는다(§1.5). [부분, 충돌]
- **추론이 기본으로 켜져 있어 샘플링을 다시 조정해야 한다**는 서빙 안내가 있다(`vllm serve Qwen/Qwen3.8-27B --max-model-len 262144` 예시). 추론/비추론 전환 방법과 기본 샘플링 값은 모델 카드로 확인한다. [부분/미확인]
- **메모리**: BF16 가중치가 약 55.6 GB(가중치만, 긴 컨텍스트의 KV 캐시는 별도), 4비트 양자화하면 24 GB GPU(RTX 3090·4090)에 들어간다는 서술이 있다. 모든 정밀도에서 Blackwell 한 장에 들어간다는 서술도 있어 일치하지 않는다. 대상 기기에서 컨텍스트 길이별로 실측한다. [부분, 충돌]

### 2.2 성능 근거를 읽는 법
- **독립 지수(Artificial Analysis)**: 노력 단계별로 `xhigh` 52, `medium` 44, `low` 43, 비추론 35. `xhigh` 페이지는 출력 속도가 초당 53 토큰으로 비교군 중앙값(106)의 절반이고 `low`의 지수 평가 비용이 $214.79라고 적었다(호스팅 환경 기준). 지수 버전(v4.1.1, v4.3)이 섞여 있어 다른 모델과 비교할 때 같은 버전인지 확인한다. [부분, 충돌]
- **벤더 보고**: SWE-bench Pro 61.7, Terminal-Bench 2.1 73.0은 Qwen이 자체 실행했고 SWE-bench Pro와 QwenSWEBench는 Claude Code 하네스에서 돌렸다는 모델 카드 각주가 있다. 독립 재현이 없고 다른 하네스에서 같은 점수를 기대하기 어렵다. [부분: 벤더 주장]
- **독립 후기는 아직 얕다.** 검색에서 Qwen3.8-27B를 직접 돌린 독립 후기는 찾지 못했다. 직전 세대 `qwen3.6-27b`가 지역 코딩 모델의 기준선으로 거론된다. 아래의 로컬 후기는 3.6·Gemma 4 세대의 것이다. [미확인]
- **환각 값(AA-Omniscience)은 찾지 못했다.** [미확인]

### 2.3 로컬로 돌릴 때
- 서빙에는 vLLM, llama.cpp 등을 쓴다. 이전 세대 후기에서 도구 호출은 Gemma 4보다 Qwen 3.6 계열이 낫다는 보고가 많았다(개인 후기, 26B/35B 변형 위주). llama.cpp에서는 `llama-server --jinja`로 네이티브 도구 호출을 쓰는 안내가 있다. 3.8-27B의 파서·템플릿 지원 상태는 사용하는 런타임의 최신 버전에서 작은 시험으로 확인한다. [부분: 개인 후기, 이전 세대]
- 로컬 모델에는 제공자 쪽 안전장치와 사용량 제한이 없다. 입력 필터, 출력 검증, 권한 제한을 직접 설계한다.

### 2.4 이 문서를 쓰는 법
- **지침은 짧게.** 이 문서는 한국어로 수천 토큰이다. §0과 §1.2·§1.3·§1.6의 핵심을 발췌해 쓰고 분야 규칙은 필요한 작업에 붙인다. 준수율을 측정한다.
- **출력은 스키마로 강제하고 코드로 검증한다.** 형식 오류는 자동 재시도하거나 폐기한다. 한국어 존댓말 준수를 직접 측정한다. [미확인]
- 추론 토큰이 기본으로 많이 나오므로 `max_tokens`와 컨텍스트 예산을 추론 길이까지 고려해 정한다. [추정]

### 2.5 비판적 평가
- 강점 후보: 24 GB급 GPU에서 4비트로 도는 비전 언어 모델, 긴 컨텍스트, Apache 2.0이라는 서술(미확인), 독립 지수 `xhigh` 52. 약점 후보: 독립 후기 부재, 라이선스 근거가 소수 출처, 벤더 수치가 특정 하네스 의존, 출력 속도가 느림(`xhigh`), 지수 버전 혼재.
- 막히면 `qwen3.6-27b`와 비교하거나 상위 모델 문서(`claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon`)의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 사양·라이선스·벤더 수치·메모리 | [Morph: Qwen 3.8 27B 벤치마크·VRAM·라이선스](https://www.morphllm.com/qwen-3-8), [Qubrid: Qwen3.8-27B 개발자 가이드](https://www.qubrid.com/blog/qwen38-27b-api-benchmarks-pricing-and-the-complete-developer-guide), [OrcaRouter: Qwen 3.8 27B 벤치마크](https://www.orcarouter.ai/pl/blog/qwen-3-8-27b-benchmarks) (스니펫만) | [부분, 충돌] |
| 라이선스 불확실성(출시 전후 글) | [OrcaRouter: Qwen 3.8 27B 공개 가중치 유출](https://www.orcarouter.ai/blog/qwen-3-8-27b-huggingface) (스니펫만) | [부분: 2차] |
| 독립 지수 | [Artificial Analysis: Qwen3.8 27B](https://artificialanalysis.ai/de/models/qwen3-8-27b), [Qwen3.8 27B (non-reasoning)](https://artificialanalysis.ai/de/models/qwen3-8-27b-non-reasoning), [Qwen3.8 27B (low)](https://artificialanalysis.ai/de/models/qwen3-8-27b-low) (스니펫만) | [부분, 충돌] |
| 이전 세대 로컬 후기 | [Brian Lovin HN](https://brianlovin.com/hn/47960507), [InsiderLLM: 로컬 모델 함수 호출](https://insiderllm.com/guides/function-calling-local-llms/) (스니펫만) | [부분: 개인 후기, 이전 세대] |
- 공식 모델 카드·LICENSE 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
