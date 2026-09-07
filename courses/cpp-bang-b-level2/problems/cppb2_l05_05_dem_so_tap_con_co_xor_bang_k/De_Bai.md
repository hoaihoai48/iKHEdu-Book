# Đếm số tập con có xor bằng k

## Bối cảnh
Anh kỹ sư bảo mật giữ một chùm mảnh khóa, mỗi mảnh mang một con số. Mã mở két được tạo bằng cách lấy phép XOR của tất cả các mảnh trong tập con được chọn.

Anh cần đếm xem có bao nhiêu tập con các mảnh ghép lại cho ra đúng mã mục tiêu $K$.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên và một số $K$. Hãy lập trình đếm số tập con có giá trị XOR của tất cả các phần tử trong tập con bằng $K$.

## Input

- Dòng đầu tiên chứa số nguyên $n$ và số nguyên $K$ ($1 \le n \le 40$, $0 \le K < 2^{20}$) — số phần tử và giá trị XOR mục tiêu.
- Dòng thứ hai chứa $n$ số nguyên không âm $a_i$ ($0 \le a_i < 2^{20}$).

## Output

- In ra một dòng duy nhất là số tập con (kể cả tập rỗng) có giá trị XOR của tất cả các phần tử đúng bằng $K$.

## Sample 1
### Input
```text
4 1
1 2 3 0
```
### Output
```text
4
```
### Giải thích

Xét dãy $[1, 2, 3, 0]$. Các tập con có XOR bằng $1$: $\{1\}$ ($1$); $\{2, 3\}$ ($2 \oplus 3 = 1$); $\{1, 0\}$ ($1 \oplus 0 = 1$); $\{2, 3, 0\}$ ($1 \oplus 0 = 1$). Các tập còn lại: $\{1, 2, 3\}$ XOR bằng $0$, tập rỗng bằng $0$, các tập đơn $\{2\}, \{3\}, \{0\}$ bằng $2, 3, 0$ — đều khác $1$. Vậy đáp án là $4$.

## Ràng buộc

- $1 \le n \le 40$, $0 \le K, a_i < 2^{20}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
