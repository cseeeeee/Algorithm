num = int(input())
num_list = map(int, input().strip().split(' '))
res = [l for l in num_list]
print(min(res), max(res))