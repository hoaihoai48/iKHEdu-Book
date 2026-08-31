# Xây Dựng Hệ Thức Truy Hồi Cho Dãy Số Đan Dấu

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho số nguyên dương $N$. Hãy tính giá trị của biểu thức $S(N) = 1 - 2 + 3 - 4 + \dots + (-1)^{N+1} N$ bằng hàm đệ quy truy hồi $S(N) = S(N-1) + (-1)^{N+1} N$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 1000$).

## Output
- In ra giá trị của biểu thức $S(N)$.

## Sample 1
### Input
```text
5
```
### Output
```text
3
```
### Giải thích
1 - 2 + 3 - 4 + 5 = 3.

## Ràng buộc
- 100% số test có $1 \le N \le 1000$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
