n = int(input())
sieu = True
if n < 2:
    sieu = False
else:
    temp = n
    while temp > 0:
        if temp < 2:
            sieu = False
            break
        la_snt = True
        for i in range(2, int(temp ** 0.5) + 1):
            if temp % i == 0:
                la_snt = False
                break
        if not la_snt:
            sieu = False
            break
        temp = temp // 10
if sieu:
    print("YES")
else:
    print("NO")
