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

その他参考情報
------------
■コマンドで確認
echo -n korirakkuma | shasum -a 257

■Web画面でSHA256ハッシュ生成ツール
https://www.milk-island.net/javascript/hashgenerator/sha2_256.html

■実装の参考ページ
https://qiita.com/economist/items/768d2f6a10d54d4fa39f
https://developer.mozilla.org/ja/docs/Web/API/SubtleCrypto/digest
