# Trung Vị Của Hai Mảng Đã Sắp Xếp (Median of Two Sorted)

## Bối cảnh
Cho hai mảng số nguyên $A$ và $B$ đã được sắp xếp tăng dần với kích thước lần lượt là $N$ và $M$. Hãy tìm giá trị trung vị (Median) của mảng hợp nhất gồm $N + M$ phần tử trong thời gian tối ưu $\mathcal{O}(\log(\min(N, M)))$.

(Quy ước: Nếu tổng số phần tử $N + M$ là lẻ, trung vị là phần tử ở chính giữa. Nếu $N + M$ là chẵn, trung vị là trung bình cộng của 2 phần tử ở chính giữa lấy 1 chữ số thập phân).

## Input
- Dòng 1: Gồm 2 số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên đã sắp xếp $B_1, B_2, \dots, B_M$ ($|B_i| \le 10^9$).

## Output
- In ra giá trị trung vị lấy đúng 1 chữ số sau dấu phẩy thập phân.

## Sample 1
### Input
```text
2 2
1 3
2 4
```
### Output
```text
2.5
```
*(Giải thích: Mảng gộp $[1, 2, 3, 4]$, trung vị là $(2 + 3) / 2 = 2.5$).*

## Ràng buộc
- $100\%$ số test có $N, M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
