# Tô Màu Đồ Thị (Graph K-Coloring)

**Phân loại bài toán:** `Challenge`

## Bối cảnh
Cho đồ thị vô hướng $G = (V, E)$ gồm $V$ đỉnh và $E$ cạnh, cùng số màu $K$. Hãy kiểm tra xem có thể tô màu $V$ đỉnh bằng $K$ màu sao cho không có 2 đỉnh kề nhau có cùng màu hay không. In `YES` nếu tô được, ngược lại in `NO`.

## Input
- Dòng 1: 3 số nguyên $V, E, K$ ($1 \le V \le 12, 0 \le E \le V(V-1)/2, 1 \le K \le 4$).
- $E$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $u, v$ mô tả một cạnh ($1 \le u, v \le V$).

## Output
- In `YES` hoặc `NO`.

## Sample 1
### Input
```text
4 5 3
1 2
2 3
3 4
4 1
1 3
```
### Output
```text
YES
```
### Giải thích
Đồ thị có thể tô hợp lệ bằng 3 màu.

## Ràng buộc
- 100% số test có $V \le 12, K \le 4$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
