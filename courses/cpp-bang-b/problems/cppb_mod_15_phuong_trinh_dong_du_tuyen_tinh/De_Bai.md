# Giải Phương Trình Đồng Dư Tuyến Tính Ax = B mod M

> [!NOTE]
> **Phân loại bài toán:** `Advanced Challenge` (Thử thách mở rộng)
## Bối cảnh
Cho 3 số nguyên $A, B, M$. Hãy tìm nghiệm nguyên không âm nhỏ nhất $X$ của phương trình $A \times X \equiv B \pmod M$. Nếu vô nghiệm in `-1`.

## Input
- Một dòng duy nhất chứa 3 số nguyên $A, B, M$ ($1 \le A, B, M \le 10^9$).

## Output
- In ra nghiệm $X$ nhỏ nhất ($0 \le X < M$), hoặc `-1` nếu vô nghiệm.

## Sample 1
### Input
```text
14 30 100
```
### Output
```text
95
```
### Giải thích
14 * 95 = 1330 = 30 mod 100.

## Ràng buộc
- $100\%$ số test có $A, B, M \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
