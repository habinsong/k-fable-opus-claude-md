# MiniMax M3 — 교차 확인
> 제공자: MiniMax · 모델 ID: `minimax-m3` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/minimax/minimax-m3/general.md`](../../../md/minimax/minimax-m3/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- MiniMax-AI/MiniMax-M3 README: 약 428B 파라미터, 약 23B 활성, 'native multimodal model with 1M context', 가중치는 `hf download MiniMaxAI/MiniMax-M3`. LICENSE는 Hugging Face 파일을 가리킬 뿐 본문이 없다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 파라미터 / 컨텍스트 | 약 428B / 약 23B 활성 / 1M | [확인] 1차 | MiniMax-AI/MiniMax-M3 README | Fireworks는 자사 오픈 웨이트 서비스가 500K까지라고 적는다. 서비스 제한이다 [추정] |
| 출시일 | 2026-06-01 | [부분] 2차 4곳 일치 | llm-stats, Artificial Analysis, tech-insider, theaitrack | 가중치 HF 게시는 06-07(한 곳) |
| 가격 (입력/출력) | $0.30 / $1.20 (512K 이하), $0.60 / $2.40 (512K 초과) | [부분] 2차 2곳 일치, 상충 | Artificial Analysis, developersdigest | codersera는 '영구 50% 할인, 정가 $0.60/$2.40'이라고 적는다 |
| 라이선스 | MiniMax Community License | [부분] 단일 출처 | developersdigest | 상업 이용 조건은 원문 확인 전까지 단정하지 않는다 |

## 아직 못 올린 것
- huggingface.co, MiniMax 문서가 이 환경에서 열리지 않았다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [MiniMax-AI/MiniMax-M3 README](https://github.com/MiniMax-AI/MiniMax-M3)
- [vals.ai (M3.1 Flash)](https://www.vals.ai/models/minimax_MiniMax-M3.1-flash)
- [datanorth (M3.1 Flash 프리뷰)](https://datanorth.ai/news/minimax-releases-m3-1-flash-preview)
- [aicybr (M3.1 Flash 가중치)](https://aicybr.com/blog/minimax-m31-flash-open-weights-428b-license-local-deployment)
- [codersera (M3.1 Flash)](https://codersera.com/blog/minimax-m3-1-flash-complete-guide-2026/amp/)
- [developersdigest (M3)](https://www.developersdigest.tech/models/minimax-m3)
- [fourweekmba (M3.1 Flash 라이선스)](https://fourweekmba.com/ai-minimax-opens-m3-1-flash-20m-products-need-its-sign-off/)
- [pasqualepillitteri (M3.1 Flash 라이선스)](https://pasqualepillitteri.it/en/news/26561/minimax-m3-1-flash-weights-hugging-face-license)
- [Artificial Analysis (M3)](https://artificialanalysis.ai/articles/minimax-m3)
- [llm-stats (M3)](https://www.llm-stats.com/models/minimax-m3)
