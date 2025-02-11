def seq_song(seq_list):
  ascending = True
  descending = True

  for i in range(len(seq_list) - 1):
    if seq_list[i+1] - seq_list[i] != 1:
      ascending = False
    if seq_list[i+1] - seq_list[i] != -1:
      descending = False
    
  if ascending:
    return "ascending"
  elif descending:
    return "descending"
  else:
    return "mixed"

seq_list = list(map(int, input().split()))
print(seq_song(seq_list))