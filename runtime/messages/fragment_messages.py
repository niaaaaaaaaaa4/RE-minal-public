from messages.banks.endings import (
    FATIGUE_FRAGMENT_SAVED,
    FRAGMENT_SAVED,
)
from messages.banks.pauses import SOFT_ACK, SOFT_NOTICE


def fragment_saved_message(fragment_type: str) -> str:
    if fragment_type == "fatigue":
        return f"{SOFT_NOTICE}\n\n{FATIGUE_FRAGMENT_SAVED}"

    return f"{SOFT_ACK}\n\n{FRAGMENT_SAVED}"
