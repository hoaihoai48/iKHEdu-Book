# Truy Vết Món Đồ Cái Túi 0/1

## Bối cảnh
Cần in ra chính xác các chỉ số của những món đồ được chọn để đạt giá trị lớn nhất trong bài toán cái túi 0/1.

## Nhiệm vụ
Dòng 1: Giá trị lớn nhất. Dòng 2: Số món đồ được chọn. Dòng 3: Danh sách chỉ số các món đồ theo thứ tự tăng dần.

## Input
- Dòng 1: $N, W$ ($1 \le N \le 500, 1 \le W \le 2000$).
- $N$ dòng tiếp theo: $W_i, V_i$ ($1 \le W_i \le W, 1 \le V_i \le 10^6$).

## Output
- Dòng 1: Max value.
- Dòng 2: Số lượng đồ.
- Dòng 3: Các chỉ số 1-based.

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

## Ràng buộc
- $100\%$ số test có $1 \le N \le 500, 1 \le W \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
