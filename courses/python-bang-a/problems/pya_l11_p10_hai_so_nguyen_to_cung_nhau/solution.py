a, b = map(int, input().split())
x = a
y = b
while y != 0:
    x, y = y, x % y
if x == 1:
    print("YES")
else:
    print("NO")
