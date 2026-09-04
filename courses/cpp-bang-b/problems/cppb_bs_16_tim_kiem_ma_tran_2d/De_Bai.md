# Tìm Kiếm Trên Ma Trận 2D Đã Sắp Xếp (Matrix Search)

## Bối cảnh
Một bảng cơ sở dữ liệu dạng ma trận kích thước N x M ô chứa các bản ghi mã định danh tài khoản, trong đó mỗi hàng được sắp xếp tăng dần từ trái qua phải, và phần tử đầu tiên của mỗi hàng lớn hơn phần tử cuối cùng của hàng trước đó. Hãy kiểm tra xem tài khoản có mã X có tồn tại trong cơ sở dữ liệu hay không.

## Nhiệm vụ
Cho ma trận N x M đã sắp xếp theo quy tắc trên và số nguyên X. Hãy kiểm tra xem X có tồn tại trong ma trận không. In YES nếu có, ngược lại in NO.

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, X$ ($1 \le N, M \le 1000, -10^9 \le X \le 10^9$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên đã sắp xếp.

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
3 4 3
1 3 5 7
10 11 16 20
23 30 34 60
```
### Output
```text
YES
```
### Giải thích
Số X = 3 nằm ở hàng 1, cột 2 của ma trận -> in YES.

## Ràng buộc
- $100\%$ số test có $N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
