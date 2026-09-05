n = int(input())
while n >= 10:
    tong = 0
    temp = n
    while temp > 0:
        tong = tong + temp % 10
        temp = temp // 10
    n = tong
print(n)
