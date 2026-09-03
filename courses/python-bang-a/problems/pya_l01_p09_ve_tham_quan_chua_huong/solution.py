# 6 dong: a, b (ve nguoi lon, tre em doan 1), x, y (ve doan 2), n, m (tong nguoi lon, tre em)
# De bai: nhap lan luot cac gia tri
inputs = [int(input().strip()) for _ in range(6)]
a, b, x, y, n, m = inputs
so_tre_em = m
so_nguoi_lon = n - m
tong_tien = so_nguoi_lon * (a + x) + so_tre_em * (b + y)
print(tong_tien)
