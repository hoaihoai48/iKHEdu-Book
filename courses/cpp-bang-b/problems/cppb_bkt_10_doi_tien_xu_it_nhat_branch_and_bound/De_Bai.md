# Đổi Tiền Xu Ít Nhất (B&B Coin Change)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Một cây ATM thông minh tại sân bay quốc tế được nạp $N$ loại tiền xu có mệnh giá khác nhau $C_1, C_2, \dots, C_N$ (số lượng mỗi loại xu trong kho không hạn chế). Khi một du khách yêu cầu đổi một lượng tiền lẻ bằng đúng $S$, hệ thống cần chi trả sao cho tổng số đồng xu trao cho khách là ít nhất có thể để tiết kiệm dung lượng khay xuất tiền.

## Nhiệm vụ
Cho $N$ mệnh giá tiền xu $C_1, C_2, \dots, C_N$ và số tiền cần đổi $S$. Hãy áp dụng thuật toán Nhánh Cận (Branch and Bound) với hàm cận dưới tối ưu để tìm số lượng đồng xu ít nhất cần dùng để đổi đúng số tiền $S$. Nếu không có phương án đổi tiền nào hợp lệ, in ra `-1`.

## Input
- Dòng 1: Hai số nguyên dương $N$ và $S$ ($1 \le N \le 15, 1 \le S \le 100$).
- Dòng 2: $N$ số nguyên dương $C_1, C_2, \dots, C_N$ ($1 \le C_i \le 100$).

## Output
- In ra số lượng đồng xu ít nhất cần dùng, hoặc in `-1` nếu không thể đổi được.

## Sample 1
### Input
```text
3 11
1 2 5
```
### Output
```text
3
```
### Giải thích
Với số tiền $S = 11$ và các mệnh giá $\{1, 2, 5\}$, phương án tối ưu nhất là chọn hai đồng mệnh giá 5 và một đồng mệnh giá 1 ($5 + 5 + 1 = 11$). Tổng số đồng xu sử dụng là 3 đồng.

## Ràng buộc
- 100% số test có $1 \le N \le 15, 1 \le S \le 100$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
