# Cái Túi 0/1 Cơ Bản (0/1 Knapsack)

## Bối cảnh
Một nhà thám hiểm chuẩn bị hành trang cho chuyến đi băng rừng. Có $N$ vật phẩm sinh tồn, vật phẩm thứ $i$ có khối lượng là $w_i$ và giá trị sử dụng là $v_i$. Nhà thám hiểm mang theo một chiếc ba lô có sức chứa tải trọng tối đa là $W$. Mỗi vật phẩm chỉ có duy nhất một chiếc (chọn lấy hoặc không lấy).

## Nhiệm vụ
Cho danh sách khối lượng và giá trị của $N$ vật phẩm cùng tải trọng $W$. Hãy lập trình chọn ra một tập hợp vật phẩm sao cho tổng khối lượng không vượt quá $W$ và tổng giá trị mang lại là lớn nhất.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 1000$).
- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $w_i$ và $v_i$ ($1 \le w_i, v_i \le 1000$) lần lượt là khối lượng và giá trị của món đồ thứ $i$.

## Output
- In ra trên một dòng duy nhất tổng giá trị lớn nhất có thể xếp vào ba lô.

## Sample 1
### Input
```text
4 7
1 1
3 4
4 5
5 7
```
### Output
```text
9
```

### Giải thích
Với 4 đồ vật có thông số [(khối lượng 2, giá trị 3), (3, 4), (4, 5), (5, 6)] và ba lô có sức chứa $W = 5$:
Phương án tối ưu là chọn đồ vật 1 ($w = 2, v = 3$) và đồ vật 2 ($w = 3, v = 4$). Tổng khối lượng là $2 + 3 = 5 \le 5$, đạt tổng giá trị tối đa là $3 + 4 = 7$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 1 \le W \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
