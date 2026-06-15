from pathlib import Path
from recall_narration import build_narration_block

BASE_DIR = Path(__file__).resolve().parent.parent

MEMORY_DIR = BASE_DIR / "memory"


def load_recent_lines(folder_name: str, limit: int = 3):

    target_dir = MEMORY_DIR / folder_name

    if not target_dir.exists():
        return []

    files = sorted(
        target_dir.glob("*.md"),
        reverse=True
    )

    collected = []

    for file_path in files:

        try:

            text = file_path.read_text(
                encoding="utf-8"
            ).strip()

            if not text:
                continue

            lines = [
                line.strip()
                for line in text.splitlines()
                if line.strip()
            ]

            content_lines = []

            for line in lines:

                if line.startswith("##"):
                    continue

                stripped = line.strip()

                if len(stripped) <= 6:
                    continue

                if stripped.startswith("source:"):
                    continue

                if stripped in [
                    "........",
                    "........うん。",
                    "うん。",
                    "........そうか。",
                    "そうか。",
                ]:
                    continue

                content_lines.append(stripped)

            collected.extend(content_lines)

        except Exception:
            continue

        if len(collected) >= limit:
            break

    return collected[:limit]


def build_recall_text():

    fragments = load_recent_lines(
        "fragments",
        limit=2
    )

    tasks = load_recent_lines(
        "tasks",
        limit=2
    )

    dev = load_recent_lines(
        "reminal_dev",
        limit=2
    )

    sections = []

    return build_narration_block(
        fragments,
        tasks,
        dev,
    )