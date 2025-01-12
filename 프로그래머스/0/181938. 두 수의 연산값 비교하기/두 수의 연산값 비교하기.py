def solution(a, b):
    str_a, str_b = str(a), str(b)
    return max(2*a*b, int(str_a + str_b))