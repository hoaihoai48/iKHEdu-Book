# Bước Nhảy Quân Mã Ngắn Nhất (Knight Moves)

## Bối cảnh
Quân mã di chuyển hình chữ L (8 hướng) trên bàn cờ $N \times M$.

## Nhiệm vụ
Tìm số nước đi ít nhất để quân mã đi từ $(sr, sc)$ đến $(er, ec)$.

## Input
- Một dòng gồm 6 số: $N, M, sr, sc, er, ec$ ($1 \le N, M \le 1000, 0 \le sr, er < N, 0 \le sc, ec < M$).

## Output
- Số bước ít nhất hoặc -1.

## Sample 1
### Input
```text
8 8 0 0 7 7
```
### Output
```text
6
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
