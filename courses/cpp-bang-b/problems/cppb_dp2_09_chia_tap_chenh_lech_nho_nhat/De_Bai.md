# Chia Tập Chênh Lệch Nhỏ Nhất (Minimum Subset Sum Difference)

## Bối cảnh
Cho $N$ đồ vật có khối lượng $A_i$. Cần chia các món đồ này cho hai người sao cho độ chênh lệch tổng khối lượng giữa hai người là nhỏ nhất có thể.

## Nhiệm vụ
Tìm độ chênh lệch nhỏ nhất $|S_1 - S_2|$.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 500$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

## Output
- Độ chênh lệch nhỏ nhất.

## Sample 1
### Input
```text
4
1 6 11 5
```
### Output
```text
1
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 500, 1 \le A_i \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
