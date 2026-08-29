# Đoạn Con Ngắn Nhất Chứa Đủ Mọi Ký Tự Của Tập Hợp

## Bối cảnh
Cho chuỗi $S$ gồm các chữ cái in thường và chuỗi mẫu $T$ gồm $M$ ký tự phân biệt. Hãy tìm độ dài ngắn nhất của một chuỗi con liên tiếp trong $S$ chứa đầy đủ tất cả các ký tự có trong $T$. Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $M$ ($1 \le M \le 26, 1 \le N \le 10^5$).
- Dòng 2: Chuỗi $S$ có độ dài $N$.
- Dòng 3: Chuỗi $T$ có độ dài $M$ gồm các ký tự phân biệt.

## Output
- In ra độ dài ngắn nhất tìm được hoặc `-1`.

## Sample 1
### Input
```text
8 3
adobecod
abc
```
### Output
```text
6
```
### Giải thích
Chuỗi con `adobec` dài 6 chứa đủ `a`, `b`, `c`.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, M \le 26$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
