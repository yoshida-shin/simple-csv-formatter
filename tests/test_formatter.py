from simple_csv_formatter import build_formatted_rows
from simple_csv_formatter import validate_rows
import pytest

#def test_build_formatted_rows_basic():
#    rows = [
#        ["name", "age", "city"],
#        ["Alice", "20", "Tokyo"],
#        ["Bob", "30", "Osaka"],
#   ]
    
#    result = build_formatted_rows(rows)
#    
#    assert result == [
#        ["city", "name", "age"],
#        ["Tokyo", "Alice", "20"],
#        ["Osaka", "Bob", "30"],
#    ]
    
#def test_empty_row_is_skipped():
#    rows = [
#        ["name", "age", "city"],
#        ["", "", ""],
#        ["Alice", "20", "Tokyo"],
#        ["Bob", "30", "Osaka"],
#    ]
    
#    result = build_formatted_rows(rows)
    
#    assert result == [
#        ["city", "name", "age"],
#        ["Tokyo", "Alice", "20"],
#        ["Osaka", "Bob", "30"],
#    ]
    
#def test_missing_required_column():
#    rows = [
#        ["name", "age"],
#        ["Alice", "20"]
#    ]
    
#    with pytest.raises(ValueError):
#        validate_rows(rows)
        
#def test_validate_rows_empty_csv():
#    rows = []
#    with pytest.raises(ValueError):
#        validate_rows(rows)

#def test_validate_rows_column_shortage():
#    rows = [
#        ["name", "age", "city"],
#        ["Alice", "20", "Tokyo"],
#        ["Bob", "30"],
#    ]
#    with pytest.raises(ValueError):
#        validate_rows(rows)


@pytest.mark.parametrize("rows", [
    pytest.param([], id = "empty_csv"),  # 空CSV
    pytest.param([["name", "age"]],id = "missing_column"),  # 必須列不足
    pytest.param(
        [
            ["name", "age", "city"],
            ["Alice", "20"],  # 列不足
        ],
        id = "column_shortage"
    ),
])
def test_validate_rows_invalid_cases(rows):
    with pytest.raises(ValueError):
        validate_rows(rows)    