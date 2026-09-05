n = int(input().strip())
val = 1
res = []
for _ in range(n):
    res.append(str(val))
    val *= 2
print(" ".join(res))
