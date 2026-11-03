# Gemma 4 12B — 교차 확인
> 제공자: Google (로컬) · 모델 ID: `gemma-4-12b` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemma/gemma-4-12b/general.md`](../../../md/gemma/gemma-4-12b/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- google-deepmind/gemma 저장소 README: `gm.nn.Gemma4_E4B()` 코드 식별자와 'Gemma 4' 주석이 있다. 크기, 컨텍스트, 가중치 라이선스는 적혀 있지 않다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-04-02 | [부분] 2차 4곳 일치 | rits.shanghai.nyu.edu, techwyse, aimlapi, notebookcheck |  |
| 라이선스 | Apache 2.0 | [부분] 2차 4곳 일치 | rits.shanghai.nyu.edu, techwyse, aimlapi, oracore | google-deepmind/gemma 저장소의 Apache-2.0은 라이브러리 코드 라이선스다. 가중치 라이선스는 모델 카드(Hugging Face, 열리지 않음)에서 확인해야 한다 |
| 파라미터 / 컨텍스트 | 약 11.95B (unified) / 256K | [부분] 단일 출처 + 컨텍스트 [부분] 2차 3곳 일치 | jacar.es 외 | 12B는 초기 보도에 없고 늦은 가이드에만 나온다. 모델 카드로 확인 필요 |

## 아직 못 올린 것
- Hugging Face 모델 카드(huggingface.co)가 이 환경에서 열리지 않아 크기, 컨텍스트, 오디오 제한, 라이선스 원문을 직접 읽지 못했다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.
- 초기 보도는 4종, 나중 가이드는 5종(E2B, E4B, 12B, 26B A4B, 31B)을 적는다. 12B는 늦은 보도에만 나온다.

## 출처
- [google-deepmind/gemma README](https://github.com/google-deepmind/gemma)
- [rits.shanghai.nyu.edu](https://rits.shanghai.nyu.edu/ai/google-releases-gemma-4-frontier-open-models-under-apache-2-0/)
- [techwyse](https://www.techwyse.com/news/ai-search/google-deepmind-gemma-4-open-models-apache-2-0-release)
- [aimlapi](https://aimlapi.com/blog/gemma-4---google-deepminds-most-powerful-open-weight-ai-model-family)
- [jacar.es](https://jacar.es/en/gemma-4-locally-with-ollama/)
- [oracore](https://oracore.dev/news/gemma-4-256k-context-open-models-en)
- [cheatsheets.zip](https://cheatsheets.zip/gemma4)
