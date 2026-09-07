# Cập nhật hình chữ nhật ma trận 2d

## Bối cảnh

Ban quản lý ký túc xá theo dõi bảng nội trú hình chữ nhật, mỗi ô ghi số sinh viên đang ở. Mỗi đợt, ban quản lý cộng thêm một số sinh viên vào tất cả các phòng trong một khu hình chữ nhật rồi cần biết nhanh số sinh viên của từng phòng.

Cô quản lý ghi lại các đợt điều chuyển rồi cập nhật bảng số liệu sao cho kịp giờ điểm danh.

## Nhiệm vụ

Cho ma trận ban đầu và các phép cộng trên hình chữ nhật con. Hãy lập trình tính giá trị cuối cùng của ma trận sau mọi phép cập nhật.

## Input

- Dòng đầu tiên chứa ba số nguyên $n, m, q$ ($1 \le n, m \le 1000$, $0 \le q \le 10^5$) — kích thước bảng và số phép cập nhật.
- $q$ dòng tiếp theo, mỗi dòng chứa năm số nguyên $x_1, y_1, x_2, y_2, val$ ($1 \le x_1 \le x_2 \le n$, $1 \le y_1 \le y_2 \le m$, $|val| \le 10^9$) — cộng $val$ vào mọi ô của hình chữ nhật từ $(x_1, y_1)$ tới $(x_2, y_2$). Bảng ban đầu toàn số $0$, chỉ số hàng/cột đánh từ $1$.

## Output

- In ra toàn bộ bảng $n \times m$ sau mọi phép cập nhật gồm $n$ dòng, mỗi dòng $m$ số cách nhau bởi một dấu cách.

## Sample 1
### Input
```text
3 3 2
1 1 2 2 5
2 2 3 3 3
```
### Output
```text
5 5 0
5 8 3
0 3 3
```
### Giải thích

Bảng $3 \times 3$ ban đầu toàn $0$. Phép thứ nhất cộng $5$ vào $4$ ô góc trên-trái. Phép thứ hai cộng $3$ vào $4$ ô góc dưới-phải. Ô $(2, 2)$ nhận cả hai lần nên bằng $8$; các ô $(1, 1), (1, 2), (2, 1)$ bằng $5$; các ô $(2, 3), (3, 2), (3, 3)$ bằng $3$; còn lại là $0$.

## Ràng buộc

- $1 \le n, m \le 1000$, $0 \le q \le 10^5$, $|val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
