n = int(input())
for p in range(2, n - 1):
    la_snt_p = True
    if p < 2:
        la_snt_p = False
    else:
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                la_snt_p = False
                break
    q = p + 2
    la_snt_q = True
    for i in range(2, int(q ** 0.5) + 1):
        if q % i == 0:
            la_snt_q = False
            break
    if la_snt_p and la_snt_q and q <= n:
        print(p, q)
