# Cập Nhật Cộng Hình Chữ Nhật (Mảng Hiệu 2D)

## Bối cảnh
Trong một trò chơi chiến thuật, bản đồ kích thước N x M ô ban đầu có mức phòng thủ bằng 0. Các người chơi lần lượt kích hoạt Q lá bùa gia cố, mỗi lá bùa cộng thêm X điểm phòng thủ cho một khu vực hình chữ nhật từ tọa độ (r1, c1) đến (r2, c2). Hãy xác định bảng điểm phòng thủ cuối cùng của toàn bộ bản đồ sau khi kết thúc Q đợt kích hoạt bùa.

## Nhiệm vụ
Cho ma trận N x M ban đầu toàn số 0. Thực hiện Q thao tác cộng giá trị X vào hình chữ nhật từ (r1, c1) đến (r2, c2). Hãy in ra ma trận kết quả sau Q thao tác bằng Mảng hiệu 2D.

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 5 số nguyên $r_1, c_1, r_2, c_2, X$.

## Output
- In ra ma trận $N \times M$ sau khi hoàn tất toàn bộ $Q$ thao tác.

## Sample 1
### Input
```text
3 3 1
1 1 2 2 5
```
### Output
```text
5 5 0
5 5 0
0 0 0
```
### Giải thích
Thao tác cộng 5 vào hình chữ nhật từ (1, 1) đến (2, 2) làm cho 4 ô ở góc trên bên trái đều có giá trị 5, các ô còn lại giữ nguyên giá trị 0.

## Ràng buộc
- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
