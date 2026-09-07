# Phần tử nhỏ thứ k của hợp hai mảng đã sắp xếp

## Bối cảnh

Hai lớp học đều đã xếp hàng theo chiều cao từ thấp đến cao. Thầy thể dục muốn biết nếu gộp cả hai hàng thành một hàng chung vẫn giữ thứ tự chiều cao thì bạn đứng thứ $K$ cao bao nhiêu.

Thầy không muốn bắt cả hai lớp xếp lại từ đầu mà chỉ so sánh từng nhóm nhỏ để tìm ra đáp án.

## Nhiệm vụ

Cho hai mảng đã sắp xếp và số $K$. Hãy lập trình tìm phần tử nhỏ thứ $K$ của dãy hợp nhất hai mảng.

## Input

- Dòng đầu tiên chứa ba số nguyên $n, m, k$ ($1 \le n, m \le 2 \cdot 10^5$, $1 \le k \le n + m$) — kích thước hai mảng và thứ tự cần tìm (đánh số từ $1$).
- Dòng thứ hai chứa $n$ số nguyên tăng dần $a_i$.
- Dòng thứ ba chứa $m$ số nguyên tăng dần $b_j$.

## Output

- In ra một dòng duy nhất là số nhỏ thứ $k$ trong hợp của hai mảng (tính cả các giá trị trùng nhau).

## Sample 1
### Input
```text
3 3 4
1 3 5
2 4 6
```
### Output
```text
4
```
### Giải thích

Hợp hai mảng $[1, 3, 5]$ và $[2, 4, 6]$ rồi xếp tăng dần được $1, 2, 3, 4, 5, 6$. Số đứng thứ $4$ là $4$.

## Ràng buộc

- $1 \le n, m \le 2 \cdot 10^5$, $1 \le k \le n + m$, hai mảng đã tăng dần.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
