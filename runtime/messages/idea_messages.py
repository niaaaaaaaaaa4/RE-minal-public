from messages.banks.endings import IDEA_SAVED
from messages.banks.pauses import SOFT_ACK


def idea_saved_message() -> str:
    return f"{SOFT_ACK}\n\n{IDEA_SAVED}"
