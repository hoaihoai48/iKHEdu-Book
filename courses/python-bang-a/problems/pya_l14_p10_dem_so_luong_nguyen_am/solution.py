s = input()
dem = 0
for ch in s:
    if ch in 'AEIOUaeiou':
        dem = dem + 1
print(dem)
