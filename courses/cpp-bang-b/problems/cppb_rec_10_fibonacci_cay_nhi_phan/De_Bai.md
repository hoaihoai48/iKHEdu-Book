# Dãy Fibonacci Đệ Quy & Khảo Sát Cây Gọi Hàm

## Bối cảnh
Để khảo sát sự bùng nổ theo cấp số nhân của cây gọi hàm đệ quy không nhớ (Exponential Call Tree), hãy viết hàm đệ quy tính số Fibonacci thứ N và đếm tổng số lần hàm fibonacci() được gọi thực thi.

## Nhiệm vụ
Cho số nguyên N (0 <= N <= 30). Hãy tính giá trị F_N và đếm tổng số lần gọi hàm fibonacci() trong toàn bộ quá trình thực thi.

## Input
- Một dòng chứa số nguyên $N$ ($0 \le N \le 30$).

## Output
- In ra 2 số nguyên cách nhau bởi khoảng trắng: giá trị $F_N$ và tổng số lần gọi hàm.

## Sample 1
### Input
```text
4
```
### Output
```text
3 9
```
### Giải thích
F(4) = 3. Cây gọi hàm fib(4) gồm 9 lần gọi hàm: fib(4) gọi fib(3) và fib(2); fib(3) gọi fib(2) và fib(1); v.v. Tổng số lần gọi là 9.

## Ràng buộc
- $100\%$ số test có $N \le 30$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
