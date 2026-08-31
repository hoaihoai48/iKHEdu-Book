# Đếm Số Cách Đổi Tiền

## Bối cảnh
Cho $N$ loại đồng xu và số tiền $S$. Mỗi loại xu có số lượng không giới hạn.

## Nhiệm vụ
Đếm số tổ hợp khác nhau để tạo thành số tiền $S$ lấy dư theo modulo $10^9+7$ (hai cách chỉ khác nhau về thứ tự xu được tính là 1 cách).

## Input
- Dòng 1: $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$).
- Dòng 2: $N$ số nguyên dương $c_i$ ($1 \le c_i \le 10^4$).

## Output
- Số cách đổi tiền theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
3 9
2 3 5
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
