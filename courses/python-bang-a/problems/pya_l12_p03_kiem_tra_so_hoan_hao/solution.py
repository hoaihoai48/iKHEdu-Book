n = int(input())
if n <= 1:
    print("NO")
else:
    tong = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            if i < n:
                tong = tong + i
            if j != i and j < n:
                tong = tong + j
    if tong == n:
        print("YES")
    else:
        print("NO")
