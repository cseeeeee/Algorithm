def xo_game(xo_str):
  sum, count = 0, 0
  for i in range(len(xo_str)):
    if xo_str[i] != "X":
      count += 1
    else:
      count = 0
    sum += count
  return sum

num = int(input())
for _ in range(num):
  xo_str = input().strip()
  print(xo_game(xo_str))