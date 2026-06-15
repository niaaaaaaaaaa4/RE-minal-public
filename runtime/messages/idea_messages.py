import random


def idea_saved_message() -> str:
    return random.choice([
        "........成程。\n\nその感覚はideaとして、残しておこう。",
        "........うん。\n\nその発想は、ideaとして置いておく。",
        "........ふむ。\n\nまだ形になる前のものとして、残しておこう。",
    ])
