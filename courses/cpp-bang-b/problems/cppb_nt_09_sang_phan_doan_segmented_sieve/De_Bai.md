# Sàng Phân Đoạn (Segmented Sieve)

## Bối cảnh
Khi cần tìm số nguyên tố trong một đoạn [L, R] với giá trị L, R có thể rất lớn (lên tới 10^12) nhưng độ dài đoạn R - L không quá 10^6, việc lập mảng thông thường bị tràn bộ nhớ. Kỹ thuật Sàng phân đoạn (Segmented Sieve) cho phép giải quyết bài toán này trong giới hạn bộ nhớ chặt chẽ.

## Nhiệm vụ
Cho hai số nguyên L, R (1 <= L <= R <= 10^12, R - L <= 10^6). Hãy đếm số lượng số nguyên tố trong đoạn [L, R].

## Input
- Một dòng duy nhất chứa 2 số nguyên $L$ và $R$.

## Output
- In ra một số nguyên duy nhất là số lượng số nguyên tố trong đoạn $[L, R]$.

## Sample 1
### Input
```text
10 20
```
### Output
```text
4
```
### Giải thích
Các số nguyên tố trong đoạn [10, 20] gồm {11, 13, 17, 19}, tổng cộng có 4 số.

## Ràng buộc
- $100\%$ số test có $1 \le L \le R \le 10^{12}, R - L \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
