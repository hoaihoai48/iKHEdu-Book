# Số Tribonacci Thứ N Bằng Nhân Ma Trận 3x3

## Bối cảnh
Dãy số Tribonacci được định nghĩa bởi hệ thức truy hồi bậc ba: $T_0 = 0, T_1 = 1, T_2 = 1$ và $T_n = T_{n-1} + T_{n-2} + T_{n-3}$ với mọi $n \ge 3$. Với $N$ cực lớn lên tới $10^{18}$, ta biểu diễn trạng thái truy hồi dưới dạng nhân vector với ma trận chuyển tiếp kích thước $3 \times 3$: $\begin{pmatrix} T_{n} \\ T_{n-1} \\ T_{n-2} \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} T_{n-1} \\ T_{n-2} \\ T_{n-3} \end{pmatrix}$. Áp dụng thuật toán Lũy thừa ma trận nhị phân để tính $T_N \pmod{10^9+7}$ trong $\mathcal{O}(3^3 \log N)$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Số Tribonacci Thứ N Bằng Nhân Ma Trận 3x3 với độ phức tạp tối ưu nhất.

## Input
- Dòng đầu chứa số bộ test $T$ ($1 \le T \le 1000$).
- $T$ dòng tiếp theo, mỗi dòng chứa một số nguyên không âm $N$ ($0 \le N \le 10^{18}$).

## Output
- Gồm $T$ dòng, mỗi dòng in ra giá trị $T_N \pmod{10^9+7}$.

## Sample 1
### Input
```text
4
0
1
3
4
```
### Output
```text
0
1
2
4
```
### Giải thích
* $T_0 = 0, T_1 = 1, T_2 = 1, T_3 = 0+1+1=2, T_4 = 1+1+2=4$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
