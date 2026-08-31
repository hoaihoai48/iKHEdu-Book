# Sinh Tất Cả Xâu Nhị Phân Độ Dài N

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho số nguyên dương $N$. Hãy sinh tất cả các xâu nhị phân độ dài $N$ theo thứ tự từ điển bằng thuật toán Quay Lui chuẩn mực (`Choose` $\to$ `Explore` $\to$ `Unchoose`).

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 16$).

## Output
- In ra tất cả các xâu nhị phân độ dài $N$, mỗi xâu trên một dòng theo thứ tự từ điển.

## Sample 1
### Input
```text
3
```
### Output
```text
000
001
010
011
100
101
110
111
```
### Giải thích
Có đúng 2^3 = 8 xâu nhị phân độ dài 3.

## Ràng buộc
- 100% số test có $1 \le N \le 16$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
