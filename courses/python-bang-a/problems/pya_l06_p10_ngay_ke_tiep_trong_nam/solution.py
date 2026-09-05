d = int(input().split()[0])
m = int(input().split()[0])
y = int(input().split()[0])
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    nhuan = True
else:
    nhuan = False
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    ngay_trong_thang = 31
elif m == 4 or m == 6 or m == 9 or m == 11:
    ngay_trong_thang = 30
elif nhuan:
    ngay_trong_thang = 29
else:
    ngay_trong_thang = 28
if d < ngay_trong_thang:
    print(d + 1, m, y)
elif m < 12:
    print(1, m + 1, y)
else:
    print(1, 1, y + 1)
