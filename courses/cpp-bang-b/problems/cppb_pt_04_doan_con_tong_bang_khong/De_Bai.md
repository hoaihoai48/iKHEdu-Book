# Đoạn Con Có Tổng Bằng 0

## Bối cảnh
Một tài khoản ngân hàng ghi nhận lịch sử N giao dịch biến động số dư liên tiếp (số dương là tiền vào, số âm là tiền ra). Chuyên viên kiểm toán nội bộ cần kiểm tra xem trong lịch sử giao dịch có tồn tại bất kỳ chuỗi giao dịch liên tiếp nào mà tổng dòng tiền ròng đúng bằng 0 hay không.

## Nhiệm vụ
Cho mảng gồm N số nguyên. Hãy kiểm tra xem có tồn tại ít nhất một đoạn con liên tiếp có tổng đúng bằng 0 hay không. Nếu có in ra YES, ngược lại in ra NO.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra `YES` nếu có đoạn con tổng bằng 0, ngược lại in ra `NO`.

## Sample 1
### Input
```text
5
4 2 -3 1 6
```
### Output
```text
YES
```
### Giải thích
Đoạn con [2, -3, 1] từ vị trí 2 đến vị trí 4 có tổng là 2 + (-3) + 1 = 0. Do đó in ra YES.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
