import re

def remove_existing_opening(text: str) -> str:
    """
    AI返答の冒頭にある pause / 相槌を削り、
    opening.py 側の入り口と二重にならないようにする。
    """

    opening_patterns = [
        ".........",
        "........",
        "......",
        "……",
        "うん。",
        "ああ。",
        "なるほど。",
        "そうか。",
    ]

    cleaned = text.strip()

    changed = True

    while changed:
        changed = False

        for pattern in opening_patterns:
            if cleaned.startswith(pattern):
                cleaned = cleaned[len(pattern):].strip()
                changed = True

    return cleaned

def soften_certainty(text: str) -> str:
    """
    強すぎる断定を少し減衰させる。
    """

    replacements = {
        "です。": "と思う。",
        "でしょう。": "かもしれない。",
        "できます。": "できると思う。",
        "必要です。": "必要かもしれない。",
        "大丈夫です。": "大丈夫だと思う。",
    }

    for src, dst in replacements.items():
        text = text.replace(src, dst)

    return text


def reduce_explanation_density(text: str) -> str:
    """
    説明が長すぎる時、
    少し呼吸を増やす。
    """

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text



def apply_seia_modulation(text: str) -> str:
    """
    RE:minal modulation layer
    """

    text = remove_existing_opening(text)
    text = soften_certainty(text)
    text = reduce_explanation_density(text)

    return text

