num = int(input()) # 참가자 수
s, m, l, xl, xxl, xxxl = list(map(int, input().split(' '))) # 티셔츠 별 신청자 수
t, p = map(int, input().split(' ')) # 티셔츠 묶음 수, 펜 묶음 수
t_res = (s + t - 1) // t + (m + t - 1) // t + (l + t - 1) // t \
      + (xl + t - 1) // t + (xxl + t - 1) // t + (xxxl + t - 1) // t
print(t_res)
print(num//p, num%p)