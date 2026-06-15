import random


def continue_task_message(task: str) -> str:
    return random.choice([
        (
            "........\n\n"
            "少し、昨日の続きを思い出していた。\n\n"
            f"{task}\n"
            "まだ机上に残っているみたいだね。"
        ),
        (
            "........\n\n"
            "先刻の続きを、少し見返していた。\n\n"
            f"{task}\n"
            "まだ灯りは残っているようだ。"
        ),
        (
            "........\n\n"
            "まだ、続きとして置かれているものがある。\n\n"
            f"{task}\n"
            "今日はこの辺りから始まりそうだ。"
        ),
    ])


def continue_empty_message() -> str:
    return random.choice([
        "........\n\n今は、続きとして残っているものは少ないようだ。",
        "........\n\n今日は、静かな状態から始まりそうだね。",
        "........\n\n今は、急いで拾う続きは少ないみたいだ。",
    ])


def morning_task_message(task: str) -> str:
    return random.choice([
        (
            "今日は、\n"
            f"{task}\n"
            "あたりから始まりそうだ。"
        ),
        (
            "朝の机上には、\n"
            f"{task}\n"
            "が、まだ残っているみたいだね。"
        ),
        (
            f"{task}\n"
            "その続きを、少し気に掛けているようだ。"
        ),
    ])


def morning_empty_message() -> str:
    return random.choice([
        "今日は、まだ急いで拾う続きを少ないようだ。",
        "朝の机上は、少し静かなようだ。",
        "今は、無理に続きを探さなくてもよさそうだ。",
    ])


# Backward-compatible aliases.
# 以前の関数名が残っていても、同じ棚へ接続できるようにしておく。
def continue_message(task: str) -> str:
    return continue_task_message(task)


def no_continue_message() -> str:
    return continue_empty_message()

def today_no_file_message() -> str:
    return "........\n\n今日は、まだtaskが置かれていないようだ。"


def today_empty_message() -> str:
    return "........\n\n今日のtaskは、今はだいぶ軽いようだ。"


def today_task_list_message(tasks: list[str]) -> str:
    joined = "\n".join(
        f"- {task}"
        for task in tasks
    )

    return (
        "........\n\n"
        "今日、机上に置かれているtaskを並べてみる。\n\n"
        f"{joined}"
    )