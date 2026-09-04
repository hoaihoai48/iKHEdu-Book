# Đếm Số Điểm Trong Hình Chữ Nhật (2D Range Query)

## Bối cảnh
Một đài thiên văn số ghi nhận tọa độ mặt phẳng $(x_i, y_i)$ của $N$ ngôi sao trên bầu trời. Các nhà thiên văn học cần thực hiện các truy vấn: đếm xem có bao nhiêu ngôi sao nằm lọt vào bên trong một vùng quan sát hình chữ nhật có góc dưới trái $(x_1, y_1)$ và góc trên phải $(x_2, y_2)$.

## Nhiệm vụ
Cho danh sách tọa độ $N$ điểm và $Q$ truy vấn hình chữ nhật. Hãy lập trình đếm số lượng điểm nằm trong từng hình chữ nhật.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $x_i, y_i$ ($1 \le x_i, y_i \le 10^5$).
- $Q$ dòng tiếp theo, mỗi dòng chứa 4 số nguyên $x_1, y_1, x_2, y_2$.

## Output
- Với mỗi truy vấn, in ra số lượng điểm nằm trong hình chữ nhật trên một dòng.

## Sample 1
### Input
```text
3 2
1 1
2 2
3 3
1 1 2 2
2 2 4 4
```
### Output
```text
2
2
```

### Giải thích
Với 3 điểm $(1, 2), (2, 3), (4, 5)$ và vùng quan sát từ $(1, 1)$ đến $(3, 4)$:
Hai điểm $(1, 2)$ và $(2, 3)$ nằm trọn vẹn bên trong vùng hình chữ nhật. Điểm $(4, 5)$ nằm ngoài. Số điểm đếm được là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10000, 1 \le X_i, Y_i \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
