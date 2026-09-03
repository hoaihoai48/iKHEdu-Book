n = int(input().strip())


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


cur = max(n, 2)
while True:
    s = str(cur)
    if s == s[::-1] and is_prime(cur):
        print(cur)
        break
    cur += 1
