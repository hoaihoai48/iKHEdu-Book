line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
try:
    print(a.index(x))
except ValueError:
    print(-1)
