# Lập Lịch Công Việc Số Máy Chủ Ít Nhất

## Bối cảnh
Có $N$ công việc, công việc thứ $i$ bắt đầu tại thời điểm $S_i$ và kết thúc tại $E_i$. Một máy chủ chỉ thực hiện được 1 công việc tại một thời điểm.

## Nhiệm vụ
Tìm số lượng máy chủ ít nhất cần thiết để thực hiện toàn bộ $N$ công việc.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- $N$ dòng tiếp theo: $S_i, E_i$ ($1 \le S_i < E_i \le 10^9$).

## Output
- Số máy chủ ít nhất.

## Sample 1
### Input
```text
3
0 30
5 10
15 20
```
### Output
```text
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 1 \le S_i < E_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
