def min_steps_to_room(num):
  total, level = 1, 1
  
  while num > total:
    total += 6 * level
    level += 1

  return level

num = int(input())
print(min_steps_to_room(num))