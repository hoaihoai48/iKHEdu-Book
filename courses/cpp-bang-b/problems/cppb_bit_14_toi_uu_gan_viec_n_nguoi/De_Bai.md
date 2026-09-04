# Tối Ưu Hóa Gán Việc Cho N Người (N <= 20)

## Bối cảnh
Một giám đốc điều hành dự án cần phân công N công việc cho N kỹ sư phần mềm (mỗi kỹ sư nhận đúng 1 việc). Chi phí để kỹ sư i hoàn thành công việc j được cho bởi ma trận chi phí C[i][j]. Hãy tìm phương án phân công sao cho tổng chi phí hoàn thành tất cả N công việc là nhỏ nhất.

## Nhiệm vụ
Cho ma trận chi phí C kích thước N x N (N <= 16). Hãy tìm tổng chi phí phân công nhỏ nhất để giao N việc cho N người bằng quy hoạch động trạng thái bitmask.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 16$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên biểu diễn ma trận chi phí $C_{i, j}$ ($0 \le C_{i, j} \le 10^6$).

## Output
- In ra tổng chi phí tối thiểu.

## Sample 1
### Input
```text
3
9 2 7
6 4 3
5 8 1
```
### Output
```text
6
```
### Giải thích
Phương án phân công tối ưu có tổng chi phí nhỏ nhất là $6$:
- Kỹ sư 1 làm việc 2 (chi phí $C_{1, 2} = 2$).
- Kỹ sư 2 làm việc 3 (chi phí $C_{2, 3} = 3$).
- Kỹ sư 3 làm việc 1 (chi phí $C_{3, 1} = 1$).
Tổng chi phí tối thiểu: $2 + 3 + 1 = 6$.

## Ràng buộc
- $100\%$ số test có $N \le 16$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
