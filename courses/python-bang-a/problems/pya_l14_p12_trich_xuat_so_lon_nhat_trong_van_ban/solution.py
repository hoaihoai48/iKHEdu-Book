s = input()
lon_nhat = -1
so_hien_tai = ''
for ch in s + ' ':
    if ch.isdigit():
        so_hien_tai = so_hien_tai + ch
    else:
        if so_hien_tai != '':
            if int(so_hien_tai) > lon_nhat:
                lon_nhat = int(so_hien_tai)
            so_hien_tai = ''
print(lon_nhat)
