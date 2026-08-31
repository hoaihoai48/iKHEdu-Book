# Sinh Dãy Ngoặc Hợp Lệ Độ Dài 2N

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho số nguyên dương $N$. Hãy sinh tất cả các dãy ngoặc đúng gồm $N$ cặp ngoặc tròn `()` theo thứ tự từ điển bằng thuật toán Quay Lui có cắt tỉa khả thi (`open < N`, `close < open`).

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10$).

## Output
- In ra tất cả các dãy ngoặc đúng độ dài $2N$, mỗi dãy trên một dòng.

## Sample 1
### Input
```text
3
```
### Output
```text
((()))
(()())
(())()
()(())
()()()
```
### Giải thích
Có đúng Catalan(3) = 5 dãy ngoặc hợp lệ.

## Ràng buộc
- 100% số test có $1 \le N \le 10$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
