# Tìm Điểm Cực Đại Mảng Unimodal (Peak Index)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Một mảng $A$ được gọi là Unimodal (mảng đỉnh núi) nếu nó tăng nghiêm ngặt đến một vị trí đỉnh $p$ rồi sau đó giảm nghiêm ngặt ($A_1 < A_2 < \dots < A_p > A_{p+1} > \dots > A_N$). Hãy tìm giá trị cực đại $A_p$ trong $\mathcal{O}(\log N)$ bằng Chia Để Trị.

## Input
- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên của mảng Unimodal $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra giá trị cực đại $A_p$.

## Sample 1
### Input
```text
7
1 3 8 12 9 4 2
```
### Output
```text
12
```
### Giải thích
Đỉnh của mảng là 12.

## Ràng buộc
- 100% số test có $3 \le N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
