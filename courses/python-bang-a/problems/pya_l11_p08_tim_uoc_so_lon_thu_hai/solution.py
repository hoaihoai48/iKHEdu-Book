n = int(input())
ket_qua = 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        ket_qua = n // i
        break
print(ket_qua)
