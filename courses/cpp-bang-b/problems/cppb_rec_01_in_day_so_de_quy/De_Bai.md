# In Dãy Số Đệ Quy 1..N và N..1

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho số nguyên dương $N$. Hãy in ra 2 dòng:
- Dòng 1: In các số từ $1$ đến $N$ cách nhau bởi dấu cách.
- Dòng 2: In các số từ $N$ về $1$ cách nhau bởi dấu cách.
Bắt buộc sử dụng 2 hàm đệ quy riêng biệt để rèn luyện tư duy Winding vs Unwinding.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 1000$).

## Output
- Dòng 1: $N$ số từ $1$ đến $N$.
- Dòng 2: $N$ số từ $N$ về $1$.

## Sample 1
### Input
```text
4
```
### Output
```text
1 2 3 4
4 3 2 1
```
### Giải thích
Dòng 1 in trong pha Unwinding (1..4), dòng 2 in trong pha Winding (4..1).

## Ràng buộc
- 100% số test có $1 \le N \le 1000$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
