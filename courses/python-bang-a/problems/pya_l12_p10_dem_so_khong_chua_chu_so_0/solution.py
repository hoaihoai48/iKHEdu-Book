n = int(input())
dem = 0
for i in range(1, n + 1):
    temp = i
    co_so_0 = False
    while temp > 0:
        if temp % 10 == 0:
            co_so_0 = True
            break
        temp = temp // 10
    if not co_so_0:
        dem = dem + 1
print(dem)
