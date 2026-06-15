# =========================================
# RE:minal Minimal Runtime
# runtime/main.py
# =========================================

import os
import time

from pathlib import Path
from datetime import datetime

from openai import OpenAI

from voice import speak
from state import build_runtime_state
from observation import build_observation
from opening import get_opening
from startup import get_startup_line
from command import parse_command
from tasks import Task, TaskStore
from listen import listen
from task_extract import detect_task_text
from thought_extract import (
    detect_idea,
    detect_fragment,
    detect_reminal_dev
)
from fragment_type import detect_fragment_type
from idea_memory import save_idea
from dev_memory import save_reminal_dev

from task_recall import load_recent_tasks
from continue_recall import (
    build_continue_text,
    build_morning_continue,
)
from task_complete import complete_task
from today_recall import build_today_text

from session import (
    save_conversation_history,
    load_conversation_history,
)

from recall import build_recall_text

from postprocess import apply_seia_modulation

from memory import (
    save_fragment,
    save_typed_fragment,
    load_recent_fragments,
)

from messages.task_messages import (
    task_saved_message,
    task_list_message,
    no_task_message,
    task_done_message,
    task_done_keyword_missing_message,
    task_not_found_message,
)
from messages.fragment_messages import fragment_saved_message
from messages.idea_messages import idea_saved_message
from messages.dev_messages import reminal_dev_saved_message
from messages.system_messages import (
    voice_not_captured_message,
    exit_message,
    recent_recall_voice_message,
)

# =========================================
# OpenAI API Key
# =========================================

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

TASK_STORE = TaskStore()

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
# Conversation Helpers
# =========================================

def record_conversation(
    conversation_history,
    user_text: str,
    ai_text: str,
):

    conversation_history.append(
        {
            "role": "user",
            "content": user_text,
        }
    )

    conversation_history.append(
        {
            "role": "assistant",
            "content": ai_text,
        }
    )

    save_conversation_history(
        conversation_history
    )


def print_reply(ai_text: str):

    print()
    print("RE:minal >")
    print(ai_text)
    print()


def complete_short_response(
    conversation_history,
    user_text: str,
    ai_text: str,
    voice_mode: str,
    save_as_fragment: bool = True,
):

    record_conversation(
        conversation_history,
        user_text,
        ai_text,
    )

    print_reply(ai_text)

    speak(
        ai_text,
        voice_mode=voice_mode,
    )

    save_log(user_text, ai_text)

    if save_as_fragment:
        save_fragment(user_text, ai_text)

# =========================================
# Build System Prompt
# =========================================

print("Loading persona files...")

persona_text = load_markdown_files()
recent_memory = load_recent_fragments()
runtime_state = build_runtime_state()


def build_system_prompt(
    long_idle=False,
    observation_text="",
    recall_text="",
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

# Recall memory

{recall_text}

Long idle:
{long_idle}
"""


print("Persona loaded.")
print(runtime_state)
print()

# =========================================
# Startup
# =========================================

print("=================================")
print(" RE:minal Minimal Runtime")
print("=================================")
print()

startup_line = get_startup_line()
morning_text = build_morning_continue()
recall_text = build_recall_text()

print("RE:minal >")
print(startup_line)
print()

speak(
    startup_line,
    voice_mode="startup",
)

if morning_text:

    print("[morning recall]")
    print(morning_text)
    print()

if recall_text:

    print("[recent recall]")
    print(recall_text)
    print()

    recall_voice = recent_recall_voice_message()

    print("RE:minal >")
    print(recall_voice)
    print()

    speak(
        recall_voice,
        voice_mode="ambient",
    )

last_input_time = time.time()

conversation_history = load_conversation_history()

# =========================================
# Conversation Loop
# =========================================

while True:

    user_input = input("You > ")
    input_source = "text"

    current_time = time.time()
    idle_seconds = current_time - last_input_time
    long_idle = idle_seconds > 60
    last_input_time = current_time

    print(f"[idle: {idle_seconds:.1f}s]")

    # -------------------------------------
    # Ambient empty input
    # -------------------------------------

    if user_input.strip() == "":

        from ambient import get_ambient_line

        ambient_text = get_ambient_line()

        print_reply(ambient_text)

        speak(
            ambient_text,
            voice_mode="ambient",
        )

        continue

    # -------------------------------------
    # Exit
    # -------------------------------------

    if user_input.lower() in ["exit", "quit"]:
        print("RE:minal >")
        print(exit_message())
        break

    # -------------------------------------
    # /commands
    # -------------------------------------

    if user_input.startswith("/listen"):

        parts = user_input.split()
        seconds = 5

        if len(parts) >= 2:
            try:
                seconds = int(parts[1])
            except ValueError:
                seconds = 5

        user_input = listen(seconds=seconds)
        input_source = "voice"

        print()
        print("You (voice) >")
        print(user_input)
        print()

        if not user_input.strip():

            ai_text = voice_not_captured_message()
            print_reply(ai_text)

            speak(
                ai_text,
                voice_mode="ambient",
            )

            continue

    if user_input.strip() == "/tasks":

        tasks = load_recent_tasks()

        print()

        if not tasks:
            ai_text = no_task_message()

        else:
            ai_text = task_list_message(tasks)

        print("RE:minal >")
        print(ai_text)
        print()

        speak(
            ai_text,
            voice_mode="fragment"
        )

        continue

    if user_input.strip() == "/continue":

        ai_text = build_continue_text()

        print()
        print("RE:minal >")
        print(ai_text)
        print()

        speak(
            ai_text,
            voice_mode="ambient"
        )

        continue

    if user_input.startswith("/done"):

        keyword = (
            user_input
            .replace("/done", "")
            .strip()
        )

        print()

        if not keyword:

            ai_text = task_done_keyword_missing_message()

        else:

            result = complete_task(keyword)

            if result:
                ai_text = task_done_message(result)

            else:

                ai_text = task_not_found_message()

        print("RE:minal >")
        print(ai_text)
        print()

        speak(
            ai_text,
            voice_mode="fragment"
        )

        continue

    if user_input.strip() == "/today":

        ai_text = build_today_text()

        print()
        print("RE:minal >")
        print(ai_text)
        print()

        speak(
            ai_text,
            voice_mode="ambient"
        )

        continue

    # -------------------------------------
    # Explicit slash commands
    # -------------------------------------

    command = parse_command(user_input)

    if command:

        if command.kind == "task":

            TASK_STORE.save(
                Task(text=command.text)
            )

            ai_text = task_saved_message()

            complete_short_response(
                conversation_history,
                user_input,
                ai_text,
                voice_mode="task",
            )

            continue

        if command.kind == "fragment":

            ai_text = fragment_saved_message("unresolved")

            save_fragment(
                command.text,
                ai_text,
            )

            complete_short_response(
                conversation_history,
                user_input,
                ai_text,
                voice_mode="fragment",
                save_as_fragment=False,
            )

            continue

    # -------------------------------------
    # Voice-derived lightweight extraction
    # -------------------------------------

    if input_source == "voice":

        detected_fragment = detect_fragment(user_input)

        if detected_fragment:

            fragment_type = detect_fragment_type(detected_fragment)
            ai_text = fragment_saved_message(fragment_type)

            print()
            print("[fragment extracted]")
            print(f"type: {fragment_type}")
            print(detected_fragment)
            print()

            save_typed_fragment(
                detected_fragment,
                ai_text,
                fragment_type=fragment_type,
            )

            complete_short_response(
                conversation_history,
                user_input,
                ai_text,
                voice_mode="fragment",
                save_as_fragment=False,
            )

            continue

        detected_dev = detect_reminal_dev(user_input)

        if detected_dev:

            save_reminal_dev(detected_dev)

            ai_text = reminal_dev_saved_message()

            print()
            print("[reminal dev extracted]")
            print(detected_dev)
            print()

            print("RE:minal >")
            print(ai_text)
            print()

            speak(ai_text, voice_mode="fragment")

            continue

        detected_idea = detect_idea(user_input)

        if detected_idea:

            save_idea(detected_idea)

            ai_text = idea_saved_message()

            print()
            print("[idea extracted]")
            print(detected_idea)
            print()

            save_fragment(
                f"[idea] {detected_idea}",
                ai_text,
            )

            complete_short_response(
                conversation_history,
                user_input,
                ai_text,
                voice_mode="fragment",
                save_as_fragment=False,
            )

            continue

        detected_task = detect_task_text(user_input)

        if detected_task:

            TASK_STORE.save(
                Task(text=detected_task)
            )

            ai_text = task_saved_message()

            print()
            print("[task extracted]")
            print(detected_task)
            print()

            complete_short_response(
                conversation_history,
                user_input,
                ai_text,
                voice_mode="task",
            )

            continue

    # -------------------------------------
    # Normal ChatGPT response
    # -------------------------------------

    try:

        observation_text = build_observation(
            user_input,
            long_idle=long_idle,
        )

        system_prompt = build_system_prompt(
            long_idle=long_idle,
            observation_text=observation_text,
            recall_text=recall_text,
        )

        input_messages = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

        input_messages.extend(
            conversation_history[-6:]
        )

        input_messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response = client.responses.create(
            model="gpt-5.5",
            input=input_messages,
        )

        ai_text = response.output_text
        ai_text = apply_seia_modulation(ai_text)

        opening = get_opening()
        ai_text = f"{opening}\n\n{ai_text}"

        record_conversation(
            conversation_history,
            user_input,
            ai_text,
        )

        print(f"[history: {len(conversation_history)} messages]")

        print_reply(ai_text)

        speak(
            ai_text,
            voice_mode="normal",
        )

        save_log(user_input, ai_text)
        save_fragment(user_input, ai_text)

    except Exception as e:

        print()
        print("[ERROR]")
        print(e)
        print()
