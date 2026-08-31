# Người Du Lịch (TSP) Nhánh Cận

**Phân loại bài toán:** `Advanced`

## Bối cảnh
Cho $N$ thành phố và ma trận khoảng cách $C$ cấp $N \times N$. Hãy tìm chi phí nhỏ nhất của một chu trình xuất phát từ thành phố $1$, đi qua tất cả các thành phố còn lại đúng 1 lần rồi quay về thành phố $1$ bằng thuật toán Nhánh Cận (Branch and Bound).

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 13$).
- $N$ dòng tiếp theo: Ma trận $C_{N \times N}$ ($0 \le C_{i, j} \le 10^6$, $C_{i, i} = 0$).

## Output
- In ra chi phí nhỏ nhất của chu trình Hamilton.

## Sample 1
### Input
```text
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```
### Output
```text
80
```
### Giải thích
Chu trình tối ưu: 1 -> 2 -> 4 -> 3 -> 1 có chi phí 10 + 25 + 30 + 15 = 80.

## Ràng buộc
- 100% số test có $2 \le N \le 13$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
