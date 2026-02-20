import subprocess
import sys

def test_dry_run_does_not_create_file(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    
    # 入力CSVを作る
    input_file.write_text(
        "name,age,city\n"
        "Alice,20,Tokyo\n"
    )
    
    result = subprocess.run(
        [
            sys.executable,
            "simple_csv_formatter.py", 
            "-i", str(input_file),
            "-o", str(output_file),
            "--dry-run",
        ],
        capture_output = True,
        text = True,
    )
    
    #正常終了している
    assert result.returncode == 0
    
    #ファイルが作られない
    assert not output_file.exists()
    
def test_dry_run_creates_file(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    
    # 入力CSVを作る
    input_file.write_text(
        "name,age,city\n"
        "Alice,20,Tokyo\n"
    )
    
    result = subprocess.run(
        [
            sys.executable,
            "simple_csv_formatter.py", 
            "-i", str(input_file),
            "-o", str(output_file),
        ],
        capture_output = True,
        text = True,
    )
    
    #正常終了している
    assert result.returncode == 0
    
    #ファイルが作られない
    assert output_file.exists()
    
    content = output_file.read_text()
    assert "city,name,age" in content
    assert "Tokyo,Alice,20" in content