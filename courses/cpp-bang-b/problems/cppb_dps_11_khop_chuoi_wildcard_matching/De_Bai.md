# Khớp Chuỗi Ký Tự Đại Diện (Wildcard Matching)

## Bối cảnh
Cho chuỗi $S$ và mẫu $P$. Mẫu $P$ chứa ký tự `?` (khớp với 1 ký tự bất kỳ) và `*` (khớp với dãy ký tự bất kỳ có độ dài $\ge 0$).

## Nhiệm vụ
In `YES` nếu mẫu $P$ khớp toàn bộ chuỗi $S$, ngược lại in `NO`.

## Input
- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 1000$).
- Dòng 2: Mẫu $P$ ($1 \le |P| \le 1000$).

## Output
- `YES` hoặc `NO`.

## Sample 1
### Input
```text
adceb
*a*b
```
### Output
```text
YES
```

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |P| \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
