# Mảng hiệu trên cây (Tree difference array)

## Bối cảnh

Trường học trồng cây theo sơ đồ hình cây, mỗi phòng học là một nút. Mỗi đợt, nhà trường cộng thêm một lượng sách vào tất cả các phòng trên đường đi giữa hai phòng cho trước, cuối cùng cần biết mỗi phòng có bao nhiêu sách.

Bác thủ thư ghi lại từng đợt điều chuyển rồi tổng hợp số sách của mỗi phòng một lần.

## Nhiệm vụ

Cho một cây có $n$ đỉnh (gốc là đỉnh $1$) và $q$ phép cập nhật, mỗi phép cộng thêm $val$ vào một đỉnh $node$ cùng toàn bộ cây con của nó. Mọi đỉnh ban đầu có giá trị $0$. Hãy lập trình tính giá trị cuối cùng của mỗi đỉnh sau mọi phép cập nhật.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, q$ ($1 \le n, q \le 2 \cdot 10^5$) — số đỉnh và số phép cập nhật.
- $n - 1$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u, v$ mô tả một cạnh của cây.
- $q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $node, val$ ($1 \le node \le n$, $|val| \le 10^9$) — cộng $val$ vào $node$ và toàn bộ cây con của nó (theo gốc $1$).

## Output

- In ra một dòng duy nhất gồm $n$ số là giá trị cuối cùng của các đỉnh $1, 2, \dots, n$, cách nhau bởi một dấu cách.

## Sample 1
### Input
```text
5 2
1 2
1 3
3 4
3 5
2 10
3 5
```
### Output
```text
15 10 5 0 0
```
### Giải thích

Cây: $1$ nối $2, 3$; $3$ nối $4, 5$. Phép thứ nhất cộng $10$ vào đỉnh $2$ (không có con). Phép thứ hai cộng $5$ vào đỉnh $3$ và cả cây con $\{3, 4, 5\}$. Dồn từ lá về gốc: đỉnh $4$ và $5$ chỉ nhận $0$ (không có phép nào nhắm vào chúng); đỉnh $3$ nhận $5$; đỉnh $2$ nhận $10$; đỉnh $1$ bằng tổng dồn của cả cây là $10 + 5 = 15$. Kết quả theo thứ tự đỉnh: $15, 10, 5, 0, 0$.

## Ràng buộc

- $1 \le n, q \le 2 \cdot 10^5$, $|val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
