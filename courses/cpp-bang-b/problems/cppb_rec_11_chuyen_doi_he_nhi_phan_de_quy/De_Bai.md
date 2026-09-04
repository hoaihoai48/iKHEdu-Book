# Chuyển Đổi Hệ Cơ Số 10 Sang Nhị Phân Bằng Đệ Quy

## Bối cảnh
Cơ chế ngăn xếp gọi hàm đệ quy tự nhiên đảo ngược thứ tự các số dư khi chia liên tiếp cho 2, giúp in ra biểu diễn nhị phân của số nguyên N từ bit có trọng số lớn nhất đến bit 0 một cách tự nhiên mà không cần mảng phụ.

## Nhiệm vụ
Cho số nguyên không âm N. Hãy in ra biểu diễn nhị phân của N bằng hàm đệ quy.

## Input
- Một dòng chứa số nguyên không âm $N$ ($0 \le N \le 10^{18}$).

## Output
- In ra chuỗi nhị phân của $N$.

## Sample 1
### Input
```text
10
```
### Output
```text
1010
```
### Giải thích
Số 10 trong hệ thập phân chuyển sang nhị phân là 1010_2.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
