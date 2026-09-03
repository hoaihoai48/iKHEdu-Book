line = input().split()
if len(line) == 2:
    a, b = map(int, line)
else:
    a = int(line[0])
    b = int(input().strip())
if a > b:
    print("a LON HON b")
elif a < b:
    print("a NHO HON b")
else:
    print("HAI SO BANG NHAU")
