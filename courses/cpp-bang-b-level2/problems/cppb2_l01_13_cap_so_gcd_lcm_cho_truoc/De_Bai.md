# Tìm cặp số biết GCD và LCM có tổng nhỏ nhất

## Bối cảnh
Cho hai số nguyên dương $G$ và $L$. Cần tìm hai số nguyên dương $A, B$ sao cho $\gcd(A, B) = G$, $\text{lcm}(A, B) = L$ và tổng $A + B$ đạt giá trị nhỏ nhất. Đặt $A = G \cdot a, B = G \cdot b \implies a \cdot b = L / G$ với $\gcd(a, b) = 1$. Ta chỉ cần phân tích $L / G$ thành các cặp thừa số nguyên tố cùng nhau.

## Nhiệm vụ
Cho hai số nguyên dương $G$ và $L$. Hãy lập trình tìm hai số $A \le B$ sao cho $\gcd(A, B) = G$, $\text{lcm}(A, B) = L$ và tổng $A + B$ nhỏ nhất; in `-1` nếu không tồn tại cặp số thỏa mãn.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $G, L$ ($1 \le G, L \le 10^{12}$).

## Output
- In ra hai số $A, B$ ($A \le B$) cách nhau bởi dấu cách. Nếu không tồn tại cặp số thỏa mãn, in `-1`.

## Sample 1
### Input
```text
2 60
```
### Output
```text
10 12
```
### Giải thích
* $L / G = 30 = 5 \times 6$ với $\gcd(5, 6) = 1 \implies A = 2 \times 5 = 10, B = 2 \times 6 = 12$ có tổng $10 + 12 = 22$ nhỏ nhất.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
