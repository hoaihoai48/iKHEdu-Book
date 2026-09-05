s = input()
hoa = 0
thuong = 0
for ch in s:
    if ch.isupper():
        hoa = hoa + 1
    elif ch.islower():
        thuong = thuong + 1
print(str(hoa) + ' ' + str(thuong))
