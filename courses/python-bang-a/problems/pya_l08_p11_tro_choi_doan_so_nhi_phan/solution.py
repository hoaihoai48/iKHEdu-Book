n = int(input())
count = 0
while True:
    count = count + 1
    if n == 1:
        break
    n = n // 2
print(count)
