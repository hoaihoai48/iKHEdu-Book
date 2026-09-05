s = input()
n = len(s)
dai_nhat = 1
for i in range(n):
    for j in range(i + 1, n + 1):
        doan = s[i:j]
        if doan == doan[::-1]:
            if len(doan) > dai_nhat:
                dai_nhat = len(doan)
print(dai_nhat)
