# Quản Lý Tập Hợp Đa Trùng Lặp (Multiset)

## Bối cảnh
Hỗ trợ 3 loại thao tác: 1 x (Thêm x), 2 x (Xóa đúng 1 phần tử có giá trị x), 3 x (Đếm số lần xuất hiện của x).

## Nhiệm vụ
Với thao tác loại 3, in ra số lần xuất hiện.

## Input
- Dòng 1: Số nguyên $Q$ ($1 \le Q \le 50000$).
- $Q$ dòng tiếp theo: `type` và $x$ ($1 \le x \le 10^9$).

## Output
- Kết quả các thao tác loại 3.

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

## Ràng buộc
- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
