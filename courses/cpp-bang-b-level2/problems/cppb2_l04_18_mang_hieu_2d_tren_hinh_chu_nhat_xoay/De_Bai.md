# Mảng hiệu trên hình vuông xoay 45 độ

## Bối cảnh
Cho một lưới ô vuông kích thước $N \times N$, ban đầu tất cả các ô đều có giá trị bằng $0$. Có $Q$ phép cập nhật, mỗi phép cập nhật cho một ô tâm $(x, y)$, bán kính khoảng cách Manhattan $d$ và một giá trị cộng thêm $val$. Nghĩa là mọi ô $(r, c)$ thỏa mãn $|r - x| + |c - y| \le d$ đều được cộng thêm giá trị $val$.

## Nhiệm vụ
Hãy tìm giá trị lớn nhất trong toàn bộ lưới ô vuông $N \times N$ sau khi thực hiện xong tất cả $Q$ phép cập nhật.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N \le 1000, 1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $x, y, d, val$ ($1 \le x, y \le N, 0 \le d \le 2N, 1 \le val \le 10^6$).

## Output
- In ra một số nguyên duy nhất là giá trị lớn nhất trong lưới sau $Q$ phép cập nhật.

## Sample 1
### Input
```text
3 2
2 2 1 5
1 1 0 3
```
### Output
```text
8
```
### Giải thích
* Phép cập nhật 1: Cộng $5$ vào vùng Manhattan bán kính $1$ quanh ô $(2, 2)$ gồm các ô $(2,2), (1,2), (3,2), (2,1), (2,3)$.
* Phép cập nhật 2: Cộng $3$ vào riêng ô $(1, 1)$. Ô $(2, 2)$ đạt giá trị lớn nhất là $5$, hoặc ô $(1, 2)$ đạt $5$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 1 \le Q \le 10^5, 1 \le val \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
