# Vận Chuyển Hàng Hóa Qua Phà Trong D Ngày

## Bối cảnh
Tại một bến cảng trung chuyển đường thủy, có N kiện hàng được xếp thành một hàng dài trên băng chuyền theo thứ tự nghiêm ngặt với trọng lượng W1, W2, ..., Wn. Chiếc phà vận tải phải chở hết toàn bộ các kiện hàng này sang bờ bên kia trong thời gian đúng D ngày (mỗi ngày phà chỉ bốc xếp một chuỗi các kiện hàng liên tiếp nhau theo thứ tự băng tải). Hãy tính tải trọng tối thiểu của phà để hoàn thành nhiệm vụ trong đúng D ngày.

## Nhiệm vụ
Cho trọng lượng N kiện hàng và số ngày D. Tìm tải trọng nhỏ nhất của phà để chở hết hàng trong D ngày.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $D$ ($1 \le D \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương $W_1, W_2, \dots, W_N$ ($1 \le W_i \le 10^9$).

## Output
- In ra tải trọng tối thiểu của phà.

## Sample 1
### Input
```text
10 5
1 2 3 4 5 6 7 8 9 10
```
### Output
```text
15
```
### Giải thích
Với tải trọng 15:
- Ngày 1: chở [1, 2, 3, 4, 5] (tổng 15)
- Ngày 2: chở [6, 7] (tổng 13)
- Ngày 3: chở [8] (tổng 8)
- Ngày 4: chở [9] (tổng 9)
- Ngày 5: chở [10] (tổng 10)
Tổng cộng 5 ngày chở hết 10 kiện hàng. Tải trọng nhỏ nhất là 15.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, D \le N$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
