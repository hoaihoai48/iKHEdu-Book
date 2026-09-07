# Đếm dãy ngoặc đúng (số Catalan modulo)

## Bối cảnh
Cô giáo mỹ thuật yêu cầu cả lớp vẽ các dãy ngoặc tròn mở và đóng sao cho mỗi ngoặc đóng đều khớp đúng với một ngoặc mở trước đó. Với $n$ cặp ngoặc, số dãy vẽ đúng có thể rất lớn nên lớp trưởng chỉ ghi lại phần dư khi chia cho $10^9+7$ để báo cáo.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ truy vấn, mỗi truy vấn gồm một số nguyên không âm $n$. Hãy lập trình đếm số dãy ngoặc đúng gồm $n$ cặp ngoặc (số Catalan thứ $n$) theo modulo $10^9+7$.

## Input

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$) — số lượng truy vấn.
- $T$ dòng tiếp theo, mỗi dòng chứa một số nguyên không âm $n$ ($0 \le n \le 10^6$).

## Output

- Với mỗi truy vấn, in ra một dòng là số dãy ngoặc đúng gồm $n$ cặp ngoặc (số Catalan thứ $n$) theo modulo $10^9+7$.

## Sample 1
### Input
```text
3
1 2 3
```
### Output
```text
1
2
5
```
### Giải thích

* $n = 1$: chỉ có `()` → $1$.
* $n = 2$: có `(())` và `()()` → $2$.
* $n = 3$: có `((()))`, `(()())`, `(())()`, `()(()`, `()()()` — liệt kê tay được $5$ dãy, không còn dãy nào khác.

## Ràng buộc

- $1 \le T \le 10^5$, $0 \le n \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
