# Tìm giá trị lớn nhất và vị trí xuất hiện

## Bối cảnh
Trong cuộc thi bắn cung, ban giám khảo ghi nhận điểm số của $N$ lượt bắn vào một bảng điện tử. Bạn hãy viết chương trình giúp ban tổ chức tìm ra điểm số cao nhất đạt được và vị trí của lượt bắn đạt điểm số cao nhất đó (tính theo thứ tự từ $1$ đến $N$). Nếu có nhiều lượt bắn cùng đạt điểm cao nhất, hãy in ra vị trí xuất hiện đầu tiên.

## Nhiệm vụ
Cho một dãy gồm $N$ số nguyên. Hãy lập trình tìm giá trị lớn nhất trong dãy và chỉ số $1$-based của vị trí xuất hiện đầu tiên của giá trị lớn nhất đó.

## Input
- Dòng thứ nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $a_1, a_2, \dots, a_N$ ($-10^9 \le a_i \le 10^9$), cách nhau bởi một khoảng trắng.

## Output
- In ra hai số nguyên cách nhau bởi một khoảng trắng: số thứ nhất là giá trị lớn nhất, số thứ hai là vị trí (bắt đầu từ $1$) xuất hiện đầu tiên.

## Sample 1
### Input
```text
5
3 7 2 7 5
```
### Output
```text
7 2
```

### Giải thích
Giá trị lớn nhất trong dãy là $7$.
Giá trị $7$ xuất hiện ở vị trí thứ $2$ và vị trí thứ $4$. Vị trí xuất hiện đầu tiên là $2$. Kết quả: `7 2`.

## Sample 2
### Input
```text
4
-5 -2 -8 -2
```
### Output
```text
-2 2
```

### Giải thích
Giá trị lớn nhất là $-2$ tại vị trí thứ $2$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, -10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
