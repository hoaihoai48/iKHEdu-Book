# So Sánh Đệ Quy Tuyến Tính & Chia Đôi Khi Tìm Min/Max

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy cài đặt hàm đệ quy chia đôi (Binary Recursion) để tìm giá trị nhỏ nhất và lớn nhất trong mảng.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra 2 số nguyên là giá trị nhỏ nhất và lớn nhất trong mảng, cách nhau bởi dấu cách.

## Sample 1
### Input
```text
6
3 1 7 9 2 8
```
### Output
```text
1 9
```
### Giải thích
Min = 1, Max = 9.

## Ràng buộc
- 100% số test có $N \le 1000, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
