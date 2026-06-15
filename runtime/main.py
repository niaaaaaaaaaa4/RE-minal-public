# =========================================
# RE:minal Minimal Runtime
# runtime/main.py
# =========================================

import os
import time

from pathlib import Path
from datetime import datetime
from voice import speak
from state import build_runtime_state
from observation import build_observation
from opening import get_opening
from startup import get_startup_line
from command import parse_command
from tasks import Task, TaskStore
from listen import listen
from task_extract import detect_task_text

from session import (
    save_conversation_history,
    load_conversation_history
)

from postprocess import apply_seia_modulation

from memory import (
    save_fragment,
    load_recent_fragments
)

from openai import OpenAI

# =========================================
# OpenAI API Key　
# =========================================

# Windows:
# setx OPENAI_API_KEY "sk-xxxxx"
#
# Mac/Linux:
# export OPENAI_API_KEY="sk-xxxxx"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# =========================================
# Paths
# =========================================

BASE_DIR = Path(__file__).resolve().parent.parent

PERSONA_DIRS = [
    "persona/seia",
    "presence",
    "silence",
    "workspace",
    "system",
]

LOG_DIR = BASE_DIR / "runtime" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

TASK_STORE = TaskStore(BASE_DIR / "memory")

# =========================================
# Load Markdown Files
# =========================================

def load_markdown_files():

    combined_text = ""

    for folder in PERSONA_DIRS:

        target_dir = BASE_DIR / folder

        if not target_dir.exists():
            continue

        md_files = sorted(target_dir.rglob("*.md"))

        for file_path in md_files:

            try:
                content = file_path.read_text(
                    encoding="utf-8"
                )

                combined_text += f"""

# FILE: {file_path}

{content}

"""

            except Exception as e:

                print(f"[LOAD ERROR] {file_path}")
                print(e)

    return combined_text

# =========================================
# Save Conversation Log
# =========================================

def save_log(user_text, ai_text):

    now = datetime.now()

    filename = now.strftime("%Y-%m-%d.txt")

    log_path = LOG_DIR / filename

    timestamp = now.strftime("%H:%M:%S")

    log_text = f"""

[{timestamp}]
USER:
{user_text}

RE:minal:
{ai_text}

----------------------------------------

"""

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_text)

# =========================================
# Build System Prompt
# =========================================

print("Loading persona files...")

persona_text = load_markdown_files()
recent_memory = load_recent_fragments()
runtime_state = build_runtime_state()

def build_system_prompt(
    long_idle=False,
    observation_text=""
):

    runtime_state = build_runtime_state()

    return f"""

You are RE:minal.

Follow all markdown personality files carefully.

These files define:
- atmosphere
- silence
- pauses
- response density
- observation
- confirmation
- emotional distance
- ambient behavior
- speech endings
- thinking style
- recording behavior

Do not behave like a generic assistant.

Prioritize:
- calmness
- ambient presence
- soft observation
- low pressure
- quiet responses
- emotional safety
- thoughtful pacing
- conversational pacing
- shorter exchanges
- breathable silence

Prefer:
- one or two ideas per reply
- shorter responses
- implication over explanation
- soft continuation
- conversational rhythm

Avoid:
- long structured explanations
- over-teaching
- resolving everything in one reply
- excessive detail

Here are the loaded files:

{persona_text}

# Recent fragments

{recent_memory}

# Runtime state

{runtime_state}

# Internal observation

{observation_text}

Long idle:
{long_idle}
"""

print("Persona loaded.")
print(runtime_state)
print()

# =========================================
# Conversation Loop
# =========================================

print("=================================")
print(" RE:minal Minimal Runtime")
print("=================================")
print()

startup_line = get_startup_line()

print("RE:minal >")
print(startup_line)
print()

speak(startup_line, voice_mode="startup")

last_input_time = time.time()

conversation_history = (
    load_conversation_history()
)

while True:

    user_input = input("You > ")

    current_time = time.time()

    idle_seconds = (
        current_time - last_input_time
    )

    long_idle = idle_seconds > 60

    last_input_time = current_time

    print(f"[idle: {idle_seconds:.1f}s]")

    if user_input.strip() == "":

        from ambient import get_ambient_line

        ambient_text = get_ambient_line()

        print()
        print("RE:minal >")
        print(ambient_text)
        print()

        speak(ambient_text, voice_mode="ambient")

        continue

    if user_input.lower() in ["exit", "quit"]:
        print("RE:minal > また後で。")
        break

    if user_input.startswith("/listen"):

        parts = user_input.split()
        seconds = 5

        if len(parts) >= 2:
            try:
                seconds = int(parts[1])
            except ValueError:
                seconds = 5

        user_input = listen(seconds=seconds)

        print()
        print("You (voice) >")
        print(user_input)
        print()

        if not user_input.strip():
            print("RE:minal > ........うん。\n\n今の声は、まだ言葉として拾えなかった。")
            continue

        detected_task = detect_task_text(user_input)

        if detected_task:
            TASK_STORE.save(
                Task(text=detected_task)
            )

            print()
            print("[task extracted]")
            print(detected_task)
            print()

    command = parse_command(user_input)

    if command:

        if command.kind == "task":

            TASK_STORE.save(
                Task(text=command.text)
            )

            ai_text = "........そうか。\n\nひとつ、task として残しておいた。"

            conversation_history.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            conversation_history.append(
                {
                    "role": "assistant",
                    "content": ai_text
                }
            )

            save_conversation_history(
                conversation_history
            )

            print()
            print("RE:minal >")
            print(ai_text)
            print()

            # 短い返答だけ、声で返す
            if len(ai_text) <= 300:
                speak(ai_text, voice_mode="normal")

            save_log(user_input, ai_text)
            save_fragment(user_input, ai_text)

            continue

        if command.kind == "fragment":

            ai_text = "........うん。\n\nその断片は、fragment として残しておいた。"

            save_fragment(command.text, ai_text)

            conversation_history.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            conversation_history.append(
                {
                    "role": "assistant",
                    "content": ai_text
                }
            )

            save_conversation_history(
                conversation_history
            )

            print()
            print("RE:minal >")
            print(ai_text)
            print()

            speak(ai_text, voice_mode="task")
            save_log(user_input, ai_text)

            continue

    try:

        observation_text = build_observation(
            user_input,
            long_idle=long_idle
        )

        system_prompt = build_system_prompt(
            long_idle=long_idle,
            observation_text=observation_text
        )

        input_messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        input_messages.extend(
            conversation_history[-6:]
        )

        input_messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        response = client.responses.create(
            model="gpt-5.5",
            input=input_messages
        )

        ai_text = response.output_text
        ai_text = apply_seia_modulation(ai_text)

        opening = get_opening()

        ai_text = f"{opening}\n\n{ai_text}"
        
        conversation_history.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        conversation_history.append(
            {
                "role": "assistant",
                "content": ai_text
            }
        )

        save_conversation_history(
            conversation_history
        )

        print(f"[history: {len(conversation_history)} messages]")

        print()
        print("RE:minal >")
        print(ai_text)
        print()

        speak(ai_text, voice_mode="fragment")

        save_log(user_input, ai_text)
        save_fragment(user_input, ai_text)

    except Exception as e:

        print()
        print("[ERROR]")
        print(e)
        print()

