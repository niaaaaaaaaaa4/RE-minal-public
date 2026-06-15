# =========================================
# RE:minal Fragment Memory
# runtime/memory.py
# =========================================

from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

MEMORY_DIR = BASE_DIR / "memory" / "fragments"
MEMORY_DIR.mkdir(parents=True, exist_ok=True)


def build_fragment_block(
    user_text: str,
    ai_text: str,
    fragment_type: str | None = None,
) -> str:

    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S")

    type_line = ""

    if fragment_type:
        type_line = f"\ntype: {fragment_type}\n"

    return f"""

## {timestamp}{type_line}
### User

{user_text}

### RE:minal

{ai_text}

"""


def save_fragment(
    user_text: str,
    ai_text: str,
):

    now = datetime.now()
    filename = now.strftime("%Y-%m-%d.md")
    file_path = MEMORY_DIR / filename

    fragment = build_fragment_block(
        user_text=user_text,
        ai_text=ai_text,
    )

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(fragment)


def save_typed_fragment(
    user_text: str,
    ai_text: str,
    fragment_type: str = "unresolved",
):
    """
    fragment を従来の一覧にも残しつつ、
    種類別フォルダにも保存する。
    """

    now = datetime.now()
    filename = now.strftime("%Y-%m-%d.md")

    base_path = MEMORY_DIR / filename

    typed_dir = MEMORY_DIR / fragment_type
    typed_dir.mkdir(parents=True, exist_ok=True)
    typed_path = typed_dir / filename

    fragment = build_fragment_block(
        user_text=user_text,
        ai_text=ai_text,
        fragment_type=fragment_type,
    )

    with open(base_path, "a", encoding="utf-8") as f:
        f.write(fragment)

    with open(typed_path, "a", encoding="utf-8") as f:
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

        except Exception:
            pass

    return "\n\n".join(collected)
