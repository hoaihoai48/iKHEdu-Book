tong_giay = int(input())
gio = tong_giay // 3600
giay_du = tong_giay % 3600
phut = giay_du // 60
giay = giay_du % 60
print(gio, phut, giay)
