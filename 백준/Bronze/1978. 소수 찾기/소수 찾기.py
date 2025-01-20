num = int(input())
nums = map(int,input().split())
count = 0

for n in nums:
  if n > 1:
    for i in range(2, int(n**0.5)+1):
      if n % i == 0:
        break;
    else:
      count += 1
print(count)