# Quản Lý Tập Hợp Đa Trùng Lặp (Multiset)

## Bối cảnh
Một kho hàng thông minh hỗ trợ 3 loại thao tác quản lý sản phẩm: thêm một sản phẩm có mã giá $x$ vào kho, xóa bỏ đúng một sản phẩm có mã giá $x$ khỏi kho (nếu có), và truy vấn sản phẩm có mã giá rẻ nhất hiện đang có trong kho.

## Nhiệm vụ
Cho $Q$ thao tác thuộc một trong 3 loại: `1 x` (thêm $x$), `2 x` (xóa một phần tử $x$), `3` (in ra giá trị nhỏ nhất hiện tại). Hãy lập trình mô phỏng lại hệ thống và in ra kết quả cho các thao tác loại 3.

## Input
- Dòng 1: Chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo chứa các thao tác mô tả như trên.

## Output
- Với mỗi thao tác loại 3, in ra giá trị nhỏ nhất hiện tại trên một dòng.

## Sample 1
### Input
```text
5
1 5
1 5
3 5
2 5
3 5
```
### Output
```text
2
1
```

### Giải thích
Với chuỗi thao tác: thêm 5, thêm 2, thêm 5, truy vấn min -> in ra 2; xóa 2, truy vấn min -> in ra 5.

## Ràng buộc
- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
