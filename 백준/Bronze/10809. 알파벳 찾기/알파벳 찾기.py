import string

s_input = input()
alpha_dict={i: -1 for i in string.ascii_lowercase}
s_dict={}
for idx, c in enumerate(s_input):
  if c not in s_dict:
    s_dict[c] = idx


for a in alpha_dict:
  for s in s_dict:
    if a == s:
      alpha_dict[a] = s_dict[s]
print(' '.join(str(i) for i in alpha_dict.values()))