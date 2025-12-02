array = [int(input()) for _ in range(9)] 

def find_max_num(array):
    max_num = array[0]
    max_idx = 0
    for idx in range(len(array)):
        if max_num < array[idx]:
            max_num = array[idx]
            max_idx = idx
    print(max_num)
    print(max_idx + 1)
    return max_num, max_idx + 1

find_max_num(array)