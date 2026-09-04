# 0-1 BFS Tìm Đường Đi Ngắn Nhất Trọng Số 0/1

## Bối cảnh
Một mạng lưới giao thông gồm $N$ nút giao và $M$ tuyến đường một chiều. Điểm đặc biệt là mỗi tuyến đường chỉ có trọng số chi phí hoặc là 0 đồng (đường công cộng miễn phí) hoặc là 1 đồng (đường cao tốc có thu phí tượng trưng). Cần tìm tổng chi phí ít nhất để di chuyển từ nút giao xuất phát $S$ tới nút giao đích $D$.

## Nhiệm vụ
Cho đồ thị có hướng $N$ đỉnh $M$ cạnh với trọng số mỗi cạnh thuộc $\{0, 1\}$. Hãy lập trình tìm khoảng cách ngắn nhất từ $S$ tới $D$. Nếu không đến được, in ra `-1`.

## Input
- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5, 1 \le S, D \le N$).
- $M$ dòng tiếp theo, mỗi dòng chứa 3 số nguyên $u, v, w$ biểu diễn đường một chiều từ $u$ tới $v$ với trọng số $w \in \{0, 1\}$.

## Output
- In ra khoảng cách ngắn nhất từ $S$ tới $D$, hoặc `-1` nếu không có đường đi.

## Sample 1
### Input
```text
4 4
1 2 1
2 3 0
3 4 1
1 4 1
```
### Output
```text
1
```

### Giải thích
Với đồ thị có đường đi từ 1 tới 3 qua cạnh trọng số 1, và từ 3 tới 4 qua cạnh trọng số 0:
Tổng chi phí từ 1 tới 4 là $1 + 0 = 1$ đồng. Đây là chi phí tối thiểu.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
