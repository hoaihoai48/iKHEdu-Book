a, b = map(int, input().split())
i = int(a ** 0.5)
while i * i < a:
    i = i + 1
while (i - 1) * (i - 1) >= a:
    i = i - 1
j = int(b ** 0.5)
while (j + 1) * (j + 1) <= b:
    j = j + 1
while j * j > b:
    j = j - 1
if j < i:
    print(0)
else:
    print(j - i + 1)
