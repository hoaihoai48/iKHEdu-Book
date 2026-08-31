# Đếm Số Cách Đi Trên Lưới

## Bối cảnh
Trên lưới ô vuông kích thước $N \times M$, một robot xuất phát từ ô $(1, 1)$ và cần di chuyển đến ô $(N, M)$. Mỗi bước robot chỉ có thể di chuyển sang phải $1$ ô hoặc xuống dưới $1$ ô.

## Nhiệm vụ
Tính số cách đi khác nhau của robot từ ô $(1, 1)$ đến ô $(N, M)$ lấy dư cho $10^9+7$.

## Input
- Một dòng chứa hai số nguyên $N$ và $M$ ($1 \le N, M \le 1000$).

## Output
- Số cách đi theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
3 3
```
### Output
```text
6
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
