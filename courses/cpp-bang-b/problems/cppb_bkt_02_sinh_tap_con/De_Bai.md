# Sinh Tất Cả Tập Con Của Tập N Phần Tử

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho tập hợp $S = \{1, 2, \dots, N\}$. Hãy sinh tất cả các tập con của $S$ (kể cả tập rỗng) theo thứ tự từ điển bằng thuật toán Quay Lui dạng Chọn / Bỏ qua.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 16$).

## Output
- In ra các tập con, mỗi tập con trên một dòng (in các phần tử cách nhau bởi dấu cách, tập rỗng in dòng trống).

## Sample 1
### Input
```text
3
```
### Output
```text

3
2
2 3
1
1 3
1 2
1 2 3
```
### Giải thích
Tất cả 8 tập con của {1, 2, 3}.

## Ràng buộc
- 100% số test có $1 \le N \le 16$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
