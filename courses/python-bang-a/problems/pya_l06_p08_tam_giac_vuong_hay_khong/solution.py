dong1 = input().split()
if len(dong1) >= 3:
    a = int(dong1[0])
    b = int(dong1[1])
    c = int(dong1[2])
else:
    a = int(dong1[0])
    b = int(input().split()[0])
    c = int(input().split()[0])
if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("VUONG")
else:
    print("KHONG VUONG")
