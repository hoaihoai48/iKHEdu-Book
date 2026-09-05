a, b = map(int, input().split())
tong_a = 0
for i in range(1, int(a ** 0.5) + 1):
    if a % i == 0:
        j = a // i
        if i < a:
            tong_a = tong_a + i
        if j != i and j < a:
            tong_a = tong_a + j
tong_b = 0
for i in range(1, int(b ** 0.5) + 1):
    if b % i == 0:
        j = b // i
        if i < b:
            tong_b = tong_b + i
        if j != i and j < b:
            tong_b = tong_b + j
if a != b and tong_a == b and tong_b == a:
    print("YES")
else:
    print("NO")
