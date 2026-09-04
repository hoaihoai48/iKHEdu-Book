# Tìm Vị Trí Đầu Tiên Có Giá Trị Lớn Hơn Hoặc Bằng X

## Bối cảnh
Một kho lưu trữ các kiện hàng được đánh số thứ tự từ $1$ đến $N$, kiện hàng thứ $i$ có khối lượng $A_i$. Một xe nâng hàng muốn tìm kiện hàng đầu tiên trong khoảng từ vị trí $L$ đến $R$ có khối lượng đủ lớn đạt từ $X$ trở lên để bốc dỡ. Nếu trong khoảng $[L, R]$ không có kiện hàng nào đạt yêu cầu, ghi nhận `-1`.

## Nhiệm vụ
Cho mảng $A$ và $Q$ truy vấn gồm 3 số $L, R, X$. Hãy lập trình tìm vị trí chỉ số đầu tiên trong đoạn $[L, R]$ có giá trị $\ge X$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng chứa 3 số nguyên $L, R, X$.

## Output
- Với mỗi truy vấn, in ra chỉ số đầu tiên tìm được, hoặc `-1` nếu không có.

## Sample 1
### Input
```text
5 3
1 3 2 4 5
2 1 5 3
1 2 1
2 1 5 3
```
### Output
```text
2
4
```

### Giải thích
Với mảng $[2, 3, 5, 1, 6]$ và truy vấn trong khoảng $[1, 5]$ tìm số $\ge 4$:
Đi từ vị trí 1 sang: vị trí 1 là 2 (< 4), vị trí 2 là 3 (< 4), vị trí 3 là 5 ($\ge 4$). Vị trí đầu tiên thỏa mãn là vị trí 3.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val, X \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
