# Giải phương trình $4$ ẩn tuyến tính (4-sum mitm)

## Bối cảnh
Trong ngày hội thể thao, ban tổ chức có bốn bảng danh sách điểm số của bốn đội. Mỗi bảng ghi điểm của các vận động viên đội mình.

Ban tổ chức muốn biết có bao nhiêu cách chọn mỗi bảng đúng một con số sao cho tổng bốn số được chọn bằng $0$, để trao giải đồng đội cân bằng.

## Nhiệm vụ
Cho bốn dãy số $A, B, C, D$. Hãy lập trình đếm số bộ bốn $(a, b, c, d)$ với $a \in A, b \in B, c \in C, d \in D$ sao cho $a + b + c + d = 0$.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 2000$) — kích thước của mỗi dãy.
- Bốn dòng tiếp theo, mỗi dòng chứa $n$ số nguyên là một trong bốn dãy $A, B, C, D$ ($|giá trị| \le 10^9$).

## Output

- In ra một dòng duy nhất là số bộ bốn $(a, b, c, d)$ với $a \in A, b \in B, c \in C, d \in D$ sao cho $a + b + c + d = 0$.

## Sample 1
### Input
```text
2
1 -1
1 -1
1 -1
-1 1
```
### Output
```text
6
```
### Giải thích

Mỗi dãy đều gồm hai số $1$ và $-1$. Tổng bốn số bằng $0$ đúng khi có hai số $+1$ và hai số $-1$: chọn $2$ trong $4$ dãy để lấy số $+1$ có đúng $6$ cách ($C_4^2 = 6$), mỗi cách cho đúng một bộ bốn. Vậy đáp án là $6$.

## Ràng buộc

- $1 \le n \le 2000$, mọi giá trị có trị tuyệt đối không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
