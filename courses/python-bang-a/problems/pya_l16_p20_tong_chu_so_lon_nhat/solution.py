n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
best = data[0]
bs = sum(map(int, str(best)))
for x in data[1:]:
    s = sum(map(int, str(x)))
    if s > bs or (s == bs and x < best):
        best = x
        bs = s
print(best)
