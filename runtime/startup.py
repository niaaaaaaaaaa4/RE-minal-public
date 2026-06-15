# =========================================
# RE:minal Startup Layer
# runtime/startup.py
# =========================================

import random
from pathlib import Path
from voice import speak

BASE_DIR = Path(__file__).resolve().parent.parent

STARTUP_FILE = (
    BASE_DIR / "data" / "startup_lines.md"
)

def load_startup_lines():

    if not STARTUP_FILE.exists():
        return []

    text = STARTUP_FILE.read_text(
        encoding="utf-8"
    )

    return [
        line.strip()
        for line in text.split("\n\n")
        if line.strip()
    ]


STARTUP_LINES = load_startup_lines()


def speak_startup_line():

    opening_text = get_startup_line()

    if not opening_text:
        return

    speak(opening_text)
    

def get_startup_line():

    lines = load_startup_lines()

    if not lines:
        return "........おや。"

    return random.choice(lines)