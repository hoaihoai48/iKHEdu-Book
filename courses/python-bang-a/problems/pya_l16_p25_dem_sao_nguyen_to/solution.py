n = int(input())
if n < 2:
    print(0)
else:
    is_p = [True] * (n + 1)
    is_p[0] = False
    is_p[1] = False
    i = 2
    while i * i <= n:
        if is_p[i]:
            j = i * i
            while j <= n:
                is_p[j] = False
                j += i
        i += 1
    print(sum(is_p))
