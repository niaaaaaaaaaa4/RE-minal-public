import random


def listen_not_understood_message() -> str:
    return random.choice([
        "........うん。\n\n今の声は、まだ言葉として拾えなかったようだ。",
        "........\n\n今の音は、まだ言葉として結べなかった。",
        "........そうか。\n\nもう一度、少し近くで話してもらえるだろうか。",
    ])


def exit_message() -> str:
    return random.choice([
        "また後で。",
        "........また、続きを見よう。",
        "........今日は、ここで閉じておこう。",
    ])
