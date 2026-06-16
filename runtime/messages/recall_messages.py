import random

from messages.banks.observations import (
    CONTINUE_EMPTY,
    CONTINUE_TASK_ENDINGS,
    CONTINUE_TASK_OPENINGS,
    MORNING_EMPTY,
    MORNING_TASK_PATTERNS,
    TODAY_EMPTY,
    TODAY_LIST_INTRO,
    TODAY_NO_FILE,
)
from messages.banks.pauses import QUIET_PAUSE


def continue_task_message(task: str) -> str:
    index = random.randrange(len(CONTINUE_TASK_OPENINGS))

    return (
        f"{QUIET_PAUSE}\n\n"
        f"{CONTINUE_TASK_OPENINGS[index]}\n\n"
        f"{task}\n"
        f"{CONTINUE_TASK_ENDINGS[index]}"
    )


def continue_empty_message() -> str:
    return f"{QUIET_PAUSE}\n\n{random.choice(CONTINUE_EMPTY)}"


def morning_task_message(task: str) -> str:
    before, after = random.choice(MORNING_TASK_PATTERNS)

    if not before:
        return (
            f"{task}\n"
            f"{after}"
        )

    return (
        f"{before}\n"
        f"{task}\n"
        f"{after}"
    )


def morning_empty_message() -> str:
    return random.choice(MORNING_EMPTY)


# Backward-compatible aliases.
# 以前の関数名が残っていても、同じ棚へ接続できるようにしておく。
def continue_message(task: str) -> str:
    return continue_task_message(task)


def no_continue_message() -> str:
    return continue_empty_message()

def today_no_file_message() -> str:
    return f"{QUIET_PAUSE}\n\n{TODAY_NO_FILE}"


def today_empty_message() -> str:
    return f"{QUIET_PAUSE}\n\n{TODAY_EMPTY}"


def today_task_list_message(tasks: list[str]) -> str:
    joined = "\n".join(
        f"- {task}"
        for task in tasks
    )

    return (
        f"{QUIET_PAUSE}\n\n"
        f"{TODAY_LIST_INTRO}\n\n"
        f"{joined}"
    )
