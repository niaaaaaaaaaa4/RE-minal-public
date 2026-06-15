from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

TASK_DIR = BASE_DIR / "memory" / "tasks"


def load_recent_tasks(limit: int = 5):

    if not TASK_DIR.exists():
        return []

    files = sorted(
        TASK_DIR.glob("*.md"),
        reverse=True
    )

    collected = []

    for file_path in files:

        try:

            text = file_path.read_text(
                encoding="utf-8"
            )

        except Exception:
            continue

        lines = text.splitlines()

        for line in lines:

            stripped = line.strip()

            if stripped.startswith("- [ ]"):

                task = (
                    stripped
                    .replace("- [ ]", "")
                    .strip()
                )

                if task not in collected:
                    collected.append(task)

        if len(collected) >= limit:
            break

    return collected[:limit]