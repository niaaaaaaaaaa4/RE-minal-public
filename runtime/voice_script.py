# runtime/voice_script.py

from __future__ import annotations

import random


def random_space(
    min_count: int,
    max_count: int
) -> str:
    count = random.randint(
        min_count,
        max_count
    )

    return "　" * count


def build_seia_voice_text(text: str) -> str:
    """
    表示用テキストを、Edge TTS に渡す音声用テキストへ変換する。

    方針:
      - segment 分割しない
      - ひとつの mp3 として生成する
      - 間は全角スペースや改行で表現する
      - pause には軽い揺らぎを持たせる
    """

    voice_text = text.strip()

    # 読み補正
    voice_text = voice_text.replace("今日は", "きょうは")
    voice_text = voice_text.replace("今日の", "きょうの")
    voice_text = voice_text.replace("今日を", "きょうを")
    voice_text = voice_text.replace("今日も", "きょうも")
    voice_text = voice_text.replace("未だ", "まだ")

    # 長い沈黙
    voice_text = voice_text.replace(
        "........",
        "\n" + random_space(4, 9) + "\n"
    )

    # 三点リーダー系
    voice_text = voice_text.replace(
        "……",
        random_space(3, 6)
    )

    voice_text = voice_text.replace(
        "...",
        random_space(3, 6)
    )

    # 大きな区切り
    voice_text = voice_text.replace(
        "／",
        "\n" + random_space(3, 7) + "\n"
    )

    # 中くらいの区切り
    voice_text = voice_text.replace(
        "｜",
        random_space(3, 7)
    )

    # 小さい区切り
    voice_text = voice_text.replace(
        "、",
        "、" + random_space(1, 3)
    )

    # 文末
    voice_text = voice_text.replace(
        "。",
        "。" + random_space(2, 5)
    )

    return voice_text