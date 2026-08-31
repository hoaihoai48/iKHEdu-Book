# Tối Ưu Hóa Chuỗi Dự Án Năng Lượng

## Bối cảnh
Có $N$ dự án năng lượng, mỗi dự án có ngưỡng sản lượng yêu cầu $V_i$ và lợi nhuận $C_i$. Một chuỗi đầu tư hợp lệ chỉ được chọn các dự án có $V$ tăng nghiêm ngặt.

## Nhiệm vụ
Tìm tổng lợi nhuận lớn nhất có thể đạt được từ một chuỗi đầu tư hợp lệ.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 2000$).
- $N$ dòng tiếp theo, mỗi dòng gồm 2 số nguyên $V_i, C_i$ ($1 \le V_i, C_i \le 10^9$).

## Output
- Tổng lợi nhuận lớn nhất.

## Sample 1
### Input
```text
3
10 100
5 50
20 200
```
### Output
```text
350
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 2000, 1 \le V_i, C_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
