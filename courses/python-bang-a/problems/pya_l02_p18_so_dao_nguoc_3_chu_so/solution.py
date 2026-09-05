n = int(input())
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10
print(don_vi * 100 + chuc * 10 + tram)
