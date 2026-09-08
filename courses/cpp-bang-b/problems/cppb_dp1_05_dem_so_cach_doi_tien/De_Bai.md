# Đếm Số Cách Đổi Tiền

## Bối cảnh
Tại một hội thảo tài chính công nghệ, ban tổ chức thiết kế một thử thách cho các bạn học sinh về phương thức kết hợp tiền tệ. Cho $N$ mệnh giá đồng xu khác nhau, mỗi mệnh giá đều có số lượng không giới hạn. Một bạn học sinh cần tạo ra tổng số tiền đúng bằng $S$ đồng. Hai cách tạo tiền được xem là khác nhau nếu số lượng sử dụng của ít nhất một mệnh giá đồng xu là khác nhau (thứ tự chọn các đồng xu không làm ảnh hưởng đến tính chất của tổ hợp).

## Nhiệm vụ
Cho $N$ mệnh giá đồng xu và số tiền mục tiêu $S$. Hãy lập trình đếm xem có tất cả bao nhiêu tổ hợp đồng xu khác nhau để có tổng giá trị đúng bằng $S$. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $10^9 + 7$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương phân biệt biểu diễn các mệnh giá đồng xu ($1 \le c_i \le 10^4$).

## Output
- In ra trên một dòng duy nhất số lượng tổ hợp đổi tiền hợp lệ theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
3 9
2 3 5
```
### Output
```text
3
```

### Giải thích
Với các mệnh giá xu $\{2, 3, 5\}$ và số tiền mục tiêu $S = 9$, có đúng 3 tổ hợp đồng xu khác nhau:

1. Ba đồng xu: $2 + 2 + 5 = 9$.
2. Ba đồng xu: $3 + 3 + 3 = 9$.
3. Bốn đồng xu: $2 + 2 + 2 + 3 = 9$.
Kết quả đếm được là 3 cách.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
