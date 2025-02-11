def seq_song(seq_list):
  if seq_list == sorted(seq_list):
    return "ascending"
  elif seq_list == sorted(seq_list, reverse=True):
    return "descending"
  else:
    return "mixed"

seq_list = list(map(int, input().split()))
print(seq_song(seq_list))