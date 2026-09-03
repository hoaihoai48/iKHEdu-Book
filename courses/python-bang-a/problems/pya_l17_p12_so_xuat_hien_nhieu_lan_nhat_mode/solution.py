n = int(input().strip())
a = list(map(int, input().split()))
counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1
max_c = max(counts.values())
candidates = [k for k, v in counts.items() if v == max_c]
print(min(candidates))
