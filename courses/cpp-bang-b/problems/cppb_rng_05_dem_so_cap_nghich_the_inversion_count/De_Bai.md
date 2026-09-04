# Đếm Số Cặp Nghịch Thế (Inversion Count)

## Bối cảnh
Một thuật toán sắp xếp cần đo lường mức độ xáo trộn của một danh sách gồm $N$ số nguyên. Một cặp nghịch thế là một cặp chỉ số $(i, j)$ thỏa mãn $i < j$ nhưng phần tử đứng trước lại lớn hơn phần tử đứng sau ($A_i > A_j$). Số lượng cặp nghịch thế thể hiện số phép đổi chỗ tối thiểu để đưa mảng về thứ tự tăng dần.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm tổng số lượng cặp nghịch thế trong mảng.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất một số nguyên là số lượng cặp nghịch thế.

## Sample 1
### Input
```text
5
2 4 1 3 5
```
### Output
```text
3
```

### Giải thích
Với mảng gồm 5 phần tử $[2, 4, 1, 3, 5]$:
Các cặp nghịch thế gồm:
- (2, 1) vì $2 > 1$.
- (4, 1) vì $4 > 1$.
- (4, 3) vì $4 > 3$.
Có tất cả 3 cặp nghịch thế, kết quả in ra là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
