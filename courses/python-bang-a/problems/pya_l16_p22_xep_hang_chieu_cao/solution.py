n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = sorted(data[:n])
print(" ".join(map(str, data)))
