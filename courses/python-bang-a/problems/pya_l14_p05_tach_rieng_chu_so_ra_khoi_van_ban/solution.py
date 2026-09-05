s = input()
kq = ''
for ch in s:
    if ch.isdigit():
        kq = kq + ch
if kq == '':
    print('KHONG CO')
else:
    print(kq)
