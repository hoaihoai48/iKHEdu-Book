# Tìm Dãy Con Có Tổng XOR Bằng K

## Bối cảnh
Trong một giao thức mã kiểm tra dư thừa nhị phân, máy thu nhận được N khối dữ liệu A1, A2, ..., An. Người nhận cần kiểm tra xem có tồn tại một tập con khác rỗng nào các khối dữ liệu có tích lũy phép toán XOR đúng bằng mã chứng thực K hay không.

## Nhiệm vụ
Cho tập hợp gồm N số nguyên dương và số nguyên K. Hãy kiểm tra xem có tồn tại một dãy con khác rỗng có tổng XOR bằng K hay không. In YES nếu có, ngược lại in NO.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 20, 0 \le K \le 10^9$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
4 7
1 2 4 8
```
### Output
```text
YES
```
### Giải thích
Chọn tập con gồm 3 phần tử {1, 2, 4} có tổng XOR là 1 ^ 2 ^ 4 = 7 đúng bằng K. Kết quả in ra: YES.

## Ràng buộc
- $100\%$ số test có $N \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
