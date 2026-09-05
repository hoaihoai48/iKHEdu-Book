# Ba cạnh tam giác hợp lệ


## Bối cảnh

Thí sinh có ba que tính với các độ dài khác nhau. Bạn ấy muốn biết liệu ba que tính đó có thể ghép thành một hình tam giác hay không. Hãy giúp kiểm tra.

## Nhiệm vụ

Nhập vào 3 số tự nhiên $a, b, c$ trên 3 dòng. Kiểm tra xem 3 số này có thể tạo thành độ dài 3 cạnh của một tam giác hay không? Nếu có in `HOP LE`, ngược lại in `KHONG HOP LE`.
## Input

Ba số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^9$).
## Output

`HOP LE` hoặc `KHONG HOP LE`.
## Sample 1

### Input
```text
3
4
5
```
### Output
```text
HOP LE
```
### Giải thích

$3+4>5$, $3+5>4$, $4+5>3$ đều đúng.
## Sample 2

### Input
```text
2
3
6
```
### Output
```text
KHONG HOP LE
```
### Giải thích

$2 + 3 = 5 < 6$ (Sai bất đẳng thức tam giác).


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
