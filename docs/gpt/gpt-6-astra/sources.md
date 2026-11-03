# GPT-6 Astra — 출처와 한계
> 제공자: OpenAI · 모델 ID: `gpt-6-astra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-astra/general.md`](../../../md/gpt/gpt-6-astra/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| API 규칙, effort, 마이그레이션 원칙 | [openai/codex `upgrading-to-gpt-6-astra.md`](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) (OpenAI 운영 저장소, 직접 읽음) | [확인] |
| 지침 충돌·반복 규칙·완료 기준·문체 | [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model), [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) (검색 스니펫만) | [부분] |
| 가격·컨텍스트 | [OpenRouter 목록](https://openrouter.ai/openai/gpt-6-astra), [CloudZero](https://www.cloudzero.com/blog/gpt-6-pricing/), [eesel.ai](https://www.eesel.ai/blog/gpt-6-astra-pricing) | [부분] |
| 비판적 평가 | [eesel.ai 리뷰](https://www.eesel.ai/blog/gpt-6-astra-review), [Layer3 Labs](https://www.layer3labs.io/guides/gpt-6-astra-review), [Transformer](https://www.transformernews.ai/p/openai-gpt-6-astra-might-be-too-powerful-to-understand-or-control), [NeoTeo](https://www.neoteo.com/en/gpt-6-astra-improves-coding-and-computer-use-but-still-needs-supervision) | [부분] |
- 이 환경에서는 `openai.com`·`developers.openai.com` 본문을 열 수 없어 스니펫만 확인했다. 컨텍스트 크기, 기본 effort, Fast·Ultrafast 요금은 **[미확인]**이다.
- 리뷰 다수는 출시 직후 블로그와 제휴 성격 사이트다. 한 곳의 수치(속도 4배 차이 등)는 다른 곳에서 재확인되지 않았다.
