import csv
import sys
import argparse
import logging
from typing import NoReturn

# 並び替えたい列順をここに書く

COLUMN_ORDER = ["city", "name", "age"]

def print_error(reason: str, line_no: int=None, expected: str=None, actual: str=None) -> NoReturn:
    message = "❌ エラーが見つかりました\n"
    message += f"原因: {reason}\n"
    if line_no is not None:
        message += f"行番号: {line_no}\n"
    
    if expected is not None:
        message += f"期待値: {expected}\n"
    
    if actual is not None:
        message += f"実際の値: {actual}\n"
    
    logging.error(message)
    sys.exit(1)

def is_empty_row(row: int) -> bool:
    """
    行がすべて空（または空白）なら True
    """
    return all(not cell.strip() for cell in row)

def load_csv(path: str) -> list[list[str]]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

def validate_rows(rows: list[list[str]]) -> None:
    if not rows:
        raise ValueError("CSVが空です")

    header = rows[0]
    required_columns = {"city", "name", "age"}
    missing = required_columns - set(header)
    if missing:
        raise ValueError("必要な列が不足しています")

    expected_len = len(header)
    for i, row in enumerate(rows[1:], start = 2):
        if not row:
            continue
        if len(row) != expected_len:
            raise ValueError(f"{i}行目の列数が不足しています")
    
def build_formatted_rows(rows: list[list[str]]) -> list[list[str]]:
    header = rows[0]
    data_rows = rows[1:]

    # ヘッダ名 → インデックス の対応表を作る
    index_map = {name: i for i, name in enumerate(header)}
    new_indexes = [index_map[col] for col in COLUMN_ORDER]
    formatted = [COLUMN_ORDER]
    for row in data_rows:
        if is_empty_row(row):
            continue
    
        new_row = [row[i] for i in new_indexes]
        formatted.append(new_row)
    return formatted

def save_csv(path: str, rows: list[list[str]]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def format_csv(input_path: str, output_path: str, dry_run: bool) -> None:
    try:
        logging.debug("入力ファイルを開きます")
        rows = load_csv(input_path)
        validate_rows(rows)
        formatted = build_formatted_rows(rows)

        if dry_run:
            print("🔍 dry-run モードのため、ファイルは作成されません")
        else:
            save_csv(output_path, formatted)
            
    except Exception as e:
        logging.error("予期せぬエラーが発生しました")
        logging.error(f"詳細: {e}")
        sys.exit(1)
            
def main():
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
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="詳細ログを表示する"
    )    
    
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("CSV処理を開始します")
    
    input_csv = args.input
    output_csv = args.output
    dry_run = args.dry_run
    
    format_csv(input_csv, output_csv, dry_run)

    logging.info("✅ 正常に処理が完了しました")
    if not dry_run:
        logging.info(f"出力ファイル: {output_csv}")

if __name__ == "__main__":
    main()