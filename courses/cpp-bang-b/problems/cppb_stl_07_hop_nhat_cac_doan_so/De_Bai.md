# Hợp Nhất Các Đoạn Số (Merge Intervals)

## Bối cảnh
Cho $N$ đoạn số $[L_i, R_i]$. Cần hợp nhất tất cả các đoạn có điểm chung lại với nhau.

## Nhiệm vụ
Dòng 1: Số lượng đoạn sau hợp nhất. Các dòng tiếp theo in các đoạn tăng dần theo $L$.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- $N$ dòng tiếp theo: $L_i, R_i$ ($1 \le L_i \le R_i \le 10^9$).

## Output
- Danh sách các đoạn sau khi hợp nhất.

## Sample 1
### Input
```text
4
1 3
2 6
8 10
15 18
```
### Output
```text
3
1 6
8 10
15 18
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 1 \le L_i \le R_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
