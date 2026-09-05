n = int(input().strip())
a, b, c = 1, 1, 2
if n == 1 or n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    for _ in range(n - 3):
        a, b, c = b, c, a + b + c
    print(c)
