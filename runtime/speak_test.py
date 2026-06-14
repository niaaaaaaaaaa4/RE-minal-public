import asyncio
import edge_tts
import os

TEXT = "……起動確認した。テスト用の音声を発話してみる。"
VOICE = "ja-JP-NanamiNeural"

OUTPUT_DIR = "runtime/output"
OUTPUT = os.path.abspath(f"{OUTPUT_DIR}/voice_test.mp3")

async def main():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT)

    os.startfile(OUTPUT)

asyncio.run(main())