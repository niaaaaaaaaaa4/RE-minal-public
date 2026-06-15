# runtime/task_extract.py

from __future__ import annotations


TASK_PATTERNS = [
    "したい",
    "やりたい",
    "進めたい",
    "進める",
    "やる",
    "やっておく",
    "確認する",
    "まとめる",
    "作る",
    "調べる",
    "見る",
]


def detect_task_text(text: str) -> str | None:

    normalized = text.strip()

    if not normalized:
        return None

    for pattern in TASK_PATTERNS:
        if pattern in normalized:
            return normalized

    return None
