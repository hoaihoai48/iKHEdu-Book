s = input().strip()
k = int(input().strip())
res = []
for ch in s:
    if 'A' <= ch <= 'Z':
        res.append(chr((ord(ch) - ord('A') - k) % 26 + ord('A')))
    else:
        res.append(ch)
print("".join(res))
