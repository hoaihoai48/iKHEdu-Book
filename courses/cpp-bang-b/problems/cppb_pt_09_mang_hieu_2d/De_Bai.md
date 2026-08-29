# Cập Nhật Cộng Hình Chữ Nhật (Mảng Hiệu 2D)

## Bối cảnh
Cho ma trận kích thước $N \times M$ ban đầu toàn số 0. Có $Q$ thao tác, mỗi thao tác gồm 5 số nguyên $x_1, y_1, x_2, y_2, V$ yêu cầu cộng giá trị $V$ vào tất cả các ô trong hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$.

## Nhiệm vụ
Hãy in ra ma trận kết quả sau khi hoàn thành $Q$ thao tác.

## Input
- Dòng 1: Gồm 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 5 số $x_1, y_1, x_2, y_2, V$ ($1 \le x_1 \le x_2 \le N, 1 \le y_1 \le y_2 \le M, |V| \le 10^9$).

## Output
- In ra $N$ dòng, mỗi dòng gồm $M$ số nguyên biểu diễn ma trận cuối cùng.

## Sample 1
### Input
```text
3 3 2
1 1 2 2 3
2 2 3 3 2
```
### Output
```text
3 3 0
3 5 2
0 2 2
```

## Ràng buộc
- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
