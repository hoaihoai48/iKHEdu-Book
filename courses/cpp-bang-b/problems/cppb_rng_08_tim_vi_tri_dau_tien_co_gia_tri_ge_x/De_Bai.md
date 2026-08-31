# Tìm Vị Trí Đầu Tiên Có Giá Trị Lớn Hơn Hoặc Bằng X

## Bối cảnh
Hỗ trợ truy vấn `2 L R X` tìm chỉ số vị trí nhỏ nhất trong đoạn $[L, R]$ có giá trị $\ge X$ (tìm kiếm nhị phân trên Segment Tree $\mathcal{O}(\log N)$).

## Nhiệm vụ
In ra chỉ số vị trí tìm được hoặc -1 nếu không có.

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
1 3 2 4 5
2 1 5 3
1 2 1
2 1 5 3
```
### Output
```text
2
4
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val, X \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
