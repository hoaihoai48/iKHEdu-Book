n = int(input())
first = True
for i in range(1, n + 1):
    if n % i == 0:
        if not first:
            print(' ', end='')
        print(i, end='')
        first = False
print()
