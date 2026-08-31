# Đếm Cấu Hình Trạng Thái Phân Nhánh Không Trùng Lặp

**Phân loại bài toán:** `Advanced Challenge`

## Bối cảnh
Cho số nguyên dương $N$. Hãy đếm số lượng cây nhị phân tìm kiếm (BST) phân biệt có thể tạo thành từ $N$ khóa có giá trị từ $1$ đến $N$ bằng hàm đệ quy cấu trúc cây (hệ thức Catalan) mà không dùng `set/map` hay công thức đại số đóng.

## Input
- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 15$).

## Output
- In ra số lượng cây nhị phân phân biệt.

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
Với N = 3 nút, có đúng C_3 = 5 cây nhị phân tìm kiếm khác nhau.

## Ràng buộc
- 100% số test có $0 \le N \le 15$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
