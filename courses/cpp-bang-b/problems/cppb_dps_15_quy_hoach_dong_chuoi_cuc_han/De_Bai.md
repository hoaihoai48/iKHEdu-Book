# Tách Từ Trong Chuỗi (Word Break)

## Bối cảnh
Cho một chuỗi ký tự $S$ và một từ điển gồm $K$ từ. Bạn cần xác định xem chuỗi $S$ có thể được phân tách thành một dãy các từ hợp lệ trong từ điển hay không.

## Nhiệm vụ
In `YES` nếu có thể phân tách được, ngược lại in `NO`.

## Input
- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 300$).
- Dòng 2: Số nguyên $K$ ($1 \le K \le 100$).
- $K$ dòng tiếp theo chứa các từ trong từ điển.

## Output
- `YES` hoặc `NO`.

## Sample 1
### Input
```text
leetcode
2
leet
code
```
### Output
```text
YES
```

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 300, 1 \le K \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
