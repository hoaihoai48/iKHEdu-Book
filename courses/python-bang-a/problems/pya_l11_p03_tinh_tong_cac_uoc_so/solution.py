n = int(input())
tong = 0
for i in range(1, n + 1):
    if n % i == 0:
        tong = tong + i
print(tong)
