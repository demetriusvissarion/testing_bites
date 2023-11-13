import pytest
from lib.password_checker import *


def test_success():
    password = PasswordChecker()
    result = password.check('mypassword')
    assert result == True


def test_fail_if_password_too_short():
    password = PasswordChecker()
    with pytest.raises(Exception) as e: 
        password.check('test1')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."