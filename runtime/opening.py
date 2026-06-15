# =========================================
# RE:minal Opening Layer
# runtime/opening.py
# =========================================

import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

OPENING_FILE = (
    BASE_DIR / "data" / "openings.md"
)

def load_openings():

    if not OPENING_FILE.exists():
        return []

    text = OPENING_FILE.read_text(
        encoding="utf-8"
    )

    return [
        line.strip()
        for line in text.split("\n\n")
        if line.strip()
    ]

OPENINGS = load_openings()

_last_opening = None


def get_opening():

    global _last_opening

    available = [
        o for o in OPENINGS
        if o != _last_opening
    ]

    if not available:
        return "........"

    selected = random.choice(available)

    _last_opening = selected

    return selected