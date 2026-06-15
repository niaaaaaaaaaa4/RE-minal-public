# RE:minal Messages

このフォルダは、RE:minal の返答文を管理する棚。

main.py は「何が起きたか」を扱い、
messages/ は「どう返すか」を扱う。

## Files

- task_messages.py
  - task 保存、一覧、完了、未検出
- fragment_messages.py
  - fragment 保存、voice 由来の状態記録
- idea_messages.py
  - idea 保存
- dev_messages.py
  - RE:minal 自身の開発 idea 保存
- recall_messages.py
  - continue / today / startup recall
- system_messages.py
  - listen 失敗、終了など

## Principle

処理文ではなく、RE:minal の声として読める文章を置く。
口調の変更は、なるべくこの棚で行う。
