# Tìm Vị Trí Xuất Hiện Đầu Tiên & Cuối Cùng

## Bối cảnh
Cho mảng $N$ phần tử đã được sắp xếp tăng dần. Có $Q$ truy vấn, mỗi truy vấn cho một số $X$. Hãy tìm vị trí xuất hiện đầu tiên và vị trí xuất hiện cuối cùng của $X$ trong mảng (đánh số từ 1 đến $N$). Nếu không tồn tại, in ra `-1 -1`.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $X$ ($|X| \le 10^9$).

## Output
- In ra $Q$ dòng, mỗi dòng gồm 2 số là vị trí đầu tiên và cuối cùng (1-based), hoặc `-1 -1`.

## Sample 1
### Input
```text
6 2
1 2 2 2 5 6
2
3
```
### Output
```text
2 4
-1 -1
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
