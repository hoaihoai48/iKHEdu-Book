# Thuật Toán Euclid Tính GCD & LCM Bằng Đệ Quy

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho 2 số nguyên dương $A, B$. Hãy tính ước chung lớn nhất $\gcd(A, B)$ và bội chung nhỏ nhất $\text{lcm}(A, B)$ bằng thuật toán Euclid đệ quy.

## Input
- Một dòng duy nhất chứa 2 số nguyên dương $A, B$ ($1 \le A, B \le 10^{18}$).

## Output
- In ra 2 số $\gcd(A, B)$ và $\text{lcm}(A, B)$ cách nhau bởi dấu cách. (Nếu LCM tràn số 64-bit, dùng `__int128`).

## Sample 1
### Input
```text
12 18
```
### Output
```text
6 36
```
### Giải thích
gcd(12, 18) = 6, lcm(12, 18) = 36.

## Ràng buộc
- 100% số test có $1 \le A, B \le 10^{18}$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
