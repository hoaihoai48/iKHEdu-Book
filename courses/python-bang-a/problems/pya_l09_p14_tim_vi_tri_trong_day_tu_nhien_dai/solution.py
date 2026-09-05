k = int(input().strip())
length = 1
count = 9
start = 1
while k > length * count:
    k -= length * count
    length += 1
    count *= 10
    start *= 10
num = start + (k - 1) // length
idx = (k - 1) % length
print(str(num)[idx])
