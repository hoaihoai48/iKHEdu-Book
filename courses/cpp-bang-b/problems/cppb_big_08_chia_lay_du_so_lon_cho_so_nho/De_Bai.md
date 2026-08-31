# Chia Lấy Dư Số Lớn Cho Số Nhỏ

> [!NOTE]
> **Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho số nguyên lớn $A$ và số nguyên nhỏ $b$ ($1 \le b \le 10^{18}$). Hãy tính $A \pmod b$.

## Input
- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Số nguyên dương $b$ ($1 \le b \le 10^{18}$).

## Output
- In ra số dư $A \pmod b$.

## Sample 1
### Input
```text
123456789
100
```
### Output
```text
89
```
### Giải thích
123456789 % 100 = 89.

## Ràng buộc
- $100\%$ số test có $|A| \le 10^5, b \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
