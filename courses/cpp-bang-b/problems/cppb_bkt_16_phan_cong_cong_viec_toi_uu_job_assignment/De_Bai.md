# Phân Công Công Việc Tối Ưu (Job Assignment B&B)

**Phân loại bài toán:** `Challenge`

## Bối cảnh
Ban quản trị một trung tâm gia công phần mềm quy mô lớn có $N$ kỹ sư chuyên trách và $N$ dự án công nghệ mới cần triển khai. Qua đánh giá năng lực và kinh nghiệm thực tế, phòng nhân sự đã xây dựng ma trận chi phí $C_{N \times N}$, trong đó $C_{i, j}$ phản ánh chi phí (hoặc thời gian hao tổn) nếu giao kỹ sư $i$ đảm nhiệm dự án $j$. Để đảm bảo tiến độ và chất lượng, mỗi kỹ sư chỉ phụ trách đúng 1 dự án và mỗi dự án được giao cho đúng 1 kỹ sư.

## Nhiệm vụ
Cho số lượng $N$ và ma trận chi phí phân công $C_{N \times N}$. Hãy áp dụng thuật toán Nhánh Cận (Branch and Bound) với hàm cận dưới tối ưu để tìm một phương án phân công toàn diện sao cho tổng chi phí hoàn thành tất cả các công việc là nhỏ nhất có thể.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 12$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên biểu diễn hàng của ma trận chi phí $C_{N \times N}$ ($0 \le C_{i, j} \le 10^6$).

## Output
- In ra một số nguyên duy nhất là tổng chi phí phân công công việc nhỏ nhất có thể đạt được.

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
Phương án phân công tối ưu nhất là:

- Kỹ sư 1 làm việc 2 (chi phí $C_{1, 2} = 2$).
- Kỹ sư 2 làm việc 1 (chi phí $C_{2, 1} = 6$).
- Kỹ sư 3 làm việc 3 (chi phí $C_{3, 3} = 1$).
- Kỹ sư 4 làm việc 4 (chi phí $C_{4, 4} = 4$).
Tổng chi phí nhỏ nhất đạt được là $2 + 6 + 1 + 4 = 13$.

## Ràng buộc
- 100% số test có $1 \le N \le 12$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
