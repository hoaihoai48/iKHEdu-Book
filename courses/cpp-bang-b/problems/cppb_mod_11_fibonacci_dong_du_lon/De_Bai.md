# Dãy Fibonacci Đồng Dư Lớn

## Bối cảnh
Trong mô hình tăng trưởng quần thể sinh học, số lượng cá thể ở chu kỳ thứ N tuân theo dãy số Fibonacci F(N). Với N có thể lên tới 10^18, thuật toán nhân ma trận kết hợp lũy thừa nhị phân ma trận cho phép tìm số F(N) mod (10^9 + 7) trong thời gian O(log N).

## Nhiệm vụ
Cho số nguyên dương N (1 <= N <= 10^18). Hãy tìm số Fibonacci thứ N (với F(1) = 1, F(2) = 1, F(3) = 2, ...) theo modulo 10^9 + 7.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra $F_N \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
6
```
### Output
```text
8
```
### Giải thích
Dãy số Fibonacci: F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8. Kết quả in ra: 8.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
