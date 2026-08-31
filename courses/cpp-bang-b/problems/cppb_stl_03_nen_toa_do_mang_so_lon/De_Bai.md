# Nén Tọa Độ Mảng Số Lớn

## Bối cảnh
Cho mảng $A$ gồm $N$ số nguyên lớn ($A_i \le 10^9$). Cần ánh xạ các giá trị về tập $\{0, 1, \dots, K-1\}$ ($K \le N$) giữ nguyên quan hệ thứ tự.

## Nhiệm vụ
In ra mảng sau khi nén tọa độ (0-based ranking).

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- Dãy số sau khi nén tọa độ.

## Sample 1
### Input
```text
5
100 20000 50 20000 100
```
### Output
```text
1 2 0 2 1
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
