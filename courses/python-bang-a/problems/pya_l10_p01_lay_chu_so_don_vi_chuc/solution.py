n = int(input())
don_vi = n % 10
temp = n
while temp >= 10:
    temp = temp // 10
chuc = temp
print(chuc, don_vi)
