# Tìm Điểm Cực Đại Mảng Unimodal (Peak Index)

## Bối cảnh
Một mảng Unimodal (mảng đỉnh núi) tăng nghiêm ngặt đến một điểm cực đại rồi giảm nghiêm ngặt về sau. Kỹ thuật chia để trị so sánh A[Mid] và A[Mid + 1] cho phép xác định sườn dốc đang leo lên hay trượt xuống, từ đó tìm điểm cực đại trong O(log N).

## Nhiệm vụ
Cho mảng Unimodal gồm N phần tử. Hãy tìm chỉ số (0-indexed) của phần tử cực đại.

## Input
- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên mô tả mảng Unimodal.

## Output
- In ra chỉ số (0-indexed) của điểm cực đại.

## Sample 1
### Input
```text
4
0 2 1 0
```
### Output
```text
1
```
### Giải thích
Điểm cực đại là 2 tại chỉ số 1 (0-indexed).

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
