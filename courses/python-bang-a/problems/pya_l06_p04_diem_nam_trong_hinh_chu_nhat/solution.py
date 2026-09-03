# Nhap x, y va HCN (0, 0) den (W, H)
parts = list(map(int, input().split()))
x, y, w, h = parts[0], parts[1], parts[2], parts[3]
if 0 <= x <= w and 0 <= y <= h:
    print("TRONG")
else:
    print("NGOAI")
