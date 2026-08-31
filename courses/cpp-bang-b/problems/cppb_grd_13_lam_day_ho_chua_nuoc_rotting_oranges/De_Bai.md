# Lây Lan Quả Cam Hỏng (Rotting Oranges)

## Bối cảnh
Ma trận chứa `0` (ô trống), `1` (cam tươi), `2` (cam hỏng). Mỗi phút, cam hỏng lan sang 4 quả cam tươi kề cạnh.

## Nhiệm vụ
Tính thời gian tối thiểu để toàn bộ cam tươi bị hỏng (hoặc -1 nếu không thể hỏng hết).

## Input
- Dòng 1: $N, M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo: Ma trận số 0, 1, 2.

## Output
- Thời gian tối thiểu hoặc -1.

## Sample 1
### Input
```text
3 3
211
110
011
```
### Output
```text
4
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
