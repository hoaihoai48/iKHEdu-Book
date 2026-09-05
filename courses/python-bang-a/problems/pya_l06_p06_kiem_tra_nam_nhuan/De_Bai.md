# Kiểm tra năm nhuận


## Bối cảnh

Lịch treo tường năm nay có 365 hay 366 ngày? Để biết được, em cần xác định năm đó có phải năm nhuận hay không. Hãy viết chương trình kiểm tra.

## Nhiệm vụ

Nhập vào một năm dương lịch $Y$. Hãy in ra `NAM NHUAN` nếu năm đó là năm nhuận, ngược lại in `NAM THUONG`.
* **Quy tắc:** Năm nhuận là năm chia hết cho 400, HOẶC chia hết cho 4 nhưng không chia hết cho 100.
## Input

Một số tự nhiên $Y$ ($1 \le Y \le 10^5$).
## Output

`NAM NHUAN` hoặc `NAM THUONG`.
## Sample 1

### Input
```text
2024
```
### Output
```text
NAM NHUAN
```
### Giải thích

Với dữ liệu đầu vào là `2024`, kết quả thu được tương ứng là `NAM NHUAN`.

## Sample 2

### Input
```text
1900
```
### Output
```text
NAM THUONG
```
## Sample 3

### Input
```text
2000
```
### Output
```text
NAM NHUAN
```
