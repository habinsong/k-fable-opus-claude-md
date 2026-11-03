# Grok 5 (미출시) — 교차 확인
> 제공자: xAI · 모델 ID: `grok-5(미확인)` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/grok/grok-5/general.md`](../../../md/grok/grok-5/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- xai-org/grok-build에서 'grok-5'는 signals_tests.rs 한 곳에만 나온다. 시험 코드일 뿐이다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 훈련 상태 | Colossus 2에서 훈련 중 (xAI Series E 발표, 2026-01-28) | [부분] 2차 2곳 일치 | geotoolbox, webpronews 등 | 일정은 2025 말 → 2026 1분기 → 2분기로 밀렸다는 서술 |
| 출시일 | 미정 | [미확인] | - | 2026-11 시점의 신뢰할 자료를 찾지 못했다 |
| 파라미터 수 | 6T·10T 등 소문 | [미확인] | - | xAI가 여러 모델을 동시에 훈련하고 있어 다른 실행의 수치가 섞였을 수 있다는 지적 |

## 아직 못 올린 것
- 사양을 쓰지 않는다. 출시 전에 모델 ID를 코드에 박지 않는다.

## 출처
- [xai-org/grok-build model.rs](https://raw.githubusercontent.com/xai-org/grok-build/main/crates/codegen/xai-grok-pager/src/slash/commands/model.rs)
- [geotoolbox](https://geotoolbox.ai/blog/grok-5)
- [webpronews](https://www.webpronews.com/xais-grok-5-delay-musks-ai-ambitions-hit-roadblock-amid-race-to-agi)
