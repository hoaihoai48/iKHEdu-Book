# Duyệt Đồ Thị Theo Chiều Sâu (DFS Traversal)

## Bối cảnh
Một robot thám hiểm cần khám phá toàn bộ các gian phòng trong một hang động ngầm gồm $N$ gian phòng và $M$ lối đi hai chiều. Robot áp dụng chiến lược tìm kiếm theo chiều sâu: Từ gian phòng hiện tại, luôn ưu tiên tiến sâu vào một gian phòng chưa từng được khám phá kề cạnh có số hiệu nhỏ nhất; khi không thể đi tiếp thì quay lui lại gian phòng trước đó.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và đỉnh xuất phát $S$. Hãy lập trình in ra thứ tự các đỉnh được robot ghé thăm trong quá trình duyệt theo chiều sâu (khi có nhiều lựa chọn, luôn ưu tiên đỉnh có số hiệu nhỏ hơn).

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, S$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5, 1 \le S \le N$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.

## Output
- In ra trên một dòng thứ tự các đỉnh được ghé thăm trong hành trình, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
4 3 1
1 2
2 3
1 4
```
### Output
```text
1 2 3 4
```

### Giải thích
Với đồ thị 4 đỉnh gồm các cạnh (1, 2), (1, 3), (2, 4) xuất phát từ đỉnh 1:

- Từ đỉnh 1 thăm đỉnh 2 (nhỏ hơn 3).
- Từ đỉnh 2 tiếp tục thăm đỉnh 4.
- Đỉnh 4 không còn đường mới, quay lui về 2, rồi về 1, từ 1 thăm tiếp đỉnh 3.
Thứ tự ghé thăm là: 1 2 4 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
