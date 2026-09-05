n = int(input())
if n < 2:
    print("NO")
else:
    la_snt = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_snt = False
            break
    if la_snt:
        print("YES")
    else:
        print("NO")
