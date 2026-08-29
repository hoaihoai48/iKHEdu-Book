# Bảng Điểm Học Sinh Đa Trường

## Bối cảnh
Cho danh sách $N$ học sinh tham gia kỳ thi. Mỗi học sinh có mã số $ID$, điểm thi Toán và điểm thi Tin. Hãy sắp xếp danh sách học sinh theo các quy tắc sau:
1. Tổng điểm (Toán + Tin) giảm dần.
2. Nếu bằng tổng điểm, điểm Tin học cao hơn đứng trước.
3. Nếu vẫn bằng nhau, mã số $ID$ nhỏ hơn đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 3 số nguyên $ID, Math, Info$ ($1 \le ID \le 10^9, 0 \le Math, Info \le 100$).

## Output
- In ra danh sách học sinh sau khi sắp xếp, mỗi học sinh gồm 3 số $ID, Math, Info$ trên một dòng.

## Sample 1
### Input
```text
3
101 8 9
102 9 8
103 10 10
```
### Output
```text
103 10 10
101 8 9
102 9 8
```

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
