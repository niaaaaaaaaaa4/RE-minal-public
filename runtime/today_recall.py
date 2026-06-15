from pathlib import Path
from datetime import datetime

from messages.recall_messages import (
    today_no_file_message,
    today_empty_message,
    today_task_list_message,
)


BASE_DIR = Path(__file__).resolve().parent.parent

TASK_DIR = BASE_DIR / "memory" / "tasks"


def build_today_text():

    today = datetime.now().strftime(
        "%Y-%m-%d.md"
    )

    path = TASK_DIR / today

    if not path.exists():
        return today_no_file_message()

    text = path.read_text(
        encoding="utf-8"
    )

    tasks = []

    for line in text.splitlines():

        stripped = line.strip()

        if stripped.startswith("- [ ]"):

            tasks.append(
                stripped.replace(
                    "- [ ]",
                    ""
                ).strip()
            )

    if not tasks:
        return today_empty_message()

    return today_task_list_message(tasks)
