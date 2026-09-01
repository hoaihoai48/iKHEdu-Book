# Đếm số bộ ba tam giác hợp lệ

## Bối cảnh
Cho một mảng $A$ gồm $N$ số nguyên dương biểu thị độ dài các thanh gỗ. Người ta muốn chọn ra 3 thanh gỗ có độ dài $A_i, A_j, A_k$ ($i < j < k$) sao cho 3 thanh gỗ này có thể ghép thành một tam giác không suy biến (nghĩa là thỏa mãn $A_i + A_j > A_k$ với $A_i \le A_j \le A_k$).

## Nhiệm vụ
Hãy đếm số lượng bộ ba chỉ số $(i, j, k)$ thỏa mãn điều kiện tạo thành tam giác bằng kỹ thuật Hai con trỏ với độ phức tạp $\mathcal{O}(N^2)$.

## Input
- Dòng 1: Gồm 1 số nguyên $N$ ($3 \le N \le 5000$) — số lượng thanh gỗ.
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng bộ ba tam giác hợp lệ.

## Sample 1
### Input
```text
4
4 6 3 7
```
### Output
```text
3
```
### Giải thích
* Sắp xếp mảng: $[3, 4, 6, 7]$.
* Các bộ ba tam giác hợp lệ: $(3, 4, 6)$ vì $3+4 > 6$, $(3, 6, 7)$ vì $3+6 > 7$, $(4, 6, 7)$ vì $4+6 > 7$. Tổng cộng có $3$ bộ ba.

## Ràng buộc
- $100\%$ số test có $3 \le N \le 5000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
