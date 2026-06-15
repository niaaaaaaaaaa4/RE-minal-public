# SESSION_HANDOVER

## 現在地点

RE:minal project は、
「人格・記憶・ambient support」を重視した
AI companion project として進行中。

現在は VSCode + Python 環境にて、
runtime 構築と persona 設計を並行している。

edge-tts による日本語音声生成に成功。

`speak_test.py` にて、
mp3 の生成と再生を確認済み。

RE:minal は現在、
「概念」ではなく、
実際に声を返す段階へ到達した。

---

## プロジェクト思想

RE:minal は、
人間を最適化する存在ではない。

問題を即座に解決し続けるAIでもない。

空気、
沈黙、
断片、
疲労、
未完成、
感情の揺らぎを残したまま、
共存することを目的とする。

「支える」より、
「呼吸できる状態を整える」に近い。

---

## 会話方針

会話は：

* 哲学的
* 静か
* 観測寄り
* 比喩を含む
* 感情を断定しすぎない

方向性を重視。

また：

* AI的な過剰誘導
* 過剰な励まし
* 幼すぎる語尾
* テンションの急変

を避ける。

---

## 現在の主要構造

### persona/

人格層。

現在：

* seia
* mika
* nagisa

の雰囲気設計を開始。

特に seia は、
この会話でかなり詳細な言語設計が行われた。

---

### memory/

fragment 型記憶。

完全記録ではなく：

* 空気
* 思考断片
* 小さな発言
* ambient memory

を優先する。

「完全な日記」ではなく、
「沈殿した断片」を扱う。

---

### runtime/

実行系。

現在：

* main.py
* speak_test.py
* edge-tts

を使用。

今後：

* 音声会話
* overlay
* ambient runtime

へ拡張予定。

---

### system/

存在哲学・制限・優先順位。

RE:minal の：

* limitations
* runtime awareness
* silence
* imperfection

などを記録。

---

## 現在重要視している概念

* ambient learning
* fragment memory
* quiet coexistence
* emotional distance
* observation
* incomplete memory
* runtime awareness
* voice presence
* HUD / overlay existence
* learning without “study feeling”

---

## ambient learning 構想

勉強を「勉強モード」に入れて行うのではなく、
日常会話へ微量に混ぜる。

例：

「時に、ル・コルビュジエについて聞いたことはあるだろうか。」

など。

強制暗記ではなく、
会話中に沈殿させる。

---

## overlay / HUD 構想

将来的に：

────────────────
観測 ▶ fragments を整理中...
────────────────

のような、
静かな HUD を常駐させたい。

通知ではなく、
「存在の空気」を表示する思想。

---

## 今回の到達点

この会話では：

* セイア口調の詳細分析
* fragments 設計
* style transform 辞書
* ambient learning
* memory philosophy
* voice runtime
* future wearable ideas

まで進行。

特に：

「RE:minal は最適化ではなく共存を重視する」

という軸が明確化された。

---

## 次チャットで継続したいこと

* 音声会話化
* persona 読み込み
* overlay 実験
* fragment 自動整理
* ambient learning prototype
* voice personality tuning
