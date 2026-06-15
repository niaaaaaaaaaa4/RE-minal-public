from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

TASK_DIR = BASE_DIR / "memory" / "tasks"
DONE_DIR = BASE_DIR / "memory" / "done"


DONE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def complete_task(keyword: str):

    files = sorted(
        TASK_DIR.glob("*.md"),
        reverse=True
    )

    for file_path in files:

        text = file_path.read_text(
            encoding="utf-8"
        )

        lines = text.splitlines()

        updated = []

        found = None

        for line in lines:

            if (
                line.strip().startswith("- [ ]")
                and keyword in line
                and found is None
            ):

                found = (
                    line
                    .replace("- [ ]", "")
                    .strip()
                )

                updated.append(
                    line.replace(
                        "- [ ]",
                        "- [x]"
                    )
                )

            else:
                updated.append(line)

        if found:

            file_path.write_text(
                "\n".join(updated),
                encoding="utf-8"
            )

            today = datetime.now().strftime(
                "%Y-%m-%d.md"
            )

            done_path = DONE_DIR / today

            with open(
                done_path,
                "a",
                encoding="utf-8"
            ) as f:

                f.write(
                    f"- {found}\n"
                )

            return found

    return None