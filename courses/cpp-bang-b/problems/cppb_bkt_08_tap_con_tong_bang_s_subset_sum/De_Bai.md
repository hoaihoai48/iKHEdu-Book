# Tập Con Có Tổng Bằng S (Subset Sum)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên dương $A$ gồm $N$ phần tử và số nguyên dương $S$. Hãy in ra tất cả các tập con của $A$ có tổng đúng bằng $S$ theo thứ tự từ điển bằng thuật toán Quay Lui có cắt tỉa khả thi (`current_sum > S`). Nếu không có tập nào, in `-1`.

## Input
- Dòng 1: Hai số nguyên $N, S$ ($1 \le N \le 20, 1 \le S \le 1000$).
- Dòng 2: $N$ số nguyên dương $A_1, \dots, A_N$ ($1 \le A_i \le 100$).

## Output
- In ra các tập con thỏa mãn (mỗi tập trên một dòng, các phần tử cách nhau bởi dấu cách), hoặc `-1`.

## Sample 1
### Input
```text
4 6
1 2 3 5
```
### Output
```text
1 2 3
1 5
```
### Giải thích
Có 2 tập con có tổng bằng 6: {1, 2, 3} và {1, 5}.

## Ràng buộc
- 100% số test có $N \le 20, S \le 1000$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
