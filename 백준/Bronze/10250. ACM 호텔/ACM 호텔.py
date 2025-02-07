def calculation_room_number(h, w, n):
  if n % h != 0:
    floor = n % h
    room = n // h + 1
    return floor * 100 + room
  else:
    floor = h
    room = n // h
    return floor * 100 + room

t = int(input())
for _ in range(t):
  h, w, n = map(int, input().split())
  print(calculation_room_number(h,w,n))