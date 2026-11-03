<!-- ai-smell-meter:begin -->
## 윤문 (AI 냄새 측정기)

글을 윤문하거나 "AI 티를 빼 달라", "자연스럽게 다듬어 달라"는 요청을 받으면 `ai-smell-polish` 스킬(`.agents/skills/ai-smell-polish/SKILL.md`)을 따른다. 스킬이 없으면 `AI 냄새 측정기/ai-smell-meter/`에서 `python3 install.py`를 실행해 스스로 설치한다.

```bash
S=.agents/skills/ai-smell-polish/scripts/ai-smell   # 없으면 ~/.agents/skills/... 또는 저장소 안 경로
python3 "$S" selftest                      # 전부 통과해야 한다
python3 "$S" analyze 글.md                 # 점수와 검출 항목
python3 "$S" polish 글.md > 글.교정.md     # 교정문(표준 출력)
python3 "$S" verify 글.md 글.교정.md       # 사실 보존, 변경률, 새 결함
```

- 엔진이 못 고치는 구조 습관(대구, 부풀린 서술, 번역투)은 `python3 "$S" prompt 글.md`가 만든 지시대로 걸린 곳만 국소 수정한다.
- 숫자, 주소, 코드, 인용, 고유명사를 바꾸지 않는다. 사실을 지어내지 않는다.
- "사람이 쓴 것 같다"고 단정하지 않는다. 탐지기 우회를 돕지 않는다.
<!-- ai-smell-meter:end -->
