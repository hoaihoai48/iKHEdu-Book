# Đếm xâu con có đúng k ký tự khác nhau

## Bối cảnh
Cho một xâu ký tự $S$ chỉ gồm các chữ cái tiếng Anh in thường và một số nguyên dương $K$.

## Nhiệm vụ
Hãy đếm số lượng xâu con liên tiếp của $S$ chứa đúng $K$ ký tự phân biệt bằng kỹ thuật Cửa sổ trượt (Sliding Window / Two Pointers).

## Input
- Dòng 1: Xâu ký tự $S$ ($1 \le |S| \le 10^5$).
- Dòng 2: Một số nguyên $K$ ($1 \le K \le 26$).

## Output
- In ra một số nguyên duy nhất là số lượng xâu con thỏa mãn.

## Sample 1
### Input
```text
pqpqs
2
```
### Output
```text
7
```
### Giải thích
* Các xâu con có đúng 2 ký tự khác nhau: `pq` (vị trí 0..1), `pqp` (0..2), `pqpq` (0..3), `qp` (1..2), `qpq` (1..3), `pq` (2..3), `qs` (3..4). Tổng cộng có $7$ xâu.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5, 1 \le K \le 26$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
