n = int(input().strip())
a = list(map(float, input().split()))
tb = sum(a) / n
print(sum(1 for x in a if x >= tb))
