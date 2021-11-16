# SheetJSの概要
JavaScriptでのExcelライブラリ
+ SheetJS
  + https://sheetjs.com
+ Community Edition
  + https://github.com/sheetjs/sheetjs
+ ドキュント・・・おそらくCommunity EditionのGitHubのREADME.mdと同じ
  + https://docs.sheetjs.com/

# エクスポート時の日付型の出力形式
+ sheet_to_json
  + rawデータを表示 => 日付のシリアル値を表示
+ sheet_to_csv
  + SheetJSのデフォルト書式での日付形式文字列

下記のデモサイトでデフォルトの動作が確認できる
https://oss.sheetjs.com/sheetjs/

# エクスポート時の日付の書式を指定するには？
それぞれのメソッドのオプション引数に、日付書式を指定する・・・たぶん

以下、https://docs.sheetjs.com/ での記載場所を示す。

## sheet_to_csv
As an alternative to the writeFile CSV type, XLSX.utils.sheet_to_csv also produces CSV output. The function takes an options argument:
にある
dateNF
に、'YYYY/MM/DD'を指定する？

## sheet_to_json
XLSX.utils.sheet_to_json generates different types of JS objects. The function takes an options argument:
にある
dateNF
に、'YYYY/MM/DD'を指定する？
