# Tối Ưu Hóa Túi Đồ Hỗn Hợp (Hybrid Knapsack)

## Bối cảnh
Một trung tâm cứu hộ thiên tai chuẩn bị các gói hàng viện trợ để thả dù xuống vùng bão lũ. Có $N$ loại hàng hóa thiết yếu, mỗi loại có khối lượng $w_i$ và giá trị cứu trợ $v_i$. Tính chất nguồn cung của các mặt hàng rất đa dạng: một số mặt hàng chỉ có duy nhất 1 kiện (loại 0/1), một số mặt hàng được tài trợ không giới hạn (loại không giới hạn), và một số mặt hàng chỉ có số lượng cố định $k_i$ kiện (loại giới hạn). Khoang hàng máy bay có sức chứa tối đa là $W$.

## Nhiệm vụ
Cho danh sách $N$ loại hàng với đặc tính số lượng của từng loại và tải trọng khoang bay $W$. Hãy lập trình tìm tổng giá trị cứu trợ lớn nhất có thể vận chuyển.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng mô tả một loại hàng: khối lượng $w_i$, giá trị $v_i$ và số lượng $k_i$ ($k_i = 0$ nghĩa là số lượng không giới hạn).

## Output
- In ra trên một dòng duy nhất tổng giá trị cứu trợ lớn nhất đạt được.

## Sample 1
### Input
```text
3 10
1 4 20
2 3 15
1 5 30
```
### Output
```text
50
```

### Giải thích
Với khoang máy bay có tải trọng $W = 15$ và danh mục hàng cứu trợ hỗn hợp:
Sự kết hợp tối ưu giữa các mặt hàng giới hạn và hàng không giới hạn đem lại tổng giá trị lớn nhất là 32.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le W \le 5000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
