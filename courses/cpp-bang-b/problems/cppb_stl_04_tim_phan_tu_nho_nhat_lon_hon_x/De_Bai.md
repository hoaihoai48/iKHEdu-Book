# Tìm Phần Tử Nhỏ Nhất Lớn Hơn Hoặc Bằng X

## Bối cảnh
Cho tập hợp $N$ số nguyên và $Q$ truy vấn. Mỗi truy vấn cho số $X$, cần tìm phần tử nhỏ nhất trong tập hợp mà $\ge X$.

## Nhiệm vụ
Với mỗi truy vấn in ra phần tử tìm được hoặc -1 nếu không tồn tại.

## Input
- Dòng 1: Hai số $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên trong tập hợp ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 1 số $X$.

## Output
- Kết quả $Q$ truy vấn.

## Sample 1
### Input
```text
5 3
10 20 30 40 50
25
50
60
```
### Output
```text
30
50
-1
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, X \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
