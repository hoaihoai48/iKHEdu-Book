n = int(input())
digits = []
while n > 0:
    digits.append(n % 10)
    n //= 10
digits = digits[::-1]
tang = all(digits[i] < digits[i + 1] for i in range(len(digits) - 1))
giam = all(digits[i] > digits[i + 1] for i in range(len(digits) - 1))
if tang:
    print("TANG")
elif giam:
    print("GIAM")
else:
    print("KHONG")
