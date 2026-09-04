# Đường Đi Ngắn Nhất Trên Đồ Thị Không Trọng Số

## Bối cảnh
Một đoàn tàu hỏa vận chuyển hàng hóa di chuyển trên mạng lưới đường ray gồm $N$ nhà ga và $M$ chặng ray hai chiều nối giữa các ga kề nhau. Đoàn tàu cần đi từ ga xuất phát $S$ đến ga đích $D$. Mỗi chặng ray mất đúng 1 giờ chạy tàu. Hãy tìm thời gian ít nhất (tổng số chặng ray ít nhất) để tàu đến được ga đích.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình tìm số cạnh trên đường đi ngắn nhất từ $S$ tới $D$. Nếu không có đường đi, in ra `-1`.

## Input
- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.

## Output
- In ra số cạnh ngắn nhất từ $S$ tới $D$, hoặc `-1` nếu không có đường đi.

## Sample 1
### Input
```text
4 4
1 2
2 3
3 4
1 3
```
### Output
```text
2
```

### Giải thích
Với mạng đường ray có các chặng (1, 2), (2, 3), (1, 4), (4, 3) từ ga 1 tới ga 3:
Có hai lộ trình cùng đạt 2 chặng là $1  × o 2  × o 3$ hoặc $1  × o 4  × o 3$. Thời gian ít nhất là 2 chặng.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
