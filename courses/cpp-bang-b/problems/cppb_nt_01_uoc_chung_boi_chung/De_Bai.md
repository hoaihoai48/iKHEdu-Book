# Ước Chung Lớn Nhất & Bội Chung Nhỏ Nhất

## Bối cảnh
Trong kỹ thuật thiết kế bánh răng truyền động cơ khí, hai bánh răng A và B có số răng lần lượt là A và B. Để hai bánh răng ăn khớp nhịp nhàng theo chu kỳ mà không làm mòn lệch răng, các kỹ sư cần xác định ước chung lớn nhất (để thiết kế bước răng chung) và bội chung nhỏ nhất (để xác định chu kỳ quay lặp lại trạng thái ban đầu).

## Nhiệm vụ
Cho hai số nguyên dương A và B. Hãy tìm ước chung lớn nhất gcd(A, B) và bội chung nhỏ nhất lcm(A, B).

## Input
- Một dòng duy nhất chứa 2 số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^{12}$).

## Output
- In ra 2 số nguyên cách nhau bởi khoảng trắng: $\gcd(A, B)$ và $\text{lcm}(A, B)$.

## Sample 1
### Input
```text
12 18
```
### Output
```text
6 36
```
### Giải thích
gcd(12, 18) = 6 và lcm(12, 18) = (12 * 18) / 6 = 36. Kết quả in ra: 6 36.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
