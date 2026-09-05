# Giao nhau của hai đoạn thẳng


## Bối cảnh

Trong giờ chơi xếp hình, hai bạn An và Bình mỗi bạn có một đoạn dây thun màu căng trên cây thước dài. Trên trục số thực, đoạn dây thứ nhất nối từ điểm $L_1$ đến $R_1$ ($L_1 \le R_1$), đoạn dây thứ hai nối từ điểm $L_2$ đến $R_2$ ($L_2 \le R_2$). Hai bạn thắc mắc không biết hai đoạn dây có chồng lên nhau ở chỗ nào không. Hãy giúp hai bạn kiểm tra xem hai đoạn dây có điểm chung không.
## Nhiệm vụ

Hãy kiểm tra xem hai đoạn thẳng này có điểm chung (giao nhau) hay không?
 * Nếu có giao nhau: in ra `GIAO NHAU` và độ dài của đoạn giao nhau đó.
 * Nếu không giao nhau: in `KHONG GIAO NHAU`.
## Input

Bốn số nguyên $L_1, R_1, L_2, R_2$ trên 4 dòng ($-10^9 \le L_1 \le R_1 \le 10^9, -10^9 \le L_2 \le R_2 \le 10^9$).
## Output

`GIAO NHAU [do_dai]` hoặc `KHONG GIAO NHAU`.
## Sample 1

### Input
```text
1
6
4
9
```
### Output
```text
GIAO NHAU 2
```
### Giải thích

Đoạn giao nhau từ 4 đến 6, độ dài: $6 - 4 = 2$.
## Sample 2

### Input
```text
1
3
5
8
```
### Output
```text
KHONG GIAO NHAU
```
### Giải thích

Hai đoạn rời nhau hoàn toàn.
## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
