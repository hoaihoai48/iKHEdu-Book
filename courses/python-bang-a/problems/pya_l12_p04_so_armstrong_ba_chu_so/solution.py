n = int(input())
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10
if tram ** 3 + chuc ** 3 + don_vi ** 3 == n:
    print("YES")
else:
    print("NO")
