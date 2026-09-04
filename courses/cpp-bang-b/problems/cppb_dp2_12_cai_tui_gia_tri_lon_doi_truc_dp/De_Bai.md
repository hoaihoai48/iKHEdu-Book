# Cái Túi Khối Lượng Cực Đại W <= 10^9 (Đổi Trục DP)

## Bối cảnh
Một tàu thám hiểm không gian vũ trụ có khoang chứa hàng với tải trọng cực lớn lên tới $W = 10^9$ kg. Có $N$ mẫu vật thể ngoài hành tinh được đánh số từ $1$ đến $N$. Mẫu vật thứ $i$ có khối lượng $w_i$ lên tới $10^9$, nhưng giá trị khoa học $v_i$ lại khá nhỏ ($v_i \le 1000$). Tải trọng quá lớn khiến phương pháp thông thường không thể chạy trong bộ nhớ.

## Nhiệm vụ
Cho $N$ mẫu vật ($w_i, v_i$) và tải trọng $W \le 10^9$. Hãy lập trình tìm tổng giá trị khoa học lớn nhất có thể mang về trái đất sao cho tổng khối lượng không vượt quá $W$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 100, 1 \le W \le 10^9$).
- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $w_i$ và $v_i$ ($1 \le w_i \le 10^9, 1 \le v_i \le 1000$).

## Output
- In ra trên một dòng duy nhất tổng giá trị lớn nhất đạt được.

## Sample 1
### Input
```text
3 8
3 30
4 50
5 60
```
### Output
```text
90
```

### Giải thích
Với $N = 3, W = 10$ và các mẫu vật $[(3, 30), (4, 50), (5, 60)]$:
Chọn mẫu vật 1 và mẫu vật 3 với tổng khối lượng $3 + 5 = 8 \le 10$, đạt tổng giá trị là $30 + 60 = 90$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le W \le 10^9, 1 \le V_i \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
