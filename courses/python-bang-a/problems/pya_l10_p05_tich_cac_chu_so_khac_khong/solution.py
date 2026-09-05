n = int(input())
tich = 1
while n > 0:
    d = n % 10
    if d != 0:
        tich = tich * d
    n = n // 10
print(tich)
