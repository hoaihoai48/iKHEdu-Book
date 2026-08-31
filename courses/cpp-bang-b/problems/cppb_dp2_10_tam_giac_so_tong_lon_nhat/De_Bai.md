# Tam Giác Số Tổng Lớn Nhất (Triangle DP)

## Bối cảnh
Cho tam giác số gồm $N$ hàng. Từ vị trí $(i, j)$, ta chỉ có thể di chuyển xuống ô $(i+1, j)$ hoặc $(i+1, j+1)$.

## Nhiệm vụ
Tìm tổng các số lớn nhất trên đường đi từ đỉnh tam giác $(0, 0)$ xuống hàng đáy.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
- $N$ dòng tiếp theo biểu diễn tam giác số ($0 \le A_{i, j} \le 10^4$).

## Output
- Tổng lớn nhất tìm được.

## Sample 1
### Input
```text
4
2
3 4
6 5 7
4 1 8 3
```
### Output
```text
21
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 0 \le A_{i, j} \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
