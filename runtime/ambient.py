# =========================================
# RE:minal Ambient Layer
# runtime/ambient.py
# =========================================

import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

AMBIENT_FILE = (
    BASE_DIR / "data" / "ambient_lines.md"
)

def load_ambient_lines():

    if not AMBIENT_FILE.exists():
        return []

    text = AMBIENT_FILE.read_text(
        encoding="utf-8"
    )

    lines = [
        line.strip()
        for line in text.split("\n\n")
        if line.strip()
    ]

    return lines

AMBIENT_LINES = load_ambient_lines()

_last_line = None


def get_ambient_line():

    global _last_line

    available = [
        line for line in AMBIENT_LINES
        if line != _last_line
    ]

    if not available:
        return "........静かな時間だね。"

    selected = random.choice(available)

    _last_line = selected

    return selected