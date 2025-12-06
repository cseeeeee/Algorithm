def solution(array):
    compare_num_list = [0] * 1000
    for num in array:
        for compare_idx in range(len(compare_num_list)):
            if num == compare_idx:
                compare_num_list[compare_idx] += 1

    max_num = compare_num_list[0]
    for compare_num in compare_num_list:
        if max_num < compare_num:
            max_num = compare_num

    count = 0
    max_idx = 0
    for idx in range(len(compare_num_list)):
        if compare_num_list[idx] == max_num:
            count += 1
            max_idx = idx

    if count > 1:
        return -1
    else:
        result = max_idx
        return result