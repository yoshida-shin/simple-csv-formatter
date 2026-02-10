# simple-csv-formatter
CSVファイルの列を指定した順番に並び替えるPythonツールです。  
列不足や不正なCSVの場合は、分かりやすいエラーメッセージを表示します。

## できること

- CSVの列を指定順に並び替える
- 必要な列が不足している場合はエラー表示
- 列数が足りない行がある場合はエラー表示
- dry-run（チェックのみ実行）に対応
\
## 使い方
```bash
python simple_csv_formatter.py -i input.csv -o output.csv
```
```bash
python simple_csv_formatter.py -i input.csv -o output.csv --dry-run
```
## オプション

| オプション | 説明 |  
|----------|------|  
| -i, --input | 入力CSVファイル |  
| -o, --output | 出力CSVファイル |  
| --dry-run | チェックのみ実行（出力ファイルは作成しない） |  

## 入力CSVの仕様

- 1行目はヘッダー行であること
- 必要な列がすべて含まれていれば、列の順番は自由
- 列数が不足している行がある場合はエラーになります

## エラーについて

以下の場合、処理は中断されエラーメッセージが表示されます。

- 必要な列が存在しない場合
- 列数が不足している行がある場合

エラーメッセージには、問題の内容が分かるように詳細が表示されます。

## 実行例

```text
$ python simple_csv_formatter.py -i input.csv -o output.csv --dry-run
✅ 正常に処理が完了しました
```
