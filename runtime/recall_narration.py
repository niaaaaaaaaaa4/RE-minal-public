import random


def clean_memory_text(text: str) -> str:

    cleaned = text.strip()

    cleaned = (
        cleaned
        .replace("- [ ]", "")
        .replace("source: terminal", "")
        .replace("source: voice", "")
        .strip()
    )

    while cleaned.endswith(("。", "、", ".", "，")):
        cleaned = cleaned[:-1].strip()

    return cleaned


def ending(kind: str) -> str:

    endings = {
        "fragment": [
            "残っているようだ。",
            "少し残っているみたいだね。",
            "気配がある。",
            "まだ机上に置かれているようだ。",
        ],
        "task": [
            "予定として残っているようだ。",
            "まだ机上にあるみたいだね。",
            "少し気に掛けているようだ。",
        ],
        "dev": [
            "と考えていたようだ。",
            "という構想が残っているみたいだね。",
            "という断片が、まだ机上にあるようだ。",
        ],
    }

    return random.choice(endings[kind])


def narrate_fragment(text: str) -> str:

    cleaned = clean_memory_text(text)

    if "眠" in cleaned:
        return "少し、眠気が残っているようだ。"

    if "疲" in cleaned:
        return "疲れの気配が、少し残っているようだ。"

    if "声" in cleaned:
        return "声の距離感が、少し見えてきたみたいだね。"

    fragment_endings = [
        f"{cleaned}、という断片が残っているようだ。",
        f"{cleaned}、という感覚が少し残っているみたいだね。",
        f"{cleaned}、という記録が机上に置かれているようだ。",
    ]

    return random.choice(fragment_endings)


def narrate_task(text: str) -> str:

    cleaned = clean_memory_text(text)

    cleaned = cleaned.replace("進めたい", "進める")
    cleaned = cleaned.replace("したい", "する")
    cleaned = cleaned.replace("やりたい", "やる")

    patterns = [
        f"{cleaned}予定がある様だ。",
        f"{cleaned}ことを、少し気に掛けているみたいだね。",
        f"{cleaned}ための準備が、まだ机上に残っているようだ。",
    ]

    return random.choice(patterns)


def narrate_dev(text: str) -> str:

    cleaned = clean_memory_text(text)

    return f"RE:minalについて、{cleaned}{ending('dev')}"


def build_narration_block(
    fragments,
    tasks,
    devs,
):

    lines = []

    for text in fragments:
        lines.append(
            narrate_fragment(text)
        )

    for text in tasks:
        lines.append(
            narrate_task(text)
        )

    for text in devs:
        lines.append(
            narrate_dev(text)
        )

    random.shuffle(lines)

    return "\n".join(
        f"- {line}"
        for line in lines[:5]
    )