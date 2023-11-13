from lib.report_length import *

def test_report_length_2():
    result = report_length('42')
    assert result == "This string was 2 characters long."

def test_report_length_5():
    result = report_length('house')
    assert result == "This string was 5 characters long."

def test_report_length_10():
    result = report_length('characters')
    assert result == "This string was 10 characters long."