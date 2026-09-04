# Thuật Toán Euclid Tính GCD & LCM Bằng Đệ Quy

## Bối cảnh
Thuật toán Euclid cổ đại phát biểu dưới dạng đệ quy một dòng gcd(A, B) = (B == 0) ? A : gcd(B, A % B) là một trong những thuật toán đẹp đẽ và hiệu quả nhất lịch sử toán học. Hãy dùng hàm đệ quy này để tính ước chung lớn nhất và bội chung nhỏ nhất.

## Nhiệm vụ
Cho 2 số nguyên dương A, B. Hãy tính ước chung lớn nhất gcd(A, B) và bội chung nhỏ nhất lcm(A, B) bằng hàm đệ quy Euclid.

## Input
- Một dòng chứa 2 số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^{12}$).

## Output
- In ra $\gcd(A, B)$ và $\text{lcm}(A, B)$ cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
24 36
```
### Output
```text
12 72
```
### Giải thích
gcd(24, 36) = 12 và lcm(24, 36) = (24 * 36) / 12 = 72.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
