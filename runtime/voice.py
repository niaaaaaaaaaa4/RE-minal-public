# =========================================
# RE:minal Voice Runtime
# runtime/voice.py
# VOICEVOX edition
# =========================================

import random
import time
from pathlib import Path

import pygame
import requests


VOICEVOX_URL = "http://127.0.0.1:50021"

SPEAKER_NAME = "暁記ミタマ"
STYLE_NAME = "ノーマル"

BASE_SETTINGS = {
    "speedScale": 0.92,
    "pitchScale": 0.09,
    "intonationScale": 1.29,
    "volumeScale": 1.22,
    "prePhonemeLength": 0.40,
    "postPhonemeLength": 0.29,
    "pauseLengthScale": 1.54,
}

TIME_STATES = {
    "morning": {
        "speedScale": -0.02,
        "intonationScale": +0.03,
        "pauseLengthScale": +0.08,
    },

    "day": {
    },

    "night": {
        "speedScale": -0.04,
        "pauseLengthScale": +0.12,
        "volumeScale": -0.03,
    },

    "deep_night": {
        "speedScale": -0.08,
        "pauseLengthScale": +0.22,
        "volumeScale": -0.06,
        "intonationScale": -0.08,
    }
}

VOICE_MODES = {
    "startup": {
        "prePhonemeLength": +0.08,
        "pauseLengthScale": +0.10,
    },

    "ambient": {
        "speedScale": -0.03,
        "volumeScale": -0.04,
        "pauseLengthScale": +0.18,
    },

    "task": {
        "speedScale": +0.01,
        "intonationScale": -0.04,
    },

    "fragment": {
        "speedScale": -0.02,
        "pauseLengthScale": +0.08,
    },

    "normal": {
    },
}

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "runtime" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def get_speaker_id() -> int:
    speakers = requests.get(
        f"{VOICEVOX_URL}/speakers",
        timeout=10
    ).json()

    for speaker in speakers:
        if speaker["name"] == SPEAKER_NAME:
            for style in speaker["styles"]:
                if style["name"] == STYLE_NAME:
                    return style["id"]

    raise RuntimeError(
        f"VOICEVOX speaker not found: {SPEAKER_NAME} / {STYLE_NAME}"
    )

from datetime import datetime

def get_time_state() -> str:

    hour = datetime.now().hour

    if 5 <= hour < 11:
        return "morning"

    if 11 <= hour < 19:
        return "day"

    if 19 <= hour < 24:
        return "night"

    return "deep_night"

def apply_runtime_variation(
    query: dict,
    voice_mode: str = "normal"
) -> dict:
    """
    時間帯と voice mode に応じて、
    声を少しだけ揺らす。
    """

    time_state = get_time_state()

    state_mod = TIME_STATES.get(
        time_state,
        {}
    )

    mode_mod = VOICE_MODES.get(
        voice_mode,
        {}
    )

    def mod_value(
        key: str,
        random_min: float,
        random_max: float
    ) -> float:

        return (
            BASE_SETTINGS[key]
            + state_mod.get(key, 0)
            + mode_mod.get(key, 0)
            + random.uniform(random_min, random_max)
        )

    query["speedScale"] = mod_value(
        "speedScale",
        -0.02,
        0.02
    )

    query["pitchScale"] = mod_value(
        "pitchScale",
        -0.01,
        0.01
    )

    query["intonationScale"] = mod_value(
        "intonationScale",
        -0.05,
        0.05
    )

    query["volumeScale"] = mod_value(
        "volumeScale",
        -0.03,
        0.03
    )

    query["prePhonemeLength"] = mod_value(
        "prePhonemeLength",
        -0.05,
        0.05
    )

    query["postPhonemeLength"] = mod_value(
        "postPhonemeLength",
        -0.04,
        0.04
    )

    query["pauseLengthScale"] = mod_value(
        "pauseLengthScale",
        -0.08,
        0.08
    )

    print(f"[voice state: {time_state} / {voice_mode}]")

    return query


def build_voice_text(text: str) -> str:
    voice_text = text.strip()

    voice_text = voice_text.replace("今日は", "きょうは")
    voice_text = voice_text.replace("今日の", "きょうの")
    voice_text = voice_text.replace("今日を", "きょうを")
    voice_text = voice_text.replace("今日も", "きょうも")
    voice_text = voice_text.replace("未だ", "まだ")

    return voice_text


def generate_voice(
    text: str,
    voice_mode: str = "normal"
) -> Path:
    speaker_id = get_speaker_id()
    voice_text = build_voice_text(text)

    query_response = requests.post(
        f"{VOICEVOX_URL}/audio_query",
        params={
            "text": voice_text,
            "speaker": speaker_id,
        },
        timeout=30
    )

    query_response.raise_for_status()
    query = query_response.json()

    query = apply_runtime_variation(
        query,
        voice_mode=voice_mode
    )

    synthesis_response = requests.post(
        f"{VOICEVOX_URL}/synthesis",
        params={
            "speaker": speaker_id,
        },
        json=query,
        timeout=60
    )

    synthesis_response.raise_for_status()

    output_path = OUTPUT_DIR / "reminal_voice.wav"

    with open(output_path, "wb") as f:
        f.write(synthesis_response.content)

    return output_path


def play_voice(file_path: Path):
    pygame.mixer.init()
    pygame.mixer.music.load(str(file_path))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

    pygame.mixer.quit()


def speak(
    text: str,
    voice_mode: str = "normal"
):
    voice_path = generate_voice(
        text,
        voice_mode=voice_mode
    )

    play_voice(voice_path)