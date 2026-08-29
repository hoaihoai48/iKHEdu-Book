# Tối Ưu Hóa Gán Việc Cho N Người (N <= 20)

## Bối cảnh
Có $N$ công việc và $N$ nhân viên ($N \le 16$). Ma trận $C_{i, j}$ biểu diễn chi phí nếu giao công việc $i$ cho nhân viên $j$. Mỗi nhân viên chỉ làm đúng 1 việc, và mỗi công việc chỉ giao cho đúng 1 nhân viên.

## Nhiệm vụ
Hãy tìm phương án phân công công việc sao cho **tổng chi phí là nhỏ nhất có thể**.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 16$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên $C_{i, j}$ ($0 \le C_{i, j} \le 10^6$).

## Output
- In ra một số nguyên duy nhất là tổng chi phí tối thiểu.

## Sample 1
### Input
```text
3
3 2 7
5 1 3
2 7 2
```
### Output
```text
6
```
*(Giải thích: Việc 0 cho người 1 (phí 2), Việc 1 cho người 2 (phí 3), Việc 2 cho người 0 (phí 2). Tổng phí = $2 + 3 + 2 = 7$; hoặc Việc 0 cho người 0 (3), Việc 1 cho người 1 (1), Việc 2 cho người 2 (2) $\implies 3 + 1 + 2 = 6$).*

## Ràng buộc
- $100\%$ số test có $N \le 16, C_{i,j} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
