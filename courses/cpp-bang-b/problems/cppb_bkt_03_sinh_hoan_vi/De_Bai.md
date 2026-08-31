# Sinh Tất Cả Hoán Vị 1..N

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho số nguyên dương $N$. Hãy sinh tất cả các hoán vị của tập hợp $\{1, 2, \dots, N\}$ theo thứ tự từ điển bằng thuật toán Quay Lui có mảng đánh dấu `visited[]`.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 8$).

## Output
- In ra tất cả $N!$ hoán vị, mỗi hoán vị trên một dòng, các phần tử cách nhau bởi dấu cách.

## Sample 1
### Input
```text
3
```
### Output
```text
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```
### Giải thích
Có đúng 3! = 6 hoán vị của {1, 2, 3}.

## Ràng buộc
- 100% số test có $1 \le N \le 8$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
