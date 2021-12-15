JavaScriptでハッシュ値（SHA256）を生成するサンプル
=============================================

+ 標準ライブラリのみで実装
+ IE11では動作しない
+ 冷やかし程度のBootstrap

処理の流れ
---------
1. 文字列をUTF-8のバイトデータ（Uint8Array: バイトデータの配列）に変換
2. バイトデータからダイジェスト値（SHA256ハッシュ値であるバイトデータの配列）を生成
3. ダイジェスト値（バイトデータの配列）を16進数の表現に変換

```
【例】
korirakkuma
  ↓  Unit8Array（アルファベットのUTF-8 => asciiコードと同じ => asciiコードに変換）
[107 111 114 105 114 97 107 107 117 109 97]
  ↓  sha256 digest
[96 157 237 176 38 51 242 196 26 155・・・・・]
  ↓  10進数=>16進数
[60  9d  ed  b0 26 33  f2  c4 1a  9b・・・・・]
  ↓　16進数表現を文字列として結合
609dedb02633f2c41a9bd937a84679aebffc4adc2430d40f1294c8520435ca07
```

その他参考情報
------------
コマンドで確認(mac or linux)
```
echo -n korirakkuma | shasum -a 256
```
+ Web画面でSHA256ハッシュ生成ツール
  + https://www.milk-island.net/javascript/hashgenerator/sha2_256.html

+ 実装の参考ページ
  + https://qiita.com/economist/items/768d2f6a10d54d4fa39f
  + https://developer.mozilla.org/ja/docs/Web/API/SubtleCrypto/digest
