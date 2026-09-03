# Doc den khi gap so trung thuong 77
cnt = 0
while True:
    try:
        x = int(input().strip())
        cnt += 1
        if x == 77:
            break
    except:
        break
print(cnt)
