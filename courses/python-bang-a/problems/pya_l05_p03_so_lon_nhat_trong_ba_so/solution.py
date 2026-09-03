line = input().split()
if len(line) == 3:
    a, b, c = map(int, line)
else:
    a = int(line[0])
    b = int(input().strip())
    c = int(input().strip())
print(max(a, b, c))
