# Tháp lũy thừa $a^{b^c} \bmod m$

## Bối cảnh
Trong cuộc thi xếp tháp số của lớp, mỗi đội dựng một "tháp lũy thừa" ba tầng $a^{b^c}$ rồi chỉ ghi lại phần dư của ngọn tháp khi chia cho $10^9+7$. Vì tầng trên cùng đã là một lũy thừa khổng lồ, không đội nào tính trực tiếp từ trên xuống được.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ bộ $(a, b, c)$. Hãy lập trình tính tháp lũy thừa $a^{b^c} \bmod (10^9+7)$.

## Input

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^4$) — số lượng truy vấn.
- $T$ dòng tiếp theo, mỗi dòng chứa ba số nguyên không âm $a, b, c$ ($0 \le a, b, c \le 10^9$), cách nhau bởi dấu cách.

## Output

- Với mỗi truy vấn, in ra một dòng là giá trị tháp lũy thừa $a^{b^c} \bmod (10^9+7)$ (tính $b^c$ trước rồi lấy kết quả làm số mũ của $a$).

## Sample 1
### Input
```text
2
2 3 2
3 2 2
```
### Output
```text
512
81
```
### Giải thích

* Với $(2, 3, 2)$: tính $3^2 = 9$ trước, sau đó $2^9 = 512$.
* Với $(3, 2, 2)$: tính $2^2 = 4$ trước, sau đó $3^4 = 81$.

## Ràng buộc

- $1 \le T \le 10^4$, $0 \le a, b, c \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
