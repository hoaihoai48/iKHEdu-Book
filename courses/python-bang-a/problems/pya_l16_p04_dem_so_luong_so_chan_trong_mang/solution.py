n = int(input().strip())
a = list(map(int, input().split()))
print(sum(1 for x in a if x % 2 == 0))
