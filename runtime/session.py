# =========================================
# RE:minal Session Layer
# runtime/session.py
# =========================================

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SESSION_DIR = (
    BASE_DIR / "runtime" / "session"
)

SESSION_DIR.mkdir(
    parents=True,
    exist_ok=True
)

SESSION_FILE = (
    SESSION_DIR / "conversation.json"
)

MAX_HISTORY = 6


def save_conversation_history(
    history
):

    trimmed = history[-MAX_HISTORY:]

    with open(
        SESSION_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            trimmed,
            f,
            ensure_ascii=False,
            indent=2
        )


def load_conversation_history():

    if not SESSION_FILE.exists():
        return []

    try:

        with open(
            SESSION_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return []