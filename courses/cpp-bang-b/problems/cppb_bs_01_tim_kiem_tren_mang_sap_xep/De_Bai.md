# Tìm Kiếm Phần Tử Trên Mảng Đã Sắp Xếp

## Bối cảnh
Tại một thư viện điện tử quốc gia, danh mục gồm N cuốn sách quý hiếm đã được sắp xếp theo số hiệu mã vạch tăng dần. Để phục vụ độc giả tra cứu nhanh trong hàng trăm ngàn đầu sách, thủ thư nhận Q yêu cầu tìm kiếm xem mã sách X có tồn tại trong hệ thống hay không.

## Nhiệm vụ
Cho mảng N số nguyên đã sắp xếp tăng dần. Với mỗi truy vấn chứa số nguyên X, hãy kiểm tra xem X có xuất hiện trong mảng hay không bằng thuật toán Tìm kiếm nhị phân. Nếu có in YES, ngược lại in NO.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên tăng dần $A_1 \le A_2 \le \dots \le A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa một số nguyên $X$ ($-10^9 \le X \le 10^9$).

## Output
- In ra $Q$ dòng, mỗi dòng là `YES` hoặc `NO`.

## Sample 1
### Input
```text
5 3
1 3 5 7 9
5
4
9
```
### Output
```text
YES
NO
YES
```
### Giải thích
- Truy vấn 1: Số 5 xuất hiện tại vị trí 3 -> YES.
- Truy vấn 2: Số 4 không có trong mảng -> NO.
- Truy vấn 3: Số 9 xuất hiện tại vị trí 5 -> YES.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
