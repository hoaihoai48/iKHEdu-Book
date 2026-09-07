# Đếm số phần tử bật BIT chung (bitwise and)

## Bối cảnh

Trường học vừa phát cho mỗi học sinh một chiếc thẻ từ ra vào cổng, bên trong thẻ lưu một mã số nguyên làm định danh. Cuối tuần, thầy giám thị muốn kiểm tra xem hệ thống đầu đọc có nhận diện lệch sóng ở vị trí bit nào không. Thầy quyết định thống kê toàn bộ thẻ: với từng vị trí bit từ $0$ đến $30$, thầy đếm xem có bao nhiêu chiếc thẻ đang bật bit đó, tức bit đó bằng $1$ trong mã số.

## Nhiệm vụ

Cho $N$ số nguyên là mã số trên các thẻ. Hãy lập trình đếm, với mỗi vị trí bit $b$ từ $0$ đến $30$, có bao nhiêu mã số có bit $b$ bằng $1$, rồi in ra toàn bộ bảng thống kê.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số lượng thẻ.
- Dòng thứ hai chứa $N$ số nguyên $x_i$ ($0 \le x_i \le 10^9$), là mã số của từng thẻ.

## Output

- In ra đúng $31$ dòng, dòng thứ $b$ (tính từ $0$) có dạng `Bit b: c`, trong đó $c$ là số lượng mã số có bit $b$ bằng $1$.

## Sample 1

### Input

```text
3
5 7 10
```

### Output

```text
Bit 0: 2
Bit 1: 2
Bit 2: 2
Bit 3: 1
Bit 4: 0
Bit 5: 0
Bit 6: 0
Bit 7: 0
Bit 8: 0
Bit 9: 0
Bit 10: 0
Bit 11: 0
Bit 12: 0
Bit 13: 0
Bit 14: 0
Bit 15: 0
Bit 16: 0
Bit 17: 0
Bit 18: 0
Bit 19: 0
Bit 20: 0
Bit 21: 0
Bit 22: 0
Bit 23: 0
Bit 24: 0
Bit 25: 0
Bit 26: 0
Bit 27: 0
Bit 28: 0
Bit 29: 0
Bit 30: 0
```

### Giải thích

- Viết ba mã số dưới dạng nhị phân: $5 = 101_2$, $7 = 111_2$, $10 = 1010_2$.
- Bit $0$ (giá trị $1$): xuất hiện trong $5$ và $7$ nên đếm được $2$.
- Bit $1$ (giá trị $2$): xuất hiện trong $7$ và $10$ nên đếm được $2$.
- Bit $2$ (giá trị $4$): xuất hiện trong $5$ và $7$ nên đếm được $2$.
- Bit $3$ (giá trị $8$): chỉ xuất hiện trong $10$ nên đếm được $1$.
- Mọi bit từ $4$ đến $30$ đều bằng $0$ trong cả ba số nên đếm được $0$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le x_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
