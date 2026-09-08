# Chuyển Danh Sách Cạnh Sang Danh Sách Kề

## Bối cảnh
Một đồ thị mạng lưới giao thông gồm $N$ nút giao và $M$ con đường hai chiều ban đầu được lưu trữ dưới dạng danh sách các cặp cạnh $(u, v)$. Để thuận tiện cho việc lập trình các thuật toán tìm kiếm và duyệt đồ thị, kỹ sư cầu đường cần chuyển đổi dữ liệu mạng lưới sang cấu trúc danh sách kề: Với mỗi nút giao, liệt kê tất cả các nút giao có đường nối trực tiếp với nó theo thứ tự số hiệu tăng dần.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình chuyển đổi sang biểu diễn danh sách kề và in ra các đỉnh kề của từng đỉnh theo thứ tự tăng dần.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u$ và $v$ ($1 \le u, v \le N, u 
e v$) biểu diễn một cạnh.

## Output
- In ra $N$ dòng, dòng thứ $i$ bắt đầu bằng số thứ tự đỉnh $i$ kèm dấu hai chấm, theo sau là danh sách các đỉnh kề với $i$ theo thứ tự tăng dần.

## Sample 1
### Input
```text
3 2
1 2
1 3
```
### Output
```text
2 2 3
1 1
1 1
```

### Giải thích
Với đồ thị 4 đỉnh và các cạnh (1, 2), (1, 3), (2, 4):

- Đỉnh 1 kề với các đỉnh: 2, 3.
- Đỉnh 2 kề với các đỉnh: 1, 4.
- Đỉnh 3 kề với đỉnh: 1.
- Đỉnh 4 kề với đỉnh: 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10000, 0 \le M \le 20000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
