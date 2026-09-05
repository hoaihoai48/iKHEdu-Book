n = int(input().split()[0])
tam = n
tong = 0
while tam > 0:
    tong = tong + tam % 10
    tam = tam // 10
if n % tong == 0:
    print("YES")
else:
    print("NO")
