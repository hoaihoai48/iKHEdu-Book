# Đếm Số Lần Xuất Hiện Xâu Con Rời Rạc (Distinct Subsequences)

## Bối cảnh
Cho chuỗi $S$ và $T$. Cần đếm số dãy con khác nhau của $S$ bằng đúng chuỗi $T$.

## Nhiệm vụ
Tính số cách chọn dãy con modulo $10^9+7$.

## Input
- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 500$).

## Output
- Số cách chọn theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
rabbbit
rabbit
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 2000, 1 \le |T| \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
