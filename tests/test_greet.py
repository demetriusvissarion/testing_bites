from lib.greet import *

def test_greet():
    result = greet('Demetrius')
    assert result == "Hello, Demetrius!"