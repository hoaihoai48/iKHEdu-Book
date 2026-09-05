n = int(input())
tim_thay = False
while n > 0:
    if n % 10 == 7:
        tim_thay = True
    n = n // 10
if tim_thay:
    print("YES")
else:
    print("NO")
