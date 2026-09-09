# Xây Dựng Hệ Thức Truy Hồi Cho Dãy Số Đan Dấu

## Bối cảnh
Một biểu thức chuỗi số đan dấu xen kẽ S(N) = 1 - 2 + 3 - 4 + ... + (-1)^(N-1) * N có thể được biểu diễn dưới dạng hệ thức truy hồi đệ quy: S(N) = S(N - 1) + (N lẻ N : -N). Hãy tính giá trị biểu thức này bằng đệ quy.

## Nhiệm vụ
Cho số nguyên dương N. Hãy tính giá trị của biểu thức S(N) bằng đệ quy.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 1000$).

## Output
- In ra giá trị của $S(N)$.

## Sample 1
### Input
```text
5
```
### Output
```text
3
```
### Giải thích
S(5) = 1 - 2 + 3 - 4 + 5 = 3.

## Ràng buộc
- $100\%$ số test có $N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
