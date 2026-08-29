# Bảng Xếp Hạng Giải Đấu Thể Thao

## Bối cảnh
Cho kết quả của $N$ đội bóng gồm: Mã đội $ID$, Điểm số $Points$, Hiệu số bàn thắng $GoalDiff$, Số bàn thắng ghi được $Goals$. Hãy xếp hạng các đội theo thứ tự:
1. Điểm số giảm dần.
2. Hiệu số bàn thắng giảm dần.
3. Số bàn thắng ghi được giảm dần.
4. Mã đội $ID$ tăng dần.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $ID, Points, GoalDiff, Goals$.

## Output
- In ra danh sách mã đội $ID$ sau khi đã sắp xếp thứ hạng, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
3
1 10 5 12
2 10 5 15
3 12 2 8
```
### Output
```text
3 2 1
```

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
