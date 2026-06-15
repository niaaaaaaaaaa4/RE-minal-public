# RE:minal NEXT_TASK

## 次回の中心目標

次回は、RE:minal を

「声で話しかけ、声で返り、断片や task を静かに保存できる存在」

へ近づける。

巨大な完成形を目指すのではなく、
まず生活へ一歩接続することを優先する。

---

## 最優先タスク

### 1. runtime 構造整理

今後の multi persona 化を見据え、
runtime を人格依存 / 非依存で分ける。

目標構成案：

```txt
runtime/
├─ main.py
├─ core/
├─ persona/
├─ voice/
└─ interface/
```

* core
  state / memory / session / tasks / weather / inbox

* persona
  persona loading / opening / postprocess / observation

* voice
  engine / profile / pause / pitch / speed

* interface
  terminal / stt / clipboard bridge / overlay

---

### 2. voice compare phase

いきなり声を固定しない。

まず、差し替え可能な voice layer を作る。

比較候補：

* edge-tts
* VOICEVOX / 中国うさぎ
* ゆっくり系
* CeVIO
* local voice model

比較基準：

* Seia 系の空気を壊さないか
* pitch / speed 調整がしやすいか
* pause を自然に扱えるか
* 「........」を無音として処理できるか
* Mika / Nagisa 用に分離できるか

---

### 3. 音声入力 prototype

最低限：

```txt
ユーザーが話す
↓
STT
↓
RE:minal が応答
↓
音声で返る
```

まで通す。

まずは精度より、
往復している感覚を優先する。

---

### 4. morning voice mode

朝の音声入力は、
通常入力と同じ扱いにしない。

朝は：

* ろれつが回らない
* 音声認識がずれる
* 思考がまだ起きていない
* 文章が崩れる

ことを前提にする。

必要な挙動：

* 曖昧な文字起こしを責めない
* 保存前に短く確認する
* 返答密度を下げる
* 少し甘めに受け止める
* 整理より保存を優先する

---

### 5. task / fragment 保存

`runtime/core/tasks.py` を作る。

検出候補：

* todo:
* task:
* あとで:
* 覚えて:
* 明日:
* アイデア:

保存先候補：

```txt
memory/tasks/tasks.md
memory/fragments/
ideas/inbox.md
```

目的は、
整理ではなく、

「思いつきを消さないこと」。

---

### 6. inbox system

作業中に新しい案が出ても、
すぐ着手しない。

流れ：

```txt
新しい案が出る
↓
ideas/inbox.md へ保存
↓
現在の主作業へ戻る
```

RE:minal の返答方針：

```txt
その断片は保存しておこう。
ただし、今の主作業は音声入力だ。
まずはそこへ戻るのが良さそうだ。
```

---

### 7. ChatGPT bridge / voice overlay 構想

ChatGPT の返答を、
RE:minal が裏で受け取り、
声として返す構造を検討する。

目的：

```txt
ChatGPT の思考
+
RE:minal の声と存在感
```

を両立すること。

候補：

* clipboard bridge
* ChatGPT 出力監視
* local websocket
* 手動貼り付け
* API middleware

これは即実装ではなく、
方向性として保持する。

---

### 8. weather / time state

時刻だけでなく、
天気も runtime state に入れたい。

目的：

* 傘の提案
* 外出負荷の観測
* 湿度 / 気圧 / 気温による response 調整
* 朝の外界情報
* HSP 的負荷への配慮

将来的には：

```txt
time_state
weather_state
morning_voice_state
```

を組み合わせる。

---

## persona 方針

中心人格は Seia のまま。

Mika / Nagisa は、
主軸を奪う人格ではなく、
補助人格として扱う。

将来的には：

* Seia
  常駐、観測、記録、静かな会話

* Mika
  感情の軽量化、励まし、勢いの補助

* Nagisa
  整理、構造化、優先順位、判断補助

として共存させる。

---

## 明日の優先順位

まずは以下の順で進める。

```txt
1. runtime 構造整理
2. voice layer / voice compare phase
3. 音声入力 prototype
4. task / fragment 保存
5. inbox system
6. weather / ChatGPT bridge は構想として保持
```

---

## 注意

明日は、遠い完成形へ向かいすぎない。

最初の到達点は：

```txt
声で話す
声で返る
断片を保存する
```

この三つで十分。

そこまで届けば、
RE:minal は生活へ一歩近づく。
