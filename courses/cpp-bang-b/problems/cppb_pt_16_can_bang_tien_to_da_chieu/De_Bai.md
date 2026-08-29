# Cân Bằng Tiền Tố Đa Chiều

## Bối cảnh
Cho một chuỗi gồm $N$ ký tự chỉ gồm các chữ cái `'A'`, `'B'`, `'C'`. Hãy tìm độ dài của đoạn con liên tiếp dài nhất chứa số lượng ký tự `'A'`, `'B'`, `'C'` bằng nhau từng đôi một.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chuỗi $S$ gồm $N$ ký tự thuộc $\{'A', 'B', 'C'\}$.

## Output
- In ra một số nguyên duy nhất là độ dài lớn nhất của đoạn con cân bằng. Nếu không có, in `0`.

## Sample 1
### Input
```text
7
ABACABA
```
### Output
```text
3
```
*(Giải thích: Đoạn `BAC` hoặc `CAB` có độ dài 3 chứa đúng 1 ký tự A, 1 ký tự B, 1 ký tự C).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
