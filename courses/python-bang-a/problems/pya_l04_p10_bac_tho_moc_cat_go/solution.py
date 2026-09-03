line = input().split()
if len(line) == 2:
    l, k = map(int, line)
else:
    l = int(line[0])
    k = int(input().strip())
if l >= k:
    print(l // k, l % k)
else:
    print("KHONG DU")
