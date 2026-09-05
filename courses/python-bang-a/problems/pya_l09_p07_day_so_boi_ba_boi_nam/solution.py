n = int(input().strip())
res = []
num = 1
while len(res) < n:
    if num % 3 == 0 or num % 5 == 0:
        res.append(str(num))
    num += 1
print(" ".join(res))
