n = int(input().strip())
a = list(map(int, input().split()))
chan = [x for x in a if x % 2 == 0]
le = [x for x in a if x % 2 != 0]
print(*chan)
print(*le)
