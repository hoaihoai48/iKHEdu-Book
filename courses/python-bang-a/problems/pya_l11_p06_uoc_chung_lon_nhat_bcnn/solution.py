a, b = map(int, input().split())
x = a
y = b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = a // gcd * b
print(gcd, lcm)
