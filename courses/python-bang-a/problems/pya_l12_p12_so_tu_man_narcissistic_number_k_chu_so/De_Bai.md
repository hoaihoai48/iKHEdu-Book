# Số Tự Mãn (Narcissistic Number K Chữ Số)


*(Đề thi Tin học trẻ Quốc gia Bảng A)*

## Bối cảnh

Bé Kiến rất tự hào vì mỗi bạn kiến trong đàn đều góp sức làm nên tổ lớn. Bạn ấy nghe cô kể về những con số cũng "tự hào" như vậy. Một số tự nhiên $N$ có $K$ chữ số được gọi là "Số tự mãn" (Narcissistic number) nếu tổng lũy thừa bậc $K$ của các chữ số của nó đúng bằng chính số $N$.
  Ví dụ:
  * $N = 153$ có 3 chữ số: $1^3 + 5^3 + 3^3 = 153$ $\implies$ Thỏa mãn.
  * $N = 1634$ có 4 chữ số: $1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$ $\implies$ Thỏa mãn. Kiến đố em tìm thêm những con số đặc biệt này, em hãy giúp bạn ấy nhé!
## Nhiệm vụ

Cho số nguyên dương $N$ ($1 \le N \le 10^9$). Hãy kiểm tra xem $N$ có phải là số tự mãn không. In `YES` nếu đúng, ngược lại in `NO`.
## Input

Một số nguyên $N$.
## Output

`YES` hoặc `NO`.
## Sample 1

### Input
```text
1634
```
### Output
```text
YES
```
## Sample 2

### Input
```text
2024
```
### Output
```text
NO
```

## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
