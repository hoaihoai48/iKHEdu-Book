# Bài 01: Lệnh xuất nhập và biến số

## 1. Tóm tắt kiến thức trọng tâm
- **Lệnh in ra màn hình `print()`:**
  - In chữ / văn bản: Đặt trong nháy kép `"` hoặc nháy đơn `'` (Ví dụ: `print("Xin chao")`).
  - In số hoặc biểu thức tính: Không dùng nháy (Ví dụ: `print(2026)` hoặc `print(10 + 5)`).
  - In nhiều món đồ trên 1 dòng: Ngăn cách bởi dấu phẩy `,`. Python tự chèn 1 khoảng trắng ở giữa.
- **Biến số (Variable):**
  - Biến số là ô nhớ lưu dữ liệu: `ten_bien = gia_tri`. Dấu `=` là phép gán.
  - Quy tắc đặt tên biến: Chỉ dùng chữ cái tiếng Anh (`a-z`, `A-Z`), chữ số (`0-9`) và dấu gạch dưới `_`. Không bắt đầu bằng chữ số, không chứa dấu cách, không trùng từ khóa Python.
- **Lệnh nhập dữ liệu `input()` & Ép kiểu:**
  - `input()` luôn trả về kiểu chuỗi (`str`).
  - Khi cần tính toán số học, bắt buộc phải ép kiểu số nguyên `int(input())` hoặc số thực `float(input())`.

## 2. Bảng công thức & Quy tắc ghi nhớ
| Thao tác | Cú pháp Python | Kết quả / Ý nghĩa |
|---|---|---|
| In chuỗi và số | `print("Ket qua:", a + b)` | In chữ kèm kết quả tính toán |
| Nhập số nguyên | `n = int(input())` | Đọc 1 dòng từ bàn phím và ép sang số nguyên |
| Nhập số thực | `x = float(input())` | Đọc 1 dòng từ bàn phím và ép sang số thực |
| Hoán đổi 2 biến | `a, b = b, a` | Đổi chỗ 2 biến mà không cần biến phụ |

## 3. Bẫy lỗi phòng thi
- ❌ **Quên ép kiểu `int()`:** `a = input()`, `b = input()` rồi `print(a + b)` sẽ thành phép ghép chữ (Ví dụ: `"5" + "3" = "53"` thay vì số 8).
- ❌ **Đặt nháy kép quanh phép tính:** `print("5 + 3")` in ra chữ `5 + 3`, phải viết `print(5 + 3)` mới ra 8.
- ❌ **Tên biến sai quy tắc:** Viết `1diem = 10` hoặc `diem toan = 10` sẽ bị báo lỗi `SyntaxError`.

## 4. Mẫu code chuẩn
```python
# Mẫu nhập 2 số nguyên trên 2 dòng và in tổng
a = int(input())
b = int(input())
tong = a + b
print(tong)
```

## 5. Concept quiz: 12 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1 (nhận diện — cú pháp):
Lệnh nào sau đây dùng để hiển thị dòng chữ `Học Python thật vui` lên màn hình máy tính?
- **A.** `echo("Học Python thật vui")`
- **B.** **[Đáp án đúng]** `print("Học Python thật vui")`
- **C.** `input("Học Python thật vui")`
- **D.** `printf("Học Python thật vui");`
> *Giải thích:* Trong Python, lệnh `print()` có chức năng in dữ liệu ra màn hình. Lệnh `input()` dùng để nhập dữ liệu.

#### Câu 2 (dự đoán output — phép cộng chuỗi):
Đoạn code sau đây sẽ in ra màn hình kết quả gì?
```python
x = "20"
y = "26"
print(x + y)
```
- **A.** `46`
- **B.** **[Đáp án đúng]** `2026`
- **C.** Báo lỗi chương trình (Error)
- **D.** `x + y`
> *Giải thích:* Cả `x` và `y` đều nằm trong dấu nháy kép nên là kiểu chuỗi (`str`). Phép toán `+` giữa hai chuỗi sẽ nối dính chúng lại với nhau thành `"2026"`.

#### Câu 3 (bản chất biến số — gán đè giá trị):
Sau khi thực hiện 3 dòng lệnh sau, giá trị cuối cùng lưu trong biến `k` là bao nhiêu?
```python
k = 5
k = k + 3
k = 10
```
- **A.** `8`
- **B.** `18`
- **C.** **[Đáp án đúng]** `10`
- **D.** `15`
> *Giải thích:* Ban đầu $k = 5$, sau đó $k = 5 + 3 = 8$. Nhưng ở dòng lệnh cuối cùng, ta gán đè $k = 10$, do đó giá trị cũ bị xóa và biến $k$ giữ giá trị $10$.

#### Câu 4 (bắt bẫy quy tắc — đặt tên biến):
Tên biến nào sau đây là **HỢP LỆ** và chạy được trong Python mà không bị báo lỗi cú pháp?
- **A.** `2_ban_than`
- **B.** `diem toan`
- **C.** **[Đáp án đúng]** `chieu_dai_1`
- **D.** `so-luong`
> *Giải thích:* Tên biến không được bắt đầu bằng chữ số (loại A), không được có khoảng trắng (loại B), không được chứa dấu gạch ngang trừ `-` (loại D). Chỉ có C dùng dấu gạch dưới `_` là hoàn toàn hợp lệ.

#### Câu 5 (bắt bẫy kiểu dữ liệu — ép kiểu):
Để nhập một số nguyên $N$ từ bàn phím để tính toán, cách viết nào sau đây là **chuẩn nhất**?
- **A.** `N = input()`
- **B.** **[Đáp án đúng]** `N = int(input())`
- **C.** `N = str(input())`
- **D.** `N = print(input())`
> *Giải thích:* `input()` nhận vào chuỗi ký tự, cần bọc ngoài bằng `int()` để chuyển thành số nguyên.

#### Câu 6 (dự đoán output — dấu phẩy trong lệnh `print`):
Đoạn chương trình sau sẽ in ra màn hình nội dung gì?
```python
ten = "Minh"
tuoi = 9
print("Ban", ten, "nam nay", tuoi, "tuoi.")
```
- **A.** `BanMinhnamnay9tuoi.`
- **B.** **[Đáp án đúng]** `Ban Minh nam nay 9 tuoi.`
- **C.** `Ban, Minh, nam nay, 9, tuoi.`
- **D.** Báo lỗi `TypeError`
> *Giải thích:* Khi dùng dấu phẩy `,` giữa các đối số trong `print()`, Python tự động chèn một khoảng trắng giữa các phần tử.

#### Câu 7 (nhận diện kiểu dữ liệu):
Giá trị `3.14` trong Python thuộc kiểu dữ liệu nào?
- **A.** `int`
- **B.** `str`
- **C.** **[Đáp án đúng]** `float`
- **D.** `bool`
> *Giải thích:* Các số có phần thập phân phân tách bằng dấu chấm `.` được gọi là số thực, ký hiệu là `float`.

#### Câu 8 (bắt bẫy logic — dấu nháy):
Bạn An viết chương trình:
```python
print("5 * 4 = ", 5 * 4)
```
Màn hình sẽ hiển thị kết quả là:
- **A.** `20 = 20`
- **B.** `5 * 4 = 5 * 4`
- **C.** **[Đáp án đúng]** `5 * 4 =  20`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Phần `"5 * 4 = "` nằm trong nháy nên giữ nguyên, phần `5 * 4` không nằm trong nháy nên máy tính tính ra $20$.

#### Câu 9 (bắt bẫy thứ tự gán giá trị):
Quan sát đoạn mã sau:
```python
a = 15
b = a
a = 20
print(b)
```
Màn hình sẽ in ra giá trị của `b` là bao nhiêu?
- **A.** `20`
- **B.** **[Đáp án đúng]** `15`
- **C.** `35`
- **D.** `b`
> *Giải thích:* Khi chạy dòng `b = a`, giá trị $15$ của `a` được sao chép vào `b`. Sau đó đổi $a = 20$ thì giá trị trong chiếc hộp `b` vẫn là $15$, không bị ảnh hưởng.

#### Câu 10 (nhận diện thông báo lỗi — nameerror):
Khi chạy đoạn code sau:
```python
diem = 10
print(Diem)
```
Chương trình sẽ xảy ra hiện tượng gì?
- **A.** In ra số 10 bình thường.
- **B.** **[Đáp án đúng]** Báo lỗi `NameError: name 'Diem' is not defined`.
- **C.** In ra chữ `Diem`.
- **D.** In ra số 0.
> *Giải thích:* Python phân biệt chữ hoa và chữ thường (Case-sensitive). Biến `diem` (chữ thường) khác hoàn toàn với `Diem` (chữ hoa). Vì chưa tạo biến `Diem` nên máy báo lỗi không tìm thấy tên biến.

#### Câu 11 (chuyển đổi kiểu dữ liệu):
Kết quả của câu lệnh `print(type(100))` trong Python là gì?
- **A.** `<class 'str'>`
- **B.** `<class 'float'>`
- **C.** **[Đáp án đúng]** `<class 'int'>`
- **D.** `100`
> *Giải thích:* Hàm `type()` dùng để kiểm tra kiểu dữ liệu của một giá trị. Số $100$ là số nguyên nên thuộc lớp `int`.

#### Câu 12 (tư duy lập trình — ứng dụng):
Một bài toán yêu cầu: *"Nhập vào số lượng học sinh $N$, sau đó in ra số lượng kẹo cần mua biết mỗi bạn được chia 3 cái kẹo"*. Đoạn code nào sau đây giải đúng bài toán?
- **A.** `N = input(); print(N * 3)`
- **B.** **[Đáp án đúng]** `N = int(input()); print(N * 3)`
- **C.** `N = int(input()); print("N * 3")`
- **D.** `print(int(input) * 3)`
> *Giải thích:* Nếu không ép kiểu `int(input())`, khi nhập `4`, lệnh `N * 3` ở đáp án A sẽ in ra chuỗi `"444"`. Chỉ có đáp án B ép kiểu thành công $4 \times 3 = 12$.
