# Đọc sách mỗi ngày


## Bối cảnh

Nghỉ hè, bạn Hoa mượn ở thư viện một cuốn truyện thật dày có tổng cộng $N$ trang để rèn thói quen đọc sách mỗi ngày. Ngày thứ nhất Hoa đọc được 1 trang thật ngon lành.
 * Ngày thứ hai Hoa đọc được 2 trang.
 * Ngày thứ ba Hoa đọc được 3 trang.
 * Cứ như vậy, ngày thứ $k$ Hoa đọc được $k$ trang.
Hoa háo hức muốn biết mình đọc hết truyện sau mấy ngày. Hãy đếm số ngày.
## Nhiệm vụ

Hỏi sau đúng bao nhiêu ngày thì Hoa sẽ đọc hết (hoặc vượt quá) $N$ trang của cuốn sách?
## Input

Một số tự nhiên $N$ ($1 \le N \le 10^4$).
## Output

Số ngày ít nhất để Hoa đọc xong cuốn sách.
## Sample 1

### Input
```text
10
```
### Output
```text
4
```
### Giải thích

Ngày 1: 1 trang; ngày 2: 2 trang (tổng 3); ngày 3: 3 trang (tổng 6); ngày 4: 4 trang (tổng 10 $\ge 10$). Sau 4 ngày đọc xong.
## Sample 2

### Input
```text
11
```
### Output
```text
5
```
### Giải thích

Sau 4 ngày mới đọc 10 trang, phải sang ngày thứ 5 mới đọc hết.


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
