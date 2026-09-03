k = int(input().strip())
cnt = 0
cur = 1
while True:
    if cur % 3 == 0 or cur % 5 == 0:
        cnt += 1
        if cnt == k:
            print(cur)
            exit()
    cur += 1
