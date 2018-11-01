# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    max_gap_length = 0
    current_gap_length = 0
    binary_string = "{0:b}".format(N)
    
    for c in binary_string:
        if c is "1":
            if (current_gap_length > max_gap_length):
                max_gap_length = current_gap_length
            current_gap_length = 0
        else:
            current_gap_length += 1

    return max_gap_length
            