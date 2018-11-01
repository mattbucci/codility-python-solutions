
def solution(A):
    A = sorted(A)
    number_to_pair = None
    
    for number in A:
        if number_to_pair is None:
            number_to_pair = number
            continue

        if number is not number_to_pair:
            return number_to_pair
        else:
            number_to_pair = None

    return number_to_pair