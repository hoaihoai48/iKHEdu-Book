# Đếm Số Ô Kề Cạnh Hợp Lệ (4 Hướng)

## Bối cảnh
Trong một hệ thống điều khiển lưới cảm biến kích thước $N × M$ ô vuông (chỉ số các ô từ $(0, 0)$ đến $(N - 1, M - 1)$), một thiết bị di động đang đứng tại ô tọa độ $(r, c)$. Thiết bị chỉ có thể gửi tín hiệu không dây tới các ô kề sát cạnh theo 4 hướng chính: lên trên $(r - 1, c)$, xuống dưới $(r + 1, c)$, sang trái $(r, c - 1)$, và sang phải $(r, c + 1)$. Kỹ sư phần mềm cần kiểm tra xem có bao nhiêu hướng di chuyển hợp lệ vẫn nằm trọn vẹn bên trong phạm vi ma trận.

## Nhiệm vụ
Cho kích thước ma trận $N, M$ và tọa độ $(r, c)$. Hãy lập trình đếm số ô kề cạnh hợp lệ nằm trong ma trận.

## Input
- Một dòng duy nhất chứa 4 số nguyên $N, M, r, c$ ($1 \le N, M \le 1000, 0 \le r < N, 0 \le c < M$).

## Output
- In ra trên một dòng duy nhất một số nguyên là số ô kề cạnh hợp lệ.

## Sample 1
### Input
```text
3 3 0 0
```
### Output
```text
2
```

### Giải thích
Với lưới kích thước $3 × 3$ và vị trí ô góc $(0, 0)$:

- Hướng lên trên và sang trái đều vượt ra ngoài biên của lưới.
- Chỉ có 2 hướng hợp lệ là xuống dưới $(1, 0)$ và sang phải $(0, 1)$.
Số ô kề cạnh hợp lệ là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
