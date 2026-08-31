# Chu Trình Ngắn Nhất Trên Đồ Thị (Girth)

## Bối cảnh
Tìm độ dài của chu trình đơn có số cạnh ít nhất trên đồ thị vô hướng không trọng số.

## Nhiệm vụ
In ra độ dài chu trình ngắn nhất hoặc -1 nếu đồ thị không có chu trình.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 1000, 0 \le M \le 2000$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- Độ dài chu trình ngắn nhất hoặc -1.

## Sample 1
### Input
```text
5 6
1 2
2 3
3 1
3 4
4 5
5 3
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 0 \le M \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
