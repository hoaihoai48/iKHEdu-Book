n = int(input().strip())
a = list(map(int, input().split()))
unique = sorted(list(set(a)))
print(*unique)
