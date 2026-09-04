# Truy Vết Món Đồ Cái Túi 0/1

## Bối cảnh
Sau khi tính toán được giá trị tài sản tối ưu xếp vào ba lô, nhà thám hiểm cần in ra danh sách chi tiết các món đồ cụ thể đã được chọn để bàn giao cho tổ hậu cần đóng gói hành lý.

## Nhiệm vụ
Cho $N$ đồ vật (mỗi vật có khối lượng $w_i$, giá trị $v_i$) và sức chứa ba lô $W$. Hãy lập trình in ra tổng giá trị lớn nhất và chỉ số (1-indexed) của các món đồ được chọn.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 1000$).
- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $w_i$ và $v_i$ ($1 \le w_i, v_i \le 1000$).

## Output
- Dòng 1: In ra tổng giá trị lớn nhất.
- Dòng 2: In ra số lượng món đồ được chọn $K$.
- Dòng 3: In ra $K$ số nguyên là chỉ số của các món đồ được chọn theo thứ tự tăng dần.

## Sample 1
### Input
```text
3 4
1 15
3 20
4 30
```
### Output
```text
35
2
1 2
```

### Giải thích
Với $N = 3, W = 4$ và các đồ vật $[(2, 3), (1, 2), (3, 4)]$:
Chọn món đồ 1 (nặng 2, giá trị 3) và món đồ 2 (nặng 1, giá trị 2). Tổng khối lượng là $2 + 1 = 3 \le 4$, tổng giá trị là $3 + 2 = 5$. Danh sách món đồ chọn là 1 và 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 500, 1 \le W \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
