# Chia Tập Hợp Thành 2 Phần Có Tổng Chênh Lệch Nhỏ Nhất

## Bối cảnh
Có N kiện hàng với khối lượng lần lượt là P1, P2, ..., Pn cần chia cho hai chiếc xe tải cùng loại để vận chuyển đường dài. Hãy tìm cách phân chia toàn bộ N kiện hàng thành hai phần sao cho độ chênh lệch khối lượng hàng hóa giữa hai xe tải là nhỏ nhất có thể.

## Nhiệm vụ
Cho N quả táo với khối lượng P1, P2, ..., Pn. Hãy chia táo vào 2 rổ sao cho độ chênh lệch tổng khối lượng giữa hai rổ là nhỏ nhất có thể.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 20$).
- Dòng 2: $N$ số nguyên dương $P_1, P_2, \dots, P_N$ ($1 \le P_i \le 10^9$).

## Output
- In ra độ chênh lệch nhỏ nhất giữa hai phần.

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
### Giải thích
Tổng khối lượng 5 quả táo là 3 + 2 + 7 + 4 + 1 = 17. Chia thành hai nhóm: nhóm 1 gồm {2, 7} có tổng 9; nhóm 2 gồm {3, 4, 1} có tổng 8. Độ chênh lệch giữa hai nhóm là |9 - 8| = 1. Đây là mức chênh lệch nhỏ nhất.

## Ràng buộc
- $100\%$ số test có $N \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
