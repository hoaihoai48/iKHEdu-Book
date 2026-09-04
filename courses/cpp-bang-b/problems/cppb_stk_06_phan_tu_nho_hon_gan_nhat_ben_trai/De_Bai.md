# Phần Tử Nhỏ Hơn Gần Nhất Bên Trái (Previous Smaller Element)

## Bối cảnh
Một hệ thống băng tải tự động gồm $N$ vị trí cảm biến. Với mỗi vị trí cảm biến $i$, hệ thống cần xác định vị trí của cảm biến đầu tiên nằm về phía bên trái có chỉ số đọc nhỏ hơn cảm biến $i$ để tính toán độ dốc địa hình ngược chiều dòng sản phẩm.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Với mỗi phần tử $A_i$, hãy tìm phần tử đầu tiên nằm bên trái nó có giá trị nhỏ hơn nó. Nếu không có phần tử nào thỏa mãn, gán `-1`.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N$ số nguyên là các giá trị nhỏ hơn gần nhất bên trái tương ứng.

## Sample 1
### Input
```text
5
4 5 2 10 8
```
### Output
```text
-1 4 -1 2 2
```

### Giải thích
Với mảng $[4, 5, 2, 10, 8]$:
- Số 4: Bên trái không có số nào $\to$ -1.
- Số 5: Số đầu tiên bên trái nhỏ hơn 5 là 4.
- Số 2: Bên trái không có số nào nhỏ hơn 2 $\to$ -1.
- Số 10: Số đầu tiên bên trái nhỏ hơn 10 là 2.
- Số 8: Số đầu tiên bên trái nhỏ hơn 8 là 2.
Kết quả in ra: -1 4 -1 2 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
