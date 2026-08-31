# Hình Chữ Nhật Lớn Nhất Trên Histogram

## Bối cảnh
Cho biểu đồ cột gồm $N$ cột liền kề có chiều rộng bằng 1 và chiều cao lần lượt là $H_i$.

## Nhiệm vụ
Tìm diện tích hình chữ nhật lớn nhất có thể tạo thành từ các cột biểu đồ.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($0 \le H_i \le 10^9$).

## Output
- Diện tích lớn nhất.

## Sample 1
### Input
```text
6
2 1 5 6 2 3
```
### Output
```text
10
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le H_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
