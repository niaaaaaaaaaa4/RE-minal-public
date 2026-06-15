from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

TASK_DIR = BASE_DIR / "memory" / "tasks"
TASK_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class Task:
    text: str
    status: str = "open"
    source: str = "terminal"


class TaskStore:

    def save(self, task: Task) -> Path:

        now = datetime.now()

        filename = now.strftime("%Y-%m-%d.md")

        path = TASK_DIR / filename

        timestamp = now.strftime("%H:%M:%S")

        block = f"""

## {timestamp}

- [ ] {task.text.strip()}
source: {task.source}

"""

        with path.open("a", encoding="utf-8") as f:
            f.write(block)

        return path