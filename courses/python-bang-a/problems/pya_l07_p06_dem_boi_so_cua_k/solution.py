data = []
for _ in range(3):
    data.append(int(input()))
a, b, k = data
count = 0
for i in range(a, b + 1):
    if i % k == 0:
        count = count + 1
print(count)
