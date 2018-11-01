from ..context import cyclicrotation

def test_shift_right():
    assert cyclicrotation.solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]

def test_shift_three_times():
    assert cyclicrotation.solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

def test_shift_should_not_modify_source_array():
    A = [3, 8, 9, 7, 6]
    assert cyclicrotation.solution(A, 3) == [9, 7, 6, 3, 8]
    assert A == [3, 8, 9, 7, 6]
