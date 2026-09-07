# Tìm phần tử nhỏ thứ k trong bảng nhân $n \times n$

## Bối cảnh

Trong giờ học bảng cửu chương, bạn Nam viết ra bảng nhân $N \times N$ rồi đố bạn cùng bàn: nếu xếp tất cả các số trong bảng theo thứ tự từ nhỏ đến lớn thì số đứng thứ $K$ là số nào.

Cả hai cùng đếm thử với bảng nhỏ trước khi nghĩ cách trả lời nhanh với bảng lớn.

## Nhiệm vụ

Cho kích thước bảng nhân $N \times N$ và số $K$. Hãy lập trình tìm phần tử nhỏ thứ $K$ khi xếp tất cả các số trong bảng theo thứ tự tăng dần.

## Input

- Gồm một dòng duy nhất chứa hai số nguyên $n, k$ ($1 \le n \le 10^9$, $1 \le k \le n^2$) — kích thước bảng nhân và thứ tự cần tìm.

## Output

- In ra một dòng duy nhất là số nhỏ thứ $k$ trong bảng nhân $n \times n$ (ô $(i, j)$ có giá trị $i \cdot j$, xếp hạng tính cả các giá trị trùng nhau).

## Sample 1
### Input
```text
3 5
```
### Output
```text
3
```
### Giải thích

Bảng $3 \times 3$: hàng $1$ là $1, 2, 3$; hàng $2$ là $2, 4, 6$; hàng $3$ là $3, 6, 9$. Xếp $9$ số tăng dần: $1, 2, 2, 3, 3, 4, 6, 6, 9$. Số đứng thứ $5$ là $3$.

## Ràng buộc

- $1 \le n \le 10^9$, $1 \le k \le n^2$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
