# Đổi Tiền Số Xu Ít Nhất

## Bối cảnh
Cho $N$ mệnh giá đồng xu và số tiền mục tiêu $S$. Mỗi mệnh giá có số lượng không giới hạn.

## Nhiệm vụ
Tìm số lượng đồng xu ít nhất để đổi được đúng số tiền $S$. Nếu không đổi được in -1.

## Input
- Dòng 1: Hai số nguyên $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$).
- Dòng 2: $N$ số nguyên dương biểu diễn các mệnh giá xu ($1 \le c_i \le 10^4$).

## Output
- Số lượng đồng xu ít nhất hoặc -1 nếu không thể đổi.

## Sample 1
### Input
```text
3 11
1 5 6
```
### Output
```text
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
