from lib.counter import *

def test_count_to_10():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_count_to_100():
    counter = Counter()
    counter.add(100)
    result = counter.report()
    assert result == "Counted to 100 so far."