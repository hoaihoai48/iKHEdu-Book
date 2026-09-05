n = int(input())
uoc = []
for i in range(1, n + 1):
    if n % i == 0:
        uoc.append(str(i))
print(" ".join(uoc))
