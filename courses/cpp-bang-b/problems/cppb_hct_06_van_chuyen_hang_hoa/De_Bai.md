# Vận Chuyển Thùng Hàng Cực Đại

## Bối cảnh
Một đội xe chuyên dụng cần chở $N$ kiện hàng $W_1, W_2, \dots, W_N$ ($W_i \le 10^{12}$) ra bến cảng. Mỗi xe chở tối đa **2 kiện hàng** và tổng khối lượng không vượt quá tải trọng $C$ ($C \le 10^{12}$). Hãy tính số chuyến xe tối thiểu.

## Input
- Dòng 1: 2 số nguyên dương $N$ và $C$ ($1 \le N \le 10^5, 1 \le C \le 10^{12}$).
- Dòng 2: $N$ số nguyên dương $W_1, W_2, \dots, W_N$ ($1 \le W_i \le C$).

## Output
- In ra số chuyến xe ít nhất.

## Sample 1
### Input
```text
5 10
3 5 8 2 7
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $N \le 10^5, C \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
