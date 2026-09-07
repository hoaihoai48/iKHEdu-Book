# Lũy thừa ma trận kích thước $k \times k$

## Bối cảnh
Mạng lưới giao thông giữa $k$ bến xe được ghi trong một bảng $k \times k$: ô $(i, j)$ cho biết có bao nhiêu chuyến xe đi thẳng từ bến $i$ đến bến $j$ trong một chặng. Để biết sau đúng $n$ chặng thì giữa các bến có bao nhiêu hành trình, người ta nhân bảng này với chính nó $n$ lần rồi lấy phần dư theo $10^9+7$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho ma trận vuông $A$ kích thước $k \times k$ và số mũ $n$. Hãy lập trình tính $A^n$ theo modulo $10^9+7$.

## Input

- Dòng đầu tiên chứa hai số nguyên $k, n$ ($1 \le k \le 30$, $0 \le n \le 10^{18}$) — kích thước ma trận và số mũ.
- $k$ dòng tiếp theo, mỗi dòng chứa $k$ số nguyên không âm (mỗi số không quá $10^9$) mô tả một hàng của ma trận $A$.

## Output

- In ra ma trận $A^n$ theo modulo $10^9+7$ gồm $k$ dòng, mỗi dòng $k$ số cách nhau bởi một dấu cách (với $n = 0$ thì kết quả là ma trận đơn vị).

## Sample 1
### Input
```text
2 3
1 1
1 0
```
### Output
```text
3 2
2 1
```
### Giải thích

Tính tay từng bước: $A^2 = A \cdot A$, hàng $1$ nhân cột $1$ được $1 \cdot 1 + 1 \cdot 1 = 2$, toàn bộ $A^2$ là `2 1 / 1 1`. Nhân tiếp với $A$: hàng $1$ nhân cột $1$ được $2 \cdot 1 + 1 \cdot 1 = 3$, hàng $1$ nhân cột $2$ được $2 \cdot 1 + 1 \cdot 0 = 2$, tương tự hàng $2$ được $2, 1$. Vậy $A^3$ là `3 2 / 2 1`.

## Ràng buộc

- $1 \le k \le 30$, $0 \le n \le 10^{18}$, mỗi phần tử của $A$ không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
