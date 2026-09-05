a, b = map(int, input().split())
dem = 0
for num in range(a, b + 1):
    if num < 2:
        continue
    la_snt = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            la_snt = False
            break
    if la_snt:
        dem = dem + 1
print(dem)
