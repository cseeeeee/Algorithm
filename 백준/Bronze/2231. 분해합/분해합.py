def convert_to_boon(m):
    total = m
    while m > 0:  
        total += m % 10
        m //= 10
    return total

def solution(n):
  for i in range(1, n):
    if (convert_to_boon(i) == n):
      return i
  return 0

n = int(input())  
print(solution(n))