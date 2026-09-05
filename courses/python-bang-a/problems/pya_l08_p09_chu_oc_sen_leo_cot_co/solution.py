h = int(input())
a = int(input())
b = int(input())
cao = 0
ngay = 0
while True:
    ngay = ngay + 1
    cao = cao + a
    if cao >= h:
        break
    cao = cao - b
print(ngay)
