# MiniMax M3.1 Flash — 교차 확인
> 제공자: MiniMax · 모델 ID: `minimax-m3.1-flash` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/minimax/minimax-m3.1-flash/general.md`](../../../md/minimax/minimax-m3.1-flash/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- MiniMax-AI/MiniMax-M3 README에 M3.1·M3.1-Flash 언급이 없다. M3.1 Flash의 1차 출처는 읽지 못했다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 프리뷰 / API / 가중치 | 2026-09-27 / 2026-10-19 / 2026-10-23 | [부분] 2차 3곳 일치 | datanorth, aicybr, magica, usagepricing | 프리뷰는 오픈 웨이트가 아니라는 서술 |
| 가격 (입력/출력) | $0.15 / $0.60, 캐시 입력 $0.015 | [부분] 2차 4곳 일치 | codersera, digitalapplied, usagepricing, vals.ai |  |
| 컨텍스트 / 최대 출력 | 1M / 512K~524K | [부분] 2차 2곳 일치, 출력 상충 | devtk.ai, codersera | 출력 상한이 512K와 524K로 갈린다 |
| 규모 | 428B MoE, 252 GB 다운로드 | [부분] 단일 출처 | aicybr |  |
| 라이선스 | MiniMax Community License: 비상업 무료, 상업은 'Built with MiniMax M3.1-Flash' 표기와 MiniMax에 통지, 연매출 2천만 달러 초과 시 사전 서면 승인, 군사 목적 등 금지 | [부분] 2차 4곳 일치 | fourweekmba, pasqualepillitteri, aicybr, gradually.ai | 'Proprietary'라고 쓴 한 곳이 있으나 다수와 상충. MIT·Apache가 아니다. LICENSE 원문(Hugging Face)을 읽지 못함 |

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
