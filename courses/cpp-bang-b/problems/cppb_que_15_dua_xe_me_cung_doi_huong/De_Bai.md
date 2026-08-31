# Đua Xe Mê Cung Đổi Hướng Ít Nhất (0-1 BFS State)

## Bối cảnh
Xe đua di chuyển trong mê cung từ vị trí `S` đến `E`. Nếu tiếp tục đi thẳng cùng hướng thì không tốn chi phí (chi phí 0), nếu rẽ sang hướng khác tốn 1 lần bẻ lái (chi phí 1).

## Nhiệm vụ
Tìm số lần đổi hướng ít nhất để đến đích.

## Input
- Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo biểu diễn mê cung.

## Output
- Số lần đổi hướng ít nhất hoặc -1.

## Sample 1
### Input
```text
3 3
S..
.#.
..E
```
### Output
```text
1
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
