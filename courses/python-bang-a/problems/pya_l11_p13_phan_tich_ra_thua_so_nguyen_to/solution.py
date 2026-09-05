n = int(input())
thua_so = []
temp = n
d = 2
while d * d <= temp:
    while temp % d == 0:
        thua_so.append(str(d))
        temp = temp // d
    d = d + 1
if temp > 1:
    thua_so.append(str(temp))
print(" * ".join(thua_so))
