n = int(input())
chan = 0
le = 0
while n > 0:
    d = n % 10
    if d % 2 == 0:
        chan = chan + 1
    else:
        le = le + 1
    n = n // 10
print(chan, le)
