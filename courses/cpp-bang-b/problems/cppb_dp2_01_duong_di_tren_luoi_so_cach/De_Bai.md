# Đếm Số Cách Đi Trên Lưới

## Bối cảnh
Một robot tự hành giao hàng được đặt ở góc trên bên trái (ô $(1, 1)$) của một kho hàng hình chữ nhật có kích thước $N  × M$ ô vuông. Robot cần di chuyển đến điểm đích ở góc dưới bên phải (ô $(N, M)$) để dỡ kiện hàng. Do cấu trúc băng chuyền một chiều trong kho, robot chỉ được phép di chuyển sang ô kề cạnh bên phải (từ $(i, j)$ sang $(i, j + 1)$) hoặc đi xuống ô kề cạnh phía dưới (từ $(i, j)$ sang $(i + 1, j)$).

## Nhiệm vụ
Cho hai số nguyên dương $N$ và $M$ là kích thước của kho hàng. Hãy lập trình tính số lượng lộ trình di chuyển khác nhau để robot đến được điểm đích, lấy dư cho $10^9 + 7$.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$) biểu diễn số hàng và số cột của lưới.

## Output
- In ra trên một dòng duy nhất số lượng lộ trình hợp lệ theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
3 3
```
### Output
```text
6
```

### Giải thích
Với lưới kích thước $3  × 3$ ($N = 3, M = 3$), robot cần thực hiện đúng 2 bước sang phải và 2 bước xuống dưới. Có tất cả 6 đường đi khác nhau từ $(1, 1)$ đến $(3, 3)$. Kết quả là 6.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
