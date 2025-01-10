str = input()

res=''
for a in str:
    if a.islower():
        res += a.upper()
    else:
        res += a.lower()

print(res)