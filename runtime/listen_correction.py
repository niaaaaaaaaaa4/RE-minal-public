# runtime/listen_correction.py

from __future__ import annotations


CORRECTION_RULES = {
    "聖夜": "セイア",
    "セイヤ": "セイア",
    "せいや": "セイア",
    "せいあ": "セイア",

    "レミナル": "RE:minal",
    "れみなる": "RE:minal",
    "リミナル": "RE:minal",

    "ミカちゃん": "ミカ",
    "ナギサさん": "ナギサ",
}


def correct_listen_text(text: str) -> str:
    corrected = text.strip()

    for before, after in CORRECTION_RULES.items():
        corrected = corrected.replace(before, after)

    return corrected