# Bài Toán Cái Túi 0/1 Nhánh Cận (B&B Knapsack)

**Phân loại bài toán:** `Advanced`

## Bối cảnh
Cho $N$ đồ vật, mỗi đồ vật $i$ có trọng lượng $W_i$ và giá trị $V_i$. Một cái túi có sức chứa tối đa $M$. Hãy tìm tổng giá trị lớn nhất của các đồ vật chọn vào túi bằng thuật toán Nhánh Cận (Branch and Bound) sử dụng hàm cận trên Fractional Knapsack.

## Input
- Dòng 1: Hai số nguyên $N, M$ ($1 \le N \le 25, 1 \le M \le 10^9$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $W_i, V_i$ ($1 \le W_i, V_i \le 10^7$).

## Output
- In ra giá trị lớn nhất có thể đạt được.

## Sample 1
### Input
```text
4 10
3 40
4 50
5 60
6 70
```
### Output
```text
120
```
### Giải thích
Chọn vật 2 (W=4, V=50) và vật 6 (W=6, V=70) -> Tổng W=10, Tổng V=120.

## Ràng buộc
- 100% số test có $N \le 25, M \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
