# =========================================
# RE:minal Command Parser
# runtime/command.py
# =========================================

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CommandResult:
    kind: str
    text: str


def parse_command(user_text: str) -> CommandResult | None:
    """
    RE:minal runtime 用の簡易コマンド判定。

    対応:
      /task 内容
      /todo 内容
      /fragment 内容
      /frag 内容
    """

    text = user_text.strip()

    if not text:
        return None

    prefixes = {
        "/task ": "task",
        "/todo ": "task",
        "/fragment ": "fragment",
        "/frag ": "fragment",
    }

    for prefix, kind in prefixes.items():
        if text.startswith(prefix):
            body = text.removeprefix(prefix).strip()

            if not body:
                return None

            return CommandResult(
                kind=kind,
                text=body
            )

    return None
