# Đếm Số Tam Giác Có Thể Tạo Thành

## Bối cảnh
Một nghệ nhân điêu khắc kiến trúc gỗ có N que gỗ thẳng với độ dài lần lượt là A1, A2, ..., An. Để tạo các mắt lưới tam giác trang trí chịu lực cho mái vòm công trình, nghệ nhân cần chọn ra bộ 3 que gỗ bất kỳ có thể ghép thành một tam giác không suy biến (nghĩa là độ dài của que bất kỳ phải nhỏ hơn tổng độ dài hai que còn lại). Hãy giúp nghệ nhân đếm xem có bao nhiêu cách chọn ra bộ 3 que gỗ hợp lệ.

## Nhiệm vụ
Cho N đoạn que với độ dài A1, A2, ..., An. Hãy đếm số lượng bộ 3 que có thể ghép lại thành một tam giác không suy biến.

## Input
- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 3000$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng tam giác tạo được.

## Sample 1
### Input
```text
4
4 6 3 7
```
### Output
```text
3
```
### Giải thích
Sắp xếp độ dài 4 que gỗ tăng dần: [3, 4, 6, 7]. Xét các bộ ba que gỗ: (3, 4, 6) có 3 + 4 = 7 > 6 -> lập được tam giác; (3, 6, 7) có 3 + 6 = 9 > 7 -> lập được tam giác; (4, 6, 7) có 4 + 6 = 10 > 7 -> lập được tam giác; (3, 4, 7) có 3 + 4 = 7 không lớn hơn 7 -> bị suy biến (không lập được tam giác). Tổng cộng tạo được đúng 3 tam giác không suy biến.

## Ràng buộc
- $100\%$ số test có $N \le 3000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
