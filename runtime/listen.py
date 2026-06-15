# =========================================
# RE:minal Listen Runtime
# runtime/listen.py
# =========================================

from __future__ import annotations

from listen_correction import correct_listen_text

import os
from pathlib import Path

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "runtime" / "input"
INPUT_DIR.mkdir(parents=True, exist_ok=True)

SAMPLE_RATE = 16000
CHANNELS = 1


def record_audio(
    seconds: int = 8,
    output_path: Path | None = None
) -> Path:
    """
    マイクから短く録音し、wav として保存する。
    """

    if output_path is None:
        output_path = INPUT_DIR / "voice_input.wav"

    print(f"[listen: recording {seconds}s]")

    audio = sd.rec(
        int(seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32"
    )

    sd.wait()

    audio_int16 = np.int16(
        np.clip(audio, -1.0, 1.0) * 32767
    )

    write(
        str(output_path),
        SAMPLE_RATE,
        audio_int16
    )

    print("[listen: recorded]")

    return output_path


def transcribe_audio(audio_path: Path) -> str:
    """
    OpenAI Speech to Text で音声を文字へ変換する。
    """

    print("[listen: transcribing]")

    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_file,
            response_format="text",
            language="ja"
        )

    text = str(transcript).strip()

    text = correct_listen_text(text)

    print("[listen: done]")

    return text


def listen(seconds: int = 5) -> str:
    """
    録音から文字起こしまでを一度に行う。
    """

    seconds = max(1, min(seconds, 30))

    audio_path = record_audio(
        seconds=seconds
    )

    return transcribe_audio(
        audio_path
    )
