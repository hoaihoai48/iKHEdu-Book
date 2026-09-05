a, b = map(int, input().split())
dem = 0
for i in range(a, b + 1):
    goc = i
    dao = 0
    temp = i
    while temp > 0:
        dao = dao * 10 + temp % 10
        temp = temp // 10
    if dao == goc:
        dem = dem + 1
print(dem)
