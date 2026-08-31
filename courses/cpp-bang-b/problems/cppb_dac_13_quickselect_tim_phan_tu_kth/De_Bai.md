# Thuật Toán QuickSelect Tìm K-th Element

**Phân loại bài toán:** `Advanced`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử và số nguyên $K$ ($1 \le K \le N$). Hãy tìm phần tử nhỏ thứ $K$ trong mảng bằng thuật toán QuickSelect Chia Để Trị đạt thời gian trung bình $\mathcal{O}(N)$.

## Input
- Dòng 1: Hai số nguyên $N, K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra giá trị của phần tử nhỏ thứ $K$.

## Sample 1
### Input
```text
6 3
7 10 4 3 20 15
```
### Output
```text
7
```
### Giải thích
Mảng sau khi sắp xếp: [3, 4, 7, 10, 15, 20]. Phần tử nhỏ thứ 3 là 7.

## Ràng buộc
- 100% số test có $N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
