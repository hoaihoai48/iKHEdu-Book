n = int(input())
r = int(n ** 0.5)
while (r + 1) * (r + 1) <= n:
    r = r + 1
while r * r > n:
    r = r - 1
if r * r == n:
    print("YES")
else:
    print("NO")
