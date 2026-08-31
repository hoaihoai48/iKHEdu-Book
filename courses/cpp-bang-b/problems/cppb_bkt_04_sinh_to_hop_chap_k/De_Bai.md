# Sinh Tất Cả Tổ Hợp Chập K Của N

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho 2 số nguyên $N, K$ ($1 \le K \le N \le 16$). Hãy sinh tất cả các tổ hợp chập $K$ của $\{1, 2, \dots, N\}$ theo thứ tự từ điển bằng thuật toán Quay Lui.

## Input
- Một dòng duy nhất chứa 2 số nguyên $N, K$ ($1 \le K \le N \le 16$).

## Output
- In ra tất cả các tổ hợp chập $K$, mỗi tổ hợp trên một dòng cách nhau bởi dấu cách.

## Sample 1
### Input
```text
4 2
```
### Output
```text
1 2
1 3
1 4
2 3
2 4
3 4
```
### Giải thích
Có đúng C(4, 2) = 6 tổ hợp chập 2 của {1, 2, 3, 4}.

## Ràng buộc
- 100% số test có $1 \le K \le N \le 16$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
