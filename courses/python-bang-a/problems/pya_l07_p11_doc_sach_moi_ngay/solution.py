n = int(input())
tong = 0
for ngay in range(1, n + 2):
    tong = tong + ngay
    if tong >= n:
        print(ngay)
        break
