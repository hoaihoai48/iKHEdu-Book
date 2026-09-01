# Tìm cực tiểu của hàm bậc hai

## Bối cảnh
Cho hàm số bậc hai $f(x) = ax^2 + bx + c$ với hệ số $a > 0$ (hàm lồi trên tập số thực $\mathbb{R}$). Cần tìm giá trị của biến số $x$ trong đoạn $[L, R]$ sao cho giá trị $f(x)$ đạt cực tiểu.

## Nhiệm vụ
Hãy sử dụng thuật toán Tìm kiếm tam phân (Ternary Search) trên tập số thực để tìm hoành độ $x \in [L, R]$ làm cho $f(x)$ đạt giá trị nhỏ nhất với độ chính xác tuyệt đối không quá $10^{-6}$.

## Input
- Một dòng duy nhất chứa 5 số thực $a, b, c, L, R$ ($a > 0, -10^6 \le b, c, L, R \le 10^6, L \le R$).

## Output
- In ra giá trị $x$ tìm được với đúng 6 chữ số thập phân sau dấu phẩy.

## Sample 1
### Input
```text
1 -4 4 0 5
```
### Output
```text
2.000000
```
### Giải thích
* Hàm số $f(x) = x^2 - 4x + 4 = (x - 2)^2$ đạt giá trị nhỏ nhất bằng $0$ tại điểm cực trị $x = -b / (2a) = 2.000000$ thuộc đoạn $[0, 5]$.

## Ràng buộc
- $100\%$ số test có $a > 0, -10^6 \le b, c, L, R \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
