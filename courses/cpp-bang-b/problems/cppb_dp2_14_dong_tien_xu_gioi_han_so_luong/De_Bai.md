# Đổi Tiền Giới Hạn Số Lượng (Bounded Knapsack)

## Bối cảnh
Tại một cây ATM phân phối tiền mặt, máy chứa $N$ mệnh giá tiền khác nhau. Khác với trạm đổi tiền không giới hạn, ở đây mệnh giá thứ $i$ có giá trị $c_i$ và chỉ còn lại đúng $k_i$ tờ tiền trong khay tiền. Khách hàng muốn rút một khoản tiền đúng bằng $S$ đồng.

## Nhiệm vụ
Cho danh sách $N$ mệnh giá kèm số lượng tờ tiền tương ứng và số tiền cần rút $S$. Hãy lập trình tìm số lượng tờ tiền ít nhất để chi trả đúng số tiền $S$. Nếu khay tiền không thể đáp ứng, in ra `-1`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$).
- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $c_i$ và $k_i$ ($1 \le c_i \le 10^4, 1 \le k_i \le 1000$).

## Output
- In ra số tờ tiền ít nhất cần dùng, hoặc `-1` nếu không thể chi trả chính xác số tiền $S$.

## Sample 1
### Input
```text
3 11
1 2
5 2
6 1
```
### Output
```text
2
```

### Giải thích
Với số tiền cần rút $S = 10$ và các mệnh giá: 5 đồng (có 1 tờ), 2 đồng (có 3 tờ):
Chọn 1 tờ 5 đồng và 2 tờ 2 đồng ($5 + 2 × 2 = 9 < 10$).
Phương án đổi đúng là dùng 5 tờ 2 đồng (nhưng chỉ có 3 tờ nên không được).
Nếu có thêm mệnh giá 1 đồng (2 tờ): Dùng 1 tờ 5, 2 tờ 2 và 1 tờ 1, tổng cộng 4 tờ tiền.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 20000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
