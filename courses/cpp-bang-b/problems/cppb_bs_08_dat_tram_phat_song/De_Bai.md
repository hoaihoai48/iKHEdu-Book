# Đặt Trạm Phát Sóng Cách Nhau Xa Nhất (Aggressive Cows)

## Bối cảnh
Dọc theo một rặng núi thẳng dài, ban viễn thông quân sự khảo sát được N vị trí địa lý thuận lợi có thể lắp đặt trạm phát sóng tại các tọa độ X1, X2, ..., Xn. Đơn vị cần chọn ra đúng C vị trí để lắp đặt C trạm phát sóng sao cho khoảng cách giữa hai trạm gần nhau nhất là lớn nhất có thể nhằm tránh tối đa hiện tượng giao thoa sóng vô tuyến cực ngắn.

## Nhiệm vụ
Cho N vị trí khả dụng và số trạm cần đặt C. Hãy tìm khoảng cách nhỏ nhất lớn nhất giữa hai trạm bất kỳ.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $C$ ($2 \le C \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên không âm $X_1, X_2, \dots, X_N$ ($0 \le X_i \le 10^9$).

## Output
- In ra khoảng cách nhỏ nhất lớn nhất có thể đạt được.

## Sample 1
### Input
```text
5 3
1 2 8 4 9
```
### Output
```text
3
```
### Giải thích
Sắp xếp tọa độ các vị trí: [1, 2, 4, 8, 9]. Để đặt 3 trạm với khoảng cách tối thiểu giữa hai trạm kề nhau là 3: ta đặt tại các tọa độ 1, 4 và 8 (hoặc 9). Khoảng cách giữa 1 và 4 là 3; giữa 4 và 8 là 4 (đều >= 3). Không thể đặt với khoảng cách tối thiểu >= 4. Vì vậy kết quả là 3.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, X_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
