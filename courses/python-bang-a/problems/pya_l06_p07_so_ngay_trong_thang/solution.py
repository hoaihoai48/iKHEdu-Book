line = input().split()
m, y = int(line[0]), int(line[1])
if m in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif m in [4, 6, 9, 11]:
    print(30)
elif m == 2:
    is_leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    print(29 if is_leap else 28)
