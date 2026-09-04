# Cặp Điểm Gần Nhất (Closest Pair Of Points)

## Bối cảnh
Trên màn hình hiển thị radar hàng hải, có $N$ tàu biển đang hoạt động trên mặt biển. Tàu thứ $i$ có tọa độ vị trí là $(X_i, Y_i)$. Để cảnh báo nguy cơ va chạm sớm cho đài chỉ huy, hệ thống an toàn hàng hải cần tính toán khoảng cách hình học nhỏ nhất (khoảng cách Euclid) giữa hai tàu biển bất kỳ trong toàn bộ khu vực.

## Nhiệm vụ
Cho tọa độ của $N$ điểm trên mặt phẳng. Hãy lập trình tìm bình phương khoảng cách Euclid nhỏ nhất giữa hai điểm bất kỳ.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($2 \le N \le 10^5$).
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $X_i$ và $Y_i$ ($-10^9 \le X_i, Y_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất bình phương khoảng cách nhỏ nhất giữa hai điểm.

## Sample 1
### Input
```text
4
0 0
1 2
3 1
4 0
```
### Output
```text
5
```

### Giải thích
Với 4 điểm tọa độ: $(0, 0), (1, 1), (2, 2), (2, 0)$:
Khoảng cách giữa điểm $(1, 1)$ và $(2, 2)$ có bình phương là $(2-1)^2 + (2-1)^2 = 1 + 1 = 2$.
Khoảng cách giữa điểm $(1, 1)$ và $(2, 0)$ có bình phương là $(2-1)^2 + (0-1)^2 = 1 + 1 = 2$.
Bình phương khoảng cách nhỏ nhất giữa hai điểm bất kỳ là 2.

## Ràng buộc
- $100\%$ số test có $2 \le N \le 10000, 0 \le X_i, Y_i \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
