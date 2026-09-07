# Chia bánh pizza đều nhau

## Bối cảnh

Lớp học tổ chức liên hoan cuối tuần với vài chiếc bánh pizza cỡ khác nhau. Cô giáo muốn cắt tất cả bánh thành những miếng bằng nhau sao cho mỗi bạn đều nhận được một miếng và phần bánh bỏ đi là ít nhất.

Các bạn háo hức đoán xem miếng bánh lớn nhất có thể chia đều được là bao nhiêu.

## Nhiệm vụ

Cho dữ liệu mô tả các chiếc bánh và số người cần chia. Hãy lập trình tìm kích thước miếng bánh lớn nhất có thể cắt đều cho mọi người sao cho phần dư ra là ít nhất.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, k$ ($1 \le n \le 100$, $1 \le k \le 10000$) — số chiếc bánh và số người ăn.
- Dòng thứ hai chứa $n$ số thực $r_i$ ($0 < r_i \le 10000$) là bán kính của từng chiếc bánh.

## Output

- In ra một dòng duy nhất là diện tích miếng bánh lớn nhất có thể chia đều cho $k$ người (mỗi người nhận các miếng có cùng diện tích, mỗi chiếc bánh có thể cắt thành nhiều miếng), làm tròn tới $6$ chữ số thập phân.

## Sample 1
### Input
```text
2 2
3 1
```
### Output
```text
14.137167
```
### Giải thích

Diện tích hai chiếc bánh là $\pi \cdot 3^2 \approx 28{,}274$ và $\pi \cdot 1^2 \approx 3{,}142$. Với miếng cỡ $14{,}137167$: chiếc bánh to cắt được đúng $2$ miếng ($28{,}274 / 2$), chiếc nhỏ không đủ một miếng — vừa đủ cho $2$ người. Nếu tăng miếng lên dù chỉ một chút, chiếc bánh to chỉ còn $1$ miếng nên không đủ chia. Vậy đây là cỡ miếng lớn nhất.

## Ràng buộc

- $1 \le n \le 100$, $1 \le k \le 10000$, $0 < r_i \le 10000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
