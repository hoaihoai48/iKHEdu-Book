n, p = map(int, input().split())
if n >= 10:
    cost = p * 0.8
elif n >= 5:
    cost = p * 0.9
else:
    cost = p
print(int(n * cost))
