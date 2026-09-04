# Tìm Căn Bậc Hai Số Nguyên Lớn

## Bối cảnh
Trong một bài toán mật mã học khóa công khai, máy chủ cần tính toán phần nguyên của căn bậc hai của một số nguyên dương cực lớn N (lên đến 10^18). Kỹ sư cần tìm số nguyên dương X lớn nhất sao cho bình phương của X không vượt quá N.

## Nhiệm vụ
Cho số nguyên dương N (1 <= N <= 10^18). Hãy tìm số nguyên dương X lớn nhất thỏa mãn X^2 <= N bằng tìm kiếm nhị phân trên tập kết quả.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra số nguyên dương $X$ lớn nhất thỏa mãn.

## Sample 1
### Input
```text
17
```
### Output
```text
4
```
### Giải thích
4^2 = 16 <= 17, trong khi 5^2 = 25 > 17. Số nguyên lớn nhất có bình phương <= 17 là 4.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
