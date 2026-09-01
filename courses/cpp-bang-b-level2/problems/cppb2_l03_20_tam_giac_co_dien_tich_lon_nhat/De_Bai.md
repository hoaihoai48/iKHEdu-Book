# Tam giác có diện tích lớn nhất

## Bối cảnh
Cho một đa giác lồi gồm $N$ đỉnh trên mặt phẳng tọa độ $Oxy$ được liệt kê theo chiều ngược chiều kim đồng hồ. Cần chọn ra 3 đỉnh phân biệt của đa giác lồi sao cho tam giác tạo bởi 3 đỉnh này có diện tích lớn nhất.

## Nhiệm vụ
Hãy lập trình tìm diện tích lớn nhất của tam giác được tạo từ 3 đỉnh bất kỳ của đa giác lồi bằng kỹ thuật Hai con trỏ quay (Rotating Calipers) với độ phức tạp $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N)$.

## Input
- Dòng 1: Gồm 1 số nguyên $N$ ($3 \le N \le 3000$) — số đỉnh của đa giác lồi.
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $x_i, y_i$ ($|x_i|, |y_i| \le 10^9$) — tọa độ đỉnh thứ $i$.

## Output
- In ra diện tích lớn nhất tìm được với đúng 1 chữ số thập phân sau dấu phẩy.

## Sample 1
### Input
```text
4
0 0
4 0
4 3
0 3
```
### Output
```text
6.0
```
### Giải thích
* 4 đỉnh tạo thành hình chữ nhật kích thước $4 \times 3$. Chọn 3 đỉnh $(0,0), (4,0), (4,3)$ tạo thành tam giác vuông có diện tích $S = \frac{1}{2} \times 4 \times 3 = 6.0$.

## Ràng buộc
- $100\%$ số test có $3 \le N \le 3000, |x_i|, |y_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
