# Chia Kẹo Cho Học Sinh Đạt Chuẩn

## Bối cảnh
Một trường tiểu học nhận được N thùng kẹo, thùng thứ i có Ai chiếc kẹo. Thầy hiệu trưởng muốn chia đều kẹo cho K em học sinh đạt danh hiệu cháu ngoan Bác Hồ sao cho mỗi em nhận được đúng X chiếc kẹo và kẹo phát cho mỗi em chỉ được lấy ra từ một thùng kẹo duy nhất (không ghép mảnh kẹo từ nhiều thùng khác nhau). Hãy tìm số lượng kẹo X lớn nhất có thể phát cho mỗi em.

## Nhiệm vụ
Cho N gói kẹo và số học sinh K. Mỗi học sinh chỉ nhận kẹo từ cùng 1 gói. Hãy tìm số kẹo X lớn nhất phát đều cho K học sinh.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 10^5, 1 \le K \le 10^9$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra số kẹo lớn nhất $X$ có thể chia cho mỗi học sinh. Nếu không chia được chiếc nào, in `0`.

## Sample 1
### Input
```text
4 6
15 8 10 7
```
### Output
```text
5
```
### Giải thích
Nếu mỗi em nhận X = 5 chiếc kẹo:
- Thùng 1 (15 kẹo) chia được 15/5 = 3 em.
- Thùng 2 (8 kẹo) chia được 8/5 = 1 em.
- Thùng 3 (10 kẹo) chia được 10/5 = 2 em.
- Thùng 4 (7 kẹo) chia được 7/5 = 1 em.
Tổng số em được nhận là 3 + 1 + 2 + 1 = 7 >= 6 em. Nếu tăng X = 6 sẽ không đủ 6 phần. Vậy X lớn nhất là 5.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, K \le 10^9, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
