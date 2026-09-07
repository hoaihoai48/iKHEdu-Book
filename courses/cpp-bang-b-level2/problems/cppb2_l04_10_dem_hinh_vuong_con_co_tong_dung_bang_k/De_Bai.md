# Đếm hình vuông con có tổng đúng bằng k

## Bối cảnh

Cô giáo vẽ một bảng số hình vuông cho cả lớp. Nhóm bạn An được giao nhiệm vụ đếm xem có bao nhiêu ô vuông con trong bảng có tổng các số bên trong đúng bằng $K$.

Cả nhóm kẻ khung vuông đủ mọi kích cỡ đặt lên bảng rồi cộng tổng từng khung để kiểm tra.

## Nhiệm vụ

Cho ma trận số và số $K$. Hãy lập trình đếm số hình vuông con có tổng các ô đúng bằng $K$.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, m$ và số nguyên $k$ ($1 \le n, m \le 300$, $|k| \le 10^{18}$) — kích thước bảng và tổng mục tiêu.
- $n$ dòng tiếp theo, mỗi dòng chứa $m$ số nguyên $a_{ij}$ ($|a_{ij}| \le 10^9$).

## Output

- In ra một dòng duy nhất là số hình vuông con (cạnh $\ge 1$, các ô kề nhau) có tổng các phần tử đúng bằng $k$.

## Sample 1
### Input
```text
2 2 10
1 2
3 4
```
### Output
```text
1
```
### Giải thích

Liệt kê: bốn ô đơn có tổng $1, 2, 3, 4$ — không ô nào bằng $10$; hình vuông $2 \times 2$ duy nhất (cả bảng) có tổng $1 + 2 + 3 + 4 = 10$ — thỏa mãn. Vậy đáp án là $1$.

## Ràng buộc

- $1 \le n, m \le 300$, $|k| \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
