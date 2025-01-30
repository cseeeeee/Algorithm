num = int(input())
scores = list(map(int, input().strip().split()))
max_score = max(scores)
total = 0
for i in range(num):
  total += scores[i]/max_score*100
print(total/num)