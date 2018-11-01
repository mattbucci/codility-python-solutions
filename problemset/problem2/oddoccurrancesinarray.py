
def solution(A):
    sortedA = sorted(A)
    sum = 0
    
    for i, number in enumerate(sortedA):
        index_is_odd = i % 2 is 1
        if index_is_odd:
            sum += number
        else:
            sum -= number

    return abs(sum)