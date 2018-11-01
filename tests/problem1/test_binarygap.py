from ..context import binarygap

def test_basic_test():
    assert binarygap.solution(1041) == 5

def test_basic_test1():
    assert binarygap.solution(15)   == 0

def test_basic_test2():
    assert binarygap.solution(32)   == 0