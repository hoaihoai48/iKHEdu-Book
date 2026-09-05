a = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a + i * d, end='')
    if i < n - 1:
        print(' ', end='')
print()
