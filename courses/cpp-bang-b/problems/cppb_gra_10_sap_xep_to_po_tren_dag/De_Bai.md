# Sắp Xếp Tô-pô (Topological Sort)

## Bối cảnh
Cho đồ thị có hướng $N$ đỉnh $M$ cạnh. Hãy tìm một thứ tự tô-pô của các đỉnh (nếu có cạnh $u \to v$ thì $u$ phải đứng trước $v$).

## Nhiệm vụ
In ra thứ tự tô-pô hoặc -1 nếu đồ thị có chu trình.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Mỗi dòng gồm cạnh có hướng $u \to v$.

## Output
- Thứ tự tô-pô hoặc -1.

## Sample 1
### Input
```text
4 3
1 2
2 3
1 3
```
### Output
```text
1 4 2 3
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
