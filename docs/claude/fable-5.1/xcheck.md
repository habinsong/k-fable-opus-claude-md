# Claude Fable 5.1 — 교차 확인
> 제공자: Anthropic · 모델 ID: `claude-fable-5-1` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.1/general.md`](../../../md/claude/fable-5.1/general.md)

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
| API ID / 컨텍스트 / 최대 출력 | `claude-fable-5-1` / 1M / 128K | [확인] 1차 | Models overview | 표의 별칭 행도 같은 ID |
| 가격 (입력/출력) | $10 / $50, 5분 캐시 쓰기 $12.50, 1시간 $20, 캐시 읽기 $0.25(입력가의 2.5%) | [확인] 1차 | 가격 페이지 | Fable 5는 캐시 읽기 $1, 5.1부터 $0.25 |
| 기본 effort / 추론 | `high` / 적응형(항상 켜짐) | [확인] 1차 | Models overview |  |
| 지식 컷오프 / 퇴역 | 2026-06 / 2027-09-01 이전에는 퇴역하지 않음 | [확인] 1차 | Models overview | 퇴역은 Anthropic이 운영하는 플랫폼 기준 약속 |
| 출시일 | 2026-09-01 (Claude Mythos 5.1과 같은 날) | [부분] 단일 출처 + 예측시장 | emergent.sh 분석, Manifold(Fable 5 2026-06-09 이후 84일) | Anthropic 발표 페이지는 읽지 못했다 |
| Mythos 5.1 | 제한 공개, 가격 $10/$50 | [확인] 1차 | 가격 페이지 | 이 폴더의 대상이 아니다. Fable 5.1과 같은 요금이라는 점만 기록 |

## 아직 못 올린 것
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [Claude 모델 개요](https://platform.claude.com/docs/en/models/overview)
- [Claude 가격](https://platform.claude.com/docs/en/about-claude/pricing)
- [emergent.sh](https://emergent.sh/news/claude-fable-5-1-release-date)
- [Manifold](https://manifold.markets/Terminator2/when-will-anthropic-release-its-nex)
