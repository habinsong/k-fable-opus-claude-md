# Claude Sonnet 5.5 — 개요·사양·라이선스
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/sonnet-5.5/general.md`](../../../md/claude/sonnet-5.5/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- "속도와 지능의 가장 좋은 조합"으로 안내된다. Anthropic은 가장 어려운 장시간 작업에는 Opus를 권한다.
- 가격은 입력 $2 / 출력 $10(100만 토큰당), 캐시 읽기 $0.10(Sonnet 5의 절반). 컨텍스트 1M, 최대 출력 128K, 지식 컷오프 2026-06. 토크나이저는 Sonnet 5와 같다. 기본 effort는 Claude API에서 **`high`**이고 `low` / `medium` / `high` / `xhigh` / `max`를 지원한다. 레벨이 재조정돼 Sonnet 5의 같은 레벨과 생각량이 다르다.
- 추론은 적응형이 기본이고, 끄려면 `thinking: {"type":"between_tools"}`를 쓴다(`low`·`medium`·`high`에서만, `xhigh`·`max`에서는 400). `disabled`는 400이다.
