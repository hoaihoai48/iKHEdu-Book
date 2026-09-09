# Lây Lan Quả Cam Hỏng (Rotting Oranges)

## Bối cảnh
Trong một thùng hàng hoa quả kích thước $N × M$, mỗi ô có thể chứa: ô trống (số `0`), một quả cam tươi nguyên vẹn (số `1`), hoặc một quả cam đã bị hỏng mốc (số `2`). Cứ sau mỗi phút, những quả cam bị hỏng sẽ làm hỏng tất cả các quả cam tươi kề sát nó theo 4 hướng. Hãy tính số phút tối thiểu để toàn bộ cam tươi trong thùng đều bị hỏng. Nếu có quả cam tươi nào mãi mãi không bị hỏng (bị cô lập), in ra `-1`.

## Nhiệm vụ
Cho ma trận trạng thái thùng cam. Hãy lập trình tìm số phút ít nhất để tất cả cam tươi đều hỏng.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên 0, 1 hoặc 2 cách nhau bởi khoảng trắng.

## Output
- In ra số phút ít nhất, hoặc `-1` nếu vẫn còn cam tươi không thể bị hỏng.

## Sample 1
### Input
```text
3 3
211
110
011
```
### Output
```text
4
```

### Giải thích
Với thùng cam kích thước $3 × 3$:

- Phút 1: cam hỏng tại $(0, 0)$ lây sang các ô $(0, 1)$ và $(1, 0)$.
- Phút 2: tiếp tục lây sang các ô kế tiếp.
Sau đúng 4 phút, toàn bộ cam tươi đều đã bị lây hỏng. Kết quả là 4.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
