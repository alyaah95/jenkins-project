from processor import format_data
import json
def test_format_data():
    result = json.loads(format_data("Test", "Dev"))
    assert result["status"] == "active"
