def solution(num_list):
    total = sum(num_list)
    mul = 1
    for num in num_list:
        mul *= num
    return 1 if total**2 > mul else 0