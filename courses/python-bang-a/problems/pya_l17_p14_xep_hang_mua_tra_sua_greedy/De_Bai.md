# Xếp hàng mua trà sữa (Greedy)


*(Đề thi lập trình Quốc gia Bảng A)*

## Bối cảnh

Giờ tan học, có $N$ bạn học sinh cùng ríu rít xếp hàng mua trà sữa ở căng tin trường. Bạn thứ $i$ cần $T_i$ phút để người bán hàng pha chế xong cốc trà sữa của mình. Tổng thời gian chờ đợi của tất cả các bạn sẽ là tổng thời gian mà mỗi bạn phải đứng xếp hàng chờ cho đến khi nhận được trà sữa. Nhìn hàng dài mà các bạn ai cũng mỏi chân, hãy cô bán hàng tìm cách xếp hàng sao cho mọi người chờ ít nhất.
## Nhiệm vụ

Hãy tìm cách sắp xếp thứ tự các bạn vào mua trà sữa sao cho **tổng thời gian chờ đợi của tất cả các bạn là NHỎ NHẤT CÓ THỂ**. Hãy in ra tổng thời gian chờ đợi nhỏ nhất đó.
## Input

 * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên $T_i$ ($1 \le T_i \le 1000$).
## Output

Một số nguyên duy nhất là tổng thời gian chờ đợi nhỏ nhất.
## Sample 1

### Input
```text
3
3 1 2
```
### Output
```text
10
```
### Giải thích

Sắp xếp người làm nhanh lên trước: thời gian làm lần lượt là 1, 2, 3.
- Bạn 1 chờ 1 phút.
- Bạn 2 chờ $1 + 2 = 3$ phút.
- Bạn 3 chờ $1 + 2 + 3 = 6$ phút.
Tổng thời gian chờ: $1 + 3 + 6 = 10$ phút (tối ưu nhất).

## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
