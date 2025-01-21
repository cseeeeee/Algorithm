a = int(input())
b = int(input())
c = int(input())
res = a*b*c
res_count = {i: 0 for i in range(10)}

for i in str(res):
  res_count[int(i)] += 1

for count in res_count.values():
  print(count)