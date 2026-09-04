k = int(input())
s = input().split()
c = 0
for w in s:
    if len(w) > k:
        c += 1
print(c)
