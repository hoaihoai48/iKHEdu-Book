# Gom Cụm Chênh Lệch Không Quá K

## Bối cảnh
Cho $N$ học sinh với điểm số $A_1, A_2, \dots, A_N$. Giáo viên muốn chia các bạn học sinh thành các nhóm sao cho trong mỗi nhóm, chênh lệch điểm số giữa bạn cao nhất và bạn thấp nhất không vượt quá $K$.

## Nhiệm vụ
Hãy tìm số lượng nhóm ít nhất để phân chia toàn bộ $N$ học sinh.

## Input
- Dòng 1: Chứa 2 số nguyên dương $N$ và $K$ ($1 \le N \le 2 \cdot 10^5, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra số lượng nhóm ít nhất cần chia.

## Sample 1
### Input
```text
6 3
1 10 3 4 12 15
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, K \le 10^9, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
