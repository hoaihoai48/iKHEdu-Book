# Đếm số đoạn con có tổng nằm trong $[l, r]$

## Bối cảnh
Chủ cửa hàng ghi lại doanh thu từng ngày liên tiếp. Cuối tháng, chị muốn thống kê có bao nhiêu chuỗi ngày liên tiếp mà tổng doanh thu nằm trong khoảng $[L, R]$.

Đó là những giai đoạn kinh doanh ổn định mà chị muốn khen thưởng nhân viên.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và hai ngưỡng $L, R$. Hãy lập trình đếm số đoạn con liên tiếp có tổng các phần tử nằm trong đoạn $[L, R]$.

## Input

- Dòng đầu tiên chứa số nguyên $n$ và hai số nguyên $L, R$ ($1 \le n \le 2 \cdot 10^5$, $|L|, |R| \le 10^{14}$, $L \le R$) — độ dài mảng và khoảng tổng.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là số đoạn con liên tiếp có tổng các phần tử nằm trong đoạn $[L, R]$.

## Sample 1
### Input
```text
5 3 8
1 2 3 4 5
```
### Output
```text
7
```
### Giải thích

Liệt kê: $[1, 2]$ tổng $3$ ✓; $[1, 2, 3]$ tổng $6$ ✓; $[2, 3]$ tổng $5$ ✓; $[3]$ tổng $3$ ✓; $[3, 4]$ tổng $7$ ✓; $[4]$ tổng $4$ ✓; $[5]$ tổng $5$ ✓. Các đoạn còn lại: $[1]$ ($1$ ✗), $[2]$ ($2$ ✗), $[2, 3, 4]$ ($9$ ✗), $[4, 5]$ ($9$ ✗), $[3, 4, 5]$ ($12$ ✗), cả dãy ($15$ ✗). Tổng cộng $7$ đoạn thỏa mãn.

## Ràng buộc

- $1 \le n \le 2 \cdot 10^5$, $L \le R$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
