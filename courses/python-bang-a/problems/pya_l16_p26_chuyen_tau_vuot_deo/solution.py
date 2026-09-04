n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
best = data[0]
c = 1
for x in data[1:]:
    if x > best:
        best = x
        c += 1
print(c)
