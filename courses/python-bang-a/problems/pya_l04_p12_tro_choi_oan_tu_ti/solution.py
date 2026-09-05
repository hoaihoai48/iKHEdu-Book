dong1 = input().split()
if len(dong1) >= 2:
    ti = int(dong1[0])
    teo = int(dong1[1])
else:
    ti = int(dong1[0])
    teo = int(input().split()[0])
if ti == teo:
    print("HOA")
elif (ti == 1 and teo == 2) or (ti == 2 and teo == 3) or (ti == 3 and teo == 1):
    print("TI THANG")
else:
    print("TEO THANG")
