# Gộp Hai Mảng Đã Sắp Xếp (Merge Step)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho 2 dãy số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy cài đặt bước gộp `merge()` bằng kỹ thuật 2 con trỏ trong $\mathcal{O}(N + M)$ để gộp $A$ và $B$ thành một dãy số tăng dần duy nhất.

## Input
- Dòng 1: Hai số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ đã sắp xếp tăng dần ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên $B_1, \dots, B_M$ đã sắp xếp tăng dần ($|B_j| \le 10^9$).

## Output
- In ra $N + M$ số nguyên của mảng sau khi gộp, cách nhau bởi dấu cách.

## Sample 1
### Input
```text
3 4
1 5 8
2 3 6 9
```
### Output
```text
1 2 3 5 6 8 9
```
### Giải thích
Mảng sau khi gộp tăng dần: 1 2 3 5 6 8 9.

## Ràng buộc
- 100% số test có $N, M \le 10^5, |A_i|, |B_j| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
