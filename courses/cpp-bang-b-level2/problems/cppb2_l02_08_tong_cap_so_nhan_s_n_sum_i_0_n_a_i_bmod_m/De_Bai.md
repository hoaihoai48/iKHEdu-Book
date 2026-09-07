# Tổng cấp số nhân $s_n = \sum_{i=0}^n a^i \bmod m$

## Bối cảnh
Một người gửi tiết kiệm theo kiểu lạ: tháng đầu gửi $1$ đồng, các tháng sau số tiền gửi gấp $a$ lần tháng trước, kéo dài tới tháng thứ $n$. Ngân hàng cần biết tổng số tiền đã gửi theo modulo $10^9+7$ để in sao kê, mà $n$ có thể rất lớn nên không thể cộng từng tháng một.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ cặp $(a, n)$. Hãy lập trình tính $S = 1 + a + a^2 + \dots + a^n$ theo modulo $10^9+7$.

## Input

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^4$) — số lượng truy vấn.
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên không âm $a, n$ ($0 \le a \le 10^9$, $0 \le n \le 10^{18}$), cách nhau bởi một dấu cách.

## Output

- Với mỗi truy vấn, in ra một dòng là giá trị $S = 1 + a + a^2 + \dots + a^n$ theo modulo $10^9+7$.

## Sample 1
### Input
```text
2
2 3
3 2
```
### Output
```text
15
13
```
### Giải thích

* Với $a = 2, n = 3$: $S = 1 + 2 + 4 + 8 = 15$.
* Với $a = 3, n = 2$: $S = 1 + 3 + 9 = 13$.

## Ràng buộc

- $1 \le T \le 10^4$, $0 \le a \le 10^9$, $0 \le n \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
