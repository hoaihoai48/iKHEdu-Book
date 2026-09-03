n = int(input().strip())
a = list(map(int, input().split()))
mx = max(a)
candidates = [x for x in a if x < mx]
if candidates:
    print(max(candidates))
else:
    print("KHONG CO")
