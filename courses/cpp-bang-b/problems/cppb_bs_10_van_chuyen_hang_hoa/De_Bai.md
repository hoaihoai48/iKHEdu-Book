# Vận Chuyển Hàng Hóa Qua Phà Trong D Ngày

## Bối cảnh
Có $N$ kiện hàng được xếp thành một hàng dọc với trọng lượng lần lượt là $W_1, W_2, \dots, W_N$. Một chiếc phà cần vận chuyển toàn bộ $N$ kiện hàng này theo đúng thứ tự ban đầu qua sông trong không quá $D$ ngày. Mỗi ngày phà chỉ chở được một khối lượng hàng có tổng trọng lượng không vượt quá tải trọng $C$ của phà.

## Nhiệm vụ
Hãy tìm tải trọng $C$ nhỏ nhất của phà để hoàn thành công việc đúng hạn trong $D$ ngày.

## Input
- Dòng 1: Gồm 2 số nguyên $N, D$ ($1 \le D \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $W_1, W_2, \dots, W_N$ ($1 \le W_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tải trọng tối thiểu của phà.

## Sample 1
### Input
```text
6 3
3 2 2 4 1 4
```
### Output
```text
6
```
*(Giải thích: Ngày 1 chở kiện $[3, 2]$ (nặng 5), ngày 2 chở $[2, 4]$ (nặng 6), ngày 3 chở $[1, 4]$ (nặng 5)).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, W_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
