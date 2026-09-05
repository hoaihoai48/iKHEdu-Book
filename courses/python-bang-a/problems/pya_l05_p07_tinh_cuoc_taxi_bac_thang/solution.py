n = int(input())
if n <= 1:
    print(10)
elif n <= 10:
    print(10 + (n - 1) * 8)
else:
    print(10 + 9 * 8 + (n - 10) * 6)
