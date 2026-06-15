# VOICE_RUNTIME_DIRECTION

## 現在の問題意識

現在の RE:minal は、
音声返答自体は成立している。

ただし現状は：

```txt
特定 voice 固定
```

に近く、

今後：

* 中国うさぎ
* edge-tts
* ゆっくり系
* CeVIO
* local voice model

などを比較・変更したくなった時に、
runtime 側へ直接手を入れる必要が出る可能性がある。

そのため、
次段階では：

```txt
「音声を選べる構造」
```

を先に作りたい。

---

## 次回の優先方針

最初にやるべきことは：

```txt
voice を決めること
```

ではなく、

```txt
voice を差し替え可能にすること
```

とする。

---

## 理想構造

```txt
voice/
├─ profiles/
│  ├─ seia.json
│  ├─ mika.json
│  └─ nagisa.json
├─ engines/
│  ├─ edge_tts.py
│  ├─ voicevox.py
│  ├─ yukkuri.py
│  └─ ...
└─ manager.py
```

---

## profile の役割

人格ごとの：

* voice engine
* voice name
* speed
* pitch
* pause behavior
* punctuation behavior
* silence duration

を定義する。

例：

```json
{
  "engine": "voicevox",
  "voice": "中国うさぎ",
  "speed": 0.92,
  "pitch": -2,
  "pause_strength": 0.8,
  "sentence_gap": 0.6
}
```

---

## 今後比較したい voice 候補

* edge-tts
* VOICEVOX（中国うさぎ）
* ゆっくり系
* CeVIO
* local voice model

---

## 比較時の重要基準

### 1.

人格空気を壊さないか

RE:minal は、
実況系テンションより：

```txt
quiet coexistence
ambient presence
```

を優先する。

---

### 2.

pause を扱えるか

特に：

```txt
........
```

を、

「てんてんてん」

ではなく、

```txt
無音 pause
```

として扱いたい。

---

### 3.

人格別分離が可能か

将来的に：

* Seia
* Mika
* Nagisa

で、
voice profile を切り替えられる構造を目指す。

---

## 特に重要

現在 RE:minal は：

```txt
「音声読み上げ」
```

ではなく、

```txt
「存在温度としての声」
```

を設計し始めている。

そのため：

* 息継ぎ
* pause
* pitch
* speech density
* silence
* sentence pacing

を、
人格層の一部として扱いたい。

---

## 次回の最初の流れ

```txt
1. voice compare phase
2. voice abstraction layer
3. profile system
4. 音声入力
5. task / fragment 保存
```

まずは：

```txt
「どの声が正しいか」
```

ではなく、

```txt
「後から自由に比較できる状態」
```

を作ることを優先したい。
