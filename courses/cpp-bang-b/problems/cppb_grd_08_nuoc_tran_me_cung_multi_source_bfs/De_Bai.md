# Nước Tràn Mê Cung (Multi-Source BFS)

## Bối cảnh
Một hầm mỏ dưới lòng đất kích thước $N × M$ gồm các buồng trống `.` và các khối đá chắn `#`. Đột ngột có một sự cố vỡ đê ngầm khiến nước tràn vào từ $K$ buồng mỏ cùng lúc tại thời điểm $t = 0$. Cứ sau mỗi phút, nước từ các buồng đã ngập sẽ tràn sang tất cả các buồng trống kề sát nó theo 4 hướng. Hãy tính thời gian để toàn bộ các buồng trống trong hầm mỏ đều bị ngập nước.

## Nhiệm vụ
Cho bản đồ hầm mỏ và vị trí các nguồn nước ban đầu. Hãy lập trình tính thời gian (phút) để nước tràn kín toàn bộ các buồng trống liên thông.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi $M$ ký tự (`.` là buồng trống, `W` là nguồn nước, `#` là tường đá).

## Output
- In ra thời gian tối đa để nước tràn ngập khắp hầm mỏ.

## Sample 1
### Input
```text
3 3
W..
.##
..E
```
### Output
```text
4
```

### Giải thích
Nước bắt đầu loang đồng thời từ các điểm 'W' theo chiều rộng:
Sau đúng 4 phút, điểm buồng mỏ xa nhất đã bị nước tràn tới ngập hoàn toàn. Kết quả là 4.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
