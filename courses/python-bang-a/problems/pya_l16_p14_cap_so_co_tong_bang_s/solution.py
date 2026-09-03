line = input().split()
n, s = int(line[0]), int(line[1])
a = list(map(int, input().split()))
seen = set()
cnt = 0
for x in a:
    if (s - x) in seen:
        cnt += 1
    seen.add(x)
print(cnt)
