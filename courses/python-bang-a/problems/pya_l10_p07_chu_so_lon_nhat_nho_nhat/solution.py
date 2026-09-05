n = int(input())
lon = -1
nho = 10
while n > 0:
    d = n % 10
    if d > lon:
        lon = d
    if d < nho:
        nho = d
    n = n // 10
print(lon, nho)
