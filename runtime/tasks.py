from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Task:
    text: str
    status: str = "open"
    source: str = "terminal"


class TaskStore:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, task: Task) -> Path:
        now = datetime.now()
        path = self.root / "tasks.md"
        line = f"- [ ] {task.text.strip()}  <!-- {now.isoformat(timespec='seconds')} / {task.source} -->\n"
        with path.open("a", encoding="utf-8") as f:
            f.write(line)
        return path
