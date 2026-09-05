n = int(input())
temp = n
k = 0
while temp > 0:
    k = k + 1
    temp = temp // 10
tong = 0
temp = n
while temp > 0:
    d = temp % 10
    tong = tong + d ** k
    temp = temp // 10
if tong == n:
    print("YES")
else:
    print("NO")
