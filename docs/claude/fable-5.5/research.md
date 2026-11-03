# Claude Fable 5.5 · 연구 (미출시 대비) — 조사 기록
> 제공자: Anthropic · 모델 ID: 미정(공식 확인 전 [미확인]) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.5/research.md`](../../../md/claude/fable-5.5/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용 (잠정)
2026-11-03 기준 Fable 5.5는 공식 목록에 없다. 모델 상태와 출시일 체크리스트는 같은 폴더의 `general.md` §2를 따른다. 출시 전에는 `claude/fable-5.1/research.md`를 적용한다.

**출시 후 연구 작업에서 따로 확인할 것**
- 긴 산출물 처리. Fable 5.1은 `xhigh`·`max`에서 긴 산출물을 생각 속에서 초안으로 쓰고 다시 써서 시간과 토큰이 늘었다. 5.5에서 같은 현상이 있는지, `max_tokens`를 어떻게 잡아야 하는지 확인한다.
- 장문 컨텍스트에서의 세부 연결. 긴 논문 묶음에서 모델이 연결한 주장을 해당 논문의 해당 위치와 대조해, 오연결 비율을 직접 센다.
- 한정어와 범위 표현. 결과 요약에서 한정어가 지워지거나 범위가 부풀려지는지, 원자료의 조건과 대조한다. 다른 계열 모델에서 이 경향에 대한 엇갈린 평가가 있었다.
- 추론을 응답에 쓰게 하는 요청의 거부 범주(`reasoning_extraction`)가 유지되는지.
- 생물학 안전장치가 정당한 생명과학 연구를 막는지, 검증 프로그램의 조건이 바뀌었는지.
- 생성 텍스트의 워터마크와 대상 학술지·arXiv의 AI 사용 정책. 저자가 내용 전체에 책임진다는 원칙은 모델이 바뀌어도 같다.
- 열린 과학 추론에서 5.1 대비 변화. 새 가설·증명·실험 설계는 모델 단독이 아니라 전문가 검토를 거친다.

**잠정 운용**
- 출시 전 연구 작업은 Fable 5.1과 Opus 5.5로 진행한다. 모든 인용은 필드 단위로 직접 확인하고, 분석은 코드를 다시 실행해서 확인한다.

## 4. 근거와 한계
- 미출시 확인: [Models overview](https://platform.claude.com/docs/en/models/overview) [확인: 2026-11-03에 직접 읽음]
- 잠정 규칙과 `xhigh` 산출물 현상: 같은 저장소의 `claude/fable-5.1/research.md`, [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) [확인: Fable 5.1 기준]
- 한계: 이 문서의 모든 5.5 관련 서술은 확인 항목 목록이며 모델 특성이 아니다.
