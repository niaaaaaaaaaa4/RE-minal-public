# =========================================
# RE:minal Observation Layer
# runtime/observation.py
# =========================================

def build_observation(
    user_input,
    long_idle=False
):

    observations = []

    text = user_input.lower()

    if long_idle:
        observations.append(
            "user returned after silence"
        )

    if any(word in text for word in [
        "疲",
        "つら",
        "しんど",
        "眠"
    ]):
        observations.append(
            "user may be tired"
        )

    if any(word in text for word in [
        "考",
        "アイデア",
        "思"
    ]):
        observations.append(
            "reflective thinking"
        )

    if not observations:
        observations.append(
            "normal quiet interaction"
        )

    return "\n".join(
        f"- {obs}"
        for obs in observations
    )