# Median Của Hai Mảng Đã Sắp Xếp

## Bối cảnh
Hợp nhất hai luồng dữ liệu thống kê đã có thứ tự để tìm giá trị trung vị trong thời gian tối ưu O(log(min(N, M))) là bài toán đỉnh cao về chia để trị kết hợp tìm kiếm nhị phân trên đường phân hoạch.

## Nhiệm vụ
Cho 2 mảng tăng dần A (kích thước N) và B (kích thước M). Hãy tìm giá trị trung vị của mảng hợp nhất với độ chính xác 1 chữ số thập phân trong thời gian O(log(min(N, M))).

## Input
- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên tăng dần của mảng $A$.
- Dòng 3: $M$ số nguyên tăng dần của mảng $B$.

## Output
- In ra giá trị trung vị làm tròn 1 chữ số sau dấu phẩy.

## Sample 1
### Input
```text
2 1
1 3
2
```
### Output
```text
2.0
```
### Giải thích
Mảng hợp nhất: [1, 2, 3] có 3 phần tử, phần tử ở giữa là 2. Trung vị là 2.0.

## Ràng buộc
- $100\%$ số test có $N, M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
