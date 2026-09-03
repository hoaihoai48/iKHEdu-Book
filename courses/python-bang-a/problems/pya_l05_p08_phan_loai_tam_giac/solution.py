a, b, c = map(int, input().split())
if a == b == c:
    print("DEU")
elif a == b or b == c or a == c:
    print("CAN")
else:
    print("THUONG")
