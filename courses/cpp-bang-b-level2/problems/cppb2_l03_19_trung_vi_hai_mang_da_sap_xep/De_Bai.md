# Trung vị của hai mảng đã sắp xếp

## Bối cảnh
Cho hai mảng số nguyên $A$ gồm $N$ phần tử và $B$ gồm $M$ phần tử đều đã được sắp xếp theo thứ tự tăng dần. Trung vị của dãy hợp nhất gồm $N + M$ phần tử là phần tử ở chính giữa (nếu $N+M$ lẻ) hoặc trung bình cộng của 2 phần tử ở chính giữa (nếu $N+M$ chẵn).

## Nhiệm vụ
Hãy tìm trung vị của tập hợp tất cả các phần tử trong cả 2 mảng với độ phức tạp thời gian $\mathcal{O}(\log(\min(N, M)))$.

## Input
- Dòng 1: Gồm 2 số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp tăng dần của mảng $A$ ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên đã sắp xếp tăng dần của mảng $B$ ($|B_j| \le 10^9$).

## Output
- In ra một số thực duy nhất là giá trị trung vị với đúng 1 chữ số thập phân sau dấu phẩy.

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
### Giải thích
* Dãy hợp nhất sau khi sắp xếp là $[1, 2, 3, 4]$. Tổng số phần tử chẵn ($4$), hai phần tử chính giữa là $2$ và $3$, trung vị là $(2 + 3) / 2 = 2.5$.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 10^5, |A_i|, |B_j| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
