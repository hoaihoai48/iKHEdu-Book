# Khoảng Cách Nhỏ Nhất

## Bối cảnh
Trên trục đường chính của một khu đô thị thông minh, ban quản lý đã cho lắp đặt $N$ trạm cảm biến đo lường môi trường tại các vị trí có tọa độ $A_1, A_2, \dots, A_N$. Nhằm đảm bảo vùng phủ sóng không bị can nhiễu tín hiệu tần số vô tuyến giữa hai trạm kề sát nhau, trung tâm điều hành cần xác định khoảng cách ngắn nhất giữa hai trạm cảm biến bất kỳ trên toàn tuyến.

## Nhiệm vụ
Cho danh sách tọa độ của $N$ trạm cảm biến. Hãy tính và in ra khoảng cách nhỏ nhất giữa hai trạm cảm biến bất kỳ trong hệ thống.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$) — số lượng trạm cảm biến.
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$) — tọa độ các trạm cảm biến.

## Output
- In ra một số nguyên duy nhất là khoảng cách nhỏ nhất giữa hai trạm cảm biến bất kỳ.

## Sample 1
### Input
```text
5
8 3 14 6 10
```
### Output
```text
2
```
### Giải thích
Tọa độ các trạm cảm biến ban đầu là: $8, 3, 14, 6, 10$.
Sau khi sắp xếp lại theo chiều tăng dần của vị trí trên trục đường:
$3, 6, 8, 10, 14$.
Khoảng cách giữa các cặp trạm liền kề nhau:
- Giữa trạm $3$ và $6$: khoảng cách là $6 - 3 = 3$.
- Giữa trạm $6$ và $8$: khoảng cách là $8 - 6 = 2$.
- Giữa trạm $8$ và $10$: khoảng cách là $10 - 8 = 2$.
- Giữa trạm $10$ và $14$: khoảng cách là $14 - 10 = 4$.

Do đó, khoảng cách nhỏ nhất giữa hai trạm bất kỳ là $2$ (đạt được giữa trạm $6$ và $8$, hoặc trạm $8$ và $10$).

## Ràng buộc
- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
