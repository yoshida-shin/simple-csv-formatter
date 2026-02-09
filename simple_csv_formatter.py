import csv
import sys

# 並び替えたい列順をここに書く

COLUMN_ORDER = ["city", "name", "age"]
def is_empty_row(row):
    """
    行がすべて空（または空白）なら True
    """
    return all(not cell.strip() for cell in row)

def format_csv(input_path, output_path):
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("CSVが空です")

    header = rows[0]
    required_columns = ["city", "name", "age"]

    for col in required_columns:
        if col not in header:
            print(f"必要な列がありません: {col}")
            sys.exit(1)
    data_rows = rows[1:]
    
    for row in rows[1:]:
        if len(row) != len(header):
            print("列数が合わない行があります")
            sys.exit(1)
            
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
    
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(formatted_rows)

def main():
    if len(sys.argv) != 3:
        print("使い方: python simple_csv_formatter.py input.csv output.csv")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]

    format_csv(input_csv, output_csv)
    print("完了しました")

if __name__ == "__main__":
    main()