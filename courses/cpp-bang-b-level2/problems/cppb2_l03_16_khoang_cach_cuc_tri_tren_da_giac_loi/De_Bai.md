# Khoảng cách cực trị trên đa giác lồi

## Bối cảnh

Đội đo đạc vẽ lại bản đồ một khu đất hình đa giác lồi rồi cắm cọc tại các đỉnh. Chú kỹ sư muốn biết hai cọc nào đứng xa nhau nhất để đặt đường dây quan trắc chính xác.

Tổ đo đạc đi vòng quanh khu đất, ghi lại tọa độ từng cọc rồi so sánh các khoảng cách.

## Nhiệm vụ

Cho một đa giác lồi có $n$ đỉnh và một điểm truy vấn $Q$. Hãy lập trình tìm khoảng cách Euclid lớn nhất từ $Q$ tới các đỉnh của đa giác.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($3 \le n \le 10^5$) — số đỉnh của đa giác.
- $n$ dòng tiếp theo, mỗi dòng chứa hai số thực $x_i, y_i$ ($|x_i|, |y_i| \le 10^9$) là tọa độ một đỉnh (cho theo thứ tự quanh đa giác).
- Dòng cuối cùng chứa hai số thực $x_Q, y_Q$ là tọa độ điểm truy vấn.

## Output

- In ra một dòng duy nhất là khoảng cách lớn nhất, làm tròn tới $6$ chữ số thập phân.

## Sample 1
### Input
```text
4
0 0
1 0
1 1
0 1
2 2
```
### Output
```text
2.828427
```
### Giải thích

Tính khoảng cách từ $(2, 2)$ tới từng đỉnh: tới $(0, 0)$ là $\sqrt{4 + 4} = \sqrt{8} \approx 2{,}828427$; tới $(1, 0)$ là $\sqrt{1 + 4} \approx 2{,}236$; tới $(1, 1)$ là $\sqrt{2} \approx 1{,}414$; tới $(0, 1)$ cũng $\approx 2{,}236$. Giá trị lớn nhất là $2{,}828427$.

## Ràng buộc

- $3 \le n \le 10^5$, tọa độ có trị tuyệt đối không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
