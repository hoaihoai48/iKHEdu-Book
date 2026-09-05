dong1 = input().split()
if len(dong1) >= 4:
    l1 = int(dong1[0])
    r1 = int(dong1[1])
    l2 = int(dong1[2])
    r2 = int(dong1[3])
else:
    l1 = int(dong1[0])
    r1 = int(input().split()[0])
    l2 = int(input().split()[0])
    r2 = int(input().split()[0])
if l1 >= l2:
    trai = l1
else:
    trai = l2
if r1 <= r2:
    phai = r1
else:
    phai = r2
if trai <= phai:
    print("GIAO NHAU", phai - trai)
else:
    print("KHONG GIAO NHAU")
