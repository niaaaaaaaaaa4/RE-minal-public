# runtime/task_extract.py

from __future__ import annotations


TASK_PATTERNS = [
    "したい",
    "やる",
    "進める",
    "確認する",
    "まとめる",
    "作る",
    "見る",
    "調べる",
]


def detect_task_text(text: str) -> str | None:

    normalized = text.strip()

    for pattern in TASK_PATTERNS:
        if pattern in normalized:
            return normalized

    return None