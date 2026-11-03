# 규칙 목록 (자동 생성)

`ai-smell rules --format md`가 만든다. 직접 고치지 말고 `ai_smell/rules/`를 고친 뒤 다시 만든다.

| id | 언어 | 범주 | 등급 | 가중치 | 교정 | 설명 |
|---|---|---|---|---|---|---|
| `en.residue.opener` | en | 챗봇 잔재 | A | 1.0 | standard | Paragraph opens with a chatbot acknowledgement. |
| `en.residue.here-is-revised` | en | 챗봇 잔재 | A | 1.0 | standard | Meta sentence introducing the edited text. |
| `en.residue.hope-helps` | en | 챗봇 잔재 | A | 1.0 | standard | Chatbot sign-off. |
| `en.residue.let-me-know` | en | 챗봇 잔재 | A | 1.0 | standard | Offer of further help at the end. |
| `en.residue.happy-to-help` | en | 챗봇 잔재 | A | 1.0 | standard | Eager-to-help line. |
| `en.residue.apology` | en | 챗봇 잔재 | A | 1.0 | standard | Stock apology. |
| `en.residue.as-an-ai` | en | 챗봇 잔재 | A | 1.0 | standard | Model self-reference as a preamble. |
| `en.residue.no-opinions` | en | 챗봇 잔재 | A | 1.0 | - | Model limitation disclaimer. |
| `en.residue.cutoff` | en | 챗봇 잔재 | A | 1.0 | - | Knowledge-cutoff disclaimer. |
| `en.residue.generated-note` | en | 챗봇 잔재 | A | 1.0 | standard | Self-label line. |
| `en.sycophancy.praise` | en | 아첨·공치사 | A | 0.6 | standard | Praises the question before answering. |
| `en.sycophancy.right` | en | 아첨·공치사 | A | 0.6 | standard | Agreement opener that agrees before checking. |
| `en.placeholder.bracket` | en | 빈 자리표시자 | A | 0.8 | - | Template slot left unfilled. |
| `any.markup.utm` | any | 누출된 마크업 | A | 1.0 | safe | Chat tool tag in a URL. |
| `en.residue.signpost-polish` | en | 챗봇 잔재 | B | 1.0 | standard | Label line for the edited text. |
| `en.puffery.testament` | en | 의미 부풀리기 | B | 1.0 | - | Inflates a small fact into a symbol. |
| `en.puffery.vital-role` | en | 의미 부풀리기 | B | 1.0 | - | Importance asserted instead of shown. |
| `en.puffery.underscores` | en | 의미 부풀리기 | B | 1.0 | - | Sentence announces its own significance. |
| `en.puffery.tapestry` | en | 의미 부풀리기 | B | 1.0 | standard | Stock metaphor. |
| `en.puffery.todays-world` | en | 의미 부풀리기 | B | 1.0 | standard | Generic scene-setting opener. |
| `en.puffery.evolving-landscape` | en | 의미 부풀리기 | B | 1.0 | - | Stock phrase for change. |
| `en.puffery.navigate` | en | 의미 부풀리기 | B | 1.0 | standard | Navigation metaphor. |
| `en.puffery.beacon` | en | 의미 부풀리기 | C | 1.0 | - | Monument metaphor. |
| `en.puffery.paving` | en | 의미 부풀리기 | B | 1.0 | - | Stock phrase for 'enables'. |
| `en.puffery.unlock` | en | 의미 부풀리기 | B | 1.0 | standard | Stock phrase. |
| `en.puffery.game-changer` | en | 의미 부풀리기 | B | 1.0 | standard | Hype word. |
| `en.puffery.future-bright` | en | 의미 부풀리기 | B | 1.0 | - | Empty forward-looking close. |
| `en.puffery.only-time` | en | 의미 부풀리기 | C | 1.0 | - | Empty forward-looking close. |
| `en.puffery.lasting` | en | 의미 부풀리기 | C | 1.0 | - | Legacy cliche. |
| `en.puffery.travel` | en | 의미 부풀리기 | C | 1.0 | - | Brochure language. |
| `en.puffery.unwavering` | en | 의미 부풀리기 | B | 1.0 | - | Intensified abstraction. |
| `en.puffery.transformative` | en | 의미 부풀리기 | B | 1.0 | - | Hype phrase. |
| `en.puffery.new-era` | en | 의미 부풀리기 | B | 1.0 | - | Importance inflation. |
| `en.puffery.metaphor-of` | en | 의미 부풀리기 | C | 1.0 | - | Stock metaphor. |
| `en.puffery.realm` | en | 의미 부풀리기 | C | 1.0 | - | Abstract container; 'in' is enough. |
| `en.puffery.fragment-closer` | en | 의미 부풀리기 | B | 1.0 | - | Dramatic one-line closer. |
| `en.puffery.the-real` | en | 의미 부풀리기 | C | 1.0 | - | Staged reveal. |
| `en.puffery.honest-answer` | en | 의미 부풀리기 | C | 1.0 | - | Anecdotal tic reported for recent assistants; weak evidence. |
| `en.attribution.vague` | en | 출처 없는 권위 | B | 1.0 | - | Authority without a named source. |
| `en.signpost.lets-pure` | en | 예고·안내 | B | 0.8 | standard | Content-free announcement. |
| `en.signpost.lets` | en | 예고·안내 | B | 0.6 | - | Announces what will be done instead of doing it. |
| `en.signpost.in-this` | en | 예고·안내 | C | 0.8 | - | Table-of-contents sentence. |
| `en.signpost.stock` | en | 예고·안내 | C | 0.8 | - | Hook phrase. |
| `en.signpost.heres-the-thing` | en | 예고·안내 | B | 0.8 | strong | Staged run-up. |
| `en.signpost.the-x-question` | en | 예고·안내 | B | 0.8 | - | Self-posed question answered at once. |
| `en.signpost.question-opener` | en | 예고·안내 | C | 0.8 | - | Hook opening. |
| `en.signpost.whether` | en | 예고·안내 | B | 0.8 | - | 'Whether you're A or B' audience sweep. |
| `en.puffery.adds-depth` | en | 의미 부풀리기 | B | 1.0 | standard | Stock depth/nuance inflation. |
| `en.puffery.signal` | en | 의미 부풀리기 | B | 1.0 | standard | Stock signalling rhetoric. |
| `en.puffery.abstract-index` | en | 의미 부풀리기 | B | 1.0 | standard | Abstract metric jargon in prose. |
| `en.puffery.density` | en | 의미 부풀리기 | B | 1.0 | standard | Pretentious density phrasing. |
| `en.puffery.paradigm-shift` | en | 의미 부풀리기 | B | 1.0 | standard | Cliché buzzword for major change. |
| `en.structure.neg-parallel` | en | 구조 습관 | A | 1.2 | strong | Negative parallelism: knocks down a view nobody held, then states the point. |
| `en.structure.neg-parallel-noun` | en | 구조 습관 | A | 1.2 | - | Negative parallelism with a noun subject. |
| `en.structure.isnt-x-but-y` | en | 구조 습관 | B | 0.8 | - | 'isn't the X but the Y' contrast. |
| `en.structure.on-one-hand` | en | 구조 습관 | C | 0.5 | - | Balanced both-sides frame. |
| `en.structure.neg-parallel-about` | en | 구조 습관 | A | 1.2 | - | Negative parallelism ('isn't about X, it's about Y'). |
| `en.structure.not-only` | en | 구조 습관 | B | 0.7 | - | 'Not only X but also Y' frame. |
| `en.structure.more-than-just` | en | 구조 습관 | B | 1.2 | - | Negative-parallel variant. |
| `en.structure.less-more` | en | 구조 습관 | B | 1.2 | - | Negative-parallel variant ('less about X, more about Y'). |
| `en.structure.no-no-just` | en | 구조 습관 | B | 1.2 | - | 'No X. No Y. Just Z.' triple. |
| `en.structure.not-a-but-a` | en | 구조 습관 | B | 1.2 | - | 'Not a X, but a Y' frame. |
| `en.structure.participial-tail` | en | 구조 습관 | B | 1.2 | strong | Tail clause that announces significance ('..., highlighting its importance'). |
| `en.structure.copula` | en | 구조 습관 | B | 1.2 | standard | Fancy verb where 'is' works. |
| `en.structure.boasts` | en | 구조 습관 | B | 1.2 | strong | 'Boasts' for 'has'. |
| `en.structure.considered` | en | 구조 습관 | C | 1.2 | - | Vague framing. |
| `en.structure.summary-open` | en | 구조 습관 | B | 0.6 | - | Paragraph restates what was just said. |
| `en.structure.summary-heading` | en | 구조 습관 | C | 0.4 | - | Template heading. |
| `en.structure.false-concession` | en | 구조 습관 | C | 1.2 | - | 'While X has limits, it is still great' frame. |
| `en.structure.false-range` | en | 구조 습관 | C | 1.2 | - | Range with no real scale. |
| `en.structure.staged-honest` | en | 구조 습관 | C | 1.2 | - | Staged candor. |
| `en.structure.paired-with` | en | 구조 습관 | B | 1.2 | standard | Overused coupling phrase. |
| `en.hedging.note-that` | en | 군더더기·유보 | B | 0.7 | standard | Throat-clearing before the actual statement. |
| `en.hedging.potentially` | en | 군더더기·유보 | B | 0.7 | standard | Stacked hedge. |
| `en.hedging.stock-lead` | en | 군더더기·유보 | C | 0.7 | strong | Filler lead-in. |
| `en.hedging.adverb-lead` | en | 군더더기·유보 | C | 0.5 | strong | Sentence adverb that comments on itself. |
| `en.hedging.that-said` | en | 군더더기·유보 | C | 0.4 | - | Stock concession opener. |
| `en.hedging.worth-ing` | en | 군더더기·유보 | B | 0.5 | - | Throat-clearing that points at the next point. |
| `en.hedging.when-it-comes` | en | 군더더기·유보 | C | 0.4 | - | Wordy topic marker; 'for' or 'with' is usually enough. |
| `en.hedging.arguably` | en | 군더더기·유보 | C | 0.4 | - | Weasel hedge. |
| `en.hedging.wordy` | en | 군더더기·유보 | C | 0.3 | standard | Wordier than the plain phrase. |
| `en.vocab.notably-lead` | en | 과다 어휘 | A | 0.8 | strong | Sentence adverb that comments on itself. |
| `en.vocab.delve` | en | 과다 어휘 | A | 0.8 | - | Peak 'LLM word' in academic prose. |
| `en.vocab.delve-into` | en | 과다 어휘 | A | 0.8 | standard | Peak 'LLM word' in academic prose. |
| `en.vocab.tapestry` | en | 과다 어휘 | A | 0.8 | - | Stock metaphor. |
| `en.vocab.showcase` | en | 과다 어휘 | A | 0.8 | - | Overused verb ('show'). |
| `en.vocab.showcase-fix` | en | 과다 어휘 | A | 0.8 | standard | Overused verb ('show'). |
| `en.vocab.underscore` | en | 과다 어휘 | A | 0.8 | - | Overused verb ('show', 'stress'). |
| `en.vocab.intricate` | en | 과다 어휘 | A | 0.8 | - | Overused adjective. |
| `en.vocab.pivotal` | en | 과다 어휘 | A | 0.8 | strong | Overused adjective ('key'). |
| `en.vocab.meticulous` | en | 과다 어휘 | A | 0.8 | - | Overused adjective. |
| `en.vocab.commendable` | en | 과다 어휘 | A | 0.8 | - | Overused adjective. |
| `en.vocab.notably` | en | 과다 어휘 | A | 0.5 | - | Overused sentence adverb. |
| `en.vocab.multifaceted` | en | 과다 어휘 | A | 0.8 | - | Overused adjective. |
| `en.vocab.crucial` | en | 과다 어휘 | B | 0.5 | - | Overused intensifier. |
| `en.vocab.comprehensive` | en | 과다 어휘 | B | 0.5 | - | Overused adjective. |
| `en.vocab.enhance` | en | 과다 어휘 | B | 0.5 | - | Overused verb. |
| `en.vocab.foster` | en | 과다 어휘 | B | 0.8 | - | Overused verb. |
| `en.vocab.garner` | en | 과다 어휘 | B | 0.8 | - | Overused verb ('get', 'win'). |
| `en.vocab.bolster` | en | 과다 어휘 | B | 0.8 | - | Overused verb ('strengthen'). |
| `en.vocab.elevate` | en | 과다 어휘 | B | 0.8 | - | Overused verb. |
| `en.vocab.streamline` | en | 과다 어휘 | B | 0.8 | - | Overused verb. |
| `en.vocab.revolutionize` | en | 과다 어휘 | B | 0.8 | - | Hype verb. |
| `en.vocab.leverage` | en | 과다 어휘 | B | 0.8 | - | Business jargon for 'use'. |
| `en.vocab.leverage-fix` | en | 과다 어휘 | B | 0.8 | standard | Business jargon for 'use'. |
| `en.vocab.utilize` | en | 과다 어휘 | C | 0.4 | standard | 'Use' is enough. |
| `en.vocab.commence` | en | 과다 어휘 | C | 0.4 | standard | 'Start' is enough. |
| `en.vocab.facilitate` | en | 과다 어휘 | B | 0.5 | - | Abstract verb. |
| `en.vocab.empower` | en | 과다 어휘 | B | 0.8 | - | Hype verb. |
| `en.vocab.unleash` | en | 과다 어휘 | B | 0.8 | - | Hype verb. |
| `en.vocab.embark` | en | 과다 어휘 | B | 0.8 | - | Journey metaphor. |
| `en.vocab.holistic` | en | 과다 어휘 | B | 0.8 | - | Abstract adjective. |
| `en.vocab.synergy` | en | 과다 어휘 | B | 0.8 | - | Business jargon. |
| `en.vocab.paradigm` | en | 과다 어휘 | C | 0.8 | - | Abstract noun. |
| `en.vocab.myriad` | en | 과다 어휘 | B | 0.8 | - | Grand quantity word ('many'). |
| `en.vocab.nuanced` | en | 과다 어휘 | C | 0.8 | - | Vague praise. |
| `en.vocab.robust` | en | 과다 어휘 | C | 0.8 | - | Vague praise. |
| `en.vocab.seamless` | en | 과다 어휘 | C | 0.8 | - | Vague praise. |
| `en.vocab.vibrant` | en | 과다 어휘 | C | 0.8 | - | Vague praise. |
| `en.vocab.groundbreaking` | en | 과다 어휘 | B | 0.8 | - | Hype adjective. |
| `en.vocab.invaluable` | en | 과다 어휘 | B | 0.8 | - | Superlative with no number behind it. |
| `en.vocab.interplay` | en | 과다 어휘 | B | 0.8 | - | Abstract noun. |
| `en.vocab.ecosystem` | en | 과다 어휘 | C | 0.5 | - | Abstract container noun. |
| `en.vocab.dynamic` | en | 과다 어휘 | C | 0.4 | - | Vague intensifier. |
| `en.vocab.era-2026` | en | 과다 어휘 | C | 0.5 | - | Reported as a recent assistant tic (anecdotal). |
| `en.vocab.gauge` | en | 과다 어휘 | B | 0.8 | standard | Abstract measuring metaphor ('gauge the impact'). |
| `en.vocab.propagate` | en | 과다 어휘 | B | 0.8 | standard | Pretentious spreading verb in prose. |
| `en.vocab.seamless-action` | en | 과다 어휘 | B | 0.8 | standard | Overused 'seamless' buzzword with verbs. |
| `en.vocab.automatically` | en | 과다 어휘 | B | 0.8 | standard | Unnecessary 'automatically' modifier. |
| `en.vocab.hardcode` | en | 과다 어휘 | B | 0.8 | standard | Slang verb for embedding or baking in. |
| `ko.residue.opener` | ko | 챗봇 잔재 | A | 1.0 | standard | 챗봇식 수락 서두. |
| `ko.residue.hope-helps` | ko | 챗봇 잔재 | A | 1.0 | standard | 챗봇식 맺음 인사. |
| `ko.residue.ask-more` | ko | 챗봇 잔재 | A | 1.0 | standard | 더 도울 일을 묻는 맺음. |
| `ko.residue.anytime` | ko | 챗봇 잔재 | A | 1.0 | standard | '언제든 말씀하세요' 맺음. |
| `ko.residue.lead-in` | ko | 챗봇 잔재 | B | 1.0 | standard | 결과물 앞의 안내 문장. |
| `ko.residue.revised-label` | ko | 챗봇 잔재 | A | 1.0 | standard | 결과물 앞의 이름표 줄. |
| `ko.residue.as-ai` | ko | 챗봇 잔재 | A | 1.0 | - | 모델 자기소개. |
| `ko.residue.confusion` | ko | 챗봇 잔재 | A | 1.0 | standard | 판에 박힌 사과. |
| `ko.sycophancy.praise` | ko | 아첨·공치사 | A | 0.6 | standard | 질문을 칭찬하며 시작한다. |
| `ko.sycophancy.right` | ko | 아첨·공치사 | B | 0.6 | - | 확인하기 전에 먼저 동의한다. |
| `ko.sycophancy.apology-thanks` | ko | 아첨·공치사 | B | 0.3 | - | 사과와 감사가 한 글에 여러 번 겹친다. |
| `ko.placeholder.bracket` | ko | 빈 자리표시자 | A | 0.8 | - | 채우지 않은 자리표시자. |
| `ko.puffery.implication` | ko | 의미 부풀리기 | B | 1.0 | - | '시사하는 바가 크다': 무엇을 시사하는지 말하지 않는다. |
| `ko.puffery.noteworthy` | ko | 의미 부풀리기 | B | 1.0 | - | '주목할 만하다': 왜 주목할지 말하지 않는다. |
| `ko.puffery.key-role` | ko | 의미 부풀리기 | B | 1.0 | - | 중요하다고만 하고 무엇을 하는지 말하지 않는다. |
| `ko.puffery.cannot-stress` | ko | 의미 부풀리기 | B | 1.0 | - | 관용적 강조. |
| `ko.puffery.new-horizon` | ko | 의미 부풀리기 | B | 1.0 | - | 의미를 부풀리는 틀. |
| `ko.puffery.grand-background` | ko | 의미 부풀리기 | B | 1.0 | - | 서두의 거대한 배경. |
| `ko.puffery.importance-rises` | ko | 의미 부풀리기 | B | 1.0 | - | 중요성이 커진다는 말만 있다. |
| `ko.puffery.various` | ko | 의미 부풀리기 | C | 0.3 | - | '다양한 ~' 묶음. |
| `ko.puffery.overall` | ko | 의미 부풀리기 | C | 0.4 | - | 포괄 표현. |
| `ko.puffery.this-means` | ko | 의미 부풀리기 | C | 0.3 | - | '이는 ~를 의미한다' 해설. |
| `ko.puffery.future-close` | ko | 의미 부풀리기 | C | 1.0 | - | 빈 전망 맺음. |
| `ko.puffery.meaning` | ko | 의미 부풀리기 | B | 0.6 | - | 의미가 크다고만 하고 내용이 없다. |
| `ko.puffery.precious` | ko | 의미 부풀리기 | C | 0.3 | - | 정형 수식. |
| `ko.puffery.honestly` | ko | 의미 부풀리기 | C | 0.4 | - | 연출된 솔직함. |
| `ko.puffery.one-step` | ko | 의미 부풀리기 | C | 1.0 | - | 상투 연결. |
| `ko.puffery.deohada` | ko | 의미 부풀리기 | B | 0.7 | standard | '~를 더하다': 깊이·가치·매력 등 추상 명사에 '더하다'를 붙이는 상투구. |
| `ko.puffery.jisu` | ko | 의미 부풀리기 | B | 0.6 | standard | '~지수': 추상적 대상에 '지수(index)'를 붙여 객관성을 가장하는 표현. |
| `ko.puffery.mildo` | ko | 의미 부풀리기 | B | 0.6 | standard | '밀도': 깊이나 짜임새를 '밀도(density)'로 은유하는 상투적 표현. |
| `ko.signpost.announce` | ko | 예고·안내 | B | 0.8 | strong | 하겠다는 예고. 하지 않고 말만 한다. |
| `ko.signpost.lets` | ko | 예고·안내 | B | 0.8 | strong | 권유형 예고. |
| `ko.signpost.qa` | ko | 예고·안내 | C | 0.8 | - | 스스로 묻고 바로 답하는 틀. |
| `ko.structure.neg-simple` | ko | 구조 습관 | B | 1.2 | strong | '단순한 A가 아니라 B': 없던 오해를 세우고 부정한다. |
| `ko.structure.neg-general` | ko | 구조 습관 | B | 0.9 | - | 'A가 아니라 B' 대구. |
| `ko.structure.neg-chain` | ko | 구조 습관 | B | 1.2 | - | 부정을 연달아 쌓고 결론을 낸다. |
| `ko.structure.not-only` | ko | 구조 습관 | C | 0.3 | - | '~뿐만 아니라' 병렬. |
| `ko.structure.beyond` | ko | 구조 습관 | B | 0.8 | - | '~를 넘어 ~로' 확장 틀. |
| `ko.structure.on-one-hand` | ko | 구조 습관 | C | 0.5 | - | 양면을 나란히 세우는 틀. |
| `ko.structure.rather` | ko | 구조 습관 | C | 0.5 | - | 대구의 변종. |
| `ko.structure.postposed` | ko | 구조 습관 | C | 0.4 | - | 서술어 뒤에 부사를 붙이는 도치('했다, 조용히.'). |
| `ko.structure.cleft` | ko | 구조 습관 | C | 0.5 | - | 강조 도입. 한 글에 한 번 이하. |
| `ko.structure.enumerate` | ko | 구조 습관 | C | 0.5 | - | '첫째, 둘째' 기계 나열. |
| `ko.structure.summary-open` | ko | 구조 습관 | B | 0.6 | - | 앞 내용을 되풀이하는 맺음 문단. |
| `ko.hedging.rago` | ko | 군더더기·유보 | B | 0.6 | strong | '~라고 할 수 있다' 유보. |
| `ko.hedging.dago` | ko | 군더더기·유보 | B | 0.6 | strong | '~다고 할 수 있다' 유보. |
| `ko.hedging.should` | ko | 군더더기·유보 | B | 0.6 | - | 당위 서술 반복. |
| `ko.hedging.importance-sentence` | ko | 군더더기·유보 | C | 0.5 | - | '~하는 것이 중요하다' 결론. |
| `ko.hedging.can-do` | ko | 군더더기·유보 | C | 0.4 | standard | '~하는 것이 가능하다'는 '~할 수 있다'로 충분하다. |
| `ko.hedging.nominal-verb` | ko | 군더더기·유보 | C | 0.4 | standard | 명사 + 만능 동사. 동사 하나로 줄인다. |
| `ko.trans.daehan` | ko | 번역투 | C | 0.25 | - | '~에 대해/대한' 번역투. |
| `ko.trans.isseo` | ko | 번역투 | C | 0.4 | - | '~에 있어서' 번역투. |
| `ko.trans.euihae` | ko | 번역투 | C | 0.3 | - | '~에 의해' 번역투. |
| `ko.trans.inhae` | ko | 번역투 | C | 0.3 | - | '~로 인해' 번역투. |
| `ko.trans.tonghae` | ko | 참고(점수 제외) | C | 0.0 | - | '~를 통해'. 사람 글에서 오히려 더 많이 나와 점수에 넣지 않는다. |
| `ko.trans.geosida` | ko | 참고(점수 제외) | C | 0.0 | - | '~것이다'. 사람 글에서 오히려 더 많이 나와 점수에 넣지 않는다. |
| `ko.trans.double-passive-doe` | ko | 번역투 | C | 0.4 | standard | '되어지다'. 비문으로 단정하지는 않지만 '되다'가 읽기 쉽다. |
| `ko.trans.double-passive` | ko | 번역투 | C | 0.4 | standard | '-어지다'가 겹친 피동. 비문으로 단정하지는 않지만 단순형이 읽기 쉽다. |
| `ko.trans.such-as` | ko | 번역투 | C | 0.25 | - | '~와 같은' (such as) 번역투. |
| `ko.trans.in-order` | ko | 번역투 | C | 0.3 | - | '~하기 위해서는', '~하는 데 있어' 번역투. |
| `ko.trans.demonstrative` | ko | 참고(점수 제외) | C | 0.0 | - | '이러한' 지시어 반복. 참고용이다. |
| `ko.trans.gajigo` | ko | 번역투 | C | 0.3 | - | '가지고 있다' 번역투. |
| `ko.trans.one-of` | ko | 번역투 | C | 0.3 | - | '~중 하나' 번역투. |
| `ko.trans.case` | ko | 번역투 | C | 0.2 | - | '~의 경우' 반복. |
| `ko.trans.jeok` | ko | 번역투 | C | 0.12 | - | '~적' 체인. |
| `ko.trans.jaeda` | ko | 번역투 | B | 0.7 | standard | '재다': 물리적 길이가 아닌 추상적 격차·비용·오류율·수치를 '재다'로 표현한 번역투. |
| `ko.trans.jeonpa` | ko | 번역투 | B | 0.6 | standard | '전파하다/전파되다': 확산·전달·공유를 기계적으로 '전파(propagate/disseminate)'로 쓴 번역투. |
| `ko.trans.jadong` | ko | 번역투 | B | 0.5 | standard | '자동으로': '스스로'나 '알아서'로 충분한 자리에 'automatically'를 직역한 표현. |
| `ko.vocab.sino-b` | ko | 과다 어휘 | B | 0.5 | - | 한자어 학술 동사. 2018→2026년 논문 초록에서 급증한 계열(arXiv 2609.07447). |
| `ko.vocab.sino-c` | ko | 과다 어휘 | C | 0.4 | - | 한자어 동사 묶음. |
| `ko.vocab.eval-b` | ko | 과다 어휘 | B | 0.7 | - | 평가 형용사. 숫자와 비교 대상 없이 칭찬만 한다. |
| `ko.vocab.eval-c` | ko | 과다 어휘 | C | 0.4 | - | 평가 형용사. |
| `ko.vocab.jjak` | ko | 과다 어휘 | B | 0.7 | standard | '짝'/'짝짓다': 둘의 대응이나 연계를 인위적으로 '짝'으로 표현한 번역투. |
| `ko.vocab.ssang` | ko | 과다 어휘 | B | 0.6 | standard | '쌍을 이루다': 둘의 병렬·대응을 상투적으로 표현한 어구. |
| `ko.vocab.sinho` | ko | 과다 어휘 | B | 0.6 | standard | '신호': 징후·단서·특징을 '신호(signal)'로 직역한 번역투. |
| `ko.vocab.bakda` | ko | 과다 어휘 | B | 0.6 | standard | '박다/박아 넣다': 거칠거나 비격식적인 삽입·하드코딩 표현 상투구. |
| `any.markup.oaicite` | any | 누출된 마크업 | A | 1.0 | safe | 누출된 인용 토큰. |
| `any.markup.turn-ref` | any | 누출된 마크업 | A | 1.0 | safe | 누출된 도구 참조 토큰. |
| `any.markup.private-use` | any | 누출된 마크업 | A | 1.0 | safe | 비공개 영역 인용 표지. |
| `any.placeholder.lorem` | any | 빈 자리표시자 | A | 0.8 | - | 더미 문구. |
| `any.format.emoji-lead` | any | 서식 신호 | B | 0.5 | standard | 줄머리 이모지(불릿, 제목). |
| `any.format.emoji-any` | any | 서식 신호 | C | 0.3 | strong | 본문 이모지. |
| `any.format.bold-lead` | any | 서식 신호 | B | 0.5 | strong | 불릿마다 굵은 라벨로 시작한다. |
| `any.format.bold-line` | any | 서식 신호 | C | 0.3 | - | 굵은 글씨만 있는 줄이 제목 구실을 한다. |
| `any.format.hashtags` | any | 서식 신호 | C | 0.3 | - | 해시태그 묶음. |
| `any.format.heading-title-case` | any | 서식 신호 | C | 0.3 | - | 제목이 모두 대문자로 시작한다(제목식 대문자). |
| `any.hygiene.nbsp` | any | 보이지 않는 문자 | B | 0.0 | safe | 줄바꿈 없는 공백 문자가 섞였다. |
| `any.hygiene.zero-width` | any | 보이지 않는 문자 | B | 0.0 | safe | 보이지 않는 문자(너비 0, 연자 부호)가 섞였다. |
