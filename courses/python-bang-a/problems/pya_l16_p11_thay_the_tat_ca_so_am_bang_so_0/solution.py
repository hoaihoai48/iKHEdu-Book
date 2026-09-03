n = int(input().strip())
a = list(map(int, input().split()))
res = [0 if x < 0 else x for x in a]
print(*res)
