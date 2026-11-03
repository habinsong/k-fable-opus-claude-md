# Claude Fable 5.5 (미출시) — 교차 확인
> 제공자: Anthropic · 모델 ID: `claude-fable-5-5(미확인)` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.5/general.md`](../../../md/claude/fable-5.5/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- Claude API 모델 개요 표(2026-11-03 직접 읽음): API ID, 가격, 컨텍스트, 최대 출력, 기본 effort, 지식 컷오프, 퇴역 약속일.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 공식 모델 목록에 있는가 | 없음 (Fable 계열 최신은 5.1) | [확인] 1차 (부재 확인) | Models overview, 가격 페이지 | 가격 페이지에도 Fable 5.5 행이 없다 |
| 출시 예고 | 없음 | [부분] 2차 일치(부재) | emergent.sh, 2026-10-05 기사 | Anthropic이 Fable 5.5의 존재를 확인한 적 없다는 서술 |

## 아직 못 올린 것
- 사양을 쓰지 않는다. 출시 전에 모델 ID를 코드에 박지 않는다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [Claude 모델 개요](https://platform.claude.com/docs/en/models/overview)
- [Claude 가격](https://platform.claude.com/docs/en/about-claude/pricing)
- [emergent.sh](https://emergent.sh/news/claude-fable-5-5-release-date)
