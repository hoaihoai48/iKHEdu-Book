n = int(input().strip())
gia = 5000
if n >= 20:
    gia = 4000
elif n >= 10:
    gia = 4500
print(n * gia)
