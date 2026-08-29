# Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau

## Bối cảnh
Cho chuỗi ký tự $S$ gồm các chữ cái tiếng Anh in thường và số nguyên dương $K$. Hãy tìm độ dài của chuỗi con liên tiếp dài nhất chứa **không quá $K$ ký tự phân biệt**.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le 26, 1 \le N \le 10^5$).
- Dòng 2: Chuỗi ký tự $S$ có độ dài $N$.

## Output
- In ra một số nguyên duy nhất là độ dài lớn nhất tìm được.

## Sample 1
### Input
```text
7 2
ecebaaa
```
### Output
```text
4
```
### Giải thích
Chuỗi con `baaa` có độ dài 4 và chứa đúng 2 ký tự phân biệt là `b` và `a`.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, K \le 26$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
