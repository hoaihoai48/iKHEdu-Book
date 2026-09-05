s = input()
kq = ''
for ch in s:
    if ch.isupper():
        kq = kq + ch.lower()
    elif ch.islower():
        kq = kq + ch.upper()
    else:
        kq = kq + ch
print(kq)
