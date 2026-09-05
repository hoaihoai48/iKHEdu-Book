# Tìm số lớn thứ nhì trong mảng


## Bối cảnh

Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.

## Nhiệm vụ

Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn thứ nhì trong dãy số (nghĩa là giá trị lớn nhất trong số các phần tử nhỏ hơn giá trị cực đại). Nếu tất cả các phần tử trong mảng đều bằng nhau, in ra `KHONG CO`.
## Input

 * Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
## Output

Giá trị lớn thứ nhì, hoặc `KHONG CO`.
## Sample 1

### Input
```text
5
10 20 20 15 5
```
### Output
```text
15
```
### Giải thích

Số lớn nhất là 20. Số lớn thứ hai nhỏ hơn 20 là 15.
## Sample 2

### Input
```text
3
5 5 5
```
### Output
```text
KHONG CO
```
### Giải thích

Tất cả bằng nhau.


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
