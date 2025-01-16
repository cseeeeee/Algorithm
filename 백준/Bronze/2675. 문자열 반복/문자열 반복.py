t = int(input())
for _ in range(0,t):
  res = ''
  r, s = input().strip().split()
  for i in s:
    res += i*int(r)
  print(res)
