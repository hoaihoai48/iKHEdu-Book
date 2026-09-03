n = int(input().strip())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(*a)
