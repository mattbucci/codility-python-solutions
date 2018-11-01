from ..context import oddoccurrancesinarray
from random import randint

def test_array_of_size_1():
    assert oddoccurrancesinarray.solution([1]) == 1

def test_example():
    example = [9,3,9,3,9,7,9]
    assert oddoccurrancesinarray.solution(example) == 7

def test_example2():
    example = [9,3,9,3,4,7,4,7,2]
    assert oddoccurrancesinarray.solution(example) == 2

def test_random():
    odd_random_int = randint(0, 1000000)
    array = []
    for __ in range(1, 10000):
        random_int = randint(0, 1000000)
        array.append(random_int)
        array.append(random_int)
    array.insert(randint(1, 10000), odd_random_int)
    assert oddoccurrancesinarray.solution(array) == odd_random_int
    