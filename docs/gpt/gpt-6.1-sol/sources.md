# GPT-6.1 Sol — 출처와 한계
> 제공자: OpenAI · 모델 ID: `gpt-6.1-sol` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6.1-sol/general.md`](../../../md/gpt/gpt-6.1-sol/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| API 규칙, effort, 이전 원칙 | [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) | [확인] |
| 모델 페이지·기본 effort·`all_turns` | [GPT-6.1 Sol Model](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model) (스니펫만) | [부분] |
| 이전 시 오류, `max` 지연 | [OpenAI 커뮤니티: 세 가지 API 변경](https://community.openai.com/t/migrating-to-gpt-6-1-sol-astra-three-api-changes-that-cause-errors-effort-none-sampling-params-tools-in-chat-completions/1412047), [OpenAI 커뮤니티: max가 느린 이유](https://community.openai.com/t/why-is-gpt-6-1-sol-max-dramatically-slower-than-gpt-5-6-sol-max-using-the-same-prompt/1406429) (사용자 글) | [부분] |
| 정확도·속도·보안 통과율 | [Endor Labs](https://www.endorlabs.com/learn/gpt-6-1-sol-on-codex-astra-level-security-a-third-faster-zero-cheating), [DataCamp](https://www.datacamp.com/blog/gpt-6-1-sol), [techaiwire](https://techaiwire.com/articles/openai-gpt-6-1-sol-nearly-matches-astra/) | [부분] |
| 가격·컨텍스트 | [lmspedia](https://lmspedia.org/gpt-6-1-sol/), [nocode.mba](https://www.nocode.mba/articles/gpt-6-1-sol-vs-gpt-6-astra) | [부분] |
- OpenAI 본문 페이지는 이 환경에서 열리지 않아 스니펫만 확인했다. 가격·장문 요금은 공식 페이지로 다시 확인한다.
- Endor Labs 수치는 한 업체의 단일 하네스 결과다. 이 저장소의 과제에서는 다를 수 있다.
