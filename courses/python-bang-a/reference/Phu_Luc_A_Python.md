# Phụ lục A: Nền tảng Python
## 1. KHUNG TƯ DUY CỦA MỌI BÀI LẬP TRÌNH
### Mô hình Input – Process – Output
| Bước | Em tự hỏi | Ghi ra giấy |
|------|-----------|-------------|
| Đầu vào | Đề cho gì? | Tên từng số, từng dòng |
| Xử lý | Tính gì, theo bước nào? | Công thức từng bước |
| Đầu ra | In ra cái gì? | Đúng thứ tự cần in |
```python
n = int(input())
tong = n + 10
print(tong)
```
### Công thức trước code
| Bước | Việc làm |
|------|----------|
| 1 | Gạch chân các số đề cho |
| 2 | Viết cách tính bằng lời của em |
| 3 | Tính tay một ví dụ nhỏ rồi mới viết code |
### Chuỗi ghi nhớ nền tảng
> Đọc vào — tính toán — in ra — thử lại.
```python
a = int(input())
b = int(input())
print(a + b)
```
## 2. KHUNG CHƯƠNG TRÌNH PYTHON TỐI THIỂU
| Việc | Mẫu |
|------|-----|
| Đọc vào | `n = int(input())` |
| Tính toán | `ket_qua = n + 5` |
| In ra | `print(ket_qua)` |
Hai số trên một dòng, cách nhau bằng dấu cách:
```python
a, b = map(int, input().split())
print(a + b)
```
## 3. BIẾN VÀ KIỂU DỮ LIỆU
### Quy tắc đặt tên biến
| Quy tắc | Đúng | Chưa đúng |
|---------|------|-----------|
| Chữ, số, dấu gạch dưới | `diem_toan` | `điểm-toán` |
| Bắt đầu bằng chữ | `tong_1` | `1_tong` |
| Ngắn mà rõ nghĩa, không trùng từ của Python | `tuoi` | `print` |
```python
tuoi = 10
ten = "Na"
print(tuoi)
```
### Các kiểu int, float, str, bool, list
| Kiểu | Nghĩa | Ví dụ |
|------|-------|-------|
| `int` | Số nguyên | `5`, `-3` |
| `float` | Số có phần lẻ | `2.5` |
| `str` | Chuỗi chữ | `"xin chào"` |
| `bool` | Đúng hoặc sai | `True`, `False` |
| `list` | Nhiều giá trị | `[2, 4, 6]` |
```python
tuoi = 10
ten = "Na"
diem = [8, 9, 10]
print(ten)
```
### Khởi tạo biến tích lũy
| Muốn làm gì | Viết lúc đầu |
|-------------|--------------|
| Tính tổng | `tong = 0` |
| Đếm số lượng | `dem = 0` |
| Tìm số to nhất | `lon_nhat = 0` |
| Ghép chữ | `cau = ""` |
## 4. NHẬP VÀ XUẤT DỮ LIỆU
### Ba lưu ý thường gặp
| Lưu ý | Mẫu đúng |
|-------|----------|
| Chữ đọc vào luôn là chuỗi | `ten = input()` |
| Muốn tính phải đổi kiểu | `n = int(input())` |
| Một dòng nhiều số thì tách ra | `a, b = map(int, input().split())` |
```python
n = int(input())
print(n + 1)
```
Đọc số có phần lẻ, đọc hai số một dòng, in theo ý muốn:
```python
x = float(input())
a, b = map(int, input().split())
print(3, 4, 5, sep="-")
print("xin", end=" ")
print("chào")
```
In kèm lời giải thích:
```python
tuoi = 10
print(f"Năm nay em {tuoi} tuổi.")
```
## 5. TOÁN TỬ VÀ BIỂU THỨC
### Toán tử số học
| Viết | Nghĩa | Kết quả của `5` và `2` |
|------|-------|------------------------|
| `+ - * /` | Cộng trừ nhân chia | `7, 3, 10, 2.5` |
| `//` | Chia lấy phần nguyên | `5 // 2` cho `2` |
| `%` | Chia lấy phần dư | `5 % 2` cho `1` |
| `**` | Lũy thừa | `2 ** 3` cho `8` |
```python
print(3 + 2)
print(5 // 2)
print(2 ** 3)
```
### Chia nguyên và phần dư
| Muốn biết | Dùng |
|-----------|------|
| Mỗi bạn được mấy cái | `7 // 2` cho `3` |
| Còn thừa mấy cái | `7 % 2` cho `1` |
| Số có chẵn không | `n % 2 == 0` |
### Toán tử so sánh
| Viết | Nghĩa |
|------|-------|
| `==` / `!=` | Bằng nhau / khác nhau |
| `>` / `<` | Lớn hơn / nhỏ hơn |
| `>=` / `<=` | Lớn hơn hoặc bằng / nhỏ hơn hoặc bằng |
```python
print(5 > 3)
print(4 == 5)
```
### Toán tử logic
| Viết | Nghĩa | Ví dụ |
|------|-------|-------|
| `and` | Cả hai đều đúng | `a > 0 and b > 0` |
| `or` | Một cái đúng là đủ | `a > 0 or b > 0` |
| `not` | Đổi đúng thành sai | `not (a > 0)` |
```python
tuoi = 10
print(tuoi > 5 and tuoi < 15)
```
### Thứ tự ưu tiên
| Trước | Sau |
|-------|-----|
| Ngoặc `( )`, rồi `**` | Nhân chia `* / // %` |
| Cộng trừ `+ -` | So sánh, `not`, `and`, `or` |
```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```
## 6. ĐIỀU KIỆN — RẼ NHÁNH
### Mẫu if / if-else / if-elif-else
| Mẫu | Khi nào dùng |
|-----|--------------|
| `if` | Chỉ làm khi đúng |
| `if-else` | Chọn một trong hai |
| `if-elif-else` | Xếp nhiều mức |
```python
diem = int(input())
if diem >= 9:
    print("giỏi")
elif diem >= 7:
    print("khá")
else:
    print("cố gắng thêm")
```
### Quy tắc thụt lề
| Quy tắc | Nhớ |
|---------|-----|
| Sau dấu `:` thụt vào 4 dấu cách | Dòng trong nhánh lùi vào |
| Cùng nhánh thì thẳng hàng | Hết nhánh thì hết thụt lề |
```python
n = int(input())
if n > 0:
    print("số dương")
print("xong")
```
### Lỗi thường gặp
| Lỗi | Cách sửa |
|-----|----------|
| Quên dấu `:` sau `if` | Thêm `:` cuối dòng điều kiện |
| Viết `=` khi so sánh | So sánh viết `==` |
| Thụt lề lệch nhau | Căn thẳng hàng, mỗi lần 4 dấu cách |
```python
n = 5
if n == 5:
    print("đúng rồi")
```
## 7. VÒNG LẶP
### for và range
| Viết | Chạy qua |
|------|----------|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 6)` | `1, 2, 3, 4, 5` |
| `range(2, 10, 2)` | `2, 4, 6, 8` |
```python
tong = 0
for i in range(1, 101):
    tong = tong + i
print(tong)
```
### while
```python
n = 5
while n > 0:
    print(n)
    n = n - 1
```
### break và continue
| Lệnh | Nghĩa |
|------|-------|
| `break` | Dừng hẳn vòng lặp |
| `continue` | Bỏ lượt này, sang lượt sau |
```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```
### Vòng lặp lồng nhau
```python
for i in range(3):
    for j in range(5):
        print("*", end="")
    print()
```
## 8. BỐN MẪU TÍCH LŨY
| Mẫu | Bắt đầu | Trong vòng lặp |
|-----|---------|----------------|
| Tổng | `tong = 0` | `tong = tong + x` |
| Đếm | `dem = 0` | `dem = dem + 1` |
| To nhất | `lon_nhat = 0` | `if x > lon_nhat:` rồi gán |
| Nhỏ nhất | `nho_nhat = danh_sach[0]` | `if x < nho_nhat:` rồi gán |
### Tính tổng
```python
tong = 0
for i in range(1, 6):
    tong = tong + i
print(tong)
```
### Đếm phần tử
```python
dem = 0
for i in range(1, 11):
    if i % 2 == 0:
        dem = dem + 1
print(dem)
```
### Tìm giá trị lớn nhất
```python
lon_nhat = 0
for x in [3, 7, 2, 9, 4]:
    if x > lon_nhat:
        lon_nhat = x
print(lon_nhat)
```
### Tìm giá trị nhỏ nhất
```python
danh_sach = [3, 7, 2, 9, 4]
nho_nhat = danh_sach[0]
for x in danh_sach:
    if x < nho_nhat:
        nho_nhat = x
print(nho_nhat)
```
## 9. DANH SÁCH VÀ CHUỖI
### Danh sách và chỉ số
Vị trí đầu là `0`, vị trí cuối là `-1`.
```python
ban = ["An", "Bình", "Chi"]
print(ban[0])
print(ban[-1])
print(len(ban))
```
### Đọc và duyệt danh sách
```python
n = int(input())
danh_sach = []
for i in range(n):
    danh_sach.append(int(input()))
for i in range(len(danh_sach)):
    print(i, danh_sach[i])
```
### Các thao tác cơ bản
| Muốn làm gì | Mẫu |
|-------------|-----|
| Thêm vào cuối | `danh_sach.append(x)` |
| Cộng tổng / to nhất / nhỏ nhất | `sum(...)` / `max(...)` / `min(...)` |
| Sắp xếp / đếm số lượng | `sort()` / `len(...)` |
### Xử lý chuỗi
| Muốn làm gì | Mẫu |
|-------------|-----|
| Đếm số chữ / lấy chữ đầu | `len(ten)` / `ten[0]` |
| Tách câu thành từ | `cau.split()` |
| So sánh hai chuỗi | `if a == b:` |
```python
cau = input()
tu = cau.split()
print(len(tu))
print(tu)
```
## 10. GỠ LỖI VÀ KIỂM THỬ
### In giá trị trung gian
```python
n = int(input())
print(n)
tong = n * 2
print(tong)
```
| Muốn xem gì | In thêm dòng nào |
|-------------|------------------|
| Giá trị đọc vào | `print(n)` sau `input()` |
| Trong vòng lặp | `print(i, tong)` trong vòng lặp |
### Bộ test tối thiểu
| Nhóm | Ví dụ với bài chẵn lẻ |
|------|-----------------------|
| Nhỏ nhất | `1` |
| Hay gặp | `4`, `7` |
| Chỗ dễ đổi kết quả | `0`, số âm `-2` |
```python
n = int(input())
if n % 2 == 0:
    print("số chẵn")
else:
    print("số lẻ")
```
## TÓM TẮT MỘT TRANG
| Việc cần làm | Mẫu nhanh |
|--------------|-----------|
| Đọc một số nguyên / hai số một dòng | `n = int(input())` / `a, b = map(int, input().split())` |
| In kết quả / in kèm chữ | `print(kq)` / `print(f"Tổng là {tong}")` |
| Cộng trừ nhân chia / nguyên, dư | `+ - * /` / `// %` |
| So sánh / kết hợp | `== != > < >= <=` / `and or not` |
| Rẽ nhánh / lặp | `if / elif / else:` / `for i in range(n):` / `while ...:` |
| Dừng hẳn / bỏ lượt này | `break / continue` |
| Tổng / đếm / to nhất, nhỏ nhất | `tong + x` / `dem + 1` / `max(...) min(...)` |
| Danh sách / số lượng | `append(x)` / `len(...)` |
