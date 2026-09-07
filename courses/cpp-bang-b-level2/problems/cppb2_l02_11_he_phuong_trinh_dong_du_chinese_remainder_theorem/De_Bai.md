# Hệ phương trình đồng dư (chinese remainder theorem)

## Bối cảnh
Ba lớp trực nhật đếm số ghế trong hội trường theo ba cách khác nhau: lớp thì đếm dư theo nhóm $m_1$, lớp thì theo nhóm $m_2$, lớp thì theo nhóm $m_3$. Từ các số dư $r_1, r_2, r_3$ đó, ban tổ chức muốn suy ra tổng số ghế nhỏ nhất khớp với cả ba cách đếm.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho hệ $k$ phương trình đồng dư $x \equiv r_i \pmod{m_i}$. Hãy lập trình tìm nghiệm $x$ nhỏ nhất không âm thỏa mãn cả hệ.

## Input

- Dòng đầu tiên chứa số nguyên $k$ ($2 \le k \le 10$) — số phương trình.
- $k$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $r_i, m_i$ ($0 \le r_i < m_i \le 10^6$), các $m_i$ đôi một nguyên tố cùng nhau.

## Output

- In ra một dòng duy nhất là số nguyên $x$ nhỏ nhất không âm thỏa mãn đồng thời mọi phương trình $x \equiv r_i \pmod{m_i}$.

## Sample 1
### Input
```text
2
2 3
3 5
```
### Output
```text
8
```
### Giải thích

Các số chia $3$ dư $2$ là $2, 5, 8, 11, \dots$ Kiểm tra từng số với điều kiện thứ hai: $2$ chia $5$ dư $2$, $5$ chia $5$ dư $0$, $8$ chia $5$ dư $3$ — đúng cả hai điều kiện và là số nhỏ nhất thỏa mãn, nên đáp án là $8$.

## Ràng buộc

- $2 \le k \le 10$, $0 \le r_i < m_i \le 10^6$, các $m_i$ đôi một nguyên tố cùng nhau.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
