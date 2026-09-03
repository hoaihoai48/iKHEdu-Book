n = int(input().strip())
a = list(map(float, input().split()))
a.sort()
trimmed = a[1:-1]
tb = sum(trimmed) / len(trimmed)
print(f"{tb:.2f}")
