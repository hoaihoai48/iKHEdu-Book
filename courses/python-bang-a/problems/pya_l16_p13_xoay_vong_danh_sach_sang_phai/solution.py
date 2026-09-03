line = input().split()
n, k = int(line[0]), int(line[1])
a = list(map(int, input().split()))
k %= n
if k == 0:
    print(*a)
else:
    print(*(a[-k:] + a[:-k]))
