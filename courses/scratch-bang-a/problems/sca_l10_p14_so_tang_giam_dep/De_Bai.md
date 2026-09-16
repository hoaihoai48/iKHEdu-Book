# Số tăng giảm đẹp


*(Đề thi lập trình cấp Tỉnh/Thành phố)*

## Bối cảnh

Bạn Cún thích xếp những bậc thang bằng các chữ số. Có hôm bạn ấy xếp được cầu thang đi lên thật đẹp, có hôm lại xếp được cầu thang đi xuống thật gọn. Cô giáo gọi đó là:
 * **Số Tăng Dần:** Nếu mỗi chữ số đứng sau luôn lớn hơn chữ số đứng trước nó (ví dụ: $1379, 258$).
 * **Số Giảm Dần:** Nếu mỗi chữ số đứng sau luôn nhỏ hơn chữ số đứng trước nó (ví dụ: $9641, 852$). Cún nhờ em nhìn giúp xem mỗi con số là cầu thang lên, cầu thang xuống hay không phải cầu thang.
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
### Giải thích

Với dữ liệu đầu vào là `1379`, kết quả thu được tương ứng là `TANG`.

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
