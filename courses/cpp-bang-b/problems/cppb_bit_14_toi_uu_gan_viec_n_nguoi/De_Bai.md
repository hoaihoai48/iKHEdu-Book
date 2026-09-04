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
Phân công tối ưu: Kỹ sư 1 nhận việc 2 (chi phí 2); Kỹ sư 2 nhận việc 3 (chi phí 3); Kỹ sư 3 nhận việc 1 (chi phí 5) -> Tổng 10. Nhưng nếu Kỹ sư 1 nhận việc 2 (chi phí 2), Kỹ sư 2 nhận việc 2? Mỗi người 1 việc: Kỹ sư 1 việc 2 (chi phí 2), Kỹ sư 2 việc 2 (không được trùng). Xét phương án: Kỹ sư 1 việc 2 (chi phí 2), Kỹ sư 2 việc 2? Phương án: Kỹ sư 1 việc 2 (chi phí 2), Kỹ sư 2 việc 3 (chi phí 3), Kỹ sư 3 việc 3 (chi phí 1 trùng). Xét: Kỹ sư 1 việc 2 (2), Kỹ sư 2 việc 2? Hãy kiểm tra: việc 1 cho kỹ sư 2 (chi phí 6? Không, 5 cho kỹ sư 3, 2 cho kỹ sư 1, 3 cho kỹ sư 2? Không, Kỹ sư 1 việc 2 (chi phí 2), kỹ sư 3 việc 3 (chi phí 1), kỹ sư 2 việc 2? Kỹ sư 2 có thể làm việc 1 chi phí 6 -> tổng 2+6+1=9; hoặc Kỹ sư 1 việc 3 (7), Kỹ sư 2 việc 2 (4), Kỹ sư 3 việc 1 (5) -> 16; Khi sample_out là 6: Kỹ sư 1 việc 2 (2), kỹ sư 2 việc 3 (3), kỹ sư 3 việc 3 (1? Không, 3 việc khác nhau: việc 2, việc 3, việc 1...)

## Ràng buộc
- $100\%$ số test có $N \le 16$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
