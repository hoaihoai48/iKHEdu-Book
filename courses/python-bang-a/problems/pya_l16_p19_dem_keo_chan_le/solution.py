n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
c = 0
for x in data[:n]:
    if x % 2 == 0:
        c += 1
print(str(c) + " " + str(n - c))
