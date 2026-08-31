# Tính Số Tổ Hợp C(N, K) mod M

> [!NOTE]
> **Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho $Q$ truy vấn, mỗi truy vấn chứa 2 số $N, K$. Hãy tính $C(N, K) \pmod{10^9 + 7}$.

## Input
- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số $N, K$ ($0 \le K \le N \le 10^6$).

## Output
- In ra $Q$ dòng tương ứng là kết quả $C(N, K) \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
3
5 2
6 3
10 0
```
### Output
```text
10
20
1
```
### Giải thích
C(5, 2) = 10, C(6, 3) = 20, C(10, 0) = 1.

## Ràng buộc
- $100\%$ số test có $Q \le 10^5, N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
