# simple-csv-formatter
This is a simple tool to format CSV files for easy reuse (e.g. spreadsheets, Notion, data cleanup).

CSVファイルを簡単に整形するPythonスクリプトです。

※ 想定外の列構成の場合はエラーメッセージを表示して終了します

## 概要

このスクリプトは、CSVファイルの列順を指定順に並び替えるための

簡易データ整形ツールです。

## できること

- 空行を削除
- 列の順番を指定通りに並び替え

## 使い方

```bash
python simple_csv_formatter.py input.csv output.csv
```
- input.csv: original CSV file
- output.csv: formatted CSV file

### Before
name,age,city

### After
city,name,age