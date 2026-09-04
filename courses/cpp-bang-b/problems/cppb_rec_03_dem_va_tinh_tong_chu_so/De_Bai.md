# Đếm & Tính Tổng Chữ Số Của N Bằng Đệ Quy

## Bối cảnh
Trong xử lý số học đệ quy, việc phân tách chữ số hàng đơn vị N % 10 và phần còn lại N / 10 cho phép duyệt qua toàn bộ các chữ số của N một cách thanh lịch mà không cần chuyển đổi sang chuỗi ký tự.

## Nhiệm vụ
Cho số nguyên dương N (1 <= N <= 10^18). Hãy viết hàm đệ quy để đếm số lượng chữ số và tính tổng các chữ số của N.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra 2 số nguyên cách nhau bởi khoảng trắng: số lượng chữ số và tổng các chữ số.

## Sample 1
### Input
```text
12345
```
### Output
```text
5 15
```
### Giải thích
Số 12345 có 5 chữ số, tổng các chữ số là 1 + 2 + 3 + 4 + 5 = 15. Kết quả in ra: 5 15.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
