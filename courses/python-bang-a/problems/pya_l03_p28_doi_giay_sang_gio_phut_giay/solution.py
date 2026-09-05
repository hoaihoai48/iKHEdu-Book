t = int(input())
gio = t // 3600
phut = (t % 3600) // 60
giay = t % 60
print(f"{gio}:{phut}:{giay}")
