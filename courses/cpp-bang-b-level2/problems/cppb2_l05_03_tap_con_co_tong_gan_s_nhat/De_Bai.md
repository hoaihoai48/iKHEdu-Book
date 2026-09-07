# Tập con có tổng gần s nhất

## Bối cảnh
Cô kế toán được giao một khoản tiền mục tiêu $S$ để mua sắm thiết bị. Mỗi món đồ có một mức giá riêng, và cô chỉ được mua mỗi món nhiều nhất một lần.

Cô cần chọn một nhóm món đồ sao cho tổng giá tiền gần với $S$ nhất có thể, để số tiền thừa hay thiếu là ít nhất.

## Nhiệm vụ

Cho dãy gồm $n$ số nguyên dương ($n \le 40$) và sức chứa $w$. Hãy lập trình chọn ra một tập con có tổng lớn nhất mà không vượt quá $w$.

## Input

- Dòng đầu tiên chứa số nguyên $n$ và số nguyên $w$ ($1 \le n \le 40$, $0 \le w \le 10^{18}$) — số phần tử và sức chứa.
- Dòng thứ hai chứa $n$ số nguyên dương $a_i$ ($1 \le a_i \le 10^{18}$).

## Output

- In ra một dòng duy nhất là tổng lớn nhất của một tập con không vượt quá $w$.

## Sample 1
### Input
```text
5 10
3 7 2 5 1
```
### Output
```text
10
```
### Giải thích

Liệt kê các tập con có tổng không vượt $10$: $\{3, 7\}$ tổng đúng $10$; $\{3, 2, 5\}$ tổng $10$; $\{7, 2, 1\}$ tổng $10$; các tập còn lại đều có tổng $\le 9$ (ví dụ $\{5, 1, 3\} = 9$). Tổng lớn nhất đạt được là $10$.

## Ràng buộc

- $1 \le n \le 40$, $0 \le w \le 10^{18}$, $1 \le a_i \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
