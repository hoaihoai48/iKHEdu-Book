# Căn bậc hai modulo nguyên tố (thuật toán tonelli-shanks)

## Bối cảnh
Ổ khóa số của phòng dụng cụ mở ra khi nhập đúng số $x$ mà bình phương của nó chia cho số nguyên tố $p$ còn dư đúng $n$. Có những con số $n$ mà không chiếc chìa nào mở được, khi đó người trực phải báo $-1$ để đổi ổ khác.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ cặp $(n, p)$ với $p$ nguyên tố. Hãy lập trình tìm $x$ sao cho $x^2 \equiv n \pmod p$; in `-1` nếu không tồn tại.

## Input

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^4$) — số lượng truy vấn.
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $n, p$ ($0 \le n < p$, $p$ là số nguyên tố, $2 \le p \le 10^9$), cách nhau bởi một dấu cách.

## Output

- Với mỗi truy vấn, in ra một dòng là nghiệm $x$ nhỏ hơn (trong hai nghiệm đối nhau) thỏa $x^2 \equiv n \pmod p$; in `-1` nếu không tồn tại nghiệm.

## Sample 1
### Input
```text
3
4 7
2 7
5 11
```
### Output
```text
2
3
4
```
### Giải thích

* $n = 4, p = 7$: $2^2 = 4$, chia $7$ dư $4$ → đáp án $2$.
* $n = 2, p = 7$: thử $3^2 = 9 = 7 + 2$ đúng; nghiệm còn lại là $7 - 3 = 4$, lấy nghiệm nhỏ hơn là $3$.
* $n = 5, p = 11$: $4^2 = 16 = 11 + 5$ đúng; nghiệm còn lại là $7$, lấy nghiệm nhỏ hơn là $4$.

## Ràng buộc

- $1 \le T \le 10^4$, $0 \le n < p$, $p$ nguyên tố không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
