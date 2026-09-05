s = input()
kq = ''
dem = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        dem = dem + 1
    else:
        kq = kq + s[i - 1] + str(dem)
        dem = 1
kq = kq + s[-1] + str(dem)
print(kq)
