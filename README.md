# simple-csv-formatter
CSVファイルの列を指定した順番に並び替えるPythonツールです。  
列不足や不正なCSVの場合は、分かりやすいエラーメッセージを表示します。

## できること

- CSVの列を指定順に並び替える
- 必要な列が不足している場合はエラー表示
- 列数が足りない行がある場合はエラー表示
- dry-run（チェックのみ実行）に対応
- verbose 詳細なログ(DEBUGレベル)を表示

## 使い方
```bash
python simple_csv_formatter.py -i input.csv -o output.csv
```
```bash
python simple_csv_formatter.py -i input.csv -o output.csv --dry-run
```
```bash
python simple_csv_formatter.py -i input.csv -o output.csv --verbose
```

## オプション

| オプション | 説明 |  
|----------|------|  
| -i, --input | 入力CSVファイル |  
| -o, --output | 出力CSVファイル |  
| --dry-run | チェックのみ実行（出力ファイルは作成しない） |  
| --verbose | 詳細なログ(DEBUGレベル)を表示 |  

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

```bash
python simple_csv_formatter.py -i input.csv -o output.csv --dry-run
```
✅ 正常に処理が完了しました  
```bash
python simple_csv_formatter.py -i input.csv -o output.csv --verbose
```
2026-02-17 19:10:48 [INFO] CSV処理を開始します
2026-02-17 19:10:48 [DEBUG] 入力ファイルを開きます
2026-02-17 19:10:48 [INFO] ✅ 正常に処理が完了しました
2026-02-17 19:10:48 [INFO] 出力ファイル: output.csv