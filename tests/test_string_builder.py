from lib.string_builder import *

def test_add_to_string():
    string = StringBuilder()
    string.add('test1')
    result = string.output()
    assert result == 'test1'

def test_size_of_string():
    string = StringBuilder()
    string.add('test2')
    result = string.size()
    assert result == 5