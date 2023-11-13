import pytest
from lib.present import *


def test_fail_if_present_not_wrapped():
    present = Present()
    with pytest.raises(Exception) as e: 
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_present():
    present = Present()
    present.wrap('test1')
    result = present.contents
    assert result == "test1"

def test_fail_if_present_already_wrapped():
    present = Present()
    present.wrap('test1')
    with pytest.raises(Exception) as e: 
        present.wrap('test1')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."