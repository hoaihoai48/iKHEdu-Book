# Đoạn Con Tổng Lớn Nhất (Maximum Subarray D&C)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử (có thể chứa số âm). Hãy tìm tổng lớn nhất của một đoạn con liên tiếp khác rỗng bằng thuật toán Chia Để Trị $\mathcal{O}(N \log N)$ (`max(Left, Right, Crossing)`).

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng lớn nhất của đoạn con liên tiếp.

## Sample 1
### Input
```text
8
-2 -3 4 -1 -2 1 5 -3
```
### Output
```text
7
```
### Giải thích
Đoạn con [4, -1, -2, 1, 5] có tổng lớn nhất = 7.

## Ràng buộc
- 100% số test có $1 \le N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
