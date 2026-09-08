# Cài Đặt Fenwick Tree Tính Tổng Đoạn (Range Sum)

## Bối cảnh
Một máy chủ tài chính theo dõi biến động số dư tài khoản của $N$ khách hàng được đánh số từ $1$ đến $N$, số dư ban đầu tại tài khoản $i$ là $A_i$. Hệ thống liên tục tiếp nhận $Q$ giao dịch trực tuyến gồm hai loại: cộng thêm một khoản tiền $val$ vào tài khoản tại vị trí $pos$, hoặc truy vấn tính tổng số dư của tất cả các tài khoản nằm trong khoảng từ $L$ đến $R$. Mọi thao tác cần được xử lý tức thời.

## Nhiệm vụ
Cho mảng $A$ và $Q$ truy vấn thuộc hai loại: `1 pos val` (cộng $val$ vào $A[pos]$), `2 L R` (tính tổng các phần tử từ $L$ đến $R$). Hãy lập trình in ra kết quả của các truy vấn loại 2.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng chứa một truy vấn theo định dạng trên.

## Output
- Với mỗi truy vấn loại 2, in ra tổng các phần tử trên đoạn $[L, R]$ trên một dòng.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
2 1 3
1 2 10
2 1 3
```
### Output
```text
6
16
```

### Giải thích
Với mảng ban đầu gồm 5 phần tử $[1, 2, 3, 4, 5]$:

- Truy vấn tính tổng đoạn từ 1 đến 3: $1 + 2 + 3 = 6$.
- Cập nhật cộng thêm 10 vào phần tử tại vị trí 3: mảng trở thành $[1, 2, 13, 4, 5]$.
- Truy vấn lại tổng đoạn từ 1 đến 3: $1 + 2 + 13 = 16$.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
