"""시험이 엔진을 불러오는 경로. 엔진은 skills 폴더 안에 있다."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "ai-smell-polish" / "scripts"
LAUNCHER = SCRIPTS / "ai-smell"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
