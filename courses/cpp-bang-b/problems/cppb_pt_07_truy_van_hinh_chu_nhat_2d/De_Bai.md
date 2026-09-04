# Truy Vấn Tổng Hình Chữ Nhật 2D

## Bối cảnh
Bản đồ nhiệt độ của một vùng biển được mô phỏng dưới dạng ma trận số nguyên kích thước N hàng và M cột. Các nhà hải dương học cần trả lời Q truy vấn độc lập từ trạm khí tượng, mỗi truy vấn yêu cầu tính tổng nhiệt độ trong một vùng hình chữ nhật giới hạn bởi góc trên-trái (r1, c1) và góc dưới-phải (r2, c2).

## Nhiệm vụ
Cho ma trận số nguyên A kích thước N x M. Hãy trả lời Q truy vấn tính tổng các phần tử trong hình chữ nhật từ (r1, c1) đến (r2, c2) bằng kỹ thuật Mảng tiền tố 2D.

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($-10^9 \le A_{i, j} \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $r_1, c_1, r_2, c_2$ ($1 \le r_1 \le r_2 \le N, 1 \le c_1 \le c_2 \le M$).

## Output
- In ra $Q$ dòng tương ứng với kết quả của mỗi truy vấn.

## Sample 1
### Input
```text
3 3 2
1 2 3
4 5 6
7 8 9
1 1 2 2
2 2 3 3
```
### Output
```text
12
28
```
### Giải thích
- Vùng từ (1, 1) đến (2, 2) gồm các ô {1, 2, 4, 5} có tổng: 1 + 2 + 4 + 5 = 12.
- Vùng từ (2, 2) đến (3, 3) gồm các ô {5, 6, 8, 9} có tổng: 5 + 6 + 8 + 9 = 28.

## Ràng buộc
- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
