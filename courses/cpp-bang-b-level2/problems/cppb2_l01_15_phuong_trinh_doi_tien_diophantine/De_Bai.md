# Đếm Số Cách Đổi Tiền Bằng Phương Trình Diophantine

## Bối cảnh
Một máy rút tiền chỉ có 2 loại mệnh giá tiền là $A$ đồng và $B$ đồng. Khách hàng muốn rút đúng $C$ đồng. Hãy đếm số cách chọn số lượng tờ tiền $(x, y)$ ($x \ge 0, y \ge 0$) sao cho $A \cdot x + B \cdot y = C$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Đếm Số Cách Đổi Tiền Bằng Phương Trình Diophantine với độ phức tạp tối ưu nhất.

## Input
- Một dòng chứa 3 số nguyên dương $A, B, C$ ($1 \le A, B \le 10^6, 1 \le C \le 10^{12}$).

## Output
- In ra số lượng bộ nghiệm không âm $(x, y)$ thỏa mãn.

## Sample 1
### Input
```text
3 5 30
```
### Output
```text
3
```
### Giải thích
* Các bộ nghiệm $(x, y)$ là: (10, 0), (5, 3), (0, 6) $\implies$ 3 cách.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
