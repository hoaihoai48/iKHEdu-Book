# Đếm Cặp Số Có Hiệu Bằng K

## Bối cảnh
Trong một thuật toán mã hóa khóa công khai, một danh sách gồm $N$ số nguyên bí mật được đưa vào xử lý. Kỹ sư an ninh cần đếm xem trong danh sách có bao nhiêu cặp chỉ số $(i, j)$ thỏa mãn điều kiện phần tử đứng sau lớn hơn phần tử đứng trước đúng một khoảng cách cố định $K$, tức là $A_j - A_i = K$ (với $i < j$).

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và số nguyên $K$. Hãy lập trình đếm số lượng cặp $(i, j)$ có $i < j$ và $A_j - A_i = K$.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $K$ ($1 \le N \le 10^5, -10^9 \le K \le 10^9$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
5 2
1 5 3 4 2
```
### Output
```text
3
```

### Giải thích
Với mảng $[1, 5, 3, 4, 2]$ và $K = 2$:
Các cặp có hiệu bằng 2 là:

- $A_2 - A_3 = 5 - 3 = 2$.
- $A_3 - A_1 = 3 - 1 = 2$.
- $A_4 - A_5 = 4 - 2 = 2$.
Có tổng cộng 3 cặp số thỏa mãn.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le K, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
