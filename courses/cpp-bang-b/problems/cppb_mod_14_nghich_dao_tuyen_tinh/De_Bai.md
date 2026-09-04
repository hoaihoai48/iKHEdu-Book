# Nghịch Đảo Tuyến Tính 1..N Trong O(N)

## Bối cảnh
Khi cần tính nghịch đảo modulo cho toàn bộ các số từ 1 đến N (với N lên tới 10^6) theo modulo M = 10^9 + 7, nếu tính riêng lẻ bằng lũy thừa nhị phân Fermat sẽ tốn O(N log M) dễ bị vượt quá thời gian. Công thức nghịch đảo tuyến tính cho phép tính trước toàn bộ mảng nghịch đảo chỉ trong đúng O(N).

## Nhiệm vụ
Cho số nguyên N và M = 10^9 + 7. Hãy tính và in ra nghịch đảo modulo của tất cả các số từ 1 đến N theo modulo M trong thời gian O(N).

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

## Output
- In ra $N$ số nguyên cách nhau bởi khoảng trắng là nghịch đảo modulo tương ứng của các số từ $1$ đến $N$.

## Sample 1
### Input
```text
3
```
### Output
```text
1 500000004 333333336
```
### Giải thích
- inv(1) = 1.
- inv(2) = 500000004 (vì 2 * 500000004 = 1 mod M).
- inv(3) = 333333336 (vì 3 * 333333336 = 1000000008 = 1 mod M).

## Ràng buộc
- $100\%$ số test có $N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
