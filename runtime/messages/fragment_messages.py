import random


def fragment_saved_message() -> str:
    return random.choice([
        "........うん。\n\nその断片は、fragmentとして残しておいた。",
        "........そうか。\n\n今の断片は、静かに置いておこう。",
        "........ふむ。\n\nその感覚は、fragmentとして預かっておく。",
    ])


def fragment_extracted_message() -> str:
    return random.choice([
        "........そうか。\n\n今の感覚は、fragmentとして置いておこう。",
        "........うん。\n\nその気配は、fragmentとして残しておく。",
        "........ふむ。\n\nこれは、今の状態として置いておいた方がよさそうだ。",
    ])
