# Cây Fenwick 2D Tính Tổng Hình Chữ Nhật (2D BIT)

## Bối cảnh
Một bức ảnh kỹ thuật số dạng lưới $N  × M$ điểm ảnh, điểm ảnh tại ô $(r, c)$ có giá trị độ sáng $A_{r,c}$. Hệ thống camera cần hỗ trợ hai thao tác: tăng độ sáng tại một điểm ảnh cụ thể thêm $val$, và tính tổng độ sáng của toàn bộ các điểm ảnh nằm trong một vùng hình chữ nhật từ $(r_1, c_1)$ đến $(r_2, c_2)$.

## Nhiệm vụ
Cho ma trận độ sáng ban đầu và $Q$ thao tác thuộc hai dạng: cập nhật điểm ảnh hoặc truy vấn tổng vùng hình chữ nhật. Hãy in ra kết quả của các thao tác truy vấn.

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- Các dòng tiếp theo mô tả ma trận ban đầu và $Q$ thao tác.

## Output
- Với mỗi thao tác truy vấn hình chữ nhật, in ra tổng độ sáng tương ứng trên một dòng.

## Sample 1
### Input
```text
3 3 3
1 1 1 5
1 2 2 10
2 1 1 2 2
```
### Output
```text
15
```

### Giải thích
Với ma trận $3 × 3$ toàn số 1: Tổng độ sáng của hình chữ nhật con kích thước $2 × 2$ từ $(1, 1)$ đến $(2, 2)$ gồm 4 ô số 1, tổng bằng 4.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000, 1 \le Q \le 50000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
