def min_steps_to_room(num):
  if num == 1:  
    return 1

  total = 1
  level = 1
  
  while num > total:
    total += 6 * level
    level += 1

  return level

num = int(input())
print(min_steps_to_room(num))