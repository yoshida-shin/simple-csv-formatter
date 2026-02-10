import csv
import sys
import argparse

parser = argparse.ArgumentParser(
    description="CSVの列を並び替えるツール"
)

parser.add_argument(
    "-i", "--input",
    required=True,
    help="入力CSVファイル"
)

parser.add_argument(
    "-o", "--output",
    required=True,
    help="出力CSVファイル"
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="チェックのみ実行（ファイルは作成しない）"
)

args = parser.parse_args()

# 並び替えたい列順をここに書く

COLUMN_ORDER = ["city", "name", "age"]

def print_error(reason, line_no=None, expected=None, actual=None):
    print("❌ エラーが見つかりました")
    print(f"原因: {reason}")
    if line_no is not None:
        print(f"行番号: {line_no}")
    if expected is not None:
        print(f"期待: {expected}")
    if actual is not None:
        print(f"実際: {actual}")
    sys.exit(1)

def is_empty_row(row):
    """
    行がすべて空（または空白）なら True
    """
    return all(not cell.strip() for cell in row)

def format_csv(input_path, output_path, dry_run):
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("CSVが空です")

    header = rows[0]

    expected_columns =len(COLUMN_ORDER)
    for col in COLUMN_ORDER:
        header_set = set(header)
        required_columns = {"city", "name", "age"}
        missing = required_columns - header_set
        if missing:
            print_error(
                reason="必要な列が不足しています",
                expected=",".join(sorted(required_columns)),
                actual=",".join(header)
            )  
    
        if col not in header:
            print_error(
                reason="必要な列がありません"
            )
    data_rows = rows[1:]

    for i, row in enumerate(rows, start=2):
        if is_empty_row(row):
            continue
        if len(row) < expected_columns:
            print_error(
                reason="列数が足りません",
                line_no=i,
                expected=f"{expected_columns}列（city,name,age）",
                actual=f"{len(row)}列"
            )
    # ヘッダ名 → インデックス の対応表を作る
    index_map = {name: i for i, name in enumerate(header)}
    
    # 指定された列順のインデックスを取得
    try:
        new_indexes = [index_map[col] for col in COLUMN_ORDER]
    except KeyError as e:
        raise ValueError(f"指定された列が見つかりません: {e}")
    
    formatted_rows = []

    # 新しいヘッダ
    formatted_rows.append(COLUMN_ORDER)
    
    for row in data_rows:
        if is_empty_row(row):
            continue
    
        new_row = [row[i] for i in new_indexes]
        formatted_rows.append(new_row)
    
    if dry_run:
        print("🔍 dry-run モードのため、ファイルは作成されません")
    else:
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(formatted_rows)

def main():
    input_csv = args.input
    output_csv = args.output
    dry_run = args.dry_run
    
    format_csv(input_csv, output_csv, dry_run)

    print("✅ 正常に処理が完了しました")
    if not dry_run:
        print(f"出力ファイル: {output_csv}")

if __name__ == "__main__":
    main()