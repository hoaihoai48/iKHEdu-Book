# Đếm Cấu Hình Trạng Thái Phân Nhánh Không Trùng Lặp

## Bối cảnh
Trong cấu trúc dữ liệu cây nhị phân tìm kiếm (Binary Search Tree - BST), với N khóa giá trị phân biệt từ 1 đến N, mỗi cấu hình cây khác nhau biểu diễn một trạng thái phân nhánh độc lập. Công thức đệ quy phân chia cây con trái kích thước i và cây con phải kích thước N - 1 - i cho phép đếm chính xác số lượng cây nhị phân tìm kiếm khác nhau.

## Nhiệm vụ
Cho số nguyên dương N. Hãy đếm số lượng cây nhị phân tìm kiếm (BST) phân biệt có thể tạo thành từ N nút mang các giá trị từ 1 đến N.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 15$).

## Output
- In ra số lượng cây BST phân biệt.

## Sample 1
### Input
```text
3
```
### Output
```text
5
```
### Giải thích
Với N = 3 có đúng 5 cấu hình cây BST khác nhau (chính là số Catalan C_3 = 5). Kết quả in ra: 5.

## Ràng buộc
- $100\%$ số test có $N \le 15$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
