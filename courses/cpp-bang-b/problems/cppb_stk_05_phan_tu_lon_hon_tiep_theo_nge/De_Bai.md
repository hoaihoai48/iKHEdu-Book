# Phần Tử Lớn Hơn Tiếp Theo (Next Greater Element)

## Bối cảnh
Cho mảng $A$ gồm $N$ số nguyên. Với mỗi vị trí $i$, cần tìm phần tử đầu tiên bên phải có giá trị lớn hơn $A[i]$.

## Nhiệm vụ
In ra $N$ số nguyên biểu diễn phần tử lớn hơn tiếp theo (hoặc -1 nếu không có).

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- $N$ số nguyên cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
4
4 5 2 25
```
### Output
```text
5 25 25 -1
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
