# Tính Số Chỉnh Hợp A(N, K) mod M

> [!NOTE]
> **Phân loại bài toán:** `Advanced Challenge` (Thử thách mở rộng)
## Bối cảnh
Cho $Q$ truy vấn, mỗi truy vấn chứa 2 số $N, K$. Hãy tính số chỉnh hợp $A(N, K) = \frac{N!}{(N - K)!} \pmod{10^9 + 7}$.

## Input
- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số $N, K$ ($0 \le K \le N \le 10^6$).

## Output
- In ra $Q$ dòng tương ứng là $A(N, K) \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
2
4 2
5 3
```
### Output
```text
12
60
```
### Giải thích
A(4, 2) = 4 * 3 = 12. A(5, 3) = 5 * 4 * 3 = 60.

## Ràng buộc
- $100\%$ số test có $Q \le 10^5, N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
