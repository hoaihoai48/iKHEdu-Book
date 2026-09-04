# Phân Tích Thừa Số Nguyên Tố

## Bối cảnh
Một thuật toán nén dữ liệu số học cần phân rã một mã định danh nguyên dương N thành tích các thừa số nguyên tố lũy thừa để tối ưu không gian lưu trữ dạng cơ số tối giản.

## Nhiệm vụ
Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố theo dạng p1^e1 * p2^e2 * ... với p1 < p2 < ...

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($2 \le N \le 10^{12}$).

## Output
- In ra chuỗi phân tích thừa số nguyên tố theo định dạng `p^e` nối với nhau bởi dấu `*`.

## Sample 1
### Input
```text
60
```
### Output
```text
2^2 * 3^1 * 5^1
```
### Giải thích
60 = 4 * 3 * 5 = 2^2 * 3^1 * 5^1. Kết quả in ra: `2^2 * 3^1 * 5^1`.

## Ràng buộc
- $100\%$ số test có $2 \le N \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
