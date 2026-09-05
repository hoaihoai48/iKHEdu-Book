n = int(input().split()[0])
cac_so = []
while len(cac_so) < n:
    try:
        cac_so.extend(map(int, input().split()))
    except EOFError:
        break
cac_so = sorted(cac_so)
tong = 0
da_cho = 0
for t in cac_so:
    da_cho = da_cho + t
    tong = tong + da_cho
print(tong)
