# Hệ Thống Quản Lý Dữ Liệu Olympic (Range Master)

## Bối cảnh
Bài toán tổng hợp nâng cao quản lý truy vấn cập nhật đoạn và tính tổng đoạn chuẩn Olympic.

## Nhiệm vụ
In ra kết quả của các truy vấn tính tổng.

## Input
- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

## Output
- Kết quả các truy vấn loại 2.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
1 2 4 2
2 1 5
2 2 4
```
### Output
```text
21
15
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
