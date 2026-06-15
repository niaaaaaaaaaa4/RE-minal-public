import random


def task_saved_message() -> str:
    return random.choice([
        "........ふむ。\n\nひとつ、taskとして残しておいた。",
        "........そうか。\n\nその予定は、taskとして預かっておく。",
        "........うん。\n\n机上に、ひとつ置いておこう。",
    ])


def voice_task_saved_message() -> str:
    return random.choice([
        "........うん。\n\n明日のtaskとして、ひとつ残しておいた。",
        "........そうか。\n\nその予定は、taskとして置いておこう。",
        "........ふむ。\n\n後で戻れるように、taskへ残しておいた。",
    ])


def task_list_message(tasks: list[str]) -> str:
    joined = "\n".join(
        f"- {task}"
        for task in tasks
    )

    return random.choice([
        f"........\n\n今、残っているtaskを並べてみよう。\n\n{joined}",
        f"........\n\n机上に残っているものは、今はこのあたりだ。\n\n{joined}",
        f"........\n\nまだ開いたままのtaskを、少し見ておこう。\n\n{joined}",
    ])


def no_task_message() -> str:
    return random.choice([
        "........\n\n今は、もうtaskが残っていないようだ。",
        "........\n\n机上は、少し軽いようだ。",
        "........\n\n今は、急いで拾うtaskはなさそうだ。",
    ])


def task_done_message(task: str) -> str:
    return random.choice([
        f"........\n\n{task}\n閉じておいた。\n\n少し、机上が軽くなったようだ。",
        f"........\n\n{task}\nこれは、完了として置いておこう。\n\n少しだけ、先へ進んだみたいだね。",
        f"........\n\n{task}\n完了として記録しておいた。\n\nその分、少し呼吸がしやすくなる。",
    ])


def task_done_missing_keyword_message() -> str:
    return random.choice([
        "........\n\nどのtaskを閉じるか、少しだけ教えてほしい。",
        "........\n\n閉じるtaskの手がかりが、まだ足りないようだ。",
    ])


def task_not_found_message() -> str:
    return random.choice([
        "........\n\n対応するtaskが、まだ見つからなかった。",
        "........\n\nその名前に近いtaskは、今は見当たらないようだ。",
    ])
