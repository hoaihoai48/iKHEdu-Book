# Bậc của số nguyên Modulo P
## Mã bài toán: CPPB2-L01-18-BAC-CUA-SO-NGUYEN-ORDER

## Bối cảnh & Nhiệm vụ
Cho hai số nguyên dương $A$ và $P$ với $\gcd(A, P) = 1$. Tìm số nguyên dương $k$ nhỏ nhất sao cho $A^k \equiv 1 \pmod P$.

## Đầu vào (Input)
Gồm 2 số nguyên $A$ và $P$ ($P$ là số nguyên tố $\le 10^9$).

## Đầu ra (Output)
In ra bậc $k = \text{ord}_P(A)$.

## Ví dụ mẫu
### Sample 1
Input:
```text
2 7
```
Output:
```text
3
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
