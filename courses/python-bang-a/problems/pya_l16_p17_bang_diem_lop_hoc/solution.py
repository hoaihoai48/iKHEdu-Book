n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
print(max(data))
print(min(data))
print(f"{sum(data) / n:.1f}")
