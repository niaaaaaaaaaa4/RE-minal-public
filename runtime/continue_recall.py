from task_recall import load_recent_tasks

from messages.recall_messages import (
    continue_task_message,
    continue_empty_message,
    morning_task_message,
)


def build_continue_text():

    tasks = load_recent_tasks(limit=1)

    if not tasks:
        return continue_empty_message()

    return continue_task_message(
        tasks[0]
    )


def build_morning_continue():

    tasks = load_recent_tasks(limit=1)

    if not tasks:
        return ""

    return morning_task_message(
        tasks[0]
    )
