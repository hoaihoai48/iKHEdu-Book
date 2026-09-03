a, b = map(int, input().split())
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("CUNG DAU")
elif (a > 0 and b < 0) or (a < 0 and b > 0):
    print("TRAI DAU")
else:
    print("CO SO KHONG")
