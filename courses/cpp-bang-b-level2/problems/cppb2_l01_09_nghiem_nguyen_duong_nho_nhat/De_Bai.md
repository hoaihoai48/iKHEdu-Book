# Nghiệm Nguyên Dương Nhỏ Nhất Của Phương Trình Diophantine

## Bối cảnh
Xét phương trình Diophantine tuyến tính $A \cdot x + B \cdot y = C$ với các hệ số nguyên dương $A, B, C$. Bằng thuật toán Euclid mở rộng, ta có thể tìm được nghiệm tổng quát $x = x_0 + k \cdot \frac{B}{\gcd(A, B)}$.

## Nhiệm vụ
Nhiệm vụ của bạn là xác định xem phương trình có tồn tại nghiệm nguyên dương $(x > 0, y > 0)$ hay không, và nếu có hãy tìm nghiệm $(x, y)$ sao cho $x$ đạt giá trị nhỏ nhất.

## Input
- Dòng đầu chứa số bộ test $T$ ($1 \le T \le 10^5$).
- $T$ dòng tiếp theo, mỗi dòng chứa 3 số nguyên dương $A, B, C$ ($1 \le A, B, C \le 10^9$).

## Output
- Gồm $T$ dòng: In ra hai số nguyên $x, y$ biểu diễn nghiệm nguyên dương có $x$ nhỏ nhất. Nếu không tồn tại nghiệm nguyên dương, in ra `NO`.

## Sample 1
### Input
```text
3
2 3 13
4 6 11
5 7 35
```
### Output
```text
2 3
NO
NO
```
### Giải thích
* $2(2) + 3(3) = 4 + 9 = 13$ là nghiệm nguyên dương có $x$ nhỏ nhất ($x=2, y=3$).
* $4x + 6y = 11$ vô nghiệm vì $\gcd(4, 6) = 2$ không chia hết cho 11.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
