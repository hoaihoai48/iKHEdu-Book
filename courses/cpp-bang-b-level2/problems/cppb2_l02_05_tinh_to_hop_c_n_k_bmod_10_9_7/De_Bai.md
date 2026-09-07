# Tính tổ hợp $c_n^k \bmod (10^9+7)$

## Bối cảnh
Đội văn nghệ của trường có $n$ bạn và cần chọn ra $k$ bạn vào đội hình biểu diễn. Số cách chọn có thể cực lớn nên thầy phụ trách chỉ cần biết phần dư của con số đó khi chia cho $10^9+7$. Vì danh sách đăng ký gửi về liên tục, thầy cần trả lời nhanh cho rất nhiều lượt hỏi khác nhau.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $Q$ truy vấn, mỗi truy vấn gồm hai số nguyên $n, k$. Hãy lập trình tính tổ hợp $C_n^k \bmod (10^9+7)$.

## Input

- Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$) — số lượng truy vấn.
- $Q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $n, k$ ($0 \le k \le n \le 10^6$), cách nhau bởi một dấu cách.

## Output

- Với mỗi truy vấn, in ra một dòng là giá trị $C_n^k \bmod (10^9+7)$.

## Sample 1
### Input
```text
3
5 2
10 3
4 4
```
### Output
```text
10
120
1
```
### Giải thích

* $C_5^2 = 10$: số cách chọn $2$ bạn từ $5$ bạn là $(5 \cdot 4)/2 = 10$.
* $C_{10}^3 = 120$: $(10 \cdot 9 \cdot 8)/6 = 120$.
* $C_4^4 = 1$: chỉ có đúng một cách chọn cả $4$ bạn.

## Ràng buộc

- $1 \le Q \le 10^5$, $0 \le k \le n \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
