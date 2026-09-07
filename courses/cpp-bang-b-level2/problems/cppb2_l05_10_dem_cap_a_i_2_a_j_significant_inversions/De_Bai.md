# Đếm cặp $a_i > 2 a_j$ (significant inversions)

## Bối cảnh
Cô giáo ghi lại điểm số của cả lớp theo đúng thứ tự chỗ ngồi. Cô muốn phát hiện những chênh lệch bất thường: một bạn ngồi phía trước nhưng điểm cao gấp hơn hai lần một bạn ngồi phía sau.

Hãy giúp cô đếm có bao nhiêu cặp bạn như vậy trong lớp.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm số cặp $(i, j)$ thỏa mãn $i < j$ và $A_i > 2 \cdot A_j$, rồi in ra tổng số cặp đếm được.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 2 \cdot 10^5$) — độ dài mảng.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là số cặp $(i, j)$ thỏa $i < j$ và $A_i > 2 \cdot A_j$.

## Sample 1
### Input
```text
5
1 3 2 3 1
```
### Output
```text
2
```
### Giải thích

Liệt kê mọi cặp $i < j$: cặp $(3, 1)$ ở vị trí $(2, 5)$ có $3 > 2 \cdot 1 = 2$ ✓; cặp $(3, 1)$ ở vị trí $(4, 5)$ cũng thỏa ✓. Các cặp còn lại: $(1, \cdot)$ quá nhỏ; $(3, 2)$ có $3 > 4$ sai; $(3, 3)$ sai; $(2, 1)$ có $2 > 2$ sai. Vậy đáp án là $2$.

## Ràng buộc

- $1 \le n \le 2 \cdot 10^5$, $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
