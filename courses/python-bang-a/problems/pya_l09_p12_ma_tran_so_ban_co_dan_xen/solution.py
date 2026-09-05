n = int(input())
for i in range(n):
    print(" ".join(str((i + j + 1) % 2) for j in range(n)))
