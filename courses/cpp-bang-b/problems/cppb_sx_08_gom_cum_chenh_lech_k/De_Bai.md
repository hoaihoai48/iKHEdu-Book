# Gom Cụm Chênh Lệch Không Quá K

## Bối cảnh
Để chuẩn bị cho kỳ thi học sinh giỏi, câu lạc bộ Tin học có $N$ bạn học sinh tham gia với mức điểm năng lực khảo sát ban đầu lần lượt là $A_1, A_2, \dots, A_N$. Huấn luyện viên muốn chia các bạn học sinh thành các nhóm học tập sao cho trình độ trong mỗi nhóm tương đối đồng đều: chênh lệch điểm số giữa bạn có điểm cao nhất và bạn có điểm thấp nhất trong cùng một nhóm không được vượt quá $K$. Để việc giảng dạy và quản lý lớp học đạt hiệu quả cao nhất, huấn luyện viên mong muốn số lượng nhóm cần chia là ít nhất có thể.

## Nhiệm vụ
Cho điểm năng lực của $N$ bạn học sinh và số nguyên $K$. Hãy tìm số lượng nhóm ít nhất để phân chia toàn bộ $N$ học sinh thỏa mãn điều kiện chênh lệch tối đa giữa bạn cao nhất và bạn thấp nhất trong mỗi nhóm không quá $K$.

## Input
- Dòng 1: Chứa 2 số nguyên dương $N$ và $K$ ($1 \le N \le 2 \cdot 10^5, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$) — điểm năng lực của các học sinh.

## Output
- In ra một số nguyên duy nhất là số lượng nhóm ít nhất cần chia.

## Sample 1
### Input
```text
6 3
1 10 3 4 12 15
```
### Output
```text
3
```
### Giải thích
Sắp xếp điểm năng lực của 6 bạn học sinh theo thứ tự tăng dần:
$1, 3, 4, 10, 12, 15$.
Với $K = 3$, ta có thể gom tối ưu thành 3 nhóm như sau:

- Nhóm 1: $\{1, 3, 4\}$ (Điểm cao nhất là $4$, thấp nhất là $1$, chênh lệch $4 - 1 = 3 \le 3$).
- Nhóm 2: $\{10, 12\}$ (Điểm cao nhất là $12$, thấp nhất là $10$, chênh lệch $12 - 10 = 2 \le 3$).
- Nhóm 3: $\{15\}$ (Chỉ gồm 1 bạn, chênh lệch bằng $0 \le 3$).

Không thể chia thành ít hơn 3 nhóm mà vẫn thỏa mãn điều kiện. Vì vậy kết quả là `3`.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, K \le 10^9, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
