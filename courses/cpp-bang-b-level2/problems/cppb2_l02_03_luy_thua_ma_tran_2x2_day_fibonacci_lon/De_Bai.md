# Lũy thừa ma trận 2x2 (dãy fibonacci lớn)

## Bối cảnh
Trang trại thỏ của bác nông dân phát triển theo quy luật quen thuộc: mỗi tháng, số cặp thỏ mới bằng tổng số cặp thỏ của hai tháng trước đó. Sau rất nhiều tháng, đàn thỏ lên tới con số khổng lồ nên bác chỉ cần biết phần dư của con số đó khi chia cho $10^9+7$ để đối chiếu với sức chứa của chuồng.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ truy vấn, mỗi truy vấn gồm một số nguyên không âm $n$. Hãy lập trình tính số Fibonacci thứ $n$ (với $F_0 = 0, F_1 = 1$) theo modulo $10^9+7$.

## Input

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^4$) — số lượng truy vấn.
- $T$ dòng tiếp theo, mỗi dòng chứa một số nguyên không âm $n$ ($0 \le n \le 10^{18}$).

## Output

- Với mỗi truy vấn, in ra một dòng là số Fibonacci thứ $n$ theo modulo $10^9+7$ (với $F_0 = 0, F_1 = 1$).

## Sample 1
### Input
```text
4
0 1 5 10
```
### Output
```text
0
1
5
55
```
### Giải thích

Dãy Fibonacci bắt đầu $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$ Do đó $F_0 = 0$, $F_1 = 1$, đếm tiếp tới vị trí thứ $5$ được $5$ và tới vị trí thứ $10$ được $55$.

## Ràng buộc

- $1 \le T \le 10^4$, $0 \le n \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
