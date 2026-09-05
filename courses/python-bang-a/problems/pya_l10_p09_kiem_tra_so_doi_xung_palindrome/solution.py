n = int(input().strip())
orig = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if rev == orig:
    print("YES")
else:
    print("NO")
