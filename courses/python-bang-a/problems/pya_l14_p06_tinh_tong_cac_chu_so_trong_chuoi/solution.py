s = input()
tong = 0
for ch in s:
    if ch.isdigit():
        tong = tong + int(ch)
print(tong)
