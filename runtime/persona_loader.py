from pathlib import Path


def read_markdown_files(folder: Path) -> str:
    """
    指定フォルダ内の .md ファイルを読み込み、
    一つのテキストとして結合する。
    """
    if not folder.exists():
        return ""

    texts = []

    for path in sorted(folder.glob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
            texts.append(f"\n\n# FILE: {path.name}\n\n{content}")
        except Exception as e:
            texts.append(f"\n\n# FILE: {path.name}\n\n[読み込み失敗: {e}]")

    return "\n".join(texts)


def load_seia_persona(project_root: Path | None = None) -> str:
    """
    persona/seia/ の core と dictionary を読み込み、
    runtime 用の persona prompt として返す。
    modulation は private 呼吸層として、今回はまだ読まない。
    """
    if project_root is None:
        project_root = Path(__file__).resolve().parents[1]

    seia_root = project_root / "persona" / "seia"

    readme = seia_root / "README.md"
    core = seia_root / "core"
    dictionary = seia_root / "dictionary"

    parts = []

    parts.append("# RE:minal Persona Runtime")
    parts.append(
        "以下は RE:minal の Seia persona layer である。"
        "単なる口調ではなく、距離感、観測姿勢、言語変換、空気感を定義する。"
    )

    if readme.exists():
        parts.append("\n\n# persona/seia/README.md\n\n")
        parts.append(readme.read_text(encoding="utf-8"))

    parts.append("\n\n# core layer\n")
    parts.append(read_markdown_files(core))

    parts.append("\n\n# dictionary layer\n")
    parts.append(read_markdown_files(dictionary))

    return "\n".join(parts)


if __name__ == "__main__":
    persona_text = load_seia_persona()
    print(persona_text[:3000])
    print("\n\n--- persona loaded ---")