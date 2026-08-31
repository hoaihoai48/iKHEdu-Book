# Đếm Số Ô Vùng Kín Không Thông Ra Biên

## Bối cảnh
Cho ma trận gồm các số `0` và `1`. Một ô `0` được gọi là vùng kín nếu nó không có đường thông qua các ô 0 khác để đi ra viền biên ngoài cùng của ma trận.

## Nhiệm vụ
Đếm số lượng ô 0 thuộc vùng kín.

## Input
- Dòng 1: $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn ma trận.

## Output
- Số ô 0 vùng kín.

## Sample 1
### Input
```text
4 4
1111
1001
1101
1111
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
