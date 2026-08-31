# Median Của Hai Mảng Đã Sắp Xếp

**Phân loại bài toán:** `Challenge`

## Bối cảnh
Cho 2 mảng số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy tìm phần tử trung vị (Median) của tập hợp hợp nhất $A \cup B$ trong thời gian tối ưu $\mathcal{O}(\log(\min(N, M)))$ bằng kỹ thuật Chia đôi không gian phân hoạch.

## Input
- Dòng 1: Hai số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên $B_1, \dots, B_M$ ($|B_j| \le 10^9$).

## Output
- In ra giá trị trung vị (nếu tổng số phần tử $N + M$ chẵn, in phần tử thứ $(N+M)/2$ theo thứ tự 1-based làm tròn dưới).

## Sample 1
### Input
```text
2 2
1 3
2 4
```
### Output
```text
2
```
### Giải thích
Mảng gộp: [1, 2, 3, 4], phần tử thứ 4/2 = 2 là 2.

## Ràng buộc
- 100% số test có $N, M \le 10^5, |A_i|, |B_j| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
