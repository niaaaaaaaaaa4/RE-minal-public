from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

DEV_DIR = BASE_DIR / "memory" / "reminal_dev"
DEV_DIR.mkdir(parents=True, exist_ok=True)


def save_reminal_dev(text: str):

    now = datetime.now()
    filename = now.strftime("%Y-%m-%d.md")
    path = DEV_DIR / filename
    timestamp = now.strftime("%H:%M:%S")

    block = f"""

## {timestamp}

{text}

"""

    with open(path, "a", encoding="utf-8") as f:
        f.write(block)