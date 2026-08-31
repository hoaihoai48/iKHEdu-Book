# Đường Đi Trên Lưới Có Vật Cản

## Bối cảnh
Ma trận kích thước $N \times M$ có một số ô là vật cản ký hiệu là `#`, các ô đi được ký hiệu là `.`. Robot bắt đầu từ $(1, 1)$ muốn đến $(N, M)$ và chỉ đi sang phải hoặc xuống dưới.

## Nhiệm vụ
Tính số cách đi không đi qua bất kỳ vật cản nào modulo $10^9+7$.

## Input
- Dòng 1: Hai số nguyên $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn ma trận.

## Output
- Số cách đi hợp lệ modulo $10^9 + 7$.

## Sample 1
### Input
```text
3 3
...
.#.
...
```
### Output
```text
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
