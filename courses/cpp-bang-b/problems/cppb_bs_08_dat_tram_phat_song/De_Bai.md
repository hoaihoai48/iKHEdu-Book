# Đặt Trạm Phát Sóng Cách Nhau Xa Nhất (Aggressive Cows)

## Bối cảnh
Dọc theo một đường thẳng có $N$ vị trí có thể đặt trạm phát sóng tại các tọa độ $X_1, X_2, \dots, X_N$. Bạn cần chọn ra đúng $C$ vị trí để đặt trạm sao cho khoảng cách giữa hai trạm bất kỳ gần nhau nhất là **lớn nhất có thể** (nhằm giảm thiểu sự can nhiễu sóng).

## Input
- Dòng 1: Gồm 2 số nguyên $N, C$ ($2 \le C \le N \le 10^5$).
- Dòng 2: $N$ số nguyên biểu diễn tọa độ các điểm $X_1, X_2, \dots, X_N$ ($0 \le X_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là khoảng cách nhỏ nhất lớn nhất tìm được.

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
*(Giải thích: Sắp xếp tọa độ: $[1, 2, 4, 8, 9]$. Đặt 3 trạm tại các vị trí $1, 4, 8$ hoặc $1, 4, 9$. Khoảng cách nhỏ nhất giữa các cặp là $\min(4-1, 8-4) = 3$).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, X_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
