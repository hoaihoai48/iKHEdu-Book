dong1 = input().split()
if len(dong1) >= 2:
    a = int(dong1[0])
    b = int(dong1[1])
else:
    a = int(dong1[0])
    b = int(input().split()[0])
if a % b == 0:
    print("YES")
else:
    print("NO")
