line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
if x in a:
    a.remove(x)
    print(*a)
else:
    print("KHONG CO")
