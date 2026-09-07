# Đếm số đoạn con có hiệu max - min $\le k$

## Bối cảnh

Thầy giáo ghi lại nhiệt độ phòng học mỗi giờ trong ngày. Thầy muốn đếm xem có bao nhiêu khoảng thời gian liên tiếp mà chênh lệch giữa nhiệt độ cao nhất và thấp nhất không vượt quá $K$.

Thầy trượt một cửa sổ thời gian dọc theo bảng ghi, mỗi lần ghi nhận nhiệt độ cao nhất và thấp nhất trong cửa sổ.

## Nhiệm vụ

Cho dãy số và số $K$. Hãy lập trình đếm số đoạn con liên tiếp có hiệu giữa phần tử lớn nhất và nhỏ nhất không vượt quá $K$.

## Input

- Dòng đầu tiên chứa số nguyên $n$ và số nguyên $k$ ($1 \le n \le 2 \cdot 10^5$, $0 \le k \le 10^9$) — độ dài dãy và ngưỡng chênh lệch.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là số đoạn con liên tiếp có hiệu giữa phần tử lớn nhất và nhỏ nhất không vượt quá $k$.

## Sample 1
### Input
```text
5 2
1 3 2 5 4
```
### Output
```text
9
```
### Giải thích

Đếm theo độ dài: $5$ đoạn dài $1$ luôn thỏa. Dài $2$: $[1, 3]$ (hiệu $2$ ✓), $[3, 2]$ ($1$ ✓), $[2, 5]$ ($3$ ✗), $[5, 4]$ ($1$ ✓) → $3$ đoạn. Dài $3$: $[1, 3, 2]$ (hiệu $3 - 1 = 2$ ✓), $[3, 2, 5]$ ($3$ ✗), $[2, 5, 4]$ ($3$ ✗) → $1$ đoạn. Dài $4$ trở lên hiệu đều vượt $2$. Tổng $5 + 3 + 1 = 9$.

## Ràng buộc

- $1 \le n \le 2 \cdot 10^5$, $0 \le k \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
