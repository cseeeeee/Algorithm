def solution(a, b):
    res1, res2 =  '', ''
    res1 = str(a) + str(b)
    res2 = str(b) + str(a)
    return int(res1) if int(res1) > int(res2) else int(res2)