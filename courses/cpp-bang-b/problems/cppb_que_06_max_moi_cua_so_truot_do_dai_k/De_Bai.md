# Max Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)

## Bối cảnh
Tương tự hệ thống giám sát lò phản ứng, để kịp thời phát hiện các đỉnh áp suất bất thường, hệ thống cần đồng thời theo dõi giá trị áp suất lớn nhất bên trong mỗi cửa sổ trượt gồm $K$ mốc đo liên tiếp.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và kích thước cửa sổ $K$. Hãy lập trình tìm giá trị lớn nhất trong mỗi cửa sổ trượt kích thước $K$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N - K + 1$ số nguyên là giá trị lớn nhất của từng cửa sổ trượt.

## Sample 1
### Input
```text
8 3
1 3 -1 -3 5 3 6 7
```
### Output
```text
3 3 5 5 6 7
```

### Giải thích
Với mảng $[1, 3, -1, -3, 5, 3, 6, 7]$ và $K = 3$:
- Cửa sổ [1, 3, -1] -> max = 3.
- Cửa sổ [3, -1, -3] -> max = 3.
- Cửa sổ [-1, -3, 5] -> max = 5.
- Cửa sổ [-3, 5, 3] -> max = 5.
- Cửa sổ [5, 3, 6] -> max = 6.
- Cửa sổ [3, 6, 7] -> max = 7.
Kết quả in ra: 3 3 5 5 6 7.

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, -10^9 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
