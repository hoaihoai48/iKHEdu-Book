# Cài Đặt Hàng Đợi Cơ Bản

## Bối cảnh
Mô phỏng hàng đợi FIFO với 3 thao tác: `1 x` (Thêm x vào đuôi), `2` (Xóa đầu hàng đợi), `3` (In ra phần tử ở đầu hàng đợi hoặc `EMPTY`).

## Nhiệm vụ
In ra kết quả của các thao tác loại 3.

## Input
- Dòng 1: Số nguyên $Q$ ($1 \le Q \le 50000$).
- $Q$ dòng tiếp theo chứa các thao tác.

## Output
- Kết quả các thao tác loại 3.

## Sample 1
### Input
```text
5
1 10
1 20
3
2
3
```
### Output
```text
10
20
```

## Ràng buộc
- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
