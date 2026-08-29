# Khoảng Trống Lớn Nhất Trên Trục Tọa Độ

## Bối cảnh
Cho $N$ chướng ngại vật tại các vị trí $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$). Hãy tìm khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp sau khi sắp xếp.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$).

## Output
- In ra khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp.

## Sample 1
### Input
```text
5
10 3 25 8 12
```
### Output
```text
13
```

## Ràng buộc
- $40\%$ số test có $N \le 1000, \vert A_i \vert \le 10^9$.
- $60\%$ số test có $N \le 10^5, \vert A_i \vert \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
