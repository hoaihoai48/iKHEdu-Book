# Hai Trạm Kiểm Soát Gần Nhau Nhất

## Bối cảnh
Trên một tuyến hành lang vận tải đường sắt cao tốc thẳng tắp kéo dài, ban điều hành dự án bố trí $N$ trạm kiểm soát tự động tại các vị trí có tọa độ $X_1, X_2, \dots, X_N$ (tính theo mét so với điểm gốc $0$). Vì tuyến đường rất dài (tọa độ có thể lên đến $10^{12}$ m), các thiết bị cảm biến liên lạc giữa các trạm đòi hỏi một khoảng cách đệm an toàn tối thiểu để tránh xung đột kênh truyền. Bộ phận kỹ thuật cần tìm ra khoảng cách nhỏ nhất giữa hai trạm bất kỳ để kiểm tra mức độ an toàn kỹ thuật.

## Nhiệm vụ
Cho danh sách tọa độ của $N$ trạm kiểm soát. Hãy tìm và in ra khoảng cách ngắn nhất giữa hai trạm kiểm soát bất kỳ trên tuyến đường.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$) — số lượng trạm kiểm soát.
- Dòng 2: $N$ số nguyên không âm $X_1, X_2, \dots, X_N$ ($0 \le X_i \le 10^{12}$) — tọa độ của các trạm.

## Output
- In ra một số nguyên duy nhất là khoảng cách ngắn nhất giữa hai trạm.

## Sample 1
### Input
```text
6
1500 300 2800 800 1200 3150
```
### Output
```text
300
```
### Giải thích
Tọa độ ban đầu của 6 trạm là: $1500, 300, 2800, 800, 1200, 3150$.
Sắp xếp các trạm theo thứ tự tăng dần của tọa độ dọc tuyến đường:
$300, 800, 1200, 1500, 2800, 3150$.
Khoảng cách giữa các trạm liên tiếp:
- $800 - 300 = 500$
- $1200 - 800 = 400$
- $1500 - 1200 = 300$
- $2800 - 1500 = 1300$
- $3150 - 2800 = 350$

Khoảng cách ngắn nhất đạt được là $300$ mét (giữa hai trạm tại tọa độ $1200$ và $1500$).

## Ràng buộc
- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5, X_i \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
