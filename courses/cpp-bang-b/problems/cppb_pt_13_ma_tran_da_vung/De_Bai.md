# Truy Vấn Ma Trận Đa Vùng Cực Đại

## Bối cảnh
Trong phân tích viễn thám tài nguyên mặt đất, một bản đồ độ che phủ thực vật ma trận N x M cần được thống kê sản lượng cho các vùng dự án nông lâm kết hợp. Mỗi truy vấn cung cấp tọa độ của hai vùng hình chữ nhật rời nhau hoàn toàn, yêu cầu tính tổng sinh khối của cả hai vùng dự án này.

## Nhiệm vụ
Cho một ma trận N x M. Mỗi truy vấn cung cấp tọa độ của hai hình chữ nhật rời nhau, hãy tính tổng giá trị của tất cả các phần tử thuộc về cả hai hình chữ nhật đó.

## Input
- Dòng 1: 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($-10^9 \le A_{i, j} \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 8 số nguyên $r_{1a}, c_{1a}, r_{2a}, c_{2a}, r_{1b}, c_{1b}, r_{2b}, c_{2b}$.

## Output
- In ra $Q$ dòng, mỗi dòng là tổng giá trị của hai vùng tương ứng.

## Sample 1
### Input
```text
3 3 1
1 1 1
1 1 1
1 1 1
1 1 1 1 2 2 3 3
```
### Output
```text
5
```
### Giải thích
Hình chữ nhật 1 là ô (1, 1) có giá trị 1. Hình chữ nhật 2 là vùng từ (2, 2) đến (3, 3) gồm 4 ô giá trị 1 (tổng bằng 4). Tổng hai vùng là 1 + 4 = 5.

## Ràng buộc
- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
