# Duyệt Tất Cả Các Tập Con Của Một Mặt Nạ Bit

## Bối cảnh
Cho một số nguyên dương $N$ biểu diễn một mặt nạ bit. Hãy liệt kê tất cả các số nguyên $S > 0$ là tập con thực sự của $N$ (tức mọi bit 1 của $S$ đều là bit 1 của $N$) theo thứ tự giảm dần.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^9$).

## Output
- In ra tất cả các submask dương của $N$ trên một dòng, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
11
```
### Output
```text
11 10 9 8 3 2 1
```
*(Giải thích: $11 = 1011_2$. Các submask là $1011_2 (11), 1010_2 (10), 1001_2 (9), 1000_2 (8), 0011_2 (3), 0010_2 (2), 0001_2 (1)$).*

## Ràng buộc
- $100\%$ số test có $N \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
