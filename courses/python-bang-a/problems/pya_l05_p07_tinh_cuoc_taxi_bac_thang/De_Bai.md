# Tính Cước Taxi Bậc Thang


## Bối cảnh

Hãng taxi "Rùa Con" tính cước đi xe như sau:
  * Giá mở cửa (cho $1\text{ km}$ đầu tiên): $10$ nghìn đồng.
  * Từ kilomet thứ 2 đến kilomet thứ 10: giá $8$ nghìn đồng mỗi km.
  * Từ kilomet thứ 11 trở đi: giá $6$ nghìn đồng mỗi km.
## Nhiệm vụ

Nhập vào số kilomet $N$ mà khách đã đi (số nguyên $N \ge 1$). Tính tổng số tiền cước (nghìn đồng).
## Input

Một số tự nhiên $N$ ($1 \le N \le 100$).
## Output

Tổng tiền cước taxi.
## Sample 1

### Input
```text
1
```
### Output
```text
10
```
### Giải thích

Đúng 1 km đầu: 10 nghìn.
## Sample 2

### Input
```text
5
```
### Output
```text
42
```
### Giải thích

1 km đầu: 10k + 4 km tiếp theo: $4 \times 8 = 32$k $\implies 10 + 32 = 42$k.
## Sample 3

### Input
```text
12
```
### Output
```text
94
```
### Giải thích

1 km đầu (10k) + 9 km tiếp theo ($9 \times 8 = 72$k) + 2 km cuối ($2 \times 6 = 12$k) $\implies 10 + 72 + 12 = 94$k.
## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$