# Mảng Tiền Tố XOR Đoạn Con

## Bối cảnh
Cho dãy số nguyên gồm $N$ phần tử. Có $Q$ truy vấn, mỗi truy vấn yêu cầu tính tích XOR của các phần tử trong đoạn từ $L$ đến $R$:
$$\text{XOR}(L, R) = A_L \oplus A_{L+1} \oplus \cdots \oplus A_R$$

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L, R$ ($1 \le L \le R \le N$).

## Output
- In ra $Q$ dòng kết quả tương ứng.

## Sample 1
### Input
```text
5 3
1 3 4 2 2
1 3
2 4
1 5
```
### Output
```text
6
5
6
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 2 \cdot 10^5, 0 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
