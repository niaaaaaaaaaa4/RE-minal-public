import random


def startup_recall_voice_message() -> str:
    return random.choice([
        "........少し、先刻の続きを思い出している。",
        "........前に置いたものが、少し残っているようだ。",
        "........机上に残っていたものを、少し見ていた。",
    ])


def continue_empty_message() -> str:
    return random.choice([
        "........\n\n今は、続きとして残っているものは少ないようだ。",
        "........\n\n今は、強く引き戻す続きを見つけていない。",
    ])


def continue_task_message(task: str) -> str:
    return random.choice([
        f"........\n\n少し、昨日の続きを思い出していた。\n\n{task}\nまだ机上に残っているみたいだね。",
        f"........\n\n前に止まっていたものなら、\n{task}\nこのあたりが近いようだ。",
        f"........\n\n続きを探すなら、\n{task}\nここへ戻るのが自然だと思う。",
    ])


def morning_continue_message(task: str) -> str:
    return random.choice([
        f"今日は、\n{task}\nあたりから始まりそうだ。",
        f"朝の入口としては、\n{task}\nこのあたりが机上に残っている。",
        f"今日の最初の手がかりは、\n{task}\nかもしれない。",
    ])


def today_no_file_message() -> str:
    return random.choice([
        "........\n\n今日は、まだtaskが置かれていないようだ。",
        "........\n\n今日の机上には、まだtaskの紙片が少ない。",
    ])


def today_empty_message() -> str:
    return random.choice([
        "........\n\n今日は、残っているtaskが少ないみたいだね。",
        "........\n\n今日のtaskは、今はだいぶ軽いようだ。",
    ])


def today_task_list_message(tasks: list[str]) -> str:
    joined = "\n".join(
        f"- {task}"
        for task in tasks
    )

    return random.choice([
        f"........\n\n今日、机上に置かれているtaskを並べてみる。\n\n{joined}",
        f"........\n\n今日残っているものは、このあたりだ。\n\n{joined}",
        f"........\n\n今日のtaskを、少し見ておこう。\n\n{joined}",
    ])
