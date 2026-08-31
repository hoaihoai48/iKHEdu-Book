# Lũy Thừa Nhị Phân Đệ Quy A^B mod M

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho 3 số nguyên $A, B, M$. Hãy tính $A^B \pmod M$ bằng thuật toán Lũy thừa nhị phân đệ quy $\mathcal{O}(\log B)$ (chú ý chỉ gọi đệ quy 1 lần vào biến tạm `half` để tránh nổ thời gian).

## Input
- Một dòng duy nhất chứa 3 số nguyên $A, B, M$ ($0 \le A, B \le 10^{18}, 1 \le M \le 10^9 + 7$).

## Output
- In ra một số nguyên duy nhất là kết quả $A^B \pmod M$.

## Sample 1
### Input
```text
3 13 1000
```
### Output
```text
323
```
### Giải thích
3^13 = 1594323 -> 1594323 % 1000 = 323.

## Ràng buộc
- 100% số test có $A, B \le 10^{18}, M \le 10^9 + 7$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
