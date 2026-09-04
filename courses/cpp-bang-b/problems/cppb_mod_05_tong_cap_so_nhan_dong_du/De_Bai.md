# Tính Tổng Cấp Số Nhân Đồng Dư

## Bối cảnh
Trong tính toán lãi suất kép liên tục qua N chu kỳ kinh tế với hệ số sinh lời A, tổng giá trị tích lũy tạo thành một chuỗi cấp số nhân S = 1 + A + A^2 + ... + A^N. Để tránh tràn số, giá trị này cần được tính đồng dư theo modulo M = 10^9 + 7 bằng kỹ thuật chia để trị O(log N).

## Nhiệm vụ
Cho A, N và M = 10^9 + 7. Hãy tính tổng S = 1 + A + A^2 + ... + A^N mod M.

## Input
- Một dòng chứa 2 số nguyên $A$ và $N$ ($0 \le A, N \le 10^9$).

## Output
- In ra giá trị tổng $S \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
2 3
```
### Output
```text
15
```
### Giải thích
S = 1 + 2 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15. Kết quả in ra: 15.

## Ràng buộc
- $100\%$ số test có $A, N \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
