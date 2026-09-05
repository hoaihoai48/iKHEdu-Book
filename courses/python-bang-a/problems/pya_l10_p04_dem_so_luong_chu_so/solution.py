n = int(input())
if n == 0:
    print(1)
else:
    dem = 0
    while n > 0:
        du = n % 10
        dem = dem + 1
        n = n // 10
    print(dem)
