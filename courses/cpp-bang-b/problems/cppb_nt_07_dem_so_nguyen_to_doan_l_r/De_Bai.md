# Đếm Số Nguyên Tố Trong Đoạn [L, R]

## Bối cảnh
Một viện nghiên cứu toán học cần thống kê mật độ phân bố các số nguyên tố trên các khoảng số liệu thực nghiệm [L, R] qua Q truy vấn liên tục.

## Nhiệm vụ
Cho Q truy vấn, mỗi truy vấn gồm 2 số nguyên L, R (1 <= L <= R <= 10^6). Hãy đếm số lượng số nguyên tố nằm trong đoạn [L, R].

## Input
- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L$ và $R$ ($1 \le L \le R \le 10^6$).

## Output
- In ra $Q$ dòng, mỗi dòng là số lượng số nguyên tố tìm được.

## Sample 1
### Input
```text
3
1 10
10 20
20 30
```
### Output
```text
4
4
2
```
### Giải thích
- Đoạn [1, 10]: có 4 số nguyên tố {2, 3, 5, 7}.
- Đoạn [10, 20]: có 4 số nguyên tố {11, 13, 17, 19}.
- Đoạn [20, 30]: có 2 số nguyên tố {23, 29}.

## Ràng buộc
- $100\%$ số test có $Q \le 10^5, R \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
