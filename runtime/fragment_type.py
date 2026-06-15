from __future__ import annotations


def detect_fragment_type(text: str) -> str:
    """
    音声から拾った fragment を、軽い辞書で分類する。
    ここでは厳密さよりも、後から育てやすいことを優先する。
    """

    normalized = text.strip()

    fatigue_words = [
        "眠い", "眠たい", "眠気", "疲れ", "疲れた", "だるい",
        "重い", "しんどい", "休みたい",
    ]

    anxiety_words = [
        "不安", "怖い", "心配", "落ち着かない", "焦る",
        "ざわざわ", "罪悪感",
    ]

    continuation_words = [
        "続き", "続けたい", "まだやりたい", "もう少し",
        "進めたい", "戻りたい",
    ]

    atmosphere_words = [
        "空気", "雰囲気", "静か", "重い", "軽い",
        "距離感", "声",
    ]

    observation_words = [
        "気づいた", "見えてきた", "分かった", "わかった",
        "よさそう", "良さそう", "いい感じ", "気がする",
    ]

    for word in fatigue_words:
        if word in normalized:
            return "fatigue"

    for word in anxiety_words:
        if word in normalized:
            return "anxiety"

    for word in continuation_words:
        if word in normalized:
            return "continuation"

    for word in atmosphere_words:
        if word in normalized:
            return "atmosphere"

    for word in observation_words:
        if word in normalized:
            return "observation"

    return "unresolved"
