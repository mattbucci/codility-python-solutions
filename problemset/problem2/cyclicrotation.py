
def solution(A, K):
    for __ in range(0, K):
        A = rotate_right(A)
    return A

def rotate_right(A):
    return A[-1:] + A[:-1]