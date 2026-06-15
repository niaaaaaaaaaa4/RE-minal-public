# =========================================
# RE:minal Fragment Memory
# runtime/memory.py
# =========================================

from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

MEMORY_DIR = BASE_DIR / "memory" / "fragments"
MEMORY_DIR.mkdir(parents=True, exist_ok=True)


def save_fragment(user_text: str, ai_text: str):

    now = datetime.now()

    filename = now.strftime("%Y-%m-%d.md")

    file_path = MEMORY_DIR / filename

    timestamp = now.strftime("%H:%M:%S")

    fragment = f"""

## {timestamp}

### User

{user_text}

### RE:minal

{ai_text}

"""

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(fragment)


def load_recent_fragments(limit: int = 3):

    files = sorted(
        MEMORY_DIR.glob("*.md"),
        reverse=True
    )

    collected = []

    for file_path in files[:limit]:

        try:
            text = file_path.read_text(
                encoding="utf-8"
            )

            collected.append(text)

        except:
            pass

    return "\n\n".join(collected)