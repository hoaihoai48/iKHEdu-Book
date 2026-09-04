# Bài Toán Tổng Tập Con Bằng S (Subset Sum)

## Bối cảnh
Trong két sắt chứa N thỏi vàng có khối lượng lần lượt là A1, A2, ..., An. Một khách hàng muốn mua đúng lượng vàng có tổng khối lượng bằng S chỉ vàng. Hãy kiểm tra xem có thể chọn ra một tập con các thỏi vàng trong két để có tổng khối lượng đúng bằng S hay không.

## Nhiệm vụ
Cho dãy gồm N số nguyên dương và số nguyên dương S. Hãy kiểm tra xem có tồn tại một tập con có tổng đúng bằng S hay không. In YES nếu có, ngược lại in NO.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 20, 1 \le S \le 10^9$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
4 9
3 34 4 12
```
### Output
```text
NO
```
### Giải thích
Các tập con có thể tạo được từ {3, 34, 4, 12} có tổng lần lượt là: 0, 3, 34, 37, 4, 7, 38, 41, 12, 15, 46, 49, 16, 19, 50, 53. Không có tập con nào có tổng bằng 9. Vì vậy in NO.

## Ràng buộc
- $100\%$ số test có $N \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
