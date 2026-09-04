# Kiểm Tra Đường Đi Giữa Hai Đỉnh

## Bối cảnh
Trong hệ thống mạng lưới điện quốc gia gồm $N$ trạm biến áp và $M$ đường dây tải điện hai chiều, trung tâm điều độ cần kiểm tra nhanh xem liệu có tồn tại tuyến đường dây kết nối (trực tiếp hoặc qua các trạm trung gian) giữa hai trạm biến áp $S$ và $D$ hay không.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình kiểm tra xem có tồn tại đường đi giữa $S$ và $D$ hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5, 1 \le S, D \le N$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.

## Output
- In ra `YES` nếu có đường đi giữa $S$ và $D$, ngược lại in ra `NO`.

## Sample 1
### Input
```text
4 2 1 4
1 2
2 3
```
### Output
```text
NO
```

### Giải thích
Với đồ thị có các cạnh (1, 2), (2, 3) và đỉnh 4 cô lập:
- Kiểm tra giữa 1 và 3: Tồn tại đường đi $1  × o 2  × o 3$, in ra YES.
- Nếu kiểm tra giữa 1 và 4: Không có đường đi, in ra NO.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
