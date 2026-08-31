# Phân Công Công Việc Tối Ưu (Job Assignment B&B)

**Phân loại bài toán:** `Challenge`

## Bối cảnh
Cho $N$ công nhân và $N$ công việc. Ma trận $C_{N \times N}$ cho biết chi phí $C_{i, j}$ nếu giao công nhân $i$ làm việc $j$. Mỗi công nhân làm đúng 1 việc, mỗi việc do đúng 1 người làm. Hãy tìm tổng chi phí phân công nhỏ nhất bằng thuật toán Nhánh Cận (Branch and Bound).

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 12$).
- $N$ dòng tiếp theo: Ma trận chi phí $C_{N \times N}$ ($0 \le C_{i, j} \le 10^6$).

## Output
- In ra tổng chi phí phân công nhỏ nhất.

## Sample 1
### Input
```text
4
9 2 7 8
6 4 3 7
5 8 1 8
7 6 9 4
```
### Output
```text
13
```
### Giải thích
Công nhân 1 làm việc 2 (2), CN 2 làm việc 4 (7? không, CN 2 làm việc 1=6, CN 3 làm việc 3=1, CN 4 làm việc 4=4 -> Tổng = 2 + 6 + 1 + 4 = 13).

## Ràng buộc
- 100% số test có $1 \le N \le 12$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
