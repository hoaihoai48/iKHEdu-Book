# Vé vào công viên


## Bối cảnh

Tại trạm kiểm soát tự động của công viên nước, hệ thống cảm biến quang học đo chiều cao $h$ (cm) của khách hàng để phân loại vé hợp lệ.

## Nhiệm vụ

Nếu chiều cao $h \ge 130\text{ cm}$, in ra `VE NGUOI LON`. Nếu $h < 130\text{ cm}$, in ra `VE TRE EM`.

## Input

Một số nguyên $h$ ($1 \le h \le 200$).
## Output

`VE NGUOI LON` hoặc `VE TRE EM`.
## Sample 1

### Input
```text
135
```
### Output
```text
VE NGUOI LON
```
### Giải thích

Chiều cao đo được là $135\text{ cm}$. Do $135 \ge 130$, khách hàng cần áp dụng mức vé người lớn. Kết quả in ra: `VE NGUOI LON`.

## Sample 2

### Input
```text
120
```
### Output
```text
VE TRE EM
```
