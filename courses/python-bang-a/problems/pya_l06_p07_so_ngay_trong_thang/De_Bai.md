# Số Ngày Trong Tháng


*(Lấy cảm hứng từ Bài 114, 115 Đề thi THT Bắc Giang)*

## Nhiệm vụ

Nhập vào tháng $M$ ($1 \le M \le 12$) và năm $Y$ ($1 \le Y \le 10^5$). Hãy in ra số lượng ngày của tháng đó trong năm $Y$.
* **Biết rằng:**
  * Tháng 1, 3, 5, 7, 8, 10, 12 có đúng 31 ngày.
  * Tháng 4, 6, 9, 11 có đúng 30 ngày.
  * Tháng 2: có 29 ngày nếu $Y$ là năm nhuận, có 28 ngày nếu $Y$ là năm thường.
## Input

Hai dòng lần lượt là $M$ và $Y$.
## Output

Một số nguyên duy nhất là số ngày của tháng.
## Sample 1

### Input
```text
2
2024
```
### Output
```text
29
```
## Sample 2

### Input
```text
2
2023
```
### Output
```text
28
```
## Sample 3

### Input
```text
4
2025
```
### Output
```text
30
```


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
