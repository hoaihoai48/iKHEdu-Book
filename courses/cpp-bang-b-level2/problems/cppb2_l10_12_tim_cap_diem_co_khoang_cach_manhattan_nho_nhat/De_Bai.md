# Tìm cặp điểm có khoảng cách manhattan nhỏ nhất

## Bối cảnh

Thành phố lắp đặt nhiều trạm quan trắc không khí tại các giao lộ trên bản đồ lưới đường phố, mỗi trạm có tọa độ nguyên $(x_i, y_i)$. Để hiệu chuẩn thiết bị, kỹ sư cần tìm hai trạm gần nhau nhất theo khoảng cách đường phố (tổng độ chênh lệch theo hai trục, vì xe hiệu chuẩn chỉ chạy dọc các con đường vuông góc). Cặp trạm gần nhất cho kết quả so sánh đáng tin cậy nhất, giúp phát hiện sớm cảm biến nào bị lệch trước khi số liệu sai lan ra toàn hệ thống.

## Nhiệm vụ

Cho $N$ điểm trên mặt phẳng với tọa độ nguyên. Khoảng cách Manhattan giữa hai điểm $(x_1, y_1)$ và $(x_2, y_2)$ là $|x_1 - x_2| + |y_1 - y_2|$. Hãy lập trình tìm khoảng cách nhỏ nhất trong mọi cặp điểm phân biệt, rồi in ra khoảng cách đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($2 \le N \le 10^5$), là số trạm quan trắc.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $x_i, y_i$ ($-10^9 \le x_i, y_i \le 10^9$), là tọa độ một trạm.

## Output

- In ra một số nguyên duy nhất là khoảng cách Manhattan nhỏ nhất.

## Sample 1

### Input

```text
3
0 0
1 1
3 0
```

### Output

```text
2
```

### Giải thích

- Liệt kê cả $3$ cặp trạm cùng khoảng cách đường phố của từng cặp.
- Cặp $(0, 0)$ và $(1, 1)$ có khoảng cách $|0 - 1| + |0 - 1| = 2$.
- Cặp $(0, 0)$ và $(3, 0)$ có khoảng cách $|0 - 3| + |0 - 0| = 3$.
- Cặp $(1, 1)$ và $(3, 0)$ có khoảng cách $|1 - 3| + |1 - 0| = 3$.
- Khoảng cách nhỏ nhất là $2$.

## Ràng buộc

- $2 \le N \le 10^5$, $-10^9 \le x_i, y_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
