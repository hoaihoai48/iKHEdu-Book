# Số Tăng Giảm Đẹp


*(Đề thi Tin học trẻ cấp Tỉnh/Thành phố)*

## Bối cảnh

Một số tự nhiên được gọi là:
  * **Số Tăng Dần:** Nếu mỗi chữ số đứng sau luôn lớn hơn chữ số đứng trước nó (ví dụ: $1379, 258$).
  * **Số Giảm Dần:** Nếu mỗi chữ số đứng sau luôn nhỏ hơn chữ số đứng trước nó (ví dụ: $9641, 852$).
## Nhiệm vụ

Cho số $N$. In ra `TANG` nếu $N$ là số tăng dần, in `GIAM` nếu $N$ là số giảm dần, và in `KHONG` nếu không thỏa mãn cả 2 tính chất trên.
## Input

Một số nguyên $N$ ($10 \le N \le 10^{12}$).
## Output

`TANG`, `GIAM` hoặc `KHONG`.
## Sample 1

### Input
```text
1379
```
### Output
```text
TANG
```
## Sample 2

### Input
```text
9520
```
### Output
```text
GIAM
```
## Sample 3

### Input
```text
1335
```
### Output
```text
`KHONG` (Có hai chữ số 3 bằng nhau)
```

## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
