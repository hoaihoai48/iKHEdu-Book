# Nghịch đảo modulo tổng quát

## Bối cảnh
Trong trò chơi chia kẹo của lớp, cô giáo quy định mỗi viên kẹo ứng với một phép nhân theo vòng tròn modulo $m$. Để "hoàn tác" một lần chia, cả lớp cần tìm số $x$ sao cho $a \cdot x$ quay đúng một vòng trở về $1$. Có những số $a$ không thể hoàn tác được, khi đó cả lớp hô to $-1$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ cặp $(a, m)$. Hãy lập trình tìm số nguyên $x$ nhỏ nhất không âm thỏa $a\cdot x \equiv 1 \pmod m$; in `-1` nếu không tồn tại.

## Input

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$) — số lượng truy vấn.
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên dương $a, m$ ($1 \le a, m \le 10^9$), cách nhau bởi một dấu cách.

## Output

- Với mỗi truy vấn, in ra một dòng là số nguyên $x$ nhỏ nhất không âm thỏa $a \cdot x \equiv 1 \pmod m$; in `-1` nếu không tồn tại số $x$ như vậy.

## Sample 1
### Input
```text
3
3 11
10 17
6 9
```
### Output
```text
4
12
-1
```
### Giải thích

* $a = 3, m = 11$: thử $x = 4$ thì $3 \cdot 4 = 12 = 11 + 1$, chia $11$ dư $1$ → đáp án $4$ (các giá trị $0, 1, 2, 3$ đều không thỏa).
* $a = 10, m = 17$: $10 \cdot 12 = 120 = 7 \cdot 17 + 1$, chia $17$ dư $1$ → đáp án $12$.
* $a = 6, m = 9$: ước chung lớn nhất của $6$ và $9$ là $3 \ne 1$ nên không tồn tại nghịch đảo → in `-1`.

## Ràng buộc

- $1 \le T \le 10^5$, $1 \le a, m \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
