# Kimi K3.1 Pro — 교차 확인
> 제공자: Moonshot · 모델 ID: `kimi-k3.1` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/kimi/kimi-k3.1/general.md`](../../../md/kimi/kimi-k3.1/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- MoonshotAI/Kimi-K3 README(직전 K3): 총 2.8T, 활성 104B(MoE, 896 전문가 중 16 + 공유 2), 컨텍스트 1,048,576, 코드와 가중치 모두 'Kimi K3 License'. K3.1은 언급되지 않는다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| K3 사양 (직전 모델) | 2.8T / 104B 활성 / 1,048,576 / Kimi K3 License | [확인] 1차 | MoonshotAI/Kimi-K3 README | K3.1 사양이 아니다. K3.1이 K3를 후속 학습한 모델이라는 서술만 있다 |
| K3.1 Pro API 출시 | 2026-10-23 | [부분] 2차 3곳 일치 | letsdatascience, pasqualepillitteri, nocode.mba | 24일·25일로 쓴 곳도 있다 |
| 가중치 | 2026-11-04 공개 예고, 2026-11-03 기준 미공개 | [부분] 2차 2곳 일치 | letsdatascience, pasqualepillitteri | 공개 뒤 LICENSE 원문을 읽기 전에는 라이선스를 단정하지 않는다 |
| 가격 | K3의 2/3 (K3 $3/$15 → 약 $2/$10은 추론) | [부분] 단일 출처 | fourweekmba (Moonshot 가격 이미지 인용) | 공식 가격표를 읽지 못했다 |
| 컨텍스트 | 1M | [부분] 단일 출처 | letsdatascience | Moonshot이 직접 확인한 유일한 사양이라는 서술 |
| 가중치 공개 표기 | vals.ai는 '오픈 웨이트'로 표기하지만 다른 출처는 2026-11-04 예정으로 적는다 | [부분] 상충 | vals.ai 대 letsdatascience, pasqualepillitteri, orcarouter | Hugging Face 업로드를 확인한 글이 없어 vals.ai 표기는 믿지 않는다 [추정] |

## 아직 못 올린 것
- Moonshot 공식 문서와 Hugging Face가 이 환경에서 열리지 않았다. 11월 4일 이후 가중치와 LICENSE를 직접 확인한다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [MoonshotAI/Kimi-K3 README](https://github.com/MoonshotAI/Kimi-K3)
- [letsdatascience](https://letsdatascience.com/news/moonshot-releases-kimi-k31-pro-api-open-weights-due-nov-4-786e160c)
- [pasqualepillitteri](https://pasqualepillitteri.it/en/news/26667/kimi-k3-1-pro-launches-open-weights-nov-4)
- [fourweekmba](https://fourweekmba.com/ai-moonshot-prices-kimi-k3-1-pro-at-half-of-claude-opus-5-5/)
- [nocode.mba](https://www.nocode.mba/ai-release-tracker/releases/kimi-k3-1-pro)
