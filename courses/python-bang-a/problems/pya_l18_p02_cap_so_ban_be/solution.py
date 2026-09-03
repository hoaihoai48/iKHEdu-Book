line = input().split()
a, b = line[0], line[1]
if sum(int(c) for c in a) == sum(int(c) for c in b):
    print("YES")
else:
    print("NO")
