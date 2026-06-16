from messages.banks.endings import DEV_SAVED
from messages.banks.pauses import SOFT_ACK


def reminal_dev_saved_message() -> str:
    return f"{SOFT_ACK}\n\n{DEV_SAVED}"
