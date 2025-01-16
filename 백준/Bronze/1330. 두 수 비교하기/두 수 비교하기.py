a, b = map(int,input().strip().split(' '))
res = ">" if a>b else "<" if a<b else "==" 
print(res)