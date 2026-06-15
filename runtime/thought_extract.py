# runtime/thought_extract.py

from __future__ import annotations


IDEA_PATTERNS = [
    "かも",
    "いいかも",
    "気がする",
    "案",
    "アイデア",
    "こうしたい",
]

FRAGMENT_PATTERNS = [
    "疲れた",
    "眠い",
    "不安",
    "少し重い",
    "落ち着かない",
]

DEV_IDEA_PATTERNS = [
    "RE:minal",
    "りみなる",
    "リミナル",
    "このAI",
    "この子",
    "この仕組み",
    "開発",
    "機能",
    "実装",
    "追加したい",
    "できるようにしたい",
]


def detect_idea(text: str) -> str | None:

    normalized = text.strip()

    if not normalized:
        return None

    for pattern in IDEA_PATTERNS:
        if pattern in normalized:
            return normalized

    return None


def detect_fragment(text: str) -> str | None:

    normalized = text.strip()

    if not normalized:
        return None

    for pattern in FRAGMENT_PATTERNS:
        if pattern in normalized:
            return normalized

    return None

def detect_reminal_dev(text: str) -> str | None:

    normalized = text.strip()

    for pattern in DEV_IDEA_PATTERNS:
        if pattern in normalized:
            return normalized

    return None
