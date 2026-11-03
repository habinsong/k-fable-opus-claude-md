# 한국어 AI 말투를 다루는 공개 프로젝트

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 직접 읽은 범위는 GitHub 저장소 페이지와 문서 파일이다(`[확인]`은 "그 프로젝트가 무엇을 주장하는지"를 읽었다는 뜻이다). 주장이 사실인지는 [`empirical-validation.md`](empirical-validation.md)에서 따로 본다.

## 1. 프로젝트별 정리

| 프로젝트 | 라이선스 | 구성 | 읽은 범위 |
|---|---|---|---|
| [im-not-ai](https://github.com/epoko77-ai/im-not-ai) | MIT | 10개 대분류(A~J) 85개 서브 패턴, 심각도 S1(결정적)·S2(강함)·S3(약함), 진단→윤문→검증 단계, 변경률 가드 | README, `skills/humanize-korean/references/`의 `ai-tell-taxonomy`·`rewriting-playbook`·`empirical-validation`·`scholarship`·`baseline.json` [확인] |
| [k-skill korean-humanizer](https://github.com/NomaDamas/k-skill) | MIT (일부 하위 경로 AGPL-3.0) | A~K 분류, 60개 이상 서브 패턴, S1~S3, 변경률 30% 경고·50% 중단, 자가 채점 A~D | 저장소 소개와 [`ai-tell-taxonomy.md`](https://github.com/NomaDamas/k-skill/blob/main/korean-humanizer/references/ai-tell-taxonomy.md) [확인] |
| [yoonmoon](https://github.com/amondnet/yoonmoon) | MIT | 6개 스킬(polish-all, humanize, translate-polish, proofread, restyle, detect), 11개 분류, **말이 모자란 쪽 실패(과소 서술)**까지 다루는 양방향 교정 | 저장소 소개 [확인] |
| [humanizer-ko](https://github.com/daleseo/korean-skills) | MIT | 6범주 40패턴(문장부호 7, 띄어쓰기 3, 품사 다양성 3, 어휘 10, 문장 구조 4, 번역투 13), 경어체 균일성 | 저장소 소개. `SKILL.md`는 404였다 [부분] |
| [blader/humanizer](https://github.com/blader/humanizer) | MIT | 영어 원조. 26개 패턴(A~F), 초안→비평→최종 처리 | 저장소 소개 [확인] |
| [KatFishNet](https://github.com/Shinwoo-Park/katfishnet) | 표기 없음 | 한국어 LLM 생성 글 탐지 연구 코드·데이터(에세이·시·논문 초록) | 저장소 README [부분] |

KatFishNet은 라이선스 표기가 없어 코드와 데이터를 가져오지 않았다. 나머지는 MIT이지만 코드를 가져오지 않았고, 아이디어를 이해해 다시 썼다(`universal/ko-core.md`).

## 2. 사용자 요구 항목과 공개 분류의 대응

| 사용자가 짚은 문제 | 공개 분류에서 가장 가까운 항목 | 비고 |
|---|---|---|
| 문장 사이의 흐름과 호흡 | im-not-ai E-1(문장 길이 표준편차), E-2(같은 종결어미 4문장 연속), H(문두 접속사) / humanizer-ko 문장부호·띄어쓰기·품사 다양성 | E-1 기준값은 `baseline.json`에 없다 |
| AI는 과하게 서술함 | D-1~D-3·D-8(결산 피벗, 의미 부풀리기), F(수식·중복), G(헤징), yoonmoon의 과잉 수식 | 과서술 반대편(과소 서술)은 yoonmoon만 별도 항목으로 둠 |
| 사람이 쓰지 않는 용어·문장 | A(번역투 19개 서브), B(영어 과다), I(형식명사), F-5(~적 N) | 일부는 실측에서 기각됨 |
| 과서술과 인위적 감정 표현 | K-2(아첨·과잉 공손), D-4(hype 어휘) | **감정 과장을 직접 다루는 항목은 없다** |
| 대구 | im-not-ai C-8(대구), F-2(부정 대비), 실측 대상 | 실측에서 가장 강한 신호 |
| 도치 | 해당 항목 없음. 가장 가까운 것은 I-2("~라는 점에 있다") | **공개 자료에서 찾지 못했다 [미확인]** |

## 3. 내가 가져온 설계 아이디어와 가져오지 않은 것

- 가져온 것: 신호가 한 단락에 겹칠 때만 고치기, 변경률 5~30% 권장·50% 중단, 사실과 필자 문체 보존, 빼기 중심, 효과적인 대구 한두 개는 남기기, 초안→점검→수정 순환.
- 가져오지 않은 것: 금지어 목록(실측에서 사람이 더 많이 쓴 표현이 섞여 있음), 탐지 점수와 등급(A~D), 탐지기 우회 목적의 기능.
- 가져오지 않은 이유(탐지기 우회): 이 저장소의 목표는 읽기 좋은 글이지 탐지 회피가 아니다. 학교·학술지·공모전의 AI 사용 규정이 있으면 그것이 먼저다.

## 4. 열람하지 못한 2차 출처

[한국어 AI 말투 정리 글](https://www.digitalmarketer.co.kr/insights/claude-load-bearing-vocabulary-github-pr), [im-not-ai 소개](https://discuss.pytorch.kr/t/im-not-ai-ai-claude-code/10666), [연합뉴스 계열 기사](https://www.koreancenter.or.kr/news/articleView.html?idxno=1431238), [한국어 휴머나이저 분석](https://blog.pebblous.ai/report/korean-ai-humanizer-teardown-2026-08/ko/)은 이 환경에서 호스트가 열리지 않아 검색 요약만 보았다 [부분]. 검색 요약에 따르면 같은 대상을 다른 낱말로 바꿔 부르는 습관(elegant variation)이 번역투를 고쳐도 남는 원인이라는 한 필자의 경험담이 있으나, 이것은 개인 경험담이다.
