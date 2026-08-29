# Phủ Sóng Trạm Phát Sóng Wifi Đô Thị

## Bối cảnh
Dọc theo tuyến phố dài, có $N$ căn nhà tại tọa độ $X_1, X_2, \dots, X_N$ ($X_1 < X_2 < \dots < X_N$). Nhà mạng muốn lắp các bộ phát wifi, mỗi bộ có bán kính phủ sóng là $R$ (phủ được đoạn $[x - R, x + R]$, tức độ dài vùng phủ là $2R$). Hãy tìm số lượng bộ phát wifi ít nhất để phủ sóng toàn bộ $N$ căn nhà.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $R$ ($1 \le N \le 10^5, 0 \le R \le 10^9$).
- Dòng 2: $N$ số nguyên tăng dần $X_1, X_2, \dots, X_N$ ($0 \le X_i \le 10^{14}$).

## Output
- In ra số bộ phát wifi ít nhất.

## Sample 1
### Input
```text
6 2
1 2 3 7 8 11
```
### Output
```text
3
```
### Giải thích
- Bộ 1 đặt tại $3$: phủ $[1, 5]$ (nhà 1, 2, 3).
- Bộ 2 đặt tại $9$: phủ $[7, 11]$ (nhà 7, 8, 11 - hoặc đặt tại 8 phủ 7, 8 và đặt bộ khác...).

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
