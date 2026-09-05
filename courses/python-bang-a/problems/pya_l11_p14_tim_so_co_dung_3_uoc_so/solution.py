n = int(input())
gioi_han = int(n ** 0.5)
if gioi_han < 2:
    print(0)
else:
    la_snt = [True] * (gioi_han + 1)
    la_snt[0] = False
    la_snt[1] = False
    for i in range(2, int(gioi_han ** 0.5) + 1):
        if la_snt[i]:
            for j in range(i * i, gioi_han + 1, i):
                la_snt[j] = False
    dem = 0
    for i in range(2, gioi_han + 1):
        if la_snt[i]:
            dem = dem + 1
    print(dem)
