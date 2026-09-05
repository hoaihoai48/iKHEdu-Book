n = int(input())
ket_qua = []
for num in range(2, n + 1):
    tong = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num // i
            if i < num:
                tong = tong + i
            if j != i and j < num:
                tong = tong + j
    if tong == num:
        ket_qua.append(str(num))
if ket_qua:
    print(" ".join(ket_qua))
