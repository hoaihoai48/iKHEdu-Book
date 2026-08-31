# Dãy Fibonacci Đệ Quy & Khảo Sát Cây Gọi Hàm

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho số nguyên $N$. Hãy tính số Fibonacci $F_N$ ($F_0 = 0, F_1 = 1, F_N = F_{N-1} + F_{N-2}$) bằng hàm đệ quy thuần túy và đếm tổng số lần hàm `fib()` được gọi.

## Input
- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 30$).

## Output
- In ra 2 số nguyên là giá trị $F_N$ và tổng số lần gọi hàm `fib()`, cách nhau bởi dấu cách.

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
F(4) = 3. Tổng số lần gọi hàm fib là 9 lần.

## Ràng buộc
- 100% số test có $0 \le N \le 30$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
