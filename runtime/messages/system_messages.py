from messages.banks.endings import EXIT
from messages.banks.pauses import QUIET_PAUSE
from messages.banks.warmth import (
    RECENT_RECALL_VOICE,
    VOICE_NOT_CAPTURED,
)


def voice_not_captured_message() -> str:
    return f"{QUIET_PAUSE}\n\n{VOICE_NOT_CAPTURED}"


def exit_message() -> str:
    return EXIT


def recent_recall_voice_message() -> str:
    return RECENT_RECALL_VOICE
