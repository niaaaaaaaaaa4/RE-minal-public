def task_saved_message() -> str:
    return "........うん。\n\n明日の task として、ひとつ残しておいた。"


def task_list_message(tasks: list[str]) -> str:
    joined = "\n".join(
        f"- {task}"
        for task in tasks
    )

    return (
        "........\n\n"
        "今、机上に残っている task は、\n\n"
        f"{joined}"
    )


def no_task_message() -> str:
    return "........\n\n今は、残っている task はないようだ。"


def task_done_message(task: str) -> str:
    return (
        "........うん。\n\n"
        f"{task}\n"
        "完了として残しておいた。"
    )


def task_done_keyword_missing_message() -> str:
    return "........\n\n完了した task の言葉を、少し添えてほしい。"


def task_not_found_message() -> str:
    return "........\n\nその言葉に合う task は、見つからなかった。"
