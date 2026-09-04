# Phép Tính Đồng Dư Cơ Bản (+, -, *)

## Bối cảnh
Trong kỹ thuật mã hóa dữ liệu đối xứng, các phép toán cộng, trừ, nhân trên số nguyên lớn đòi hỏi phải luôn được thu hẹp về vành số nguyên hữu hạn Z_M với M = 10^9 + 7 để tránh hoàn toàn hiện tượng tràn số nguyên 64-bit và duy trì tính khép kín của thuật toán.

## Nhiệm vụ
Cho 2 số nguyên A, B và số nguyên dương M = 10^9 + 7. Hãy tính (A + B) mod M, (A - B) mod M và (A * B) mod M sao cho kết quả luôn thuộc [0, M - 1].

## Input
- Một dòng duy nhất chứa 2 số nguyên $A$ và $B$ ($0 \le A, B \le 10^{18}$).

## Output
- In ra 3 số nguyên cách nhau bởi khoảng trắng lần lượt là tổng, hiệu và tích theo modulo $M = 10^9 + 7$.

## Sample 1
### Input
```text
10 15
```
### Output
```text
25 1000000002 150
```
### Giải thích
Với M = 10^9 + 7:
- Tổng: (10 + 15) mod M = 25.
- Hiệu: (10 - 15) mod M = -5 mod M = 10^9 + 7 - 5 = 1000000002.
- Tích: (10 * 15) mod M = 150.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
