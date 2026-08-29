# Chia Kẹo Cho Học Sinh Đạt Chuẩn

## Bối cảnh
Có $N$ gói kẹo, gói thứ $i$ chứa $A_i$ chiếc kẹo. Thầy giáo muốn chia đều kẹo cho $K$ học sinh sao cho mỗi học sinh nhận được đúng $M$ chiếc kẹo từ một gói nào đó (mỗi gói có thể chia cho nhiều học sinh, nhưng kẹo thừa trong gói không được ghép với gói khác).

## Nhiệm vụ
Hãy tìm số lượng kẹo $M$ lớn nhất mà mỗi học sinh có thể nhận được. Nếu không thể chia cho đủ $K$ học sinh (ngay cả khi mỗi bạn 1 chiếc), in ra `0`.

## Input
- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le N \le 10^5, 1 \le K \le 10^{14}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là giá trị $M$ lớn nhất tìm được.

## Sample 1
### Input
```text
4 6
10 15 20 25
```
### Output
```text
10
```
*(Giải thích: Với $M = 10$, các gói chia được lần lượt: $\lfloor 10/10 \rfloor = 1$, $\lfloor 15/10 \rfloor = 1$, $\lfloor 20/10 \rfloor = 2$, $\lfloor 25/10 \rfloor = 2$. Tổng cộng $1 + 1 + 2 + 2 = 6$ phần kẹo, đủ cho 6 học sinh).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, K \le 10^{14}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
