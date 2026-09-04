s = input().strip()
t = 0
for c in s:
    if "0" <= c <= "9":
        t += ord(c) - ord("0")
if t % 7 == 0:
    print("YES")
else:
    print("NO")
