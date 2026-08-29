# Chia Tập Hợp Thành 2 Phần Có Tổng Chênh Lệch Nhỏ Nhất

## Bối cảnh
Cho $N$ quả táo với khối lượng lần lượt là $P_1, P_2, \dots, P_N$. Bạn muốn chia $N$ quả táo này vào 2 giỏ sao cho độ chênh lệch khối lượng giữa 2 giỏ là **nhỏ nhất có thể**.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 20$).
- Dòng 2: $N$ số nguyên dương $P_1, P_2, \dots, P_N$ ($1 \le P_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là độ chênh lệch khối lượng nhỏ nhất tìm được.

## Sample 1
### Input
```text
5
3 2 7 4 1
```
### Output
```text
1
```
*(Giải thích: Giỏ 1: $[2, 7]$ (tổng 9), Giỏ 2: $[3, 4, 1]$ (tổng 8). Hiệu là $|9 - 8| = 1$).*

## Ràng buộc
- $100\%$ số test có $N \le 20, P_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
