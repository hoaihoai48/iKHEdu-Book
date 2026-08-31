# Cặp Điểm Gần Nhất (Closest Pair of Points)

**Phân loại bài toán:** `Challenge`

## Bối cảnh
Cho $N$ điểm trên mặt phẳng tọa độ $2D$. Hãy tìm khoảng cách Euclidean nhỏ nhất giữa 2 điểm bất kỳ trong tập hợp bằng thuật toán Chia Để Trị $\mathcal{O}(N \log N)$ (chia đôi theo hoành độ và quét dải Strip $\le 7$ điểm).

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 5 \cdot 10^4$).
- $N$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $X_i, Y_i$ ($|X_i|, |Y_i| \le 10^9$).

## Output
- In ra bình phương khoảng cách nhỏ nhất giữa 2 điểm (để tránh sai số số thực).

## Sample 1
### Input
```text
4
0 0
1 1
2 4
3 1
```
### Output
```text
2
```
### Giải thích
Khoảng cách giữa (0,0) và (1,1) là sqrt(2) -> bình phương bằng 2.

## Ràng buộc
- 100% số test có $2 \le N \le 5 \cdot 10^4, |X_i|, |Y_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
