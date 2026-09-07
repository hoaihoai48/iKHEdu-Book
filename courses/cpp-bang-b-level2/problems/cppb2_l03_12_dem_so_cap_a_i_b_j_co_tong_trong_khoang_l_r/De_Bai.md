# Đếm số cặp $(a_i, b_j)$ có tổng trong khoảng $[l, r]$

## Bối cảnh

Hai đội văn nghệ mỗi đội chuẩn bị một danh sách tiết mục với thời lượng khác nhau. Ban tổ chức muốn ghép mỗi tiết mục của đội một với một tiết mục của đội hai sao cho tổng thời lượng của cặp ghép nằm trong khoảng thời gian cho phép của chương trình.

Ban tổ chức liệt kê thời lượng từng tiết mục rồi đếm xem có bao nhiêu cặp ghép vừa khung giờ.

## Nhiệm vụ

Cho hai dãy $A, B$ và khoảng $[L, R]$. Hãy lập trình đếm số cặp $(A_i, B_j)$ có tổng nằm trong khoảng $[L, R]$.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, m$ và hai số nguyên $L, R$ ($1 \le n, m \le 2 \cdot 10^5$, $|L|, |R| \le 10^9$, $L \le R$) — kích thước hai mảng và khoảng tổng.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- Dòng thứ ba chứa $m$ số nguyên $b_j$ ($|b_j| \le 10^9$).

## Output

- In ra một dòng duy nhất là số cặp $(i, j)$ sao cho $L \le a_i + b_j \le R$.

## Sample 1
### Input
```text
3 4 5 9
1 2 3
4 5 6 7
```
### Output
```text
11
```
### Giải thích

* Với $a_1 = 1$: cần $b$ từ $4$ tới $8$, cả $4$ số $4, 5, 6, 7$ đều thỏa → $4$ cặp.
* Với $a_2 = 2$: cần $b$ từ $3$ tới $7$, cả $4$ số đều thỏa → $4$ cặp.
* Với $a_3 = 3$: cần $b$ từ $2$ tới $6$, các số $4, 5, 6$ thỏa → $3$ cặp.
Tổng cộng $4 + 4 + 3 = 11$.

## Ràng buộc

- $1 \le n, m \le 2 \cdot 10^5$, $L \le R$, mọi giá trị có trị tuyệt đối không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
