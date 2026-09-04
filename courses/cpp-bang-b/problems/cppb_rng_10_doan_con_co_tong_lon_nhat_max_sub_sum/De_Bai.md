# Đoạn Con Có Tổng Lớn Nhất Trên Đoạn (Maximum Subarray Query)

## Bối cảnh
Một bảng giá vàng ghi nhận mức biến động giá qua $N$ ngày. Các nhà đầu tư muốn tra cứu xem trong một khoảng thời gian bất kỳ từ ngày $L$ đến ngày $R$, một đợt sóng tăng giá liên tiếp (đoạn con có tổng lớn nhất) có thể đem lại lợi nhuận tối đa là bao nhiêu.

## Nhiệm vụ
Cho mảng $A$ và $Q$ truy vấn gồm hai số $L, R$. Hãy tìm tổng lớn nhất của một đoạn con không rỗng nằm trọn vẹn bên trong đoạn $[L, R]$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $L$ và $R$.

## Output
- Với mỗi truy vấn, in ra tổng đoạn con lớn nhất tìm được trên một dòng.

## Sample 1
### Input
```text
5 3
1 2 -5 4 5
2 1 5
1 3 10
2 1 5
```
### Output
```text
9
22
```

### Giải thích
Với mảng $[-2, 1, -3, 4, -1, 2, 1, -5, 4]$ và truy vấn đoạn từ vị trí 1 đến 9:
Đoạn con liên tiếp có tổng lớn nhất là $[4, -1, 2, 1]$ mang lại tổng là $4 + (-1) + 2 + 1 = 6$.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, -10^9 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
