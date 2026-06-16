from messages.banks.endings import (
    TASK_DONE,
    TASK_KEYWORD_MISSING,
    TASK_NOT_FOUND,
    TASK_SAVED,
)
from messages.banks.observations import TASK_LIST_INTRO
from messages.banks.pauses import QUIET_PAUSE, SOFT_ACK


def task_saved_message() -> str:
    return f"{SOFT_ACK}\n\n{TASK_SAVED}"


def task_list_message(tasks: list[str]) -> str:
    joined = "\n".join(
        f"- {task}"
        for task in tasks
    )

    return (
        f"{QUIET_PAUSE}\n\n"
        f"{TASK_LIST_INTRO}\n\n"
        f"{joined}"
    )


def no_task_message() -> str:
    return f"{QUIET_PAUSE}\n\n今は、残っている task はないようだ。"


def task_done_message(task: str) -> str:
    return (
        f"{SOFT_ACK}\n\n"
        f"{task}\n"
        f"{TASK_DONE}"
    )


def task_done_keyword_missing_message() -> str:
    return f"{QUIET_PAUSE}\n\n{TASK_KEYWORD_MISSING}"


def task_not_found_message() -> str:
    return f"{QUIET_PAUSE}\n\n{TASK_NOT_FOUND}"
