n = int(input().strip())
a = list(map(int, input().split()))
if n == 0:
    print(0)
    exit()
max_len = 1
cur_len = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)
