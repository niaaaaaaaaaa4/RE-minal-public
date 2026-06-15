# =========================================
# RE:minal Runtime State
# runtime/state.py
# =========================================

from datetime import datetime


def detect_time_state():

    now = datetime.now()

    hour = now.hour

    if 0 <= hour <= 4:
        return "deep_night"

    elif 5 <= hour <= 10:
        return "morning"

    elif 11 <= hour <= 17:
        return "daytime"

    elif 18 <= hour <= 22:
        return "evening"

    else:
        return "night"


def build_runtime_state():

    time_state = detect_time_state()

    state_text = f"""
# Runtime State

Current state:
{time_state}

Behavior hints:

- deep_night:
  quieter
  slower
  softer responses
  more pauses

- morning:
  gentle startup
  low pressure

- daytime:
  clearer structure
  slightly higher energy

- evening:
  calm transition

- night:
  ambient quietness

Response density rules:

- deep_night:
  shorter responses
  more silence
  softer pacing

- morning:
  gentle pacing
  gradual startup

- daytime:
  more structured
  slightly more detailed

- evening:
  reflective
  calm pacing

- night:
  ambient
  quiet
"""

    return state_text