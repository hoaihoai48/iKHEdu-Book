# Nhặt Vàng Trên Lưới

## Bối cảnh
Trong một trò chơi phiêu lưu, một nhà khảo cổ học thám hiểm một lăng mộ cổ hình chữ nhật gồm $N  × M$ gian phòng. Gian phòng tại tọa độ $(i, j)$ chứa một số thỏi vàng có giá trị là $A_{i,j}$. Nhà khảo cổ xuất phát từ căn phòng $(1, 1)$ và cần thoát ra ở căn phòng $(N, M)$. Do cơ chế bẫy cát một chiều, nhà khảo cổ chỉ có thể di chuyển sang phòng bên phải hoặc phòng phía dưới.

## Nhiệm vụ
Cho ma trận số vàng tại các gian phòng. Hãy lập trình tìm tổng số vàng lớn nhất mà nhà khảo cổ có thể thu thập được trên đường thoát ra.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên không âm $A_{i,j}$ ($0 \le A_{i,j} \le 10^4$).

## Output
- In ra trên một dòng duy nhất tổng lượng vàng lớn nhất có thể thu thập.

## Sample 1
### Input
```text
3 3
1 2 3
0 5 0
4 1 2
```
### Output
```text
13
```

### Giải thích
Với lưới vàng kích thước $3  × 3$:
Lộ trình thu thập tối ưu là đi qua các gian phòng có lượng vàng phong phú nhất, đạt tổng giá trị lớn nhất là 15.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000, 0 \le A_{i, j} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
