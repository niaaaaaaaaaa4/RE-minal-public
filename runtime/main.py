# =========================================
# RE:minal Minimal Runtime
# runtime/main.py
# =========================================

import os
from pathlib import Path
from datetime import datetime

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

SYSTEM_PROMPT = f"""
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

Here are the loaded files:

{persona_text}
"""

print("Persona loaded.")
print()

# =========================================
# Conversation Loop
# =========================================

print("=================================")
print(" RE:minal Minimal Runtime")
print("=================================")
print()

while True:

    user_input = input("You > ")

    if user_input.lower() in ["exit", "quit"]:
        print("RE:minal > また後で。")
        break

    try:

        response = client.responses.create(
            model="gpt-5.5",
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        ai_text = response.output_text

        print()
        print("RE:minal >")
        print(ai_text)
        print()

        save_log(user_input, ai_text)

    except Exception as e:

        print()
        print("[ERROR]")
        print(e)
        print()
