# iKHEDU PYTHON BẢNG A — TỔNG HỢP NỘI DUNG 7 CHƯƠNG

> File tổng hợp tự động toàn bộ nội dung lesson của khóa Python Bảng A — Level 1.
> Nguồn canonical vẫn là các file trong `lessons/`; không chỉnh sửa trực tiếp file này.

## MỤC LỤC TỔNG QUAN

### Chương 1: TÍNH TOÁN CƠ BẢN
- Bài 01: lesson-01
- Bài 02: lesson-02
- Bài 03: lesson-03
### Chương 2: TƯ DUY RẼ NHÁNH & ĐIỀU KIỆN LOGIC
- Bài 04: lesson-04
### Chương 3: VÒNG LẶP
- Bài 05: lesson-05
- Bài 06: lesson-06
### Chương 4: BÀI TOÁN SỐ HỌC
- Bài 07: lesson-07
- Bài 08: lesson-08
- Bài 09: lesson-09
- Bài 10: lesson-10
### Chương 5: DANH SÁCH (LIST)
- Bài 11: lesson-11
- Bài 12: lesson-12
### Chương 6: XỬ LÝ CHUỖI & KÝ TỰ
- Bài 13: lesson-13
- Bài 14: lesson-14
### Chương 7: LUYỆN ĐỀ THI
- Bài 15: lesson-15
- Bài 16: lesson-16

================================================================================
# PHẦN I — CURRICULUM AUDIT VÀ ALGORITHM PATTERNS
================================================================================

# CURRICULUM AUDIT — PYTHON BẢNG A LEVEL 1

## Quyết định phạm vi

Khóa học giữ nguyên **6 chương / 18 bài**, tập trung vào Python 3 và tư duy giải bài cho Python Bảng A. Đây là khóa Python định hướng thuật toán, không phải khóa Python tổng quát.

Các nội dung như `def`, `return`, `dict`, `set`, tuple, module, file I/O, exception nâng cao và comprehension không phải chuẩn bắt buộc của Level 1. Có thể giới thiệu ở Level 2 hoặc phụ lục khi cần.

## Tiêu chí kiểm tra từng bài

| Tiêu chí | Câu hỏi kiểm tra |
|---|---|
| Prerequisite | Học sinh cần biết gì trước khi bắt đầu bài? |
| Bắt buộc Knowledge | Kiến thức nào bắt buộc đạt sau bài? |
| Algorithm Pattern | Học sinh có nhận ra mẫu giải có thể chuyển giao không? |
| Practice Coverage | Bài tập có đi từ cơ bản đến thử thách theo độ khó hợp lý không? |
| Exit Skill | Học sinh có thể tự làm được việc gì sau bài? |

## Ma trận audit

| Bài | Prerequisite | Bắt buộc Knowledge | Algorithm Pattern | Practice Coverage | Exit Skill |
|:---:|---|---|---|---|---|
| 01 | Không | `print`, `input`, biến, kiểu dữ liệu | Input → process → output | Cơ bản đến luyện tập | Viết chương trình nhập, tính và in kết quả |
| 02 | Bài 01 | Toán tử, `//`, `%`, `**` | Công thức trực tiếp, modulo | Cơ bản đến vận dụng | Chọn đúng phép toán cho bài toán |
| 03 | Bài 02 | Hình học, đổi đơn vị/thời gian, làm tròn | Tách đại lượng và ghép công thức | Cơ bản đến vận dụng | Mô hình hóa bài toán thực tế bằng công thức |
| 04 | Bài 01–03 | So sánh, Boolean, `if/elif/else`, `and/or/not` | Decision + Classification + Boolean expression | Cơ bản đến thử thách | Viết rẽ nhánh nhiều hướng và điều kiện ghép đúng |
| 05 | Bài 02 | `for`, `range` | Sum / accumulator | Cơ bản đến thử thách | Duyệt một khoảng và tích lũy kết quả |
| 06 | Bài 04–05 | `while`, `break`, `continue` | Sentinel / flag | Cơ bản đến vận dụng | Điều khiển vòng lặp chưa biết trước số lượt |
| 07 | Bài 05–06 | Dãy số, Fibonacci, nested loop | Rolling variables / pattern | Bắt buộc và thử thách | Sinh dãy và in mẫu bằng vòng lặp |
| 08 | Bài 02, 06 | Tách chữ số bằng `// 10`, `% 10` | Digit extraction | Bắt buộc và thử thách | Xử lý từng chữ số của số nguyên |
| 09 | Bài 02, 05 | Ước, bội, nguyên tố, GCD | Divisor scan | Bắt buộc và thử thách | Kiểm tra và đếm tính chất số học |
| 10 | Bài 08–09 | Số đặc biệt và đếm theo đoạn | Predicate + counting | Bắt buộc và thử thách | Đếm phần tử thỏa điều kiện |
| 11 | Bài 05, 13 | List, index, mutable, thao tác cơ bản | List traversal | Cơ bản đến vận dụng | Duyệt và cập nhật danh sách |
| 12 | Bài 11 | Thống kê, sắp xếp, trùng lặp | Statistics / ordering | Bắt buộc và thử thách | Tóm tắt và sắp xếp dữ liệu |
| 13 | Bài 01 | Index, slice, chuỗi là sequence | Sequence access | Cơ bản đến vận dụng | Lấy và cắt đúng phần chuỗi |
| 14 | Bài 13 | Duyệt, biến đổi ký tự, `split/join`, `ord/chr` | String traversal + Tokenize → transform → join | Cơ bản đến vận dụng | Duyệt và biến đổi chuỗi theo quy tắc |
| 15 | Bài 01–14 | Đọc đề, test biên, chiến lược thi | Pattern selection | Cơ bản đến vận dụng | Chọn mô hình giải và tự kiểm thử |
| 16 | Bài 01–15 | Đề contest giấu pattern, subtask, phân bổ thời gian | Pattern selection + vét điểm subtask | Đề thi thử (đang biên soạn) | Tự làm đề thi thử trong giới hạn thời gian |

## Mức độ bài tập

- **Cơ bản:** làm quen và áp dụng trực tiếp kiến thức mới.
- **Luyện tập:** biến đổi dữ liệu hoặc điều kiện trong bài quen thuộc.
- **Vận dụng:** chuyển kiến thức sang bối cảnh mới.
- **Thử thách:** bài mở rộng, không dùng làm điều kiện loại học sinh khỏi Level 1.

## Pattern card dùng xuyên suốt

Các pattern chuẩn được đặt trong [`ALGORITHM_PATTERNS.md`](ALGORITHM_PATTERNS.md) và được gọi lại trong lesson phù hợp: input/process/output, counting, sum, maximum, flag, digit extraction, nested loop, rolling variables, string traversal, list traversal và complexity check.

## Kết luận audit

Phạm vi kiến thức đủ để chốt Level 1. Giai đoạn tiếp theo là chuẩn hóa ví dụ, giảm claim không có nguồn, đánh dấu Core/Thử thách và kiểm tra từng bài theo ma trận trên; không mở rộng thêm chương.

# ALGORITHM PATTERNS — PYTHON BẢNG A LEVEL 1

Các mẫu dưới đây là thẻ nhớ dùng xuyên suốt khóa học. Học sinh cần nhận ra mẫu, hiểu điều kiện dùng và tự thay đổi phần điều kiện hoặc phép cập nhật.

## 1. Input → Process → Output

```python
du_lieu = int(input())
ket_qua = du_lieu + 5
print(ket_qua)
```

## 2. Counting

```python
dem = 0
for x in day:
    if dieu_kien(x):
        dem += 1
```

## 3. Sum / Accumulator

```python
tong = 0
for x in day:
    tong += x
```

## 4. Maximum hoặc minimum

```python
lon_nhat = day[0]
for x in day[1:]:
    if x > lon_nhat:
        lon_nhat = x
```

## 5. Flag / Search

```python
found = False
for x in day:
    if dieu_kien(x):
        found = True
        break
```

## 6. Digit extraction

```python
while n > 0:
    digit = n % 10
    n //= 10
```

## 7. Nested loop

```python
for i in range(so_hang):
    for j in range(so_cot):
        xu_ly(i, j)
```

Hai vòng lặp lồng nhau thường cần kiểm tra lại với giới hạn $N$ trước khi dùng.

## 8. Rolling variables

```python
a, b = b, a + b
```

Mẫu này phù hợp với Fibonacci và các dãy mà trạng thái mới phụ thuộc vào một vài trạng thái ngay trước đó.

## 9. String traversal

```python
for ch in s:
    xu_ly(ch)
```

Khi cần vị trí, dùng `for i in range(len(s))`.

## 10. List traversal

```python
for x in a:
    xu_ly(x)

for i in range(len(a)):
    a[i] = bien_doi(a[i])
```

Dùng cách thứ nhất khi chỉ cần giá trị; dùng cách thứ hai khi cần index hoặc thay đổi phần tử.

## 11. Nghĩ về tốc độ

| Dấu hiệu | Mẫu thường gặp | Cần nhớ |
|---|---|---|
| Không phụ thuộc $N$ | Công thức trực tiếp | $\mathcal{O}(1)$ |
| Duyệt một lần | Một vòng lặp qua $N$ phần tử | $\mathcal{O}(N)$ |
| Duyệt lồng nhau | Hai vòng lặp theo $N$ | $\mathcal{O}(N^2)$ |
| Mỗi bước giảm một phần | Tách chữ số hoặc chia đôi | Thường nhỏ hơn $\mathcal{O}(N)$ |

Trước khi chọn vòng lặp, luôn hỏi: $N$ lớn đến đâu và số lần lặp thực tế là bao nhiêu?


================================================================================
# PHẦN II — NỘI DUNG CHI TIẾT
================================================================================


================================================================================
# CHƯƠNG 01: TÍNH TOÁN CƠ BẢN
================================================================================


--------------------------------------------------------------------------------
<!-- Bài 01: lesson-01 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

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

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 01: Lệnh xuất nhập và biến số

---

## Bảng ma trận bài tập (10 bài tập phân tầng cơ bản → luyện tập)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L01-P01` | Lời chào robot | `Cơ bản` | Không có input | Lệnh `print()` in chuỗi ký tự cơ bản |
| 02 | `PYA-L01-P02` | Tấm danh thiếp thông minh | `Cơ bản` | Chuỗi $S$ không quá 50 ký tự | Lệnh `input()` chuỗi và in kèm thông điệp |
| 03 | `PYA-L01-P03` | Tuổi của bé sau 5 năm | `Cơ bản` | $1 \le N \le 12$ | Nhập số nguyên `int(input())`, phép cộng cơ bản |
| 04 | `PYA-L01-P04` | Cặp số nhân đôi | `Cơ bản` | $0 \le A \le 10^6$ | Phép nhân số nguyên và in kết quả |
| 05 | `PYA-L01-P05` | Đổi thước kẻ milimet | `Cơ bản` | $1 \le a, b \le 1000$ | Nhập 2 dòng số nguyên, chuyển đổi đơn vị đo |
| 06 | `PYA-L01-P06` | Cửa hàng bánh rán | `Luyện tập` | $1 \le a, b \le 100$ | Nhập đơn giá và số lượng, tính tổng số tiền |
| 07 | `PYA-L01-P07` | Chiếc hộp hoán đổi bí mật | `Luyện tập` | $0 \le A, B \le 10^9$ | Tư duy biến trung gian / hoán đổi giá trị 2 biến |
| 08 | `PYA-L01-P08` | Đoàn tàu toa xe ghép số | `Luyện tập` | $1 \le a, b \le 100$ | Phân biệt phép cộng số học và phép ghép chữ |
| 09 | `PYA-L01-P09` | Vé tham quan chùa hương | `Luyện tập` | $0 < a, b, x, y, n, m < 100$ | Bài toán thực tế nhiều biến, tổ chức luồng tính toán |
| 10 | `PYA-L01-P10` | Cỗ máy thời gian 3 thế hệ | `Luyện tập` | $1 \le a, b, c \le 100$ | Biến phụ thuộc, thiết lập quan hệ toán học giữa các biến |

---

### Bài 1 (Cơ bản): Lời chào robot (`PYA-L01-P01`)

* **Bối cảnh:** Bạn Robot vừa được khởi động trong phòng thí nghiệm iKHEDU. Em hãy giúp Robot phát ra lời chào mừng đến các bạn nhỏ.
* **Yêu cầu:** Viết chương trình in ra chính xác dòng chữ sau trên một dòng:
  ```text
  Xin chao cac ban! Toi la Robot Python.
  ```
* **Đầu vào (Input):** Không có dữ liệu vào.
* **Đầu ra (Output):** In ra một dòng chứa câu chào theo đúng mẫu.
* **Gợi ý thuật toán:** Sử dụng lệnh `print("...")`. Lưu ý gõ đúng từng chữ cái, dấu chấm và khoảng trắng.

---

### Bài 2 (Cơ bản): Tấm danh thiếp thông minh (`PYA-L01-P02`)

* **Bối cảnh:** Robot muốn làm quen với từng bạn nhỏ. Robot sẽ hỏi tên của bạn và in ra một câu chào thân thiện.
* **Yêu cầu:** Nhập vào tên của bạn nhỏ (một từ hoặc cụm từ), sau đó in ra câu chào theo mẫu: `Xin chao ban [Ten]!`
* **Đầu vào (Input):** Một dòng duy nhất chứa chuỗi ký tự tên của bạn nhỏ.
* **Đầu ra (Output):** In ra dòng thông điệp: `Xin chao ban <Ten>!` (giữa chữ `ban` và tên cách nhau một dấu cách, cuối câu có dấu chấm than `!`).
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Nam` | `Xin chao ban Nam!` |
  | `Bao Anh` | `Xin chao ban Bao Anh!` |
* **Gợi ý thuật toán:**
  ```python
  ten = input()
  print("Xin chao ban", ten + "!")
  ```

---

### Bài 3 (Cơ bản): Tuổi của bé sau 5 năm (`PYA-L01-P03`)

* **Bối cảnh:** Bé Bo năm nay tròn $N$ tuổi. Bé rất tò mò muốn biết sau 5 năm nữa thì bé sẽ bao nhiêu tuổi.
* **Yêu cầu:** Nhập vào số tuổi hiện tại $N$ của bé Bo. Hãy tính và in ra số tuổi của bé sau 5 năm nữa.
* **Đầu vào (Input):** Một dòng duy nhất chứa số tự nhiên $N$ ($1 \le N \le 12$).
* **Đầu ra (Output):** Một số nguyên duy nhất là số tuổi của bé Bo sau 5 năm.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `8` | `13` | Bé 8 tuổi, sau 5 năm nữa bé: $8 + 5 = 13$ tuổi |
* **Gợi ý thuật toán:** Bắt buộc phải ép kiểu số nguyên: `N = int(input())` rồi in `N + 5`.

---

### Bài 4 (Cơ bản): Cặp số nhân đôi (`PYA-L01-P04`)

* **Bối cảnh:** Trong trò chơi ảo thuật, nhà ảo thuật đặt một số nguyên $A$ vào chiếc hộp ma thuật. Khi mở hộp ra, số lượng viên ngọc sẽ được nhân lên gấp đôi.
* **Yêu cầu:** Nhập vào số nguyên $A$. Hãy in ra số lượng viên ngọc sau khi được nhân đôi.
* **Đầu vào (Input):** Gồm một số tự nhiên $A$ ($0 \le A \le 10^6$).
* **Đầu ra (Output):** In ra một số nguyên là kết quả nhân đôi ($A \times 2$).
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `15` | `30` |
  | `0` | `0` |
* **Gợi ý thuật toán:** `A = int(input()); print(A * 2)`.

---

### Bài 5 (Cơ bản): Đổi thước kẻ milimet (`PYA-L01-P05`)
*(Lấy cảm hứng từ Bài 2 Đề thi Lập trình Python TP Bắc Ninh)*

* **Bối cảnh:** Bạn An có một chiếc thước kẻ dài $a\text{ cm}$ và thêm một đoạn nhỏ dài $b\text{ mm}$. Em hãy giúp An đổi toàn bộ chiều dài chiếc thước đó ra đơn vị milimet ($\text{mm}$).
* **Biết rằng:** $1\text{ cm} = 10\text{ mm}$.
* **Đầu vào (Input):**
  * Dòng 1: Chứa số tự nhiên $a$ ($1 \le a \le 1000$).
  * Dòng 2: Chứa số tự nhiên $b$ ($1 \le b \le 1000$).
* **Đầu ra (Output):** Một số tự nhiên duy nhất là độ dài của thước tính theo đơn vị milimet ($\text{mm}$).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `2`<br>`5` | `25` | $2\text{ cm} = 20\text{ mm}$. Tổng cộng là: $20 + 5 = 25\text{ mm}$. |
* **Gợi ý thuật toán:** Đọc lần lượt 2 dòng:
  ```python
  a = int(input())
  b = int(input())
  ket_qua = a * 10 + b
  print(ket_qua)
  ```

---

### Bài 6 (Luyện tập): Cửa hàng bánh rán (`PYA-L01-P06`)

* **Bối cảnh:** Chú mèo máy Doraemon đi mua bánh rán. Mỗi chiếc bánh rán có giá $a$ nghìn đồng. Doraemon muốn mua đúng $b$ chiếc bánh rán.
* **Yêu cầu:** Hãy tính số tiền (nghìn đồng) mà Doraemon cần phải trả cho người bán hàng.
* **Đầu vào (Input):** Nhập vào 2 số tự nhiên $a$ và $b$ mỗi số trên một dòng ($1 \le a \le 100, 1 \le b \le 100$).
* **Đầu ra (Output):** In ra số tiền Doraemon cần trả.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12`<br>`5` | `60` | Mua 5 chiếc bánh, mỗi chiếc 12 nghìn đồng: $12 \times 5 = 60$. |

---

### Bài 7 (Luyện tập): Chiếc hộp hoán đổi bí mật (`PYA-L01-P07`)

* **Bối cảnh:** Bạn Tèo có hai chiếc hộp: hộp $A$ đựng số kẹo của Tèo, hộp $B$ đựng số kẹo của Tí. Bây giờ hai bạn muốn đổi kẹo cho nhau (số kẹo trong hộp $A$ chuyển sang hộp $B$, và số kẹo trong hộp $B$ chuyển sang hộp $A$).
* **Yêu cầu:** Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của 2 biến và in ra giá trị mới của $A$ và $B$ sau khi hoán đổi (cách nhau một dấu cách).
* **Đầu vào (Input):** Dòng 1 chứa số $A$, dòng 2 chứa số $B$ ($0 \le A, B \le 10^9$).
* **Đầu ra (Output):** In ra hai số $A$ và $B$ sau khi hoán đổi trên cùng một dòng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `7`<br>`12` | `12 7` | Ban đầu $A=7, B=12$. Sau khi đổi: $A=12, B=7$. |
* **Gợi ý thuật toán:**
  * Cách 1 (Dùng biến trung gian): `tam = a; a = b; b = tam`
  * Cách 2 (Đặc quyền Python): `a, b = b, a`
  * Sau đó in: `print(a, b)`

---

### Bài 8 (Luyện tập): Đoàn tàu toa xe ghép số (`PYA-L01-P08`)

* **Bối cảnh:** Ga xe lửa có 2 toa xe mang 2 con số $a$ và $b$. Bác trưởng ga muốn nhìn thấy cả hai kết quả:
  1. Nếu ghép 2 toa tàu lại thành một dãy số (Ghép chữ).
  2. Nếu cộng giá trị của 2 toa tàu lại với nhau (Cộng số học).
* **Yêu cầu:** Nhập vào 2 số tự nhiên $a$ và $b$. Dòng 1 in ra kết quả khi ghép chuỗi chữ. Dòng 2 in ra kết quả khi cộng số.
* **Đầu vào (Input):** Nhập 2 số tự nhiên $a, b$ ($1 \le a, b \le 100$) trên 2 dòng.
* **Đầu ra (Output):**
  * Dòng 1: Chuỗi ghép dính $a$ và $b$.
  * Dòng 2: Tổng giá trị số học $a + b$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `25`<br>`30` | `2530`<br>`55` | Dòng 1 ghép chữ: `"25" + "30" = "2530"`.<br>Dòng 2 cộng số: $25 + 30 = 55$. |
* **Gợi ý thuật toán:**
  ```python
  s1 = input()
  s2 = input()
  print(s1 + s2)
  print(int(s1) + int(s2))
  ```

---

### Bài 9 (Luyện tập): Vé tham quan chùa hương (`PYA-L01-P09`)
*(Lấy cảm hứng từ Bài 4 Đề thi Lập trình Python Thị xã Thái Hòa - Nghệ An)*

* **Bối cảnh:** Một đoàn khách chuẩn bị đi tham quan Chùa Hương Tích. Để lên chùa, đoàn phải đi thuyền và đi cáp treo:
  * Vé thuyền: người lớn $a$ nghìn đồng/người, trẻ em $b$ nghìn đồng/người.
  * Vé cáp treo: người lớn $x$ nghìn đồng/người, trẻ em $y$ nghìn đồng/người.
  * Đoàn khách có tổng cộng $n$ người, trong đó có $m$ trẻ em.
* **Yêu cầu:** Em hãy tính tổng số tiền (đơn vị nghìn đồng) cần chuẩn bị để mua toàn bộ vé thuyền và vé cáp treo cho cả đoàn khách.
* **Đầu vào (Input):** Gồm 6 dòng lần lượt chứa các số tự nhiên: $a, b, x, y, n, m$ ($0 < a, b, x, y < 100$; $0 \le m \le n < 100$).
* **Đầu ra (Output):** In ra một số nguyên duy nhất là tổng số tiền cần chuẩn bị.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `20`<br>`10`<br>`50`<br>`30`<br>`10`<br>`4` | `580` | - Số trẻ em: $4$, số người lớn: $10 - 4 = 6$ người.<br>- Tiền thuyền: $6 \times 20 + 4 \times 10 = 120 + 40 = 160$.<br>- Tiền cáp treo: $6 \times 50 + 4 \times 30 = 300 + 120 = 420$.<br>- Tổng tiền: $160 + 420 = 580$ nghìn đồng. |
* **Gợi ý thuật toán:**
  * Số người lớn: `nguoi_lon = n - m`
  * Tiền người lớn: `nguoi_lon * (a + x)`
  * Tiền trẻ em: `m * (b + y)`
  * Tổng tiền là tổng 2 khoản trên.

---

### Bài 10 (Luyện tập): Cỗ máy thời gian 3 thế hệ (`PYA-L01-P10`)

* **Bối cảnh:** Trong gia đình bạn Nam có 3 thế hệ: Nam, Bố của Nam và Ông nội của Nam.
  * Nam năm nay $a$ tuổi.
  * Bố hơn Nam $b$ tuổi.
  * Ông nội hơn Bố $c$ tuổi.
* **Yêu cầu:** Nhập vào 3 số tự nhiên $a, b, c$ lần lượt trên 3 dòng. Hãy tính và in ra:
  * Dòng 1: Tuổi của Bố.
  * Dòng 2: Tuổi của Ông nội.
  * Dòng 3: Tổng số tuổi của cả ba người.
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số nguyên $a, b, c$ ($1 \le a \le 20, 20 \le b \le 40, 20 \le c \le 40$).
* **Đầu ra (Output):** Gồm 3 dòng tương ứng với 3 yêu cầu của bài toán.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`30`<br>`25` | `40`<br>`65`<br>`115` | - Tuổi Nam: $10$.<br>- Tuổi Bố: $10 + 30 = 40$.<br>- Tuổi Ông: $40 + 25 = 65$.<br>- Tổng cả 3 người: $10 + 40 + 65 = 115$. |
* **Gợi ý thuật toán:** Sử dụng các biến liên kết:
  ```python
  nam = int(input())
  b = int(input())
  c = int(input())
  bo = nam + b
  ong = bo + c
  tong = nam + bo + ong
  print(bo)
  print(ong)
  print(tong)
  ```


--------------------------------------------------------------------------------
<!-- Bài 02: lesson-02 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 02: Phép toán số học, chia nguyên và chia dư

## 1. Kiến thức chuyên sâu dành cho học sinh Phổ thông
Python cung cấp 7 phép toán số học. Trong đó, bộ đôi **Chia lấy phần nguyên (`//`)** và **Chia lấy phần dư (`%`)** là nền tảng cốt lõi của mọi bài thi Lập trình Python:

```
Phép chia: A : B  (Ví dụ: 17 chia cho 5)
17 = 5 x 3 + 2
       │     │
       │     └─► 17 % 5  = 2 (Số dư - Modulo)
       └───────► 17 // 5 = 3 (Thương nguyên - Floor Division)
```

### A. Phép chia thực (`/`)
- Ký hiệu một dấu gạch chéo `/`.
- **Đặc điểm sống còn:** Kết quả luôn luôn là số thực (`float`), kể cả khi chia hết. Ví dụ: `8 / 2` cho ra `4.0` chứ không phải `4`. Nếu đề bài yêu cầu in ra số nguyên, dùng `/` sẽ bị trừ điểm!

### B. Phép chia lấy phần nguyên (`//`)
- Ký hiệu hai dấu gạch chéo liền nhau `//`.
- **Ý nghĩa:** Trả lời câu hỏi *"Có thể chia được trọn vẹn bao nhiêu phần bằng nhau?"*.
- Bỏ hoàn toàn phần thập phân, chỉ giữ lại số nguyên: `19 // 4 = 4` (vì $19 : 4 = 4.75$, lấy phần nguyên là $4$).

### C. Phép chia lấy phần dư (`%`)
- Ký hiệu dấu phần trăm `%`.
- **Ý nghĩa:** Trả lời câu hỏi *"Sau khi chia đều hết mức có thể, còn thừa ra bao nhiêu?"*.
- `19 % 4 = 3` (vì $4 	\times 4 = 16$, còn dư $19 - 16 = 3$).

### D. Định lý chia có dư Toán Phổ thông trong Python
$$\mathbf{A} = (\mathbf{A} // \mathbf{B}) 	\times \mathbf{B} + (\mathbf{A} \% \mathbf{B})$$

### E. Thứ tự ưu tiên tính toán (Quy tắc PEMDAS)
$$	\text{Ngoặc } () \longrightarrow 	\text{Lũy thừa } ** \longrightarrow 	\text{Nhân, Chia } (*, /, //, \%) \longrightarrow 	\text{Cộng, Trừ } (+, -)$$
*Lưu ý:* Các phép toán cùng cấp độ được thực hiện lần lượt từ **Trái sang Phải**.

## 2. Sổ tay 6 kỹ thuật ứng dụng thực chiến của `//` và `%`

### Kỹ thuật 1: Kiểm tra tính chẵn lẻ
- Số chẵn là số chia hết cho 2 (dư 0): `n % 2 == 0`.
- Số lẻ là số chia cho 2 dư 1: `n % 2 == 1` (hoặc `n % 2 != 0`).

### Kỹ thuật 2: Kiểm tra tính chia hết
- Số $A$ là bội số của $B$ (hay $A$ chia hết cho $B$): `A % B == 0`.

### Kỹ thuật 3: Bóc tách chữ số hàng đơn vị và hàng chục
- Lấy chữ số hàng đơn vị (chữ số cuối cùng): `don_vi = n % 10`.
- Gọt bỏ chữ số hàng đơn vị: `tam = n // 10`.
- Lấy chữ số hàng chục của số $N$: `chuc = (n // 10) % 10`.

### Kỹ thuật 4: Kỹ thuật làm tròn lên (Ceiling Division)
- *Bài toán:* Có $N$ học sinh, cần thuê xe chở học sinh, mỗi xe chở được $K$ bạn. Cần ít nhất bao nhiêu xe để không bạn nào bị bỏ lại?
- Nếu dùng `N // K`, với $N = 25, K = 10$ sẽ ra $2$ (thiếu 1 xe chở 5 bạn còn lại!).
- **Công thức làm tròn lên chuẩn thi đấu:**
  $$\mathbf{so\_xe = (N + K - 1) // K}$$
  *Kiểm tra:* $(25 + 10 - 1) // 10 = 34 // 10 = 3$ xe (Tuyệt đối chính xác!).

### Kỹ thuật 5: Bài toán chu kỳ vòng tròn (Đồng hồ, Vòng chạy)
- Một vòng có $M$ trạng thái (từ 0 đến $M-1$). Di chuyển thêm $K$ bước:
  $$\mathbf{vi\_tri\_moi = (vi\_tri\_cu + K) \% M}$$
- Đồng hồ 12 giờ: Sau $K$ giờ nữa kim chỉ số mấy?
  `gio_moi = (gio_hien_tai + K) % 12`. Nếu `gio_moi == 0` thì kết quả là `12`.
  *Hoặc mẹo 1 dòng:* `(gio_hien_tai + K - 1) % 12 + 1`.

### Kỹ thuật 6: Đổi số thứ tự $K$ sang tọa độ (Hàng, Cột) trên bàn cờ
- Một bảng ô vuông có chiều rộng mỗi hàng là $W$ ô. Ô thứ $K$ ($K$ tính từ 1):
  - `idx = K - 1` (Chuyển về mốc 0)
  - `hang = (idx // W) + 1`
  - `cot = (idx % W) + 1`

## 3. Bảng bẫy lỗi phòng thi thường gặp
| Code sai | Báo lỗi / Hiện tượng | Nguyên nhân | Cách sửa đúng |
|---|---|---|---|
| `a / b` | In ra `3.0` thay vì `3` | Dùng chia thực `/` | Dùng chia nguyên `a // b` |
| `a % 0` hoặc `a // 0` | `ZeroDivisionError` | Mẫu số chia bằng 0 | Đảm bảo mẫu số $> 0$ |
| `a ^ b` | Kết quả sai hoàn toàn | `^` là phép XOR bit, không phải mũ | Viết `a ** b` |
| `a x b` | `SyntaxError` | Dùng chữ `x` làm dấu nhân | Viết `a * b` |

## 4. Concept quiz: 18 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1 (nhận diện phép toán):
Trong Python, ký hiệu nào sau đây dùng để thực hiện phép chia lấy phần nguyên?
- **A.** `/`
- **B.** **[Đáp án đúng]** `//`
- **C.** `%`
- **D.** `\`
> *Giải thích:* Ký hiệu `//` là phép chia lấy phần nguyên. Ký hiệu `/` là chia thực, còn `%` là chia lấy phần dư.

#### Câu 2 (dự đoán output — chia nguyên):
Kết quả của biểu thức `19 // 4` trong Python là bao nhiêu?
- **A.** `4.75`
- **B.** **[Đáp án đúng]** `4`
- **C.** `3`
- **D.** `5`
> *Giải thích:* $19 : 4 = 4$ dư $3$. Phép `//` chỉ lấy phần nguyên là $4$.

#### Câu 3 (dự đoán output — chia dư):
Kết quả của biểu thức `19 % 4` trong Python là bao nhiêu?
- **A.** `4`
- **B.** **[Đáp án đúng]** `3`
- **C.** `0.75`
- **D.** `1`
> *Giải thích:* $19 : 4 = 4$ dư $3$. Phép `%` lấy số dư là $3$.

#### Câu 4 (bắt bẫy kiểu dữ liệu của phép chia `/`):
Kết quả của phép tính `8 / 2` trong Python là gì?
- **A.** Số nguyên `4`
- **B.** **[Đáp án đúng]** Số thực `4.0`
- **C.** Chuỗi `"4"`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Trong Python 3, phép chia đơn `/` luôn luôn trả về kiểu số thực (`float`), dù phép chia đó có chia hết hay không.

#### Câu 5 (ứng dụng — lũy thừa):
Để tính $3^4$ ($3$ mũ $4 = 3 \times 3 \times 3 \times 3 = 81$), câu lệnh Python nào sau đây viết đúng?
- **A.** `3 ^ 4`
- **B.** **[Đáp án đúng]** `3 ** 4`
- **C.** `3 * 4`
- **D.** `pow = 3 * 4`
> *Giải thích:* Toán tử lũy thừa trong Python là hai dấu sao liền nhau `**`. Ký hiệu `^` trong Python là phép toán XOR trên bit, không phải phép tính lũy thừa!

#### Câu 6 (bắt bẫy thứ tự ưu tiên):
Giá trị của biểu thức `10 - 2 * 3 + 4` là:
- **A.** `28`
- **B.** **[Đáp án đúng]** `8`
- **C.** `0`
- **D.** `16`
> *Giải thích:* Nhân trước: $2 \times 3 = 6$. Sau đó tính từ trái sang phải: $10 - 6 + 4 = 4 + 4 = 8$.

#### Câu 7 (kiểm tra số chẵn lẻ):
Điều kiện nào sau đây dùng để kiểm tra số nguyên $N$ có phải là số chẵn hay không?
- **A.** `N // 2 == 0`
- **B.** **[Đáp án đúng]** `N % 2 == 0`
- **C.** `N / 2 == 0`
- **D.** `N % 2 == 1`
> *Giải thích:* Số chẵn là số chia hết cho 2, nghĩa là số dư khi chia cho 2 phải bằng 0 (`N % 2 == 0`).

#### Câu 8 (tách chữ số cuối cùng):
Làm thế nào để lấy ra chữ số hàng đơn vị của một số nguyên dương $A = 987$?
- **A.** `A // 10`
- **B.** `A / 10`
- **C.** **[Đáp án đúng]** `A % 10`
- **D.** `A % 100`
> *Giải thích:* $987 \% 10 = 7$, đây chính là chữ số hàng đơn vị. Còn $987 // 10 = 98$ là phần số đứng trước.

#### Câu 9 (nhận diện lỗi crash — zerodivisionerror):
Câu lệnh nào sau đây sẽ khiến chương trình bị dừng ngay lập tức do lỗi `ZeroDivisionError`?
- **A.** `print(0 / 5)`
- **B.** `print(0 // 5)`
- **C.** **[Đáp án đúng]** `print(5 % 0)`
- **D.** `print(5 ** 0)`
> *Giải thích:* Không có phép chia cho số 0 trong toán học và lập trình. Biểu thức `5 % 0` chia cho 0 nên gây lỗi nghiêm trọng. Còn `0 / 5 = 0.0` và `5 ** 0 = 1` hoàn toàn hợp lệ.

#### Câu 10 (ứng dụng — chia kẹo):
Cô giáo có $M$ cái kẹo chia đều cho $K$ học sinh. Số kẹo còn thừa lại không đủ chia đều cho các bạn được tính bằng công thức nào?
- **A.** `M // K`
- **B.** **[Đáp án đúng]** `M % K`
- **C.** `M / K`
- **D.** `M - K`
> *Giải thích:* Số kẹo dư thừa sau khi chia đều chính là phần dư của phép chia: `M % K`.

#### Câu 11 (bắt bẫy biểu thức trung bình cộng):
Để tính trung bình cộng của 3 số nguyên $a, b, c$, cách viết nào sau đây là **CHÍNH XÁC**?
- **A.** `tbc = a + b + c / 3`
- **B.** **[Đáp án đúng]** `tbc = (a + b + c) / 3`
- **C.** `tbc = (a + b + c) // 3`
- **D.** `tbc = a + (b + c) / 3`
> *Giải thích:* Phải dùng ngoặc `(a + b + c)` để tính tổng 3 số trước rồi mới chia cho 3. Phép `/` cho giá trị trung bình chính xác (kể cả khi ra số thập phân).

#### Câu 12 (dự đoán output — chia số âm):
Trong Python, kết quả của biểu thức `-7 // 2` là bao nhiêu?
- **A.** `-3`
- **B.** **[Đáp án đúng]** `-4`
- **C.** `-3.5`
- **D.** `3`
> *Giải thích:* Phép chia nguyên `//` trong Python làm tròn xuống số nguyên nhỏ hơn gần nhất (Floor division). Vì $-3.5$ nằm giữa $-4$ và $-3$, số nguyên nhỏ hơn là $-4$.

#### Câu 13 (đảo ngược số chục):
Cho số có 2 chữ số $N = 83$. Biểu thức nào sau đây cho kết quả là số đảo ngược $38$?
- **A.** `(N % 10) + (N // 10)`
- **B.** **[Đáp án đúng]** `(N % 10) * 10 + (N // 10)`
- **C.** `(N // 10) * 10 + (N % 10)`
- **D.** `N % 10 * N // 10`
> *Giải thích:* Chữ số hàng đơn vị là $N \% 10 = 3$. Chữ số hàng chục là $N // 10 = 8$. Để tạo thành số $38$, ta lấy hàng đơn vị nhân 10 cộng hàng chục: $3 \times 10 + 8 = 38$.

#### Câu 14 (chu kỳ thời gian):
Một trận bóng đá bắt đầu lúc $H$ giờ và kéo dài đúng 15 giờ liên tục. Giờ kết thúc theo đồng hồ 24 giờ được tính theo công thức:
- **A.** `H + 15`
- **B.** **[Đáp án đúng]** `(H + 15) % 24`
- **C.** `(H + 15) // 24`
- **D.** `24 - (H + 15)`
> *Giải thích:* Một ngày có 24 giờ, khi thời gian vượt qua 24 giờ thì đồng hồ quay lại từ 0, do đó ta lấy phần dư cho 24: `(H + 15) % 24`.

#### Câu 15 (số lớn không giới hạn trong Python):
Điều gì xảy ra khi bạn tính `2 ** 100` trong Python?
- **A.** Bị lỗi tràn số (Overflow Error) giống C++ 32-bit.
- **B.** **[Đáp án đúng]** Python tính toán chính xác ra một con số khổng lồ gồm hơn 30 chữ số.
- **C.** Máy tính bị đơ và treo máy.
- **D.** Trả về kết quả `Infinity`.
> *Giải thích:* Đây là đặc sản của Python! Python tự động hỗ trợ tính toán số nguyên lớn vô hạn (Arbitrary-precision arithmetic), không bao giờ lo bị tràn số như kiểu `int` trong các ngôn ngữ khác.

#### Câu 16 (thứ tự ưu tiên PEMDAS):
Giá trị của biểu thức `2 + 3 * 4 ** 2` trong Python là bao nhiêu?
- **A.** `80`
- **B.** `56`
- **C.** **[Đáp án đúng]** `50`
- **D.** `36`
> *Giải thích:* Thứ tự PEMDAS: lũy thừa trước $4 ** 2 = 16$, rồi nhân $3 * 16 = 48$, cuối cùng cộng $2 + 48 = 50$. Muốn cộng trước phải thêm ngoặc: $(2 + 3) * 16 = 80$.

#### Câu 17 (phân biệt `//` và `/`):
Kết quả của hai biểu thức `7 / 2` và `7 // 2` trong Python lần lượt là:
- **A.** `3` và `3`
- **B.** `3.5` và `3.5`
- **C.** **[Đáp án đúng]** `3.5` và `3`
- **D.** `3` và `3.5`
> *Giải thích:* Phép `/` luôn trả về số thực $7 / 2 = 3.5$, còn phép `//` chỉ giữ phần nguyên $7 // 2 = 3$.

#### Câu 18 (lũy thừa `**`):
Kết quả của biểu thức `2 ** 3 ** 2` trong Python là bao nhiêu?
- **A.** `64`
- **B.** `36`
- **C.** **[Đáp án đúng]** `512`
- **D.** `12`
> *Giải thích:* Toán tử `**` có tính kết hợp từ phải sang trái nên $2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = 512$. Đây là bẫy kinh điển khi viết lũy thừa chồng!

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 02: Phép toán số học, chia nguyên và chia dư

---

## Bảng ma trận bài tập (16 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L02-P01` | Chia đều bánh quy | `Cơ bản` | $1 \le a, b \le 1000$ | Thành thạo phép chia nguyên `//` và chia dư `%` |
| 02 | `PYA-L02-P02` | Nhân đôi lũy thừa | `Cơ bản` | $1 \le n \le 30$ | Lũy thừa `**` cơ số 2 |
| 03 | `PYA-L02-P03` | Số kẹo còn thừa | `Cơ bản` | $1 \le N, K \le 10^9$ | Phép modulo `%`, xử lý số nguyên lớn |
| 04 | `PYA-L02-P04` | Đổi giờ ra phút giây | `Cơ bản` | $0 \le H, M, S \le 59$ | Biểu thức nhân cộng liên hoàn |
| 05 | `PYA-L02-P05` | Bóng đèn viền biển hiệu | `Luyện tập` | $1 \le a \le 10^7$ | Phép nhân chia đổi đơn vị (PYA đà nẵng) |
| 06 | `PYA-L02-P06` | Trồng cây đại lộ | `Luyện tập` | $1 \le N, K \le 10^6$ | Phép chia khoảng cách cộng 1 ở đầu mút |
| 07 | `PYA-L02-P07` | Vòng chạy điền kinh | `Luyện tập` | $1 \le N \le 10^9$ | Chu kỳ vòng lặp sân thể thao qua modulo |
| 08 | `PYA-L02-P08` | Kim đồng hồ 12 giờ | `Luyện tập` | $1 \le H \le 12, 1 \le K \le 10^9$ | Phép chia dư xử lý chu kỳ đồng hồ |
| 09 | `PYA-L02-P09` | Tách chữ số tận cùng | `Luyện tập` | $10 \le N \le 10^9$ | Tách hàng đơn vị `% 10` và hàng chục |
| 10 | `PYA-L02-P10` | Đảo ngược số 2 chữ số | `Luyện tập` | $10 \le N \le 99$ | Hoán vị vị trí chữ số bằng `//` và `%` |
| 11 | `PYA-L02-P11` | Xe buýt chở học sinh | `Luyện tập` | $1 \le N, K \le 10^6$ | Kỹ thuật làm tròn lên: `(N + K - 1) // K` |
| 12 | `PYA-L02-P12` | Bàn cờ ca-rô vô tận | `Vận dụng` | $1 \le K, W \le 10^6$ | Xác định tọa độ hàng cột $(row, col)$ từ số thứ tự |
| 13 | `PYA-L02-P13` | Lũy thừa cầu thang | `Luyện tập` | $1 \le a \le 10, 0 \le n \le 10$ | Lũy thừa tổng quát `a ** n` |
| 14 | `PYA-L02-P14` | Đổi phút ra giờ phút | `Luyện tập` | $0 \le T \le 10000$ | Đổi đơn vị thời gian bằng `// 60` và `% 60` |
| 15 | `PYA-L02-P15` | Giá trị biểu thức PEMDAS | `Vận dụng` | $1 \le a, b, c \le 100$ | Thứ tự ưu tiên mũ nhân cộng `a + b * c ** 2` |
| 16 | `PYA-L02-P16` | Đu quay vòng tròn | `Vận dụng` | $1 \le N, C \le 10^9$ | Chu kỳ vòng tròn tổng quát `N // C`, `N % C` |

---

### Bài 1 (Cơ bản): Chia đều bánh quy (`PYA-L02-P01`)

* **Bối cảnh:** Mẹ làm được $a$ chiếc bánh quy và muốn chia đều vào $b$ chiếc đĩa.
* **Yêu cầu:** Em hãy tính xem mỗi chiếc đĩa có bao nhiêu chiếc bánh, và còn dư lại bao nhiêu chiếc bánh không đủ chia đều.
* **Đầu vào (Input):** Nhập vào 2 số nguyên dương $a$ và $b$ trên 2 dòng ($1 \le a, b \le 1000$).
* **Đầu ra (Output):** In ra 2 số trên một dòng cách nhau một dấu cách: số bánh trên mỗi đĩa và số bánh còn dư.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `17`<br>`5` | `3 2` | $17 : 5 = 3$ dư $2$. Mỗi đĩa 3 cái, còn dư 2 cái bánh. |
* **Gợi ý thuật toán:** `print(a // b, a % b)`.

---

### Bài 2 (Cơ bản): Nhân đôi lũy thừa (`PYA-L02-P02`)

* **Bối cảnh:** Trong một thí nghiệm vi sinh vật, ban đầu có 1 tế bào. Cứ sau mỗi giờ, số lượng tế bào lại nhân đôi một lần ($2^1, 2^2, 2^3, \dots$).
* **Yêu cầu:** Hỏi sau $n$ giờ thì có tất cả bao nhiêu tế bào?
* **Đầu vào (Input):** Một số tự nhiên $n$ ($1 \le n \le 30$).
* **Đầu ra (Output):** In ra số lượng tế bào sau $n$ giờ ($2^n$).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4` | `16` | Sau 4 giờ: $2^4 = 16$ tế bào. |
* **Gợi ý thuật toán:** `n = int(input()); print(2 ** n)`.

---

### Bài 3 (Cơ bản): Số kẹo còn thừa (`PYA-L02-P03`)
*(Lấy cảm hứng từ Bài 9 Đề thi PYA Toàn quốc)*

* **Bối cảnh:** Nhà máy sản xuất bánh kẹo vừa đóng gói được $N$ viên kẹo. Người ta đóng các viên kẹo này vào các hộp quà, mỗi hộp quà chứa đúng $K$ viên kẹo. Những viên kẹo còn thừa lại không đủ đóng thành một hộp quà sẽ được tặng cho các em nhỏ đi tham quan nhà máy.
* **Yêu cầu:** Hãy tính số kẹo được tặng cho các em nhỏ.
* **Đầu vào (Input):** Gồm 2 dòng lần lượt chứa hai số tự nhiên $N$ và $K$ ($1 \le N, K \le 10^9$).
* **Đầu ra (Output):** In ra số viên kẹo còn thừa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `100`<br>`8` | `4` |
* **Gợi ý thuật toán:** `print(N % K)`. Nhờ Python hỗ trợ số lớn, $N = 10^9$ vẫn chạy tức thì trong 0.001 giây!

---

### Bài 4 (Cơ bản): Đổi giờ ra phút giây (`PYA-L02-P04`)

* **Bối cảnh:** Đồng hồ điện tử hiển thị thời gian gồm $H$ giờ, $M$ phút và $S$ giây.
* **Yêu cầu:** Em hãy tính xem tổng cộng khoảng thời gian đó tương đương với bao nhiêu giây?
* **Biết rằng:** $1\text{ giờ} = 60\text{ phút} = 3600\text{ giây}$, $1\text{ phút} = 60\text{ giây}$.
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số tự nhiên $H, M, S$ ($0 \le H \le 23, 0 \le M, S \le 59$).
* **Đầu ra (Output):** Một số nguyên duy nhất là tổng số giây.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1`<br>`20`<br>`15` | `4815` | $1 \times 3600 + 20 \times 60 + 15 = 3600 + 1200 + 15 = 4815$ giây. |

---

### Bài 5 (Luyện tập): Bóng đèn viền biển hiệu (`PYA-L02-P05`)
*(Lấy cảm hứng từ Bài 1 PYA Sơn Trà - Đà Nẵng)*

* **Bối cảnh:** Người ta muốn mắc các bóng đèn màu trang trí xung quanh viền của một bảng quảng cáo hình vuông. Bảng quảng cáo có chiều dài cạnh là $a\text{ dm}$. Các bóng đèn được mắc liên tiếp nhau và cách nhau đúng $5\text{ cm}$ dọc theo chu vi hình vuông (bao gồm cả các góc).
* **Yêu cầu:** Em hãy tính số lượng bóng đèn cần mắc.
* **Biết rằng:** $1\text{ dm} = 10\text{ cm}$.
* **Đầu vào (Input):** Một số nguyên dương $a$ ($1 \le a \le 10^7$).
* **Đầu ra (Output):** Một số nguyên duy nhất là số bóng đèn cần mắc.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1` | `8` | Cạnh $1\text{ dm} = 10\text{ cm}$. Chu vi bảng hình vuông là $10 \times 4 = 40\text{ cm}$.<br>Khoảng cách giữa các đèn là $5\text{ cm}$. Số đèn mắc là: $40 : 5 = 8$ bóng đèn. |
* **Gợi ý thuật toán:**
  * Đổi cạnh sang cm: `canh_cm = a * 10`
  * Chu vi viền: `chu_vi = canh_cm * 4`
  * Số bóng đèn: `chu_vi // 5`

---

### Bài 6 (Luyện tập): Trồng cây đại lộ (`PYA-L02-P06`)
*(Lấy cảm hứng từ Bài 7 Đề thi PYA Toàn quốc)*

* **Bối cảnh:** Trên một đại lộ thẳng tắp có chiều dài $N$ mét, người ta cần trồng các cây xanh thẳng hàng ở một bên đường để tạo bóng mát. Bắt đầu trồng một cây ngay tại điểm xuất phát (mét thứ 0), và cứ sau mỗi khoảng cách đúng $K$ mét lại trồng tiếp một cây.
* **Yêu cầu:** Hãy tính tổng số lượng cây xanh được trồng trên đoạn đường từ mét thứ 0 đến mét thứ $N$.
* **Đầu vào (Input):** Gồm 2 số tự nhiên $N$ và $K$ ($1 \le N, K \le 10^6$) mỗi số trên một dòng.
* **Đầu ra (Output):** Một số nguyên duy nhất là số cây trồng được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`3` | `4` | Các cây được trồng tại các vị trí mét thứ: 0, 3, 6, 9. Tổng cộng có 4 cây. |
* **Gợi ý thuật toán:**
  * Số khoảng cách $K$ mét trọn vẹn là: `N // K`.
  * Do có thêm 1 cây ở điểm mút đầu tiên (vị trí 0), nên số cây trồng được là: `(N // K) + 1`.

---

### Bài 7 (Luyện tập): Vòng chạy điền kinh (`PYA-L02-P07`)
*(Lấy cảm hứng từ Bài 8 Đề thi PYA Bắc Giang)*

* **Bối cảnh:** Một đường chạy thể thao hình chữ nhật có chu vi đúng $100\text{ mét}$. Vận động viên An xuất phát từ vạch số 0 và chạy liên tục theo một chiều dọc theo mép sân được tổng quãng đường là $N\text{ mét}$.
* **Yêu cầu:** Em hãy cho biết:
  1. An đã chạy được bao nhiêu vòng sân trọn vẹn?
  2. Hiện tại An đang dừng lại ở vị trí cách vạch xuất phát bao nhiêu mét?
* **Đầu vào (Input):** Một số nguyên $N$ ($1 \le N \le 10^9$).
* **Đầu ra (Output):** Hai số nguyên trên một dòng cách nhau dấu cách lần lượt là số vòng chạy trọn vẹn và khoảng cách tính từ vạch xuất phát.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `250` | `2 50` | $250 = 2 \times 100 + 50$. Đã chạy 2 vòng trọn vẹn và đang ở mét thứ 50. |
* **Gợi ý thuật toán:** `print(N // 100, N % 100)`.

---

### Bài 8 (Luyện tập): Kim đồng hồ 12 giờ (`PYA-L02-P08`)

* **Bối cảnh:** Đồng hồ kim treo tường có 12 số đánh dấu từ 1 đến 12. Hiện tại kim giờ đang chỉ vào đúng số $H$.
* **Yêu cầu:** Sau đúng $K$ giờ nữa, hỏi kim giờ sẽ chỉ vào số mấy?
* **Đầu vào (Input):** Nhập vào 2 số nguyên $H$ ($1 \le H \le 12$) và $K$ ($1 \le K \le 10^9$).
* **Đầu ra (Output):** In ra một số nguyên từ 1 đến 12 là số mà kim giờ đang chỉ.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`5` | `3` | Lúc 10 giờ, sau 5 giờ nữa là 15 giờ. Trên đồng hồ 12 số tương ứng số 3. |
  | `9`<br>`3` | `12` | Lúc 9 giờ, sau 3 giờ nữa là 12 giờ. |
* **Gợi ý thuật toán:**
  * Lưu ý bẫy số 12: Khi tính chia dư, số 12 chia 12 dư 0.
  * Công thức chuẩn: `gio_moi = (H + K) % 12`. Nếu `gio_moi == 0` thì kết quả là `12`! Hoặc dùng mẹo: `(H + K - 1) % 12 + 1`.

---

### Bài 9 (Luyện tập): Tách chữ số tận cùng (`PYA-L02-P09`)

* **Bối cảnh:** Bé Na có một mã số may mắn là một số tự nhiên $N$. Na muốn tìm ra chữ số hàng đơn vị và chữ số hàng chục của số này.
* **Yêu cầu:** Nhập vào số tự nhiên $N$ ($10 \le N \le 10^9$). Hãy in ra:
  * Dòng 1: Chữ số hàng đơn vị của $N$.
  * Dòng 2: Chữ số hàng chục của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `857` | `7`<br>`5` | Chữ số hàng đơn vị là 7, hàng chục là 5. |
* **Gợi ý thuật toán:**
  * Chữ số hàng đơn vị: `don_vi = N % 10`
  * Chữ số hàng chục: Bỏ hàng đơn vị đi `tam = N // 10`, rồi lấy chữ số cuối của phần còn lại `chuc = tam % 10` (hoặc gộp lại `(N // 10) % 10`).

---

### Bài 10 (Luyện tập): Đảo ngược số 2 chữ số (`PYA-L02-P10`)

* **Bối cảnh:** Trong một mật thư thám tử, các con số 2 chữ số đã bị đảo ngược vị trí hai chữ số cho nhau (ví dụ số 27 bị biến thành 72).
* **Yêu cầu:** Nhập vào một số tự nhiên $N$ có đúng 2 chữ số ($10 \le N \le 99$). Hãy in ra số sau khi đảo ngược hai chữ số.
* **Đầu vào (Input):** Một số tự nhiên $N$.
* **Đầu ra (Output):** Số nguyên sau khi đảo ngược. (Lưu ý: Nếu số là 30 thì đảo lại là 3).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `49` | `94` | Hàng chục là 4, hàng đơn vị là 9 $\to$ Đảo lại thành 94. |
  | `50` | `5` | Hàng chục là 5, đơn vị là 0 $\to$ Đảo lại thành $0 \times 10 + 5 = 5$. |
* **Gợi ý thuật toán:**
  ```python
  N = int(input())
  chuc = N // 10
  don_vi = N % 10
  dao_nguoc = don_vi * 10 + chuc
  print(dao_nguoc)
  ```

---

### Bài 11 (Luyện tập): Xe buýt chở học sinh (`PYA-L02-P11`)

* **Bối cảnh:** Một trường phổ thông tổ chức dã ngoại cho $N$ học sinh. Nhà trường thuê các xe buýt loại $K$ chỗ ngồi. Mỗi xe buýt chở được tối đa $K$ bạn học sinh.
* **Yêu cầu:** Hỏi nhà trường cần thuê **ít nhất bao nhiêu xe buýt** để chở hết toàn bộ $N$ học sinh (không để bạn nào phải ở lại trường)?
* **Đầu vào (Input):** Nhập vào 2 số nguyên dương $N$ và $K$ ($1 \le N, K \le 10^6$).
* **Đầu ra (Output):** Một số nguyên duy nhất là số lượng xe buýt tối thiểu cần thuê.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `25`<br>`10` | `3` | 2 xe đầu chở được 20 bạn, còn 5 bạn nữa bắt buộc phải thuê thêm 1 xe thứ ba. |
  | `30`<br>`10` | `3` | 3 xe chở vừa khít 30 bạn. |
* **Gợi ý thuật toán (Kỹ thuật làm tròn lên kinh điển trong lập trình):**
  * Nếu dùng `N // K`: khi $N = 25, K = 10 \implies 25 // 10 = 2$ (bị thiếu 1 xe!).
  * Công thức làm tròn lên chuẩn mực thi đấu: `so_xe = (N + K - 1) // K`.
  * Thử lại: $(25 + 10 - 1) // 10 = 34 // 10 = 3$ (Đúng!).
  * Thử lại: $(30 + 10 - 1) // 10 = 39 // 10 = 3$ (Vẫn đúng!).

---

### Bài 12 (Vận dụng): Bàn cờ ca-rô vô tận (`PYA-L02-P12`)

* **Bối cảnh:** Một bàn cờ ô vuông vô tận được chia thành các hàng, mỗi hàng có đúng $W$ ô vuông. Các ô vuông được đánh số liên tiếp bắt đầu từ $1$:
  * Hàng 1 gồm các ô: $1, 2, \dots, W$.
  * Hàng 2 gồm các ô: $W+1, W+2, \dots, 2W$.
  * Cứ như vậy tiếp tục cho các hàng tiếp theo.
* **Yêu cầu:** Cho biết số thứ tự của một ô là $K$. Em hãy xác định xem ô đó nằm ở **Hàng thứ mấy** và **Cột thứ mấy** (Cột tính từ 1 đến $W$)?
* **Đầu vào (Input):** Gồm hai số tự nhiên $K$ và $W$ ($1 \le K, W \le 10^6$) mỗi số trên một dòng.
* **Đầu ra (Output):** In ra hai số nguyên trên một dòng cách nhau dấu cách: `hang cot`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `11`<br>`4` | `3 3` | Mỗi hàng có 4 ô.<br>Hàng 1: 1, 2, 3, 4<br>Hàng 2: 5, 6, 7, 8<br>Hàng 3: 9, 10, 11, 12.<br>Ô số 11 nằm ở Hàng 3, Cột 3. |
* **Gợi ý thuật toán:**
  * Chuyển về chỉ số bắt đầu từ 0: `idx = K - 1`
  * Hàng (tính từ 1): `hang = (idx // W) + 1`
  * Cột (tính từ 1): `cot = (idx % W) + 1`
  * In: `print(hang, cot)`.

---

### Bài 13 (Luyện tập): Lũy thừa cầu thang (`PYA-L02-P13`)

* **Bối cảnh:** Bạn Thỏ Nâu xếp các khối gỗ thành cầu thang toán học, mỗi tầng gấp $a$ lần tầng trước, cả cầu thang có $n$ tầng.
* **Yêu cầu:** Tính số khối gỗ ở tầng cao nhất, tức giá trị $a^n$.
* **Đầu vào (Input):** Hai dòng lần lượt là cơ số $a$ và số mũ $n$ ($1 \le a \le 10, 0 \le n \le 10$).
* **Đầu ra (Output):** Một số nguyên duy nhất là $a^n$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`4` | `81` | $3^4 = 3 \times 3 \times 3 \times 3 = 81$. |
* **Gợi ý thuật toán:** `print(a ** n)`. Nhớ `**` mới là lũy thừa, `^` là phép XOR bit!

---

### Bài 14 (Luyện tập): Đổi phút ra giờ phút (`PYA-L02-P14`)

* **Bối cảnh:** Bạn Mèo Cam bấm giờ chạy bộ được tổng cộng $T$ phút và muốn khoe thành tích theo dạng mấy giờ mấy phút.
* **Yêu cầu:** Đổi tổng số phút $T$ thành số giờ trọn vẹn và số phút lẻ.
* **Đầu vào (Input):** Một số nguyên $T$ ($0 \le T \le 10000$).
* **Đầu ra (Output):** Hai số nguyên trên một dòng cách nhau dấu cách: giờ và phút dư.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `135` | `2 15` | $135 = 2 \times 60 + 15$. Được 2 giờ và dư 15 phút. |
* **Gợi ý thuật toán:** `print(T // 60, T % 60)`.

---

### Bài 15 (Vận dụng): Giá trị biểu thức PEMDAS (`PYA-L02-P15`)

* **Bối cảnh:** Cô giáo viết biểu thức bí mật $a + b \times c^2$ lên bảng, bạn nào tính đúng thứ tự ưu tiên sẽ thắng cuộc thi tính nhẩm.
* **Yêu cầu:** Cho ba số $a, b, c$, hãy tính giá trị biểu thức $a + b \times c^2$ (lũy thừa trước, nhân trước, cộng sau).
* **Đầu vào (Input):** Ba dòng lần lượt là $a, b, c$ ($1 \le a, b, c \le 100$).
* **Đầu ra (Output):** Một số nguyên duy nhất là giá trị biểu thức.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `2`<br>`3`<br>`4` | `50` | $4^2 = 16$, $3 \times 16 = 48$, $2 + 48 = 50$. |
* **Gợi ý thuật toán:** `print(a + b * c ** 2)`. Không được thêm ngoặc sai thành `(a + b) * c ** 2`!

---

### Bài 16 (Vận dụng): Đu quay vòng tròn (`PYA-L02-P16`)

* **Bối cảnh:** Chiếc đu quay mỗi vòng mất đúng $C$ phút, bạn Sóc Nâu ngồi liên tục $N$ phút để ngắm thành phố.
* **Yêu cầu:** Tính số vòng quay trọn vẹn và số phút dở dang của vòng hiện tại.
* **Đầu vào (Input):** Hai dòng lần lượt là $N$ và $C$ ($1 \le N, C \le 10^9$).
* **Đầu ra (Output):** Hai số nguyên trên một dòng cách nhau dấu cách: số vòng trọn và số phút dư.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `250`<br>`60` | `4 10` | $250 = 4 \times 60 + 10$. Đi được 4 vòng và dư 10 phút. |
* **Gợi ý thuật toán:** `print(N // C, N % C)`. Kiểm tra lại bằng $N = \text{vòng} \times C + \text{dư}$.


--------------------------------------------------------------------------------
<!-- Bài 03: lesson-03 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 03: Công thức tính toán, hình học và đổi đơn vị

## 1. Kiến thức chuyên sâu dành cho học sinh Phổ thông

### A. Các công thức hình học nền tảng
* **Hình chữ nhật:**
  - Chu vi: $P = (a + b) 	\times 2 \implies$ Code: `(a + b) * 2` *(Bắt buộc phải có dấu ngoặc tròn)*.
  - Diện tích: $S = a 	\times b \implies$ Code: `a * b`.
  - Nửa chu vi: $P_{nua} = P // 2$.
  - Tìm một cạnh khi biết chu vi $P$ và một cạnh $a$: $b = (P // 2) - a$.
* **Hình vuông:**
  - Chu vi: $P = a 	\times 4 \implies$ Code: `a * 4`.
  - Cạnh hình vuông từ chu vi: $a = P // 4$.
  - Diện tích: $S = a 	\times a = a^2 \implies$ Code: `a * a` hoặc `a ** 2`.
* **Tam giác vuông:**
  - Diện tích khi biết 2 cạnh góc vuông $a$ và $b$: $S = \frac{a 	\times b}{2} \implies$ Code: `(a * b) // 2` (nếu tích chia hết cho 2).
* **Hình thang:**
  - Diện tích: $S = \frac{(a + b) 	\times h}{2} \implies$ Code: `((a + b) * h) // 2`.

### B. Bài toán diện tích hình học lồng ghép (Trừ phần giao / Phần còn lại)
* *Mô hình:* Có một khu đất lớn diện tích $S_1$, bên trong xây một công trình có diện tích $S_2$. Diện tích đất còn lại là:
  $$\mathbf{S_{con\_lai} = S_1 - S_2}$$
* *Bài toán bờ hồ & hòn đảo:* Hồ hình vuông cạnh $A$, đảo hình chữ nhật $B 	\times C$:
  `mat_nuoc = (A * A) - (B * C)`.

### C. Thuật toán phân rã đơn vị thời gian (Từ giây sang Giờ — Phút — Giây)
Biết rằng: $1	\text{ giờ} = 60	\text{ phút} = 3600	\text{ giây}$, $1	\text{ phút} = 60	\text{ giây}$.
Cho trước $S$ giây, quy trình phân rã gồm 3 bước:
1. **Tính số giờ:** `gio = S // 3600`
2. **Lấy số giây còn dư sau khi tính giờ:** `giay_du = S % 3600`
3. **Tính số phút và giây từ phần dư:**
   - `phut = giay_du // 60`
   - `giay = giay_du % 60`

### D. Kỹ thuật in số thập phân và làm tròn
- Làm tròn 2 chữ số thập phân: `round(x, 2)`.
- **In chuẩn định dạng thi đấu bằng f-string:** `print(f"{x:.2f}")` (Đảm bảo số `5` sẽ in ra đủ `5.00`).
- **In bù số 0 ở đầu (Ví dụ: in 5 giây thành `05`):** `print(f"{giay:02d}")`.

## 2. Bảng công thức quy đổi đơn vị đo lường cần thuộc lòng
| Tên đơn vị | Quy đổi xuôi | Lưu ý khi tính diện tích |
|---|---|---|
| Độ dài | $1	\text{ m} = 10	\text{ dm} = 100	\text{ cm} = 1000	\text{ mm}$ | $1	\text{ km} = 1000	\text{ m}$ |
| Diện tích | $1	\text{ m}^2 = 100	\text{ dm}^2 = 10,000	\text{ cm}^2$ | **Độ dài nhân 10 thì diện tích nhân 100!** |
| Khối lượng | $1	\text{ tấn} = 10	\text{ tạ} = 1000	\text{ kg}$; $1	\text{ kg} = 1000	\text{ g}$ | Luôn đổi về cùng đơn vị nhỏ nhất trước |

## 3. Bẫy lỗi phòng thi
- ❌ **Quên đổi về cùng đơn vị:** Dài $2	\text{ m}$, rộng $30	\text{ cm}$ mà tính diện tích $2 	\times 30 = 60$ là sai! Phải đổi $2	\text{ m} = 200	\text{ cm}$, diện tích là $200 	\times 30 = 6000	\text{ cm}^2$.
- ❌ **Thiếu ngoặc phép tính nửa chu vi:** Viết `P // 2 - a` thì đúng, nhưng viết `P - a // 2` là sai hoàn toàn!

## 4. Concept quiz: 18 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1 (công thức chu vi hình chữ nhật):
Cho chiều dài `a` và chiều rộng `b`. Biểu thức Python nào tính đúng chu vi hình chữ nhật?
- **A.** `P = a + b * 2`
- **B.** **[Đáp án đúng]** `P = (a + b) * 2`
- **C.** `P = a * b * 2`
- **D.** `P = (a * b) // 2`
> *Giải thích:* Chu vi bằng tổng chiều dài và chiều rộng rồi nhân đôi. Cần có dấu ngoặc `(a + b)` để thực hiện phép cộng trước phép nhân.

#### Câu 2 (tìm cạnh hình chữ nhật):
Một hình chữ nhật có chu vi là `P` và chiều rộng là `w`. Chiều dài của hình chữ nhật đó được tính bằng công thức:
- **A.** `P - w`
- **B.** `P // 2 + w`
- **C.** **[Đáp án đúng]** `P // 2 - w`
- **D.** `(P - w) // 2`
> *Giải thích:* Nửa chu vi là $P // 2$. Chiều dài bằng nửa chu vi trừ đi chiều rộng: `P // 2 - w`.

#### Câu 3 (đổi đơn vị thời gian):
Một giờ có bao nhiêu giây?
- **A.** 60 giây
- **B.** 360 giây
- **C.** **[Đáp án đúng]** 3600 giây
- **D.** 6000 giây
> *Giải thích:* $1\text{ giờ} = 60\text{ phút} = 60 \times 60 = 3600\text{ giây}$.

#### Câu 4 (dự đoán output — phân rã thời gian):
Đoạn code sau in ra kết quả gì?
```python
s = 125
phut = s // 60
giay = s % 60
print(phut, giay)
```
- **A.** `2 5`
- **B.** **[Đáp án đúng]** `2 5`
- **C.** `1 65`
- **D.** `12 5`
> *Giải thích:* $125 : 60 = 2$ dư $5$. Vậy in ra `2 5` (2 phút 5 giây).

#### Câu 5 (hình học lồng nhau):
Một bức tường hình vuông cạnh $a = 10\text{m}$. Người ta khoét một cửa sổ hình vuông cạnh $b = 2\text{m}$. Diện tích phần tường còn lại là:
- **A.** 16
- **B.** 80
- **C.** **[Đáp án đúng]** 96
- **D.** 100
> *Giải thích:* $S_{tuong} = 10 \times 10 = 100$. $S_{cua} = 2 \times 2 = 4$. Diện tích còn lại: $100 - 4 = 96\text{ m}^2$.

#### Câu 6 (bắt bẫy đơn vị đo lường):
Cạnh hình vuông $a = 2\text{ m}$. Diện tích hình vuông đó tính theo đơn vị $\text{cm}^2$ là:
- **A.** $4\text{ cm}^2$
- **B.** $400\text{ cm}^2$
- **C.** **[Đáp án đúng]** $40000\text{ cm}^2$
- **D.** $20000\text{ cm}^2$
> *Giải thích:* $2\text{ m} = 200\text{ cm}$. Diện tích là $200 \times 200 = 40000\text{ cm}^2$. Rất nhiều học sinh nhầm chỉ nhân thêm 100!

#### Câu 7 (làm tròn số thập phân):
Kết quả của lệnh `round(4.5678, 2)` là:
- **A.** `4.56`
- **B.** **[Đáp án đúng]** `4.57`
- **C.** `4.6`
- **D.** `5`
> *Giải thích:* Chữ số thứ ba sau dấu phẩy là 7 ($\ge 5$), do đó làm tròn lên thành `4.57`.

#### Câu 8 (tính vận tốc — thời gian gặp nhau):
Hai người đứng cách nhau khoảng cách $D$ (km). Người thứ nhất đi về phía người thứ hai với vận tốc $V$ (km/h). Thời gian (giờ) để hai người gặp nhau là:
- **A.** `D * V`
- **B.** `V / D`
- **C.** **[Đáp án đúng]** `D / V`
- **D.** `D - V`
> *Giải thích:* Thời gian = Quãng đường : Vận tốc $\implies D / V$.

#### Câu 9 (bắt bẫy phép chia diện tích tam giác):
Cho tam giác có đáy $a = 5$ và chiều cao $h = 3$. Lệnh `dien_tich = a * h / 2` sẽ cho kết quả thuộc kiểu dữ liệu nào?
- **A.** `int`
- **B.** **[Đáp án đúng]** `float` (kết quả `7.5`)
- **C.** `str`
- **D.** Báo lỗi
> *Giải thích:* Vì có dấu chia thực `/`, kết quả luôn là kiểu `float`, giá trị là `7.5`.

#### Câu 10 (chu vi hình vuông từ diện tích):
Một hình vuông có diện tích là $S = 64$. Chu vi hình vuông đó là bao nhiêu?
- **A.** 16
- **B.** **[Đáp án đúng]** 32
- **C.** 64
- **D.** 256
> *Giải thích:* Cạnh hình vuông là $\sqrt{64} = 8$. Chu vi là $8 \times 4 = 32$.

#### Câu 11 (ghép gạch lát sân):
Một sân hình chữ nhật kích thước $6\text{m} \times 4\text{m}$. Người ta dùng các viên gạch hình vuông cạnh $1\text{m}$ để lát kín sân. Cần bao nhiêu viên gạch?
- **A.** 10 viên
- **B.** 20 viên
- **C.** **[Đáp án đúng]** 24 viên
- **D.** 48 viên
> *Giải thích:* Diện tích sân: $6 \times 4 = 24\text{ m}^2$. Mỗi viên gạch diện tích $1 \times 1 = 1\text{ m}^2$. Số viên gạch là $24 : 1 = 24$ viên.

#### Câu 12 (format chuỗi thời gian đẹp):
Lệnh nào sau đây in ra số phút và số giây luôn có 2 chữ số (ví dụ: phút 5 in ra `05`, giây 9 in ra `09`)?
- **A.** `print(f"{phut}:{giay}")`
- **B.** **[Đáp án đúng]** `print(f"{phut:02d}:{giay:02d}")`
- **C.** `print(round(phut, 2), round(giay, 2))`
- **D.** `print("0" + phut + "0" + giay)`
> *Giải thích:* Cú pháp `:02d` trong `f-string` của Python tự động bù thêm số 0 ở đằng trước nếu số đó có ít hơn 2 chữ số.

#### Câu 13 (diện tích tam giác vuông):
Một miếng bánh hình tam giác vuông có hai cạnh góc vuông dài $6\text{ cm}$ và $4\text{ cm}$. Diện tích miếng bánh đó là:
- **A.** $10\text{ cm}^2$
- **B.** $20\text{ cm}^2$
- **C.** **[Đáp án đúng]** $12\text{ cm}^2$
- **D.** $24\text{ cm}^2$
> *Giải thích:* Diện tích tam giác vuông bằng tích hai cạnh góc vuông chia cho 2: $(6 \times 4) : 2 = 24 : 2 = 12\text{ cm}^2$.

#### Câu 14 (thể tích hộp chữ nhật):
Một hộp sữa có chiều dài $3\text{ cm}$, chiều rộng $2\text{ cm}$ và chiều cao $4\text{ cm}$. Thể tích của hộp sữa đó là:
- **A.** $9\text{ cm}^3$
- **B.** $14\text{ cm}^3$
- **C.** **[Đáp án đúng]** $24\text{ cm}^3$
- **D.** $29\text{ cm}^3$
> *Giải thích:* Thể tích hộp chữ nhật bằng dài nhân rộng nhân cao: $3 \times 2 \times 4 = 24\text{ cm}^3$.

#### Câu 15 (đổi đơn vị thời gian xuôi):
Bạn Bi chạy bộ trong $2$ giờ $15$ phút. Hỏi bạn Bi đã chạy tổng cộng bao nhiêu giây?
- **A.** $215$ giây
- **B.** $2250$ giây
- **C.** **[Đáp án đúng]** $8100$ giây
- **D.** $135$ giây
> *Giải thích:* $2$ giờ $= 2 \times 3600 = 7200$ giây. $15$ phút $= 15 \times 60 = 900$ giây. Tổng cộng: $7200 + 900 = 8100$ giây.

#### Câu 16 (dự đoán output — phân rã giờ phút giây):
Đoạn code sau in ra kết quả gì?
```python
s = 7325
gio = s // 3600
du = s % 3600
phut = du // 60
giay = du % 60
print(gio, phut, giay)
```
- **A.** `1 62 5`
- **B.** `7 3 25`
- **C.** **[Đáp án đúng]** `2 2 5`
- **D.** `2 3 5`
> *Giải thích:* $7325 : 3600 = 2$ dư $125$. Từ $125$ giây dư: $125 : 60 = 2$ phút dư $5$ giây. Vậy in ra `2 2 5` (2 giờ 2 phút 5 giây).

#### Câu 17 (làm tròn với `round()`):
Kết quả của lệnh `round(5.678, 2)` là:
- **A.** `5.67`
- **B.** **[Đáp án đúng]** `5.68`
- **C.** `5.6`
- **D.** `6`
> *Giải thích:* Chữ số thứ ba sau dấu phẩy là 8 ($\ge 5$) nên làm tròn lên: `5.678` thành `5.68`.

#### Câu 18 (làm tròn với `f-string`):
Cho `x = 7.456`. Lệnh nào in ra `7.5` (làm tròn đến 1 chữ số thập phân)?
- **A.** `print(round(x))`
- **B.** `print(f"{x:.2f}")`
- **C.** **[Đáp án đúng]** `print(f"{x:.1f}")`
- **D.** `print(x // 10)`
> *Giải thích:* Cú pháp `:.1f` trong `f-string` nghĩa là làm tròn và hiển thị đúng 1 chữ số sau dấu phẩy, nên `7.456` thành `7.5`.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 03: Công thức tính toán, hình học và đổi đơn vị

---

## Bảng ma trận bài tập (10 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L03-P01` | Mảnh vườn chữ nhật | `Cơ bản` | $1 \le a, b \le 10^4$ | Tính chu vi và diện tích hình chữ nhật |
| 02 | `PYA-L03-P02` | Khung tranh hình vuông | `Cơ bản` | $1 \le a \le 10^4$ | Tính chu vi và diện tích hình vuông |
| 03 | `PYA-L03-P03` | Chu vi tam giác abc | `Cơ bản` | $1 \le a, b, c \le 10^8$ | Tổng 3 cạnh tam giác, số lớn (PYA hà tĩnh) |
| 04 | `PYA-L03-P04` | Cạnh còn lại của hình chữ nhật | `Cơ bản` | $10 < P \le 10^6, a < P // 2$ | Tìm cạnh từ chu vi và một cạnh (PYA bắc giang) |
| 05 | `PYA-L03-P05` | Hồ cá sấu và đảo nhỏ | `Luyện tập` | $1 \le A, B, C \le 10^4$ | Hiệu hai diện tích hình học lồng nhau (PYA lâm đồng) |
| 06 | `PYA-L03-P06` | Đổi giây sang giờ phút giây | `Luyện tập` | $0 \le S \le 10^8$ | Phân rã thời gian ngược dùng `// 3600`, `% 3600` |
| 07 | `PYA-L03-P07` | Lát gạch sân trường | `Luyện tập` | $1 \le D, R, K \le 1000$ | Số viên gạch lát diện tích hình chữ nhật |
| 08 | `PYA-L03-P08` | Thuận đi gặp ánh | `Luyện tập` | $0 \le x, y \le 10^9, 1 \le v \le 10^9$ | Vận tốc, khoảng cách và thời gian (PYA từ sơn) |
| 09 | `PYA-L03-P09` | Rào quanh vườn hoa có cửa | `Luyện tập` | $1 \le a, b \le 10^4, 1 \le c < a$ | Chu vi trừ đi độ rộng lối vào cửa |
| 10 | `PYA-L03-P10` | Diện tích bồn hoa chữ thập | `Vận dụng` | $1 \le a, b \le 10^4$ | Phân tích hình học ghép, trừ phần giao nhau |
| 11 | `PYA-L03-P11` | Diện tích tam giác vuông | `Luyện tập` | $1 \le a, h \le 1000, (a \times h)$ chẵn | Diện tích tam giác vuông $(a \times h) : 2$ |
| 12 | `PYA-L03-P12` | Thể tích hộp chữ nhật | `Luyện tập` | $1 \le d, r, c \le 1000$ | Thể tích khối hộp $d \times r \times c$ |
| 13 | `PYA-L03-P13` | Đổi đô la sang tiền Việt | `Luyện tập` | $1 \le D \le 10^6$ | Đổi đơn vị tiền tệ, nhân tỉ giá $25000$ |
| 14 | `PYA-L03-P14` | Đổi độ C sang độ F | `Luyện tập` | $-50 \le C \le 50, C$ chia hết cho $5$ | Biểu thức hỗn hợp $C \times 9 : 5 + 32$ |
| 15 | `PYA-L03-P15` | Tính vận tốc làm tròn | `Vận dụng` | $1 \le D, T \le 10^4$ | Chia thực $D : T$, làm tròn $2$ chữ số thập phân |
| 16 | `PYA-L03-P16` | Tiền điện bậc thang | `Vận dụng` | $1 \le N \le 10^6$ | Giá bậc thang có điều kiện theo ngưỡng $100$ |

---

### Bài 1 (Cơ bản): Mảnh vườn chữ nhật (`PYA-L03-P01`)

* **Bối cảnh:** Bác Nông dân có một mảnh vườn trồng rau hình chữ nhật với chiều dài $a\text{ mét}$ và chiều rộng $b\text{ mét}$.
* **Yêu cầu:** Em hãy tính chu vi và diện tích của mảnh vườn đó.
* **Đầu vào (Input):** Gồm 2 dòng lần lượt chứa 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$).
* **Đầu ra (Output):** In ra trên một dòng 2 số nguyên cách nhau một dấu cách lần lượt là: Chu vi và Diện tích của mảnh vườn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`6` | `32 60` | Chu vi: $(10 + 6) \times 2 = 32$. Diện tích: $10 \times 6 = 60$. |
* **Gợi ý thuật toán:**
  ```python
  a = int(input())
  b = int(input())
  chu_vi = (a + b) * 2
  dien_tich = a * b
  print(chu_vi, dien_tich)
  ```

---

### Bài 2 (Cơ bản): Khung tranh hình vuông (`PYA-L03-P02`)

* **Bối cảnh:** Bạn Hoa vừa vẽ xong một bức tranh tuyệt đẹp hình vuông có cạnh là $a\text{ cm}$. Hoa muốn làm khung gỗ bọc viền xung quanh bức tranh và dán giấy kính lên toàn bộ bề mặt tranh.
* **Yêu cầu:** Hãy tính độ dài khung gỗ cần mua (chu vi) và diện tích giấy kính cần dán (diện tích).
* **Đầu vào (Input):** Một số tự nhiên $a$ ($1 \le a \le 10^4$).
* **Đầu ra (Output):** In ra 2 số nguyên cách nhau một khoảng trắng: Chu vi và Diện tích.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `8` | `32 64` |

---

### Bài 3 (Cơ bản): Chu vi tam giác abc (`PYA-L03-P03`)
*(Lấy cảm hứng từ Bài 3 Đề thi Lập trình Python tỉnh Hà Tĩnh)*

* **Bối cảnh:** Trong giờ học hình học, thầy giáo cho 3 số tự nhiên $a, b, c$ lần lượt là độ dài 3 cạnh của một tam giác $ABC$.
* **Yêu cầu:** Em hãy lập trình tính và đưa ra chu vi của tam giác $ABC$.
* **Đầu vào (Input):** Ba dòng lần lượt ghi 3 số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^8$).
* **Đầu ra (Output):** In ra một số tự nhiên duy nhất là chu vi tam giác.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`4`<br>`5` | `12` | Chu vi: $3 + 4 + 5 = 12$. |

---

### Bài 4 (Cơ bản): Cạnh còn lại của hình chữ nhật (`PYA-L03-P04`)
*(Lấy cảm hứng từ Bài 6 Đề thi Lập trình Python tỉnh Bắc Giang)*

* **Bối cảnh:** Một cái ao hình chữ nhật có một cạnh bằng $a\text{ mét}$ và có chu vi là $P\text{ mét}$ ($P$ là số chẵn).
* **Yêu cầu:** Em hãy tính và in ra độ dài của cạnh còn lại của hình chữ nhật.
* **Đầu vào (Input):** Gồm 2 dòng: dòng 1 chứa chu vi $P$ ($P$ chẵn, $P \le 10^6$), dòng 2 chứa độ dài cạnh đã biết $a$ ($1 \le a < P // 2$).
* **Đầu ra (Output):** Một số tự nhiên là độ dài cạnh còn lại.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `30`<br>`5` | `10` | Nửa chu vi là: $30 : 2 = 15$. Cạnh còn lại: $15 - 5 = 10$. |
* **Gợi ý thuật toán:** `P = int(input()); a = int(input()); print((P // 2) - a)`.

---

### Bài 5 (Luyện tập): Hồ cá sấu và đảo nhỏ (`PYA-L03-P05`)
*(Lấy cảm hứng từ Bài 2 Đề thi Lập trình Python tỉnh Lâm Đồng)*

* **Bối cảnh:** Một trang trại nuôi cá sấu có một hồ nước hình vuông cạnh $A$. Ở chính giữa hồ, người ta xây một hòn đảo nhỏ hình chữ nhật có kích thước $B \times C$ để cá sấu bò lên phơi nắng (hòn đảo nằm trọn trong hồ nước và không chạm vào bờ hồ).
* **Yêu cầu:** Hãy tính diện tích phần mặt nước còn lại sau khi đã xây hòn đảo nhỏ.
* **Đầu vào (Input):** Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le B, C < A \le 10^4$).
* **Đầu ra (Output):** Một số nguyên duy nhất là diện tích mặt nước còn lại.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`3`<br>`4` | `88` | Diện tích hồ: $10 \times 10 = 100$. Diện tích đảo: $3 \times 4 = 12$.<br>Mặt nước còn lại: $100 - 12 = 88$. |
* **Gợi ý thuật toán:** `print(A * A - B * C)`.

---

### Bài 6 (Luyện tập): Đổi giây sang giờ phút giây (`PYA-L03-P06`)
*(Lấy cảm hứng từ Bài 7 Đề thi Lập trình Python tỉnh Đồng Nai)*

* **Bối cảnh:** Một vệ tinh bay quanh trái đất hết $S$ giây. Nhân vật Robot muốn thông báo khoảng thời gian này dưới dạng dễ hiểu: gồm bao nhiêu Giờ, bao nhiêu Phút và bao nhiêu Giây.
* **Yêu cầu:** Nhập vào tổng số giây $S$. Hãy phân rã thành $H$ giờ, $M$ phút, $S$ giây.
* **Đầu vào (Input):** Một số nguyên $S$ ($0 \le S \le 10^8$).
* **Đầu ra (Output):** In ra ba số nguyên $H, M, S$ cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3665` | `1 1 5` | 3665 giây = 1 giờ (3600s) + 1 phút (60s) + 5 giây. |
* **Gợi ý thuật toán:**
  ```python
  tong_giay = int(input())
  gio = tong_giay // 3600
  giay_du = tong_giay % 3600
  phut = giay_du // 60
  giay = giay_du % 60
  print(gio, phut, giay)
  ```

---

### Bài 7 (Luyện tập): Lát gạch sân trường (`PYA-L03-P07`)

* **Bối cảnh:** Sân trường của trường Phổ thông iKHEDU có hình chữ nhật dài $D\text{ mét}$ và rộng $R\text{ mét}$. Nhà trường muốn lát gạch men cho toàn bộ sân trường bằng các viên gạch hình vuông có cạnh là $K\text{ mét}$ ($D$ và $R$ đều chia hết cho $K$).
* **Yêu cầu:** Tính số lượng viên gạch men cần dùng để lát kín mặt sân.
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số tự nhiên $D, R, K$ ($1 \le K \le R \le D \le 1000$).
* **Đầu ra (Output):** Một số nguyên duy nhất là số viên gạch.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `20`<br>`10`<br>`2` | `50` | Diện tích sân: $20 \times 10 = 200$. Diện tích 1 viên gạch: $2 \times 2 = 4$.<br>Số gạch cần: $200 : 4 = 50$ viên. |
* **Gợi ý thuật toán:** `(D * R) // (K * K)`.

---

### Bài 8 (Luyện tập): Thuận đi gặp ánh (`PYA-L03-P08`)
*(Lấy cảm hứng từ Bài 5 Đề thi Lập trình Python Huyện Từ Sơn - Bắc Ninh)*

* **Bối cảnh:** Thuận và Ánh sống trên một con đường thẳng có các mốc tọa độ tính bằng kilomet. Thuận đang đứng ở vị trí $x$, còn Ánh đang đứng ở vị trí $y$ ($x < y$). Thuận bắt đầu đi xe đạp về phía nhà Ánh với vận tốc không đổi là $v\text{ km/h}$.
* **Biết rằng:** Khoảng cách $y - x$ chia hết cho vận tốc $v$.
* **Yêu cầu:** Sau bao nhiêu giờ thì Thuận sẽ gặp được Ánh?
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số tự nhiên $x, y, v$ ($0 \le x < y \le 10^9, 1 \le v \le 10^9$).
* **Đầu ra (Output):** Số giờ để Thuận gặp Ánh.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`70`<br>`15` | `4` | Khoảng cách giữa 2 bạn: $70 - 10 = 60\text{ km}$.<br>Thời gian gặp nhau: $60 : 15 = 4$ giờ. |
* **Gợi ý thuật toán:** `print((y - x) // v)`.

---

### Bài 9 (Luyện tập): Rào quanh vườn hoa có cửa (`PYA-L03-P09`)

* **Bối cảnh:** Bác thợ làm vườn có một vườn hoa hình chữ nhật kích thước chiều dài $a\text{ mét}$, chiều rộng $b\text{ mét}$. Bác muốn dựng một hàng rào thép gai xung quanh vườn hoa, nhưng chừa lại một lối đi ở một góc vườn làm cổng ra vào rộng đúng $c\text{ mét}$ (không rào cửa).
* **Biết giá thành làm rào:** Mỗi mét hàng rào tốn $15$ nghìn đồng.
* **Yêu cầu:** Tính tổng số tiền (nghìn đồng) bác thợ cần dùng để mua đủ rào thép.
* **Đầu vào (Input):** Ba dòng lần lượt là $a, b, c$ ($1 \le a, b \le 10^4, 1 \le c < (a + b) * 2$).
* **Đầu ra (Output):** Một số nguyên là số tiền (nghìn đồng).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12`<br>`8`<br>`2` | `570` | Chu vi cả vườn: $(12 + 8) \times 2 = 40\text{ m}$.<br>Độ dài rào cần mua: $40 - 2 = 38\text{ m}$.<br>Số tiền: $38 \times 15 = 570$ nghìn đồng. |
* **Gợi ý thuật toán:** `((a + b) * 2 - c) * 15`.

---

### Bài 10 (Vận dụng): Diện tích bồn hoa chữ thập (`PYA-L03-P10`)

* **Bối cảnh:** Trong công viên có một bồn hoa hình chữ thập (dấu cộng) được tạo thành bởi hai luống hoa hình chữ nhật đặt chồng lên nhau:
  * Một luống hoa nằm ngang có kích thước $a \times b$ ($a$ là chiều dài, $b$ là chiều rộng).
  * Một luống hoa nằm dọc có kích thước $b \times a$ ($b$ là chiều rộng, $a$ là chiều dài).
  * Hai luống hoa giao nhau ở chính giữa tạo thành một hình vuông kích thước $b \times b$.
* **Yêu cầu:** Em hãy tính diện tích thực tế của toàn bộ bồn hoa chữ thập này (không được tính trùng lặp phần diện tích giao nhau ở chính giữa).
* **Đầu vào (Input):** Nhập 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$) trên 2 dòng.
* **Đầu ra (Output):** Diện tích thực tế của bồn hoa.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`3` | `51` | - Luống ngang: $10 \times 3 = 30$.<br>- Luống dọc: $3 \times 10 = 30$.<br>- Phần giao nhau ở giữa: $3 \times 3 = 9$.<br>- Diện tích bồn hoa: $30 + 30 - 9 = 51$. |
* **Gợi ý thuật toán:**
  * Công thức gộp: $S = (a \times b) + (a \times b) - (b \times b) = 2ab - b^2$ hoặc $b \times (2a - b)$.
  * Code: `print(2 * a * b - b * b)`.

---

### Bài 11 (Luyện tập): Diện tích tam giác vuông (`PYA-L03-P11`)

* **Bối cảnh:** Bé Na có một miếng bánh hình tam giác vuông với hai cạnh góc vuông dài $a\text{ cm}$ và $h\text{ cm}$ (tích $a \times h$ luôn là số chẵn).
* **Yêu cầu:** Em hãy tính diện tích của miếng bánh tam giác vuông đó.
* **Đầu vào (Input):** Hai dòng lần lượt chứa 2 số tự nhiên $a$ và $h$ ($1 \le a, h \le 1000$, $a \times h$ chia hết cho $2$).
* **Đầu ra (Output):** Một số nguyên là diện tích tam giác vuông.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `6`<br>`4` | `12` | Tích hai cạnh: $6 \times 4 = 24$. Diện tích: $24 : 2 = 12$. |
* **Gợi ý thuật toán:** `print(a * h // 2)`.

---

### Bài 12 (Luyện tập): Thể tích hộp chữ nhật (`PYA-L03-P12`)

* **Bối cảnh:** Bé Tí được tặng một hộp sữa dâu hình hộp chữ nhật có chiều dài $d\text{ cm}$, chiều rộng $r\text{ cm}$ và chiều cao $c\text{ cm}$.
* **Yêu cầu:** Em hãy tính thể tích của hộp sữa đó.
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số tự nhiên $d, r, c$ ($1 \le d, r, c \le 1000$).
* **Đầu ra (Output):** Một số nguyên là thể tích hộp chữ nhật.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`3`<br>`2` | `30` | Thể tích: $5 \times 3 \times 2 = 30$. |
* **Gợi ý thuật toán:** `print(d * r * c)`.

---

### Bài 13 (Luyện tập): Đổi đô la sang tiền Việt (`PYA-L03-P13`)

* **Bối cảnh:** Bác Hùng mang theo $D$ tờ đô la Mỹ (mỗi tờ $1$ đô la) về Việt Nam. Ngân hàng đổi $1$ đô la lấy $25000$ đồng.
* **Yêu cầu:** Em hãy tính số tiền Việt Nam (đồng) bác Hùng nhận được.
* **Đầu vào (Input):** Một số tự nhiên $D$ ($1 \le D \le 10^6$).
* **Đầu ra (Output):** Một số nguyên là số tiền Việt Nam tính bằng đồng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4` | `100000` | Số tiền: $4 \times 25000 = 100000$ đồng. |
* **Gợi ý thuật toán:** `print(D * 25000)`.

---

### Bài 14 (Luyện tập): Đổi độ C sang độ F (`PYA-L03-P14`)

* **Bối cảnh:** Hôm nay trời nóng $C$ độ C ($C$ luôn chia hết cho $5$). Em hãy đổi nhiệt độ này sang độ F để kể cho bạn nhỏ ở Mỹ nghe.
* **Yêu cầu:** Em hãy tính nhiệt độ độ F theo công thức $F = C \times 9 : 5 + 32$.
* **Đầu vào (Input):** Một số nguyên $C$ ($-50 \le C \le 50$, $C$ chia hết cho $5$).
* **Đầu ra (Output):** Một số nguyên là nhiệt độ độ F.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `30` | `86` | $30 \times 9 : 5 + 32 = 54 + 32 = 86$. |
* **Gợi ý thuật toán:** `print(C * 9 // 5 + 32)`.

---

### Bài 15 (Vận dụng): Tính vận tốc làm tròn (`PYA-L03-P15`)

* **Bối cảnh:** Bạn Mít đạp xe quãng đường $D\text{ km}$ hết $T$ giờ để về thăm bà ngoại. Mẹ dặn bạn ghi lại vận tốc trung bình, làm tròn đến đúng $2$ chữ số sau dấu chấm thập phân.
* **Yêu cầu:** Em hãy tính vận tốc trung bình $V = D : T$ (km/h) và làm tròn đến $2$ chữ số thập phân.
* **Đầu vào (Input):** Hai dòng lần lượt chứa 2 số nguyên $D$ và $T$ ($1 \le D, T \le 10^4$).
* **Đầu ra (Output):** Vận tốc trung bình làm tròn đến $2$ chữ số thập phân.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `100`<br>`6` | `16.67` | $100 : 6 = 16.666\ldots$, làm tròn $2$ chữ số được $16.67$. |
* **Gợi ý thuật toán:** `print(f"{D / T:.2f}")`.

---

### Bài 16 (Vận dụng): Tiền điện bậc thang (`PYA-L03-P16`)

* **Bối cảnh:** Gia đình bạn Bông dùng hết $N$ số điện. Giá điện: $100$ số đầu giá $2000$ đồng một số, từ số thứ $101$ trở đi giá $3500$ đồng một số.
* **Yêu cầu:** Em hãy tính tổng số tiền điện (đồng) cả nhà phải trả.
* **Đầu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 10^6$).
* **Đầu ra (Output):** Một số nguyên là tổng tiền điện tính bằng đồng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `120` | `270000` | $100 \times 2000 = 200000$. $20 \times 3500 = 70000$.<br>Tổng: $200000 + 70000 = 270000$. |
* **Gợi ý thuật toán:** Nếu $N \le 100$ thì in $N \times 2000$, ngược lại in $100 \times 2000 + (N - 100) \times 3500$.


================================================================================
# CHƯƠNG 02: TƯ DUY RẼ NHÁNH & ĐIỀU KIỆN LOGIC
================================================================================


--------------------------------------------------------------------------------
<!-- Bài 04: lesson-04 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 04: Rẽ nhánh và điều kiện logic

## 1. Tóm tắt kiến thức trọng tâm
- **Cấu trúc rẽ nhánh:** Dùng để đưa ra quyết định dựa trên điều kiện `True` (Đúng) hoặc `False` (Sai).
- **Cú pháp đầy đủ:**
  ```python
  if <Dieu_kien_1>:
      # Chạy khi Dieu_kien_1 Đúng
  elif <Dieu_kien_2>:
      # Chạy khi Dieu_kien_1 Sai nhưng Dieu_kien_2 Đúng
  else:
      # Chạy khi tất cả các điều kiện trên đều Sai
  ```
- **Quy tắc thụt lề:** Khối lệnh con phải lùi vào 4 dấu cách. Sau `if`, `elif`, `else` bắt buộc có dấu hai chấm `:`.
- **Toán tử so sánh:** Bằng nhau (`==`), Khác nhau (`!=`), Lớn hơn (`>`), Nhỏ hơn (`<`), Lớn hơn hoặc bằng (`>=`), Nhỏ hơn hoặc bằng (`<=`).
- **Liên minh logic:**
  - `and`: Bắt buộc tất cả cùng đúng.
  - `or`: Chỉ cần ít nhất một điều kiện đúng.
  - `not`: Đảo ngược Đúng $\\leftrightarrow$ Sai.
  - Cú pháp so sánh kẹp tiện lợi trong Python: `10 <= x <= 99`.

## 2. Sổ tay các biểu thức logic hay thi
- Kiểm tra tam giác hợp lệ: `(a + b > c) and (a + c > b) and (b + c > a)`
- Kiểm tra năm nhuận: `(nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)`
- Kiểm tra số có 2 chữ số: `10 <= n <= 99`

## 3. Bẫy lỗi phòng thi
- ❌ Nhầm `==` (so sánh) thành `=` (gán): `if a = 5:` $\implies$ Báo lỗi `SyntaxError`.
- ❌ Bẫy viết tắt sai: `if a == 1 or 2:` $\implies$ Python hiểu là `if (a == 1) or (2)`, số 2 khác 0 luôn là `True` nên câu `if` luôn chạy sai! Phải viết: `if a == 1 or a == 2:`.

## 4. Mẫu code chuẩn
```python
# Kiểm tra phân loại tam giác
a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("TAM GIAC DEU")
    elif a == b or b == c or c == a:
        print("TAM GIAC CAN")
    else:
        print("TAM GIAC THUONG")
else:
    print("KHONG PHAI TAM GIAC")
```

## 5. Concept quiz: 44 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Phép toán nào sau đây dùng để so sánh hai giá trị có bằng nhau không trong Python?
- **A.** `=`
- **B.** **[Đáp án đúng]** `==`
- **C.** `===`
- **D.** `equal`
> *Giải thích:* Trong Python, `==` là phép so sánh bằng, còn `=` là phép gán giá trị.

#### Câu 2: Kết quả của biểu thức so sánh `10 != 10` là:
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `10`
- **D.** Báo lỗi
> *Giải thích:* `!=` là phép so sánh khác. Vì $10$ bằng $10$, nên khẳng định $10$ khác $10$ là sai (`False`).

#### Câu 3: Ký tự bắt buộc phải có ở cuối dòng lệnh `if` và `else` là:
- **A.** Dấu chấm phẩy `;`
- **B.** **[Đáp án đúng]** Dấu hai chấm `:`
- **C.** Dấu chấm `.`
- **D.** Dấu mũi tên `->`
> *Giải thích:* Python quy định sau điều kiện `if` và sau từ khóa `else` bắt buộc phải có dấu hai chấm `:`.

#### Câu 4: Đoạn code sau sẽ in ra gì?
```python
x = 7
if x > 5:
    print("A")
else:
    print("B")
```
- **A.** `B`
- **B.** **[Đáp án đúng]** `A`
- **C.** Cả `A` và `B`
- **D.** Không in gì cả
> *Giải thích:* Vì $7 > 5$ là đúng (`True`), máy tính thực hiện khối lệnh của `if`, in ra `A`.

#### Câu 5: Đoạn code sau gặp lỗi gì?
```python
tuoi = 8
if tuoi >= 6:
print("Vao lop 1")
```
- **A.** `SyntaxError`
- **B.** **[Đáp án đúng]** `IndentationError`
- **C.** `TypeError`
- **D.** `NameError`
> *Giải thích:* Lệnh `print` dưới `if` không được thụt lề vào trong, vi phạm quy tắc Indentation của Python.

#### Câu 6: Biểu thức kiểm tra số tự nhiên $A$ có chia hết cho 3 hay không là:
- **A.** `A / 3 == 0`
- **B.** `A // 3 == 0`
- **C.** **[Đáp án đúng]** `A % 3 == 0`
- **D.** `A % 3 != 0`
> *Giải thích:* $A$ chia hết cho 3 khi và chỉ khi phần dư bằng 0: `A % 3 == 0`.

#### Câu 7: Đoạn code sau in ra gì khi nhập $n = 10$?
```python
n = int(input())
if n % 2 == 0:
    print("Chan")
print("Xong")
```
- **A.** `Chan`
- **B.** **[Đáp án đúng]** `Chan` và `Xong` (trên 2 dòng)
- **C.** `Xong`
- **D.** Báo lỗi
> *Giải thích:* Vì $10$ là số chẵn nên in `Chan`. Dòng `print("Xong")` không thụt lề nên là lệnh độc lập, luôn được thực thi.

#### Câu 8: Khi nào thì khối lệnh bên trong `else:` được thực thi?
- **A.** Luôn luôn được thực thi
- **B.** **[Đáp án đúng]** Khi điều kiện trong `if` có giá trị là `False`
- **C.** Khi điều kiện trong `if` có giá trị là `True`
- **D.** Khi chương trình xảy ra lỗi
> *Giải thích:* Khối `else` chỉ chạy khi điều kiện của `if` bị sai (`False`).

#### Câu 9: Trong Python, biểu thức so sánh `5 >= 5` trả về giá trị gì?
- **A.** **[Đáp án đúng]** `True`
- **B.** `False`
- **C.** `5`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Phép so sánh lớn hơn hoặc bằng `>=` thỏa mãn khi số bên trái bằng số bên phải.

#### Câu 10: Đoạn code nào tìm giá trị nhỏ nhất giữa 2 số $a$ và $b$ đúng chuẩn?
- **A.** `if a < b: min_val = b else: min_val = a`
- **B.** **[Đáp án đúng]** `if a < b: min_val = a else: min_val = b`
- **C.** `min_val = a > b`
- **D.** `if a == b: min_val = a`
> *Giải thích:* Nếu $a < b$ thì $a$ là số nhỏ hơn, ngược lại $b$ là số nhỏ hơn.

#### Câu 11: Cho đoạn code sau:
```python
a = 15
if a % 5 == 0:
    a = a + 5
else:
    a = a - 5
print(a)
```
Giá trị in ra màn hình là:
- **A.** `10`
- **B.** `15`
- **C.** **[Đáp án đúng]** `20`
- **D.** `25`
> *Giải thích:* $15$ chia hết cho $5$ ($15 \% 5 == 0$ là `True`), nên thực hiện `a = a + 5 = 20`.

#### Câu 12: Điều gì xảy ra nếu viết `if (a = 5):` trong Python?
- **A.** Máy hiểu là so sánh `a` với 5.
- **B.** **[Đáp án đúng]** Báo lỗi `SyntaxError: invalid syntax`.
- **C.** Gán `a = 5` rồi luôn chạy nhánh `if`.
- **D.** In ra số 5.
> *Giải thích:* Python cấm dùng toán tử gán `=` bên trong điều kiện của lệnh `if`.

#### Câu 13: Có bao nhiêu dấu cách (spaces) chuẩn thường dùng để thụt lề trong Python?
- **A.** 1 dấu cách
- **B.** 2 dấu cách
- **C.** **[Đáp án đúng]** 4 dấu cách (hoặc 1 lần nhấn phím Tab)
- **D.** 8 dấu cách
> *Giải thích:* Chuẩn PEP 8 của Python quy định thụt lề chuẩn là 4 dấu cách.

#### Câu 14: Lệnh `else` có thể đứng một mình mà không có `if` ở trước không?
- **A.** Được phép
- **B.** **[Đáp án đúng]** Không được phép (Báo lỗi `SyntaxError`)
- **C.** Chỉ được phép khi có vòng lặp
- **D.** Tùy trường hợp
> *Giải thích:* `else` là nhánh phủ định bắt buộc phải đi kèm với một cấu trúc điều kiện `if` trước đó.

#### Câu 15: Kết quả của đoạn code sau:
```python
diem = 10
if diem == 10:
    print("Xuat sac")
if diem >= 8:
    print("Gioi")
```
- **A.** Chỉ in `Xuat sac`
- **B.** Chỉ in `Gioi`
- **C.** **[Đáp án đúng]** In cả hai dòng: `Xuat sac` và `Gioi`
- **D.** Báo lỗi
> *Giải thích:* Đây là hai lệnh `if` độc lập nhau. Cả hai điều kiện đều thỏa mãn nên cả hai câu lệnh đều được thực thi!

#### Câu 16: Từ khóa `elif` trong Python là viết tắt của cụm từ nào?
- **A.** `else if`
- **B.** **[Đáp án đúng]** `else if`
- **C.** `early if`
- **D.** `end if`
> *Giải thích:* `elif` là dạng viết tắt của `else if` (nếu không thì nếu).

#### Câu 17: Trong cấu trúc `if - elif - else`, có tối đa bao nhiêu khối `elif`?
- **A.** Chỉ được có 1 khối
- **B.** Tối đa 3 khối
- **C.** **[Đáp án đúng]** Không giới hạn số lượng khối `elif`
- **D.** Bắt buộc phải có ít nhất 2 khối
> *Giải thích:* Em có thể đặt bao nhiêu khối `elif` tùy thích để phân loại nhiều trường hợp khác nhau.

#### Câu 18: Khối `else` ở cuối cùng có bắt buộc phải có không?
- **A.** Bắt buộc
- **B.** **[Đáp án đúng]** Không bắt buộc (có thể bỏ qua nếu không cần xử lý trường hợp còn lại)
- **C.** Chỉ bắt buộc khi có `elif`
- **D.** Báo lỗi cú pháp nếu thiếu `else`
> *Giải thích:* Khối `else` là tùy chọn (optional). Nếu không có trường hợp mặc định thì không cần viết `else`.

#### Câu 19: Đoạn code sau in ra kết quả gì?
```python
x = 10
if x > 5:
    print("A")
elif x > 8:
    print("B")
else:
    print("C")
```
- **A.** `B`
- **B.** `A` và `B`
- **C.** **[Đáp án đúng]** `A`
- **D.** `C`
> *Giải thích:* Mặc dù $10 > 8$ cũng đúng, nhưng máy tính gặp `x > 5` đúng trước nên in `A` và thoát ra ngay, không xét tới `elif` nữa.

#### Câu 20: Đoạn code sau in ra gì?
```python
tuoi = 4
if tuoi >= 18:
    print("Nguoi lon")
elif tuoi >= 6:
    print("Hoc sinh")
else:
    print("Mam non")
```
- **A.** `Nguoi lon`
- **B.** `Hoc sinh`
- **C.** **[Đáp án đúng]** `Mam non`
- **D.** Không in gì cả
> *Giải thích:* Cả 2 điều kiện đầu đều sai nên rơi vào khối `else`, in `Mam non`.

#### Câu 21: Thứ tự sắp xếp các điều kiện trong chuỗi `if - elif` có quan trọng không?
- **A.** Không quan trọng, viết cái nào trước cũng được
- **B.** **[Đáp án đúng]** Rất quan trọng, phải sắp xếp theo trật tự logic (từ chặt chẽ nhất đến lỏng hơn)
- **C.** Python tự động sắp xếp lại cho đúng
- **D.** Chỉ quan trọng khi có số âm
> *Giải thích:* Nếu viết `if diem >= 5:` lên trước `elif diem >= 9:`, mọi điểm 9 và 10 đều bị rơi vào điều kiện $\ge 5$ và không bao giờ xuống được điều kiện $\ge 9$!

#### Câu 22: Bác bảo vệ phân loại xe: Xe đạp phí 2k, xe máy 5k, ô tô 20k. Cần ít nhất bao nhiêu nhánh điều kiện?
- **A.** 1 nhánh
- **B.** 2 nhánh
- **C.** **[Đáp án đúng]** 3 nhánh (hoặc 1 `if`, 1 `elif`, 1 `else`)
- **D.** 4 nhánh
> *Giải thích:* Có 3 loại xe nên cần cấu trúc 3 nhánh.

#### Câu 23: Đoạn code nào sau đây báo lỗi cú pháp?
- **A.** `if a > 0: print("Duong")`
- **B.** `elif a == 0: print("Khong")` (đứng một mình không có `if`)
- **C.** **[Đáp án đúng]** Câu B vì `elif` không thể đứng mở đầu mà không có `if`
- **D.** Cả A và B đều đúng
> *Giải thích:* `elif` bắt buộc phải đi sau một lệnh `if`.

#### Câu 24: Để tìm số lớn nhất trong 3 số $a, b, c$, hàm nào có sẵn trong Python giúp ta làm việc này chỉ trong 1 dòng?
- **A.** `maximum(a, b, c)`
- **B.** **[Đáp án đúng]** `max(a, b, c)`
- **C.** `greatest(a, b, c)`
- **D.** `top(a, b, c)`
> *Giải thích:* Hàm `max()` trong Python có thể nhận nhiều đối số và trả về số lớn nhất.

#### Câu 25: Cho đoạn code sau:
```python
a = 0
if a > 0:
    print("Duong")
elif a < 0:
    print("Am")
else:
    print("Khong")
```
Màn hình sẽ in ra:
- **A.** `Duong`
- **B.** `Am`
- **C.** **[Đáp án đúng]** `Khong`
- **D.** Báo lỗi
> *Giải thích:* Số 0 không dương cũng không âm nên chạy vào `else`.

#### Câu 26: Có thể lồng một khối lệnh `if - else` vào bên trong một khối `if` khác không?
- **A.** Không được phép
- **B.** **[Đáp án đúng]** Hoàn toàn được phép (gọi là Nested if - If lồng nhau)
- **C.** Chỉ được lồng tối đa 2 lần
- **D.** Python sẽ báo lỗi bộ nhớ
> *Giải thích:* Python cho phép lồng các cấu trúc điều kiện thoải mái, chỉ cần chú ý thụt lề cho chính xác.

#### Câu 27: Đoạn code sau in ra gì?
```python
n = 15
if n % 3 == 0:
    print("Chia het cho 3")
elif n % 5 == 0:
    print("Chia het cho 5")
```
- **A.** `Chia het cho 5`
- **B.** In cả hai dòng
- **C.** **[Đáp án đúng]** `Chia het cho 3`
- **D.** Không in gì
> *Giải thích:* 15 chia hết cho cả 3 và 5, nhưng điều kiện `n % 3 == 0` đứng trước nên thực hiện xong là kết thúc.

#### Câu 28: Làm thế nào để in ra cả hai dòng nếu số chia hết cho cả 3 và 5?
- **A.** Dùng `elif`
- **B.** **[Đáp án đúng]** Dùng 2 lệnh `if` độc lập nhau
- **C.** Dùng `else`
- **D.** Dùng phép chia dư `% 15`
> *Giải thích:* Hai lệnh `if` độc lập sẽ không loại trừ nhau, máy tính sẽ kiểm tra và thực thi cả hai nếu cùng đúng.

#### Câu 29: Đoạn code sau in ra gì?
```python
x = 5
if x == 1:
    print(1)
elif x == 2:
    print(2)
elif x == 3:
    print(3)
```
- **A.** `0`
- **B.** `None`
- **C.** **[Đáp án đúng]** Không in ra bất kỳ ký tự nào
- **D.** Báo lỗi
> *Giải thích:* Cả 3 điều kiện đều sai và không có nhánh `else`, chương trình kết thúc êm đẹp mà không in gì.

#### Câu 30: Biểu thức `(True and False)` cho kết quả là gì?
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `None`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Phép `and` đòi hỏi cả 2 vế phải cùng là `True`. Có 1 vế `False` thì kết quả là `False`.

#### Câu 31: Biểu thức `(True or False)` cho kết quả là gì?
- **A.** **[Đáp án đúng]** `True`
- **B.** `False`
- **C.** `None`
- **D.** Báo lỗi
> *Giải thích:* Phép `or` chỉ cần ít nhất 1 vế là `True` thì kết quả sẽ là `True`.

#### Câu 32: Kết quả của biểu thức `not (10 > 5)` là:
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `10 < 5`
- **D.** `None`
> *Giải thích:* $10 > 5$ là `True`. Phép `not True` đảo ngược lại thành `False`.

#### Câu 33: Cú pháp nào sau đây kiểm tra số $x$ là số chẵn và lớn hơn 10?
- **A.** `x % 2 == 0 or x > 10`
- **B.** **[Đáp án đúng]** `x % 2 == 0 and x > 10`
- **C.** `x % 2 == 0 not x > 10`
- **D.** `x % 2 == 0 & x > 10`
> *Giải thích:* Từ khóa `and` dùng để kết hợp hai điều kiện cần xảy ra đồng thời.

#### Câu 34: Năm nào sau đây là năm nhuận?
- **A.** 1900
- **B.** 2021
- **C.** 2023
- **D.** **[Đáp án đúng]** 2024
> *Giải thích:* 2024 chia hết cho 4 và không chia hết cho 100 nên là năm nhuận. Năm 1900 chia hết cho 100 nhưng không chia hết cho 400 nên không phải năm nhuận.

#### Câu 35: Điều kiện tồn tại tam giác với 3 cạnh $a, b, c$ là:
- **A.** `a + b + c > 0`
- **B.** `a + b > c or a + c > b or b + c > a`
- **C.** **[Đáp án đúng]** `a + b > c and a + c > b and b + c > a`
- **D.** `a * a + b * b == c * c`
> *Giải thích:* Bắt buộc cả 3 bất đẳng thức phải cùng thỏa mãn (`and`).

#### Câu 36: Đoạn code sau in ra gì?
```python
a = 15
if a % 3 == 0 and a % 5 == 0:
    print("YES")
else:
    print("NO")
```
- **A.** `NO`
- **B.** **[Đáp án đúng]** `YES`
- **C.** `YES NO`
- **D.** Báo lỗi
> *Giải thích:* 15 vừa chia hết cho 3 vừa chia hết cho 5, cả hai vế đều đúng nên in `YES`.

#### Câu 37: Đoạn code sau in ra gì?
```python
x = 7
if 1 <= x <= 10:
    print("Trong khoang")
else:
    print("Ngoai khoang")
```
- **A.** **[Đáp án đúng]** `Trong khoang`
- **B.** `Ngoai khoang`
- **C.** Báo lỗi cú pháp
- **D.** Không in gì
> *Giải thích:* Python hỗ trợ so sánh kẹp $1 \le 7 \le 10$, điều kiện đúng nên in `Trong khoang`.

#### Câu 38: Thứ tự ưu tiên giữa các toán tử logic trong Python là:
- **A.** `or` trước, `and` sau, `not` cuối
- **B.** **[Đáp án đúng]** `not` ưu tiên cao nhất, sau đó đến `and`, cuối cùng là `or`
- **C.** Từ trái sang phải, cái nào đứng trước làm trước
- **D.** `and` và `or` ngang hàng nhau
> *Giải thích:* Quy tắc chuẩn: `not` > `and` > `or`. (Tuy nhiên nên dùng ngoặc `( ... )` để code rõ ràng nhất).

#### Câu 39: Biểu thức `not False and True` tương đương với:
- **A.** `not (False and True)`
- **B.** **[Đáp án đúng]** `(not False) and True` $\implies$ `True and True` = `True`
- **C.** `False`
- **D.** Báo lỗi
> *Giải thích:* `not` có ưu tiên cao hơn `and`, nên `not False` được tính trước thành `True`, sau đó `True and True` ra `True`.

#### Câu 40: Làm sao để kiểm tra tháng $M$ có 31 ngày?
- **A.** `M in (1, 3, 5, 7, 8, 10, 12)`
- **B.** `M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12`
- **C.** **[Đáp án đúng]** Cả A và B đều đúng
- **D.** `M % 2 != 0`
> *Giải thích:* Cả hai cách viết đều đúng logic các tháng có 31 ngày trong năm.

#### Câu 41: Biểu thức nào kiểm tra một điểm tọa độ $(x, y)$ nằm ở góc phần tư thứ nhất (cả $x$ và $y$ đều dương)?
- **A.** `x > 0 or y > 0`
- **B.** **[Đáp án đúng]** `x > 0 and y > 0`
- **C.** `x * y > 0`
- **D.** `x + y > 0`
> *Giải thích:* Góc phần tư thứ nhất yêu cầu cả hoành độ và tung độ đều phải dương.

#### Câu 42: Bẫy lỗi: Đoạn code `if a == 1 or 2:` có ý nghĩa là gì?
- **A.** Kiểm tra xem `a` có bằng 1 hoặc bằng 2 không
- **B.** **[Đáp án đúng]** Luôn luôn đúng (`True`) vì số 2 khác 0 được Python coi là `True`!
- **C.** Báo lỗi cú pháp
- **D.** Kiểm tra `a == 3`
> *Giải thích:* Đây là bẫy lỗi kinh điển! Phải viết đầy đủ: `if a == 1 or a == 2:`. Nếu viết `or 2`, Python sẽ xét giá trị độc lập của số 2, mà số khác 0 luôn là `True`, dẫn đến câu `if` luôn chạy!

#### Câu 43: Đoạn code sau in ra gì?
```python
troi_mua = False
co_o = False
if not troi_mua or co_o:
    print("Di choi")
else:
    print("O nha")
```
- **A.** `O nha`
- **B.** **[Đáp án đúng]** `Di choi`
- **C.** Cả hai
- **D.** Không in gì
> *Giải thích:* `not troi_mua` trở thành `True`. `True or False` ra `True`, nên in `Di choi`.

#### Câu 44: Kiểm tra số tự nhiên $N$ có đúng 2 chữ số:
- **A.** `N >= 10 and N <= 99`
- **B.** `10 <= N <= 99`
- **C.** **[Đáp án đúng]** Cả A và B đều hoàn toàn chính xác
- **D.** `N // 10 > 0`
> *Giải thích:* Cả hai cách viết đều giới hạn chính xác các số nguyên từ 10 đến 99.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 04: Rẽ nhánh và điều kiện logic

---

## Bảng ma trận bài tập (36 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L04-P01` | Kiểm tra số chẵn lẻ | `Cơ bản` | $0 \le N \le 10^9$ | Cú pháp `if - else` với phép `% 2` |
| 02 | `PYA-L04-P02` | Vé vào công viên | `Cơ bản` | $1 \le h \le 200$ | So sánh chiều cao $\ge 130\text{ cm}$ |
| 03 | `PYA-L04-P03` | Ai cao hơn? | `Cơ bản` | $50 \le a, b \le 200$ | So sánh 2 số, in tên bạn cao hơn |
| 04 | `PYA-L04-P04` | Số lớn nhất trong hai số | `Cơ bản` | $-10^9 \le a, b \le 10^9$ | Tìm max giữa 2 số nguyên bất kỳ |
| 05 | `PYA-L04-P05` | Chia kẹo công bằng | `Cơ bản` | $1 \le a, b \le 10^6$ | Kiểm tra tính chia hết `a % b == 0` |
| 06 | `PYA-L04-P06` | Điền phép tính lớn nhất | `Luyện tập` | $0 \le A \le 100$ | So sánh kết quả các phép tính (PYA bắc giang) |
| 07 | `PYA-L04-P07` | Giảm giá siêu thị | `Luyện tập` | $1 \le N \le 10^6$ | Điều kiện giảm giá khi tổng tiền $\ge 500$K |
| 08 | `PYA-L04-P08` | Cặp số bằng nhau hay khác? | `Luyện tập` | $0 \le a, b \le 10^9$ | Ba trường hợp: Lớn hơn, nhỏ hơn hay bằng nhau |
| 09 | `PYA-L04-P09` | Trị tuyệt đối của một số | `Luyện tập` | $-10^9 \le N \le 10^9$ | Tự cài đặt hàm trị tuyệt đối đổi dấu số âm |
| 10 | `PYA-L04-P10` | Bác thợ mộc cắt gỗ | `Luyện tập` | $1 \le L, K \le 10^9$ | So sánh xem thanh gỗ có đủ dài để cắt không |
| 11 | `PYA-L04-P11` | Cạnh thứ tư hình chữ nhật | `Luyện tập` | $1 \le A, B, C \le 1000$ | Nhận diện 2 cặp cạnh bằng nhau (PYA miền bắc) |
| 12 | `PYA-L04-P12` | Trò chơi oẳn tù tì | `Vận dụng` | $a, b \in \{1, 2, 3\}$ | Logic thắng thua vòng tròn quy ước số |
| 13 | `PYA-L05-P01` | Đèn giao thông ngã tư | `Cơ bản` | Ký tự `D, V, X` | Cấu trúc 3 nhánh `if - elif - else` cơ bản |
| 14 | `PYA-L05-P02` | Dấu của số nguyên | `Cơ bản` | $-10^9 \le N \le 10^9$ | Phân biệt: Dương (`DUONG`), âm (`AM`), không (`KHONG`) |
| 15 | `PYA-L05-P03` | Số lớn nhất trong ba số | `Cơ bản` | $-10^9 \le a, b, c \le 10^9$ | Kỹ thuật tìm max 3 số hoặc dùng lính canh |
| 16 | `PYA-L05-P04` | Xếp loại học lực | `Cơ bản` | $0.0 \le diem \le 10.0$ | Phân loại bậc thang điểm số số thực |
| 17 | `PYA-L05-P05` | Vé gửi xe bến bãi | `Cơ bản` | Loại xe $1, 2, 3$ | Tính tiền gửi xe theo từng mức quy định |
| 18 | `PYA-L05-P06` | Mario cứu công chúa | `Luyện tập` | $1 \le K, P, N \le 1000$ | Mô phỏng di chuyển năng lượng (PYA củ chi) |
| 19 | `PYA-L05-P07` | Tính cước taxi bậc thang | `Luyện tập` | $1 \le km \le 100$ | Bài toán tính cước lũy tiến kinh điển |
| 20 | `PYA-L05-P08` | Phân loại tam giác | `Luyện tập` | $1 \le a, b, c \le 1000$ | Phân biệt tam giác đều, cân hay thường |
| 21 | `PYA-L05-P09` | Thuận đi tìm ánh đa vận tốc | `Luyện tập` | $0 \le x, y \le 10^9, v \ge 0$ | Bắt bẫy $x == y$ hoặc $v == 0$ (PYA từ sơn) |
| 22 | `PYA-L05-P10` | Thứ mấy trong tuần? | `Luyện tập` | $1 \le k \le 365$ | Đổi số ngày sang thứ hai đến chủ nhật |
| 23 | `PYA-L05-P11` | Cửa hàng bánh bột lọc khuyến mãi | `Luyện tập` | $1 \le N \le 1000$ | Bài toán mua theo gói bậc thang (PYA Bảng A) |
| 24 | `PYA-L05-P12` | Bốn mùa trong năm | `Vận dụng` | $1 \le thang \le 12$ | Gom nhóm nhiều giá trị vào các mùa xuân, hạ, thu, đông |
| 25 | `PYA-L06-P01` | Số chẵn có hai chữ số | `Cơ bản` | $1 \le N \le 1000$ | Điều kiện kết hợp `and`: $10 \le N \le 99$ và chẵn |
| 26 | `PYA-L06-P02` | Bội chung của 3 và 5 | `Cơ bản` | $1 \le N \le 10^9$ | Chia hết đồng thời cho cả 3 và 5 |
| 27 | `PYA-L06-P03` | Ngày nghỉ cuối tuần | `Cơ bản` | $2 \le d \le 8$ | Điều kiện `or`: Thứ bảy hoặc chủ nhật |
| 28 | `PYA-L06-P04` | Điểm nằm trong hình chữ nhật | `Cơ bản` | $0 \le x, y \le 100$ | Kiểm tra tọa độ kẹp: $0 \le x \le W$ và $0 \le y \le H$ |
| 29 | `PYA-L06-P05` | Ba cạnh tam giác hợp lệ | `Cơ bản` | $1 \le a, b, c \le 10^9$ | Bất đẳng thức tam giác 3 điều kiện `and` |
| 30 | `PYA-L06-P06` | Kiểm tra năm nhuận | `Luyện tập` | $1 \le Y \le 10^5$ | Quy tắc năm nhuận thiên văn học kết hợp `and`/`or` |
| 31 | `PYA-L06-P07` | Số ngày trong tháng | `Luyện tập` | $1 \le M \le 12, 1 \le Y \le 10^5$ | Xác định 28, 29, 30 hay 31 ngày (PYA bắc giang) |
| 32 | `PYA-L06-P08` | Tam giác vuông hay không? | `Luyện tập` | $1 \le a, b, c \le 10^4$ | Định lý pytago kết hợp 3 trường hợp cạnh huyền |
| 33 | `PYA-L06-P09` | Rút thẻ may mắn | `Luyện tập` | $1 \le N \le 10^9$ | Thẻ trúng thưởng chia hết cho 7 hoặc tận cùng bằng 7 |
| 34 | `PYA-L06-P10` | Ngày kế tiếp trong năm | `Luyện tập` | Ngày, tháng, năm hợp lệ | Xử lý chuyển ngày cuối tháng, cuối năm nhuận |
| 35 | `PYA-L06-P11` | Cặp đôi cùng dấu hay trái dấu | `Vận dụng` | $-10^9 \le a, b \le 10^9$ | Bắt bẫy số 0, cùng dương, cùng âm hoặc trái dấu |
| 36 | `PYA-L06-P12` | Giao nhau của hai đoạn thẳng | `Thử thách` | $-10^9 \le L_1, R_1, L_2, R_2 \le 10^9$ | Xác định hai đoạn trên trục số có giao nhau không |

---

### Bài 1 (Cơ bản): Kiểm tra số chẵn lẻ (`PYA-L04-P01`)

* **Yêu cầu:** Nhập vào một số tự nhiên $N$. Nếu $N$ là số chẵn, in ra `CHAN`. Ngược lại in ra `LE`.
* **Input:** Một số tự nhiên $N$ ($0 \le N \le 10^9$).
* **Output:** Chuỗi `CHAN` hoặc `LE`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `18` | `CHAN` |
  | `7` | `LE` |
* **Gợi ý thuật toán:** `if N % 2 == 0: print("CHAN") else: print("LE")`.

---

### Bài 2 (Cơ bản): Vé vào công viên (`PYA-L04-P02`)

* **Bối cảnh:** Ở công viên nước, các bạn nhỏ có chiều cao từ $130\text{ cm}$ trở lên phải mua vé người lớn (`VE NGUOI LON`), còn dưới $130\text{ cm}$ được mua vé trẻ em (`VE TRE EM`).
* **Yêu cầu:** Nhập vào chiều cao $h$ (cm) của bạn nhỏ. In ra loại vé tương ứng.
* **Input:** Một số nguyên $h$ ($1 \le h \le 200$).
* **Output:** `VE NGUOI LON` hoặc `VE TRE EM`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `135` | `VE NGUOI LON` |
  | `120` | `VE TRE EM` |

---

### Bài 3 (Cơ bản): Ai cao hơn? (`PYA-L04-P03`)

* **Bối cảnh:** Bạn Minh cao $a\text{ cm}$, bạn Nam cao $b\text{ cm}$. Biết chiều cao của hai bạn không bằng nhau.
* **Yêu cầu:** Hãy in ra tên của bạn cao hơn (`Minh` hoặc `Nam`).
* **Input:** Hai số tự nhiên $a$ và $b$ trên 2 dòng ($50 \le a, b \le 200, a \ne b$).
* **Output:** Tên bạn cao hơn.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `142`<br>`138` | `Minh` |

---

### Bài 4 (Cơ bản): Số lớn nhất trong hai số (`PYA-L04-P04`)

* **Yêu cầu:** Nhập vào hai số nguyên $a$ và $b$. Hãy in ra số lớn hơn trong hai số đó. Nếu hai số bằng nhau thì in ra giá trị đó.
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Một số nguyên là giá trị lớn nhất.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `-15`<br>`8` | `8` |

---

### Bài 5 (Cơ bản): Chia kẹo công bằng (`PYA-L04-P05`)

* **Bối cảnh:** Cô giáo có $a$ chiếc kẹo muốn chia đều cho $b$ bạn học sinh sao cho tất cả các bạn đều nhận được số kẹo bằng nhau và không còn thừa cái nào.
* **Yêu cầu:** Kiểm tra xem số kẹo có chia đều được hay không? Nếu chia đều được thì in `YES`, ngược lại in `NO`.
* **Input:** Hai số nguyên dương $a, b$ ($1 \le a, b \le 10^6$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `20`<br>`4` | `YES` | 20 chia hết cho 4, mỗi bạn 5 cái kẹo. |
  | `20`<br>`6` | `NO` | 20 không chia hết cho 6 (dư 2). |

---

### Bài 6 (Luyện tập): Điền phép tính lớn nhất (`PYA-L04-P06`)
*(Lấy cảm hứng từ Bài 1 Đề thi PYA tỉnh Bắc Giang)*

* **Bối cảnh:** Cho số tự nhiên $A$ và biểu thức sau: $A \text{ ? } A = B$.
* **Yêu cầu:** Hãy dùng một trong các phép tính $+$, $-$, $\times$ điền vào dấu $?$ để giá trị $B$ đạt được là **lớn nhất**. In ra số $B$ lớn nhất tìm được.
* **Input:** Một số tự nhiên $A$ ($0 \le A \le 100$).
* **Output:** Một số nguyên duy nhất là số $B$ lớn nhất.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3` | `9` | $3 + 3 = 6$, $3 - 3 = 0$, $3 \times 3 = 9$. Số lớn nhất là 9. |
  | `1` | `2` | $1 + 1 = 2$, $1 - 1 = 0$, $1 \times 1 = 1$. Số lớn nhất là 2! |
* **Gợi ý thuật toán:**
  * Chú ý bẫy: Với $A = 0$ hoặc $A = 1$, phép cộng $A + A$ lại cho kết quả lớn hơn phép nhân $A \times A$!
  * Tính 3 giá trị: `cong = A + A`, `tru = 0`, `nhan = A * A`.
  * Dùng lệnh: `print(max(cong, nhan))`.

---

### Bài 7 (Luyện tập): Giảm giá siêu thị (`PYA-L04-P07`)

* **Bối cảnh:** Siêu thị có chương trình khuyến mãi: Khách hàng mua đơn hàng có tổng giá trị từ $500$ nghìn đồng trở lên sẽ được giảm giá ngay $50$ nghìn đồng. Các đơn hàng dưới $500$ nghìn đồng giữ nguyên giá.
* **Yêu cầu:** Nhập vào tổng tiền đơn hàng $N$ (nghìn đồng). Hãy in ra số tiền thực tế khách hàng phải trả sau khi đã áp dụng khuyến mãi.
* **Input:** Một số nguyên dương $N$ ($1 \le N \le 10^6$).
* **Output:** Số tiền phải trả.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `620` | `570` | Được giảm 50 nghìn: $620 - 50 = 570$. |
  | `450` | `450` | Dưới 500 nghìn, không được giảm. |

---

### Bài 8 (Luyện tập): Cặp số bằng nhau hay khác? (`PYA-L04-P08`)

* **Yêu cầu:** Nhập vào 2 số nguyên $a$ và $b$. Hãy so sánh và in ra màn hình một trong ba thông báo:
  * `a LON HON b` (nếu $a > b$)
  * `a NHO HON b` (nếu $a < b$)
  * `HAI SO BANG NHAU` (nếu $a == b$)
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Một dòng thông báo theo đúng mẫu.

---

### Bài 9 (Luyện tập): Trị tuyệt đối của một số (`PYA-L04-P09`)

* **Bối cảnh:** Trị tuyệt đối $|N|$ của một số là khoảng cách từ số đó đến số 0 trên trục số:
  * Nếu $N \ge 0$, thì $|N| = N$.
  * Nếu $N < 0$, thì $|N| = -N$ (đổi dấu thành số dương).
* **Yêu cầu:** Nhập vào số nguyên $N$ (có thể là số âm). Không dùng hàm `abs()` có sẵn, hãy dùng cấu trúc `if - else` để in ra giá trị tuyệt đối của $N$.
* **Input:** Một số nguyên $N$ ($-10^9 \le N \le 10^9$).
* **Output:** Giá trị tuyệt đối của $N$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `-25` | `25` |
  | `10` | `10` |

---

### Bài 10 (Luyện tập): Bác thợ mộc cắt gỗ (`PYA-L04-P10`)

* **Bối cảnh:** Bác thợ mộc có một thanh gỗ dài $L\text{ cm}$. Bác cần cắt ra các đoạn gỗ nhỏ dài $K\text{ cm}$ để đóng bàn ghế.
* **Yêu cầu:**
  * Nếu thanh gỗ đủ dài để cắt được ít nhất một đoạn (nghĩa là $L \ge K$), hãy in ra số đoạn gỗ cắt được và phần gỗ thừa còn lại.
  * Nếu thanh gỗ quá ngắn ($L < K$), in ra chữ `KHONG DU`.
* **Input:** Hai số tự nhiên $L$ và $K$ trên 2 dòng ($1 \le L, K \le 10^9$).
* **Output:** Hai số cách nhau dấu cách `so_doan go_thua` hoặc in chữ `KHONG DU`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `17`<br>`5` | `3 2` |
  | `4`<br>`10` | `KHONG DU` |

---

### Bài 11 (Luyện tập): Cạnh thứ tư hình chữ nhật (`PYA-L04-P11`)
*(Lấy cảm hứng từ Bài 4 Đề thi THTA Khu vực Miền Bắc)*

* **Bối cảnh:** Một hình chữ nhật luôn có 4 cạnh tạo thành 2 cặp cạnh đối bằng nhau (2 chiều dài bằng nhau và 2 chiều rộng bằng nhau). Bạn Nam nhặt được 3 thanh gỗ có độ dài là $A, B, C$ và biết chắc chắn 3 thanh này là 3 cạnh của một hình chữ nhật.
* **Yêu cầu:** Em hãy tìm độ dài thanh gỗ thứ 4 còn thiếu để ghép vừa khít thành hình chữ nhật.
* **Input:** Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le A, B, C \le 1000$).
* **Output:** Độ dài cạnh thứ 4.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`5`<br>`3` | `5` | Đã có 2 cạnh bằng 3, vậy cạnh còn lại phải là 5. |
  | `8`<br>`6`<br>`8` | `6` | Cạnh còn lại là 6. |
* **Gợi ý thuật toán:**
  * Nếu $A == B$ thì cạnh còn lại là $C$.
  * Ngược lại nếu $A == C$ thì cạnh còn lại là $B$.
  * Ngược lại thì cạnh còn lại là $A$.
  *(Hoặc dùng phép XOR: `A ^ B ^ C`!)*

---

### Bài 12 (Vận dụng): Trò chơi oẳn tù tì (`PYA-L04-P12`)

* **Bối cảnh:** Hai bạn Tí và Tèo chơi trò Oẳn Tù Tì. Quy ước các lựa chọn bằng số:
  * `1`: Búa (Đấm)
  * `2`: Kéo
  * `3`: Bao (Lá)
* **Luật chơi:** Búa (1) thắng Kéo (2); Kéo (2) thắng Bao (3); Bao (3) thắng Búa (1). Nếu ra cùng số thì hòa nhau.
* **Yêu cầu:** Nhập vào lựa chọn của Tí và Tèo. Hãy in ra kết quả: `TI THANG`, `TEO THANG` hoặc `HOA`.
* **Input:** Hai số tự nhiên lần lượt là lựa chọn của Tí và Tèo ($1, 2, 3$).
* **Output:** `TI THANG`, `TEO THANG` hoặc `HOA`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1`<br>`2` | `TI THANG` | Tí ra Búa (1), Tèo ra Kéo (2) $\to$ Tí thắng. |
  | `1`<br>`3` | `TEO THANG` | Tí ra Búa (1), Tèo ra Bao (3) $\to$ Tèo thắng. |
  | `2`<br>`2` | `HOA` | Cả hai cùng ra Kéo. |

### Bài 13 (Cơ bản): Đèn giao thông ngã tư (`PYA-L05-P01`)

* **Yêu cầu:** Nhập vào một chữ cái in hoa đại diện cho màu đèn: `D` (Đỏ), `V` (Vàng), `X` (Xanh).
  * Nếu là `D`: in ra `DUNG LAI`.
  * Nếu là `V`: in ra `DI CHAM`.
  * Nếu là `X`: in ra `DUOC DI`.
* **Input:** Một ký tự `D`, `V` hoặc `X`.
* **Output:** Thông báo tương ứng.

---

### Bài 14 (Cơ bản): Dấu của số nguyên (`PYA-L05-P02`)

* **Yêu cầu:** Nhập vào số nguyên $N$. Hãy in ra:
  * `DUONG` nếu $N > 0$.
  * `AM` nếu $N < 0$.
  * `KHONG` nếu $N == 0$.
* **Input:** Một số nguyên $N$ ($-10^9 \le N \le 10^9$).
* **Output:** Chuỗi kết quả.

---

### Bài 15 (Cơ bản): Số lớn nhất trong ba số (`PYA-L05-P03`)

* **Yêu cầu:** Nhập vào 3 số nguyên $a, b, c$ mỗi số trên một dòng. Hãy tìm và in ra số có giá trị lớn nhất trong 3 số đó.
* **Input:** Ba số nguyên $a, b, c$ ($-10^9 \le a, b, c \le 10^9$).
* **Output:** Một số nguyên duy nhất là số lớn nhất.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `15`<br>`28`<br>`9` | `28` |
* **Gợi ý thuật toán:** `print(max(a, b, c))`.

---

### Bài 16 (Cơ bản): Xếp loại học lực (`PYA-L05-P04`)

* **Yêu cầu:** Nhập vào điểm trung bình môn Tin học của một bạn nhỏ (số thực $0.0 \le diem \le 10.0$).
  * Điểm $\ge 9.0$: in `XUAT SAC`.
  * Điểm $\ge 8.0$ và $< 9.0$: in `GIOI`.
  * Điểm $\ge 6.5$ và $< 8.0$: in `KHA`.
  * Điểm $< 6.5$: in `CAN CO GANG`.
* **Input:** Một số thực $diem$.
* **Output:** Xếp loại tương ứng.

---

### Bài 17 (Cơ bản): Vé gửi xe bến bãi (`PYA-L05-P05`)

* **Bối cảnh:** Bãi giữ xe thông minh quy định giá vé theo loại phương tiện:
  * Loại `1` (Xe đạp): giá $2$ nghìn đồng.
  * Loại `2` (Xe máy): giá $5$ nghìn đồng.
  * Loại `3` (Xe ô tô): giá $30$ nghìn đồng.
  * Các loại khác: in `LOI PHUONG TIEN`.
* **Input:** Một số nguyên mã loại xe.
* **Output:** Số tiền gửi xe hoặc chữ `LOI PHUONG TIEN`.

---

### Bài 18 (Luyện tập): Mario cứu công chúa (`PYA-L05-P06`)
*(Lấy cảm hứng từ Bài 3 Đề thi PYA Huyện Củ Chi - TP.HCM)*

* **Bối cảnh:** Mario có $K$ năng lượng, Công chúa có $P$ năng lượng. Chiếc cầu thang ngăn cách giữa hai người có đỉnh cao $N$ bậc: Mario đứng ở chân cầu thang bên trái (cần đi lên $N$ bậc và đi xuống $N$ bậc), Công chúa đứng ở chân cầu thang bên phải (cần đi lên $N$ bậc).
  * Mỗi bậc thang Mario đi tốn $1$ năng lượng.
  * Mỗi bậc thang Công chúa đi tốn $2$ năng lượng.
* **Yêu cầu:** Hỏi với mức năng lượng hiện có, Mario và Công chúa có thể gặp được nhau ở một điểm nào đó trên cầu thang hay không? Nếu gặp được in `YES`, ngược lại in `NO`.
* **Biết rằng:** Tổng số bậc cầu thang từ chân bên này sang chân bên kia là $2N$. Để gặp nhau, tổng số bậc mà Mario leo được cộng với tổng số bậc mà Công chúa leo được phải $\ge 2N$.
* **Input:** Ba số tự nhiên $K, P, N$ ($1 \le K, P, N \le 1000$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`3`<br>`2` | `YES` | Cầu thang $2N = 4$ bậc. Mario đi được $\min(3, 4) = 3$ bậc. Công chúa có 3 năng lượng đi được $3 // 2 = 1$ bậc. Tổng số bậc đi được là $3 + 1 = 4 \ge 4 \implies$ Gặp nhau! |
* **Gợi ý thuật toán:**
  * Bậc Mario đi được: `bac_mario = min(K, 2 * N)`
  * Bậc Công chúa đi được: `bac_cong_chua = min(P // 2, 2 * N)`
  * Nếu `bac_mario + bac_cong_chua >= 2 * N` in `YES`, ngược lại in `NO`.

---

### Bài 19 (Luyện tập): Tính cước taxi bậc thang (`PYA-L05-P07`)

* **Bối cảnh:** Hãng taxi "Rùa Con" tính cước đi xe như sau:
  * Giá mở cửa (cho $1\text{ km}$ đầu tiên): $10$ nghìn đồng.
  * Từ kilomet thứ 2 đến kilomet thứ 10: giá $8$ nghìn đồng mỗi km.
  * Từ kilomet thứ 11 trở đi: giá $6$ nghìn đồng mỗi km.
* **Yêu cầu:** Nhập vào số kilomet $N$ mà khách đã đi (số nguyên $N \ge 1$). Tính tổng số tiền cước (nghìn đồng).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 100$).
* **Output:** Tổng tiền cước taxi.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1` | `10` | Đúng 1 km đầu: 10 nghìn. |
  | `5` | `42` | 1 km đầu: 10k + 4 km tiếp theo: $4 \times 8 = 32$k $\implies 10 + 32 = 42$k. |
  | `12` | `94` | 1 km đầu (10k) + 9 km tiếp theo ($9 \times 8 = 72$k) + 2 km cuối ($2 \times 6 = 12$k) $\implies 10 + 72 + 12 = 94$k. |
* **Gợi ý thuật toán:** Dùng `if - elif - else` chia 3 nấc: $N = 1$, $1 < N \le 10$, và $N > 10$.

---

### Bài 20 (Luyện tập): Phân loại tam giác (`PYA-L05-P08`)

* **Bối cảnh:** Cho 3 số tự nhiên $a, b, c$ đã đảm bảo là độ dài 3 cạnh của một tam giác hợp lệ.
* **Yêu cầu:** Hãy phân loại tam giác đó:
  * Nếu 3 cạnh bằng nhau ($a == b == c$): in `TAM GIAC DEU`.
  * Nếu có 2 cạnh bằng nhau ($a == b$ hoặc $b == c$ hoặc $c == a$): in `TAM GIAC CAN`.
  * Các trường hợp còn lại: in `TAM GIAC THUONG`.
* **Input:** Ba số tự nhiên $a, b, c$ trên 3 dòng ($1 \le a, b, c \le 1000$).
* **Output:** Tên phân loại tam giác.

---

### Bài 21 (Luyện tập): Thuận đi tìm ánh đa vận tốc (`PYA-L05-P09`)
*(Lấy cảm hứng từ Bài 5 Đề thi PYA Huyện Từ Sơn)*

* **Bối cảnh:** Thuận đứng ở vị trí $x$, Ánh đứng ở vị trí $y$. Thuận đi về phía Ánh với vận tốc $v\text{ km/h}$.
* **Yêu cầu:** Hãy phân tích các tình huống:
  * Nếu $x == y$: in `DA GAP NHAU` (vì đang đứng cùng một chỗ).
  * Nếu $x \ne y$ nhưng $v == 0$: in `KHONG THE GAP` (vì Thuận đứng yên).
  * Nếu $x \ne y$ và $v > 0$:
    * Nếu khoảng cách $|y - x|$ chia hết cho $v$: in ra số giờ để gặp nhau.
    * Nếu không chia hết: in `GAP NHAU LE GIO`.
* **Input:** Ba số nguyên $x, y, v$ ($-10^9 \le x, y \le 10^9, 0 \le v \le 10^9$).
* **Output:** Thông báo tương ứng hoặc số giờ nguyên.

---

### Bài 22 (Luyện tập): Thứ mấy trong tuần? (`PYA-L05-P10`)

* **Bối cảnh:** Ngày mùng 1 tháng Giêng là ngày **Thứ Hai**.
* **Yêu cầu:** Cho biết ngày thứ $K$ trong năm đó là thứ mấy?
  * Biết rằng: ngày 1 là Thứ Hai, ngày 2 là Thứ Ba, ..., ngày 7 là Chủ Nhật, ngày 8 lại quay về Thứ Hai.
* **Input:** Một số tự nhiên $K$ ($1 \le K \le 365$).
* **Output:** In ra một trong các chuỗi: `THU HAI`, `THU BA`, `THU TU`, `THU NAM`, `THU SAU`, `THU BAY`, `CHU NHAT`.
* **Gợi ý thuật toán:** Tính số dư `du = K % 7`. Nếu `du == 1`: Thứ Hai, `du == 2`: Thứ Ba, ..., `du == 0`: Chủ Nhật.

---

### Bài 23 (Luyện tập): Cửa hàng bánh bột lọc khuyến mãi (`PYA-L05-P11`)

* **Bối cảnh:** Cửa hàng bánh bột lọc bán bánh với chương trình ưu đãi số lượng:
  * Mua dưới 10 cái: giá $5$ nghìn đồng/cái.
  * Mua từ 10 đến 49 cái: giá $4$ nghìn đồng/cái.
  * Mua từ 50 cái trở lên: giá chỉ còn $3$ nghìn đồng/cái.
* **Yêu cầu:** Nhập vào số lượng bánh $N$ mà khách muốn mua. Tính tổng số tiền khách phải trả.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** Tổng số tiền (nghìn đồng).

---

### Bài 24 (Vận dụng): Bốn mùa trong năm (`PYA-L05-P12`)

* **Bối cảnh:** Một năm có 12 tháng được chia thành 4 mùa:
  * **Mùa Xuân:** Tháng 1, 2, 3.
  * **Mùa Hạ (Hè):** Tháng 4, 5, 6.
  * **Mùa Thu:** Tháng 7, 8, 9.
  * **Mùa Đông:** Tháng 10, 11, 12.
* **Yêu cầu:** Nhập vào một số nguyên $M$.
  * Nếu $1 \le M \le 12$, hãy in ra tên mùa tương ứng (`XUAN`, `HA`, `THU`, `DONG`).
  * Nếu $M$ không nằm từ 1 đến 12, in ra `THANG KHONG HOP LE`.
* **Input:** Một số nguyên $M$ ($-100 \le M \le 100$).
* **Output:** Tên mùa hoặc thông báo lỗi.

### Bài 25 (Cơ bản): Số chẵn có hai chữ số (`PYA-L06-P01`)

* **Yêu cầu:** Nhập vào một số tự nhiên $N$. Kiểm tra xem $N$ có phải là **số chẵn có đúng hai chữ số** hay không? Nếu đúng in `YES`, ngược lại in `NO`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `24` | `YES` | 24 là số chẵn và có 2 chữ số. |
  | `8` | `NO` | 8 là số chẵn nhưng chỉ có 1 chữ số. |
  | `35` | `NO` | 35 có 2 chữ số nhưng là số lẻ. |
* **Gợi ý thuật toán:** `if (10 <= N <= 99) and (N % 2 == 0): print("YES") else: print("NO")`.

---

### Bài 26 (Cơ bản): Bội chung của 3 và 5 (`PYA-L06-P02`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$. Nếu $N$ chia hết cho cả 3 và 5 thì in `FIZZBUZZ`. Ngược lại in `KHONG`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** `FIZZBUZZ` hoặc `KHONG`.
* **Gợi ý:** `if N % 3 == 0 and N % 5 == 0: print("FIZZBUZZ") else: print("KHONG")`.

---

### Bài 27 (Cơ bản): Ngày nghỉ cuối tuần (`PYA-L06-P03`)

* **Bối cảnh:** Quy ước các ngày trong tuần bằng số: `2` (Thứ Hai), `3` (Thứ Ba), ..., `7` (Thứ Bảy), `8` (Chủ Nhật).
* **Yêu cầu:** Nhập vào một số nguyên $d$ đại diện cho một ngày. Nếu $d$ là Thứ Bảy hoặc Chủ Nhật thì in `NGHI HOC`, ngược lại in `DI HOC`.
* **Input:** Một số nguyên $d$ ($2 \le d \le 8$).
* **Output:** `NGHI HOC` hoặc `DI HOC`.
* **Gợi ý:** `if d == 7 or d == 8: print("NGHI HOC") else: print("DI HOC")`.

---

### Bài 28 (Cơ bản): Điểm nằm trong hình chữ nhật (`PYA-L06-P04`)

* **Bối cảnh:** Trong mặt phẳng tọa độ, một hình chữ nhật có góc dưới-trái tại $(0, 0)$ và góc trên-phải tại $(W, H)$.
* **Yêu cầu:** Nhập vào $W, H$ và tọa độ của một điểm $(x, y)$. Kiểm tra xem điểm $(x, y)$ có nằm bên trong hoặc trên mép biên của hình chữ nhật hay không? Nếu có in `TRONG`, ngược lại in `NGOAI`.
* **Input:** Bốn số tự nhiên $W, H, x, y$ trên 4 dòng ($1 \le W, H \le 1000, 0 \le x, y \le 1000$).
* **Output:** `TRONG` hoặc `NGOAI`.
* **Gợi ý:** `if (0 <= x <= W) and (0 <= y <= H): print("TRONG") else: print("NGOAI")`.

---

### Bài 29 (Cơ bản): Ba cạnh tam giác hợp lệ (`PYA-L06-P05`)
*(Lấy cảm hứng từ Bài 11 Đề thi PYA Toàn quốc)*

* **Yêu cầu:** Nhập vào 3 số tự nhiên $a, b, c$ trên 3 dòng. Kiểm tra xem 3 số này có thể tạo thành độ dài 3 cạnh của một tam giác hay không? Nếu có in `HOP LE`, ngược lại in `KHONG HOP LE`.
* **Input:** Ba số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^9$).
* **Output:** `HOP LE` hoặc `KHONG HOP LE`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`4`<br>`5` | `HOP LE` | $3+4>5$, $3+5>4$, $4+5>3$ đều đúng. |
  | `2`<br>`3`<br>`6` | `KHONG HOP LE` | $2 + 3 = 5 < 6$ (Sai bất đẳng thức tam giác). |

---

### Bài 30 (Luyện tập): Kiểm tra năm nhuận (`PYA-L06-P06`)

* **Yêu cầu:** Nhập vào một năm dương lịch $Y$. Hãy in ra `NAM NHUAN` nếu năm đó là năm nhuận, ngược lại in `NAM THUONG`.
* **Quy tắc:** Năm nhuận là năm chia hết cho 400, HOẶC chia hết cho 4 nhưng không chia hết cho 100.
* **Input:** Một số tự nhiên $Y$ ($1 \le Y \le 10^5$).
* **Output:** `NAM NHUAN` hoặc `NAM THUONG`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2024` | `NAM NHUAN` |
  | `1900` | `NAM THUONG` |
  | `2000` | `NAM NHUAN` |

---

### Bài 31 (Luyện tập): Số ngày trong tháng (`PYA-L06-P07`)
*(Lấy cảm hứng từ Bài 114, 115 Đề thi PYA Bắc Giang)*

* **Yêu cầu:** Nhập vào tháng $M$ ($1 \le M \le 12$) và năm $Y$ ($1 \le Y \le 10^5$). Hãy in ra số lượng ngày của tháng đó trong năm $Y$.
* **Biết rằng:**
  * Tháng 1, 3, 5, 7, 8, 10, 12 có đúng 31 ngày.
  * Tháng 4, 6, 9, 11 có đúng 30 ngày.
  * Tháng 2: có 29 ngày nếu $Y$ là năm nhuận, có 28 ngày nếu $Y$ là năm thường.
* **Input:** Hai dòng lần lượt là $M$ và $Y$.
* **Output:** Một số nguyên duy nhất là số ngày của tháng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2`<br>`2024` | `29` |
  | `2`<br>`2023` | `28` |
  | `4`<br>`2025` | `30` |

---

### Bài 32 (Luyện tập): Tam giác vuông hay không? (`PYA-L06-P08`)

* **Bối cảnh:** Theo định lý Pytago, tam giác có 3 cạnh $a, b, c$ là tam giác vuông nếu bình phương một cạnh bằng tổng bình phương hai cạnh còn lại ($a^2 + b^2 = c^2$ hoặc $a^2 + c^2 = b^2$ hoặc $b^2 + c^2 = a^2$).
* **Yêu cầu:** Cho 3 số dương $a, b, c$. Nếu chúng tạo thành một tam giác vuông thì in `VUONG`, ngược lại in `KHONG VUONG`.
* **Input:** Ba số nguyên $a, b, c$ ($1 \le a, b, c \le 10^4$).
* **Output:** `VUONG` hoặc `KHONG VUONG`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`4`<br>`5` | `VUONG` | $3^2 + 4^2 = 9 + 16 = 25 = 5^2$. |

---

### Bài 33 (Luyện tập): Rút thẻ may mắn (`PYA-L06-P09`)
*(Lấy cảm hứng từ Bài 113 Đề thi PYA Nghệ An – Khánh Hòa)*

* **Bối cảnh:** Trong hội chợ xuân, mỗi bạn nhỏ được bốc một chiếc thẻ có ghi một số tự nhiên $N$. Chiếc thẻ được coi là "Thẻ Trúng Thưởng" nếu:
  * Số $N$ chia hết cho 7, **HOẶC**
  * Số $N$ có chữ số tận cùng là 7.
* **Yêu cầu:** Nhập vào số $N$ trên thẻ. In ra `TRUNG THUONG` nếu trúng thưởng, ngược lại in `CHUC MAY MAN LAN SAU`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Thông báo tương ứng.
* **Gợi ý thuật toán:** `if N % 7 == 0 or N % 10 == 7: print("TRUNG THUONG")`.

---

### Bài 34 (Luyện tập): Ngày kế tiếp trong năm (`PYA-L06-P10`)

* **Bối cảnh:** Nhập vào một ngày hợp lệ gồm 3 số: ngày $D$, tháng $M$, năm $Y$.
* **Yêu cầu:** Hãy tính và in ra ngày, tháng, năm của **ngày kế tiếp ngay sau đó**.
* **Input:** Ba số tự nhiên $D, M, Y$ trên 3 dòng.
* **Output:** Ba số nguyên cách nhau một dấu cách `D_tiep M_tiep Y_tiep`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `31`<br>`12`<br>`2024` | `1 1 2025` | Ngày cuối năm chuyển sang ngày đầu năm mới! |
  | `28`<br>`2`<br>`2024` | `29 2 2024` | Năm 2024 là năm nhuận nên tháng 2 có ngày 29. |
  | `28`<br>`2`<br>`2023` | `1 3 2023` | Năm 2023 thường nên sau 28/2 là sang 1/3. |

---

### Bài 35 (Vận dụng): Cặp đôi cùng dấu hay trái dấu (`PYA-L06-P11`)

* **Yêu cầu:** Nhập vào hai số nguyên $a$ và $b$ (có thể âm, dương hoặc bằng 0).
  * In `CO SO KHONG` nếu có ít nhất một số bằng 0 ($a == 0$ hoặc $b == 0$).
  * In `CUNG DAU` nếu cả hai số cùng mang dấu dương hoặc cùng mang dấu âm ($a \times b > 0$).
  * In `TRAI DAU` nếu một số dương và một số âm ($a \times b < 0$).
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Thông báo theo quy định.

---

### Bài 36 (Thử thách): Giao nhau của hai đoạn thẳng (`PYA-L06-P12`)

* **Bối cảnh:** Trên trục số thực, đoạn thẳng thứ nhất nối từ điểm $L_1$ đến $R_1$ ($L_1 \le R_1$). Đoạn thẳng thứ hai nối từ điểm $L_2$ đến $R_2$ ($L_2 \le R_2$).
* **Yêu cầu:** Em hãy kiểm tra xem hai đoạn thẳng này có điểm chung (giao nhau) hay không?
  * Nếu có giao nhau: in ra `GIAO NHAU` và độ dài của đoạn giao nhau đó.
  * Nếu không giao nhau: in `KHONG GIAO NHAU`.
* **Input:** Bốn số nguyên $L_1, R_1, L_2, R_2$ trên 4 dòng ($-10^9 \le L_1 \le R_1 \le 10^9, -10^9 \le L_2 \le R_2 \le 10^9$).
* **Output:** `GIAO NHAU [do_dai]` hoặc `KHONG GIAO NHAU`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1`<br>`6`<br>`4`<br>`9` | `GIAO NHAU 2` | Đoạn giao nhau từ 4 đến 6, độ dài: $6 - 4 = 2$. |
  | `1`<br>`3`<br>`5`<br>`8` | `KHONG GIAO NHAU` | Hai đoạn rời nhau hoàn toàn. |
* **Gợi ý thuật toán:**
  * Điểm bắt đầu giao: `start = max(L1, L2)`
  * Điểm kết thúc giao: `end = min(R1, R2)`
  * Nếu `start <= end`: in `GIAO NHAU`, độ dài là `end - start`. Ngược lại in `KHONG GIAO NHAU`.


================================================================================
# CHƯƠNG 03: VÒNG LẶP
================================================================================


--------------------------------------------------------------------------------
<!-- Bài 05: lesson-05 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 05: Vòng lặp for và hàm range

## 1. Tóm tắt kiến thức trọng tâm
- Dùng khi **đã biết trước số lần lặp cụ thể**.
- Cú pháp: `for <bien> in range(start, stop, step):`
- Cận dừng `stop` không bao giờ được lấy tới (máy dừng ngay trước `stop`).
- **Mẫu tích lũy ống heo (Accumulator):** Khởi tạo `tong = 0` trước vòng lặp, mỗi lượt cộng dồn `tong += i`.

## 2. Bảng công thức ghi nhớ
| Cú pháp | Dãy số sinh ra |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, N + 1)` | `1, 2, 3, ..., N` |
| `range(2, N + 1, 2)` | Các số chẵn từ 2 đến $N$ |
| `range(N, 0, -1)` | Đếm lùi từ $N$ về 1 |

## 3. Mẫu code chuẩn
```python
# Tính tổng các số chẵn từ A đến B
a = int(input())
b = int(input())
tong = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        tong += i
print(tong)
```

## 4. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Hàm `range(5)` tạo ra dãy số gồm những số nào?
- **A.** `1, 2, 3, 4, 5`
- **B.** **[Đáp án đúng]** `0, 1, 2, 3, 4`
- **C.** `0, 1, 2, 3, 4, 5`
- **D.** `1, 2, 3, 4`
> *Giải thích:* Mặc định `range(N)` bắt đầu từ 0 và dừng trước $N$.

#### Câu 2: Để vòng lặp chạy đúng các giá trị `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`, ta viết:
- **A.** `range(1, 10)`
- **B.** **[Đáp án đúng]** `range(1, 11)`
- **C.** `range(0, 10)`
- **D.** `range(1, 10, 1)`
> *Giải thích:* Cận trên phải là $11$ thì vòng lặp mới chạy đến hết số $10$.

#### Câu 3: Đoạn code sau in ra màn hình bao nhiêu dòng?
```python
for i in range(4):
    print("Python")
```
- **A.** 3 dòng
- **B.** **[Đáp án đúng]** 4 dòng (ứng với $i = 0, 1, 2, 3$)
- **C.** 5 dòng
- **D.** Vô hạn dòng
> *Giải thích:* `range(4)` có 4 giá trị nên lệnh `print` chạy 4 lần.

#### Câu 4: Kết quả của đoạn code sau là gì?
```python
s = 0
for i in range(1, 4):
    s = s + i
print(s)
```
- **A.** `3`
- **B.** **[Đáp án đúng]** `6`
- **C.** `10`
- **D.** `0`
> *Giải thích:* $s = 0 + 1 + 2 + 3 = 6$.

#### Câu 5: Cú pháp nào sau đây in ra các số chẵn từ 2 đến 10?
- **A.** `range(2, 10)`
- **B.** **[Đáp án đúng]** `range(2, 11, 2)`
- **C.** `range(2, 10, 2)`
- **D.** `range(0, 10, 2)`
> *Giải thích:* Bắt đầu từ 2, bước nhảy 2, dừng trước 11 sẽ gồm: `2, 4, 6, 8, 10`.

#### Câu 6: Để đếm ngược từ 5 về 1, ta viết:
- **A.** `range(5, 1, -1)`
- **B.** **[Đáp án đúng]** `range(5, 0, -1)`
- **C.** `range(5, -1, 0)`
- **D.** `range(1, 5, -1)`
> *Giải thích:* Bắt đầu từ 5, dừng trước 0 với bước nhảy âm $-1$ sẽ ra: `5, 4, 3, 2, 1`.

#### Câu 7: Bẫy thụt lề: Đoạn code sau in ra gì?
```python
tong = 0
for i in range(1, 4):
    tong = tong + i
    print(tong)
```
- **A.** Chỉ in một số 6
- **B.** **[Đáp án đúng]** In 3 dòng lần lượt là: `1`, `3`, `6`
- **C.** In `0, 1, 3, 6`
- **D.** Báo lỗi
> *Giải thích:* Vì lệnh `print(tong)` bị thụt lề nằm BÊN TRONG vòng lặp `for`, nên sau mỗi bước lặp nó đều in ra giá trị hiện tại của `tong`.

#### Câu 8: Đoạn code sau in ra gì?
```python
for i in range(5, 5):
    print("Hello")
```
- **A.** In 1 chữ Hello
- **B.** In 5 chữ Hello
- **C.** **[Đáp án đúng]** Không in ra gì cả
- **D.** Báo lỗi
> *Giải thích:* `start = 5` và `stop = 5`, khoảng rỗng nên vòng lặp không chạy lần nào.

#### Câu 9: Trong vòng lặp `for i in range(1, 10):`, sau mỗi lần lặp, biến `i` tự động:
- **A.** Giữ nguyên giá trị
- **B.** **[Đáp án đúng]** Tự động tăng lên 1 đơn vị
- **C.** Tự động giảm đi 1 đơn vị
- **D.** Bị xóa khỏi bộ nhớ
> *Giải thích:* Bước nhảy mặc định của `range` là $+1$.

#### Câu 10: Vòng lặp `for` thường được dùng trong trường hợp nào?
- **A.** Khi không biết trước số lần lặp
- **B.** **[Đáp án đúng]** Khi đã biết trước số lần lặp cụ thể
- **C.** Khi muốn chương trình chạy mãi mãi không dừng
- **D.** Khi muốn chia lấy dư
> *Giải thích:* Vòng lặp `for` là vòng lặp với số lần biết trước (xác định bởi số phần tử của dãy).

#### Câu 11: Đoạn code tính giai thừa $3! = 1 \times 2 \times 3$ nào sau đây đúng?
- **A.** `tich = 0; for i in range(1, 4): tich = tich * i`
- **B.** **[Đáp án đúng]** `tich = 1; for i in range(1, 4): tich = tich * i`
- **C.** `tich = 1; for i in range(1, 3): tich = tich * i`
- **D.** `tich = 3 * 2 * 1`
> *Giải thích:* Tính tích bắt buộc biến khởi tạo phải là $1$. Nếu gán `tich = 0` thì $0$ nhân với số nào cũng bằng $0$!

#### Câu 12: Đoạn code sau in ra gì?
```python
dem = 0
for i in range(1, 11):
    if i % 2 != 0:
        dem = dem + 1
print(dem)
```
- **A.** `10`
- **B.** **[Đáp án đúng]** `5`
- **C.** `25`
- **D.** `4`
> *Giải thích:* Từ 1 đến 10 có đúng 5 số lẻ ($1, 3, 5, 7, 9$). Mỗi lần gặp số lẻ thì `dem` tăng 1, vậy kết quả là 5.

#### Câu 13: Giá trị của `i` sau khi kết thúc vòng lặp `for i in range(3): pass` là:
- **A.** `0`
- **B.** `1`
- **C.** **[Đáp án đúng]** `2`
- **D.** `3`
> *Giải thích:* Giá trị cuối cùng được gán cho `i` trong `range(3)` là số 2.

#### Câu 14: Biểu thức `range(10, 2, -2)` sinh ra những số nào?
- **A.** `10, 8, 6, 4, 2`
- **B.** **[Đáp án đúng]** `10, 8, 6, 4`
- **C.** `8, 6, 4, 2`
- **D.** `10, 9, 8`
> *Giải thích:* Dừng trước 2 nên chỉ lấy: $10, 8, 6, 4$.

#### Câu 15: Công thức tính nhanh tổng $1 + 2 + \dots + N$ trong toán học mà không cần dùng vòng lặp là:
- **A.** $N \times (N + 1)$
- **B.** **[Đáp án đúng]** $N \times (N + 1) // 2$
- **C.** $(N + 1) // 2$
- **D.** $N \times N // 2$
> *Giải thích:* Công thức tính tổng cấp số cộng Gauss: $S = \frac{N(N+1)}{2}$. Khi $N = 10^9$, dùng công thức này tính trong 0.00001s thay vì lặp $10^9$ lần!

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 05: Vòng lặp for và hàm range

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L07-P01` | Đếm sao lên trời | `Cơ bản` | $1 \le N \le 100$ | In các số từ 1 đến $N$ trên một dòng |
| 02 | `PYA-L07-P02` | Đếm ngược phóng tên lửa | `Cơ bản` | $1 \le N \le 100$ | Vòng lặp đếm lùi `range(N, 0, -1)` |
| 03 | `PYA-L07-P03` | Tổng các số tự nhiên | `Cơ bản` | $1 \le N \le 10^5$ | Kỹ thuật ống heo tích lũy tổng $1 + \dots + N$ |
| 04 | `PYA-L07-P04` | Bảng cửu chương | `Cơ bản` | $1 \le K \le 9$ | In bảng cửu chương của số $K$ |
| 05 | `PYA-L07-P05` | Tổng số chẵn trong đoạn | `Cơ bản` | $1 \le A \le B \le 10^4$ | Vòng lặp `range(A, B + 1)` kết hợp `if i % 2 == 0` |
| 06 | `PYA-L07-P06` | Đếm bội số của K | `Luyện tập` | $1 \le A \le B \le 10^5, 1 \le K \le 100$ | Đếm số lượng phần tử chia hết cho $K$ |
| 07 | `PYA-L07-P07` | Tính giai thừa $N!$ | `Luyện tập` | $1 \le N \le 20$ | Kỹ thuật tích lũy nhân `tich = tich * i` |
| 08 | `PYA-L07-P08` | Dãy số cách đều | `Luyện tập` | $1 \le a \le 100, 1 \le d \le 10, 1 \le n \le 100$ | In $n$ số hạng đầu tiên của cấp số cộng |
| 09 | `PYA-L07-P09` | Tìm ước số của N | `Luyện tập` | $1 \le N \le 10^4$ | Duyệt từ 1 đến $N$ tìm các số $N \% i == 0$ |
| 10 | `PYA-L07-P10` | Tổng bình phương | `Luyện tập` | $1 \le N \le 1000$ | Tính $S = 1^2 + 2^2 + \dots + N^2$ |
| 11 | `PYA-L07-P11` | Đọc sách mỗi ngày | `Luyện tập` | $1 \le N \le 10^4$ | Mô phỏng số trang sách đọc tăng dần (PYA Bảng A) |
| 12 | `PYA-L07-P12` | Hàng cột dấu sao | `Luyện tập` | $1 \le R, C \le 50$ | Vòng lặp lồng nhau in hình chữ nhật dấu `*` |
| 13 | `PYA-L07-P13` | Tam giác vuông dấu sao | `Vận dụng` | $1 \le N \le 50$ | In tam giác vuông chiều cao $N$ dòng |
| 14 | `PYA-L07-P14` | Tổng dãy siêu lớn không lặp | `Thử thách` | $1 \le N \le 10^9$ | Tối ưu thuật toán từ $\mathcal{O}(N)$ sang $\mathcal{O}(1)$ bằng công thức |

---

### Bài 1 (Cơ bản): Đếm sao lên trời (`PYA-L07-P01`)

* **Yêu cầu:** Nhập vào một số tự nhiên $N$. Hãy in các số từ $1$ đến $N$ trên cùng một dòng, mỗi số cách nhau một khoảng trắng.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 100$).
* **Output:** Dãy số từ 1 đến $N$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5` | `1 2 3 4 5` |
* **Gợi ý:** Dùng `for i in range(1, N + 1): print(i, end=" ")`.

---

### Bài 2 (Cơ bản): Đếm ngược phóng tên lửa (`PYA-L07-P02`)

* **Yêu cầu:** Trước khi phóng tàu vũ trụ, đồng hồ đếm ngược từ $N$ về 1, cuối cùng in ra chữ `PHONG!`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 20$).
* **Output:** Mỗi số trên một dòng, dòng cuối in `PHONG!`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `3` | `3`<br>`2`<br>`1`<br>`PHONG!` |
* **Gợi ý:** `for i in range(N, 0, -1): print(i)` rồi `print("PHONG!")`.

---

### Bài 3 (Cơ bản): Tổng các số tự nhiên (`PYA-L07-P03`)

* **Yêu cầu:** Nhập số nguyên dương $N$. Hãy tính tổng $S = 1 + 2 + 3 + \dots + N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^5$).
* **Output:** Một số nguyên duy nhất là tổng $S$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4` | `10` | $1 + 2 + 3 + 4 = 10$. |

---

### Bài 4 (Cơ bản): Bảng cửu chương (`PYA-L07-P04`)

* **Yêu cầu:** Nhập vào một số nguyên $K$ ($1 \le K \le 9$). Hãy in ra bảng cửu chương nhân của số $K$ từ 1 đến 10 theo đúng mẫu.
* **Input:** Một số nguyên $K$.
* **Output:** Gồm 10 dòng, mỗi dòng có định dạng: `K x i = [ket_qua]`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5` | `5 x 1 = 5`<br>`5 x 2 = 10`<br>...<br>`5 x 10 = 50` |

---

### Bài 5 (Cơ bản): Tổng số chẵn trong đoạn (`PYA-L07-P05`)

* **Yêu cầu:** Cho hai số nguyên dương $A$ và $B$ ($A \le B$). Hãy tính tổng tất cả các số chẵn nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$ nếu chúng là số chẵn).
* **Input:** Hai số tự nhiên $A$ và $B$ trên 2 dòng ($1 \le A \le B \le 10^4$).
* **Output:** Tổng các số chẵn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`8` | `18` | Các số chẵn là: 4, 6, 8. Tổng: $4 + 6 + 8 = 18$. |

---

### Bài 6 (Luyện tập): Đếm bội số của K (`PYA-L07-P06`)

* **Yêu cầu:** Nhập vào 3 số tự nhiên $A, B, K$ ($A \le B$). Hãy đếm xem có bao nhiêu số trong đoạn $[A, B]$ chia hết cho $K$.
* **Input:** Ba số $A, B, K$ trên 3 dòng ($1 \le A \le B \le 10^5, 1 \le K \le 100$).
* **Output:** Số lượng số chia hết cho $K$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1`<br>`10`<br>`3` | `3` | Gồm các số: 3, 6, 9. Tổng cộng 3 số. |

---

### Bài 7 (Luyện tập): Tính giai thừa $N!$ (`PYA-L07-P07`)

* **Bối cảnh:** Giai thừa của số tự nhiên $N$ (ký hiệu $N!$) là tích của tất cả các số tự nhiên từ 1 đến $N$:
  $$N! = 1 \times 2 \times 3 \times \dots \times N$$
* **Yêu cầu:** Nhập số tự nhiên $N$ ($1 \le N \le 20$). Hãy tính và in ra giá trị $N!$.
* **Input:** Một số tự nhiên $N$.
* **Output:** Giá trị $N!$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5` | `120` | $1 \times 2 \times 3 \times 4 \times 5 = 120$. |

---

### Bài 8 (Luyện tập): Dãy số cách đều (`PYA-L07-P08`)

* **Bối cảnh:** Một dãy số bắt đầu bằng số $a$, số tiếp theo hơn số đứng trước nó đúng $d$ đơn vị.
* **Yêu cầu:** Nhập vào số bắt đầu $a$, khoảng cách $d$ và số lượng phần tử cần in $n$. Hãy in ra $n$ số đầu tiên của dãy trên một dòng, cách nhau dấu cách.
* **Input:** Ba số tự nhiên $a, d, n$ ($1 \le a, d, n \le 100$).
* **Output:** Dãy số gồm $n$ phần tử.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2`<br>`3`<br>`5` | `2 5 8 11 14` |

---

### Bài 9 (Luyện tập): Tìm ước số của N (`PYA-L07-P09`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$. Hãy in ra tất cả các ước số dương của $N$ theo thứ tự tăng dần trên một dòng.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^4$).
* **Output:** Các ước số của $N$ cách nhau một dấu cách.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `12` | `1 2 3 4 6 12` |

---

### Bài 10 (Luyện tập): Tổng bình phương (`PYA-L07-P10`)

* **Yêu cầu:** Nhập vào số nguyên dương $N$. Hãy tính tổng:
  $$S = 1^2 + 2^2 + 3^2 + \dots + N^2$$
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** Một số nguyên duy nhất là tổng $S$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3` | `14` | $1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$. |

---

### Bài 11 (Luyện tập): Đọc sách mỗi ngày (`PYA-L07-P11`)
*(Lấy cảm hứng từ Bài 52 Đề thi Scratch PYA Toàn quốc)*

* **Bối cảnh:** Bạn Hoa quyết tâm rèn luyện thói quen đọc sách trong dịp hè. Cuốn sách có tổng cộng $N$ trang.
  * Ngày thứ nhất Hoa đọc được 1 trang.
  * Ngày thứ hai Hoa đọc được 2 trang.
  * Ngày thứ ba Hoa đọc được 3 trang.
  * Cứ như vậy, ngày thứ $k$ Hoa đọc được $k$ trang.
* **Yêu cầu:** Hỏi sau đúng bao nhiêu ngày thì Hoa sẽ đọc hết (hoặc vượt quá) $N$ trang của cuốn sách?
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^4$).
* **Output:** Số ngày ít nhất để Hoa đọc xong cuốn sách.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `4` | Ngày 1: 1 trang; ngày 2: 2 trang (tổng 3); ngày 3: 3 trang (tổng 6); ngày 4: 4 trang (tổng 10 $\ge 10$). Sau 4 ngày đọc xong. |
  | `11` | `5` | Sau 4 ngày mới đọc 10 trang, phải sang ngày thứ 5 mới đọc hết. |

---

### Bài 12 (Luyện tập): Hàng cột dấu sao (`PYA-L07-P12`)

* **Yêu cầu:** Nhập vào số hàng $R$ và số cột $C$. Hãy in ra một hình chữ nhật đặc gồm các dấu sao `*` có kích thước $R$ hàng và $C$ cột.
* **Input:** Hai số tự nhiên $R$ và $C$ ($1 \le R, C \le 50$).
* **Output:** Hình chữ nhật dấu `*`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `3`<br>`5` | `*****`<br>`*****`<br>`*****` |
* **Gợi ý:** `for i in range(R): print("*" * C)`.

---

### Bài 13 (Vận dụng): Tam giác vuông dấu sao (`PYA-L07-P13`)

* **Yêu cầu:** Nhập vào chiều cao $N$ của tam giác vuông. Hãy in ra tam giác vuông cân gồm các dấu sao theo mẫu:
  * Dòng 1 có 1 dấu `*`
  * Dòng 2 có 2 dấu `*`
  * ...
  * Dòng $N$ có $N$ dấu `*`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 50$).
* **Output:** Tam giác vuông dấu `*`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4` | `*`<br>`**`<br>`***`<br>`****` |

---

### Bài 14 (Thử thách): Tổng dãy siêu lớn không lặp (`PYA-L07-P14`)

* **Bối cảnh:** Trong kỳ thi Lập trình Python, ban giám khảo cho số $N$ cực lớn lên tới $10^9$ ($1$ tỷ). Nếu em dùng vòng lặp `for i in range(1, N + 1):` thì chương trình sẽ bị chạy quá thời gian quy định (Time Limit Exceeded - TLE) vì máy tính phải lặp 1 tỷ lần mất hơn 10 giây!
* **Yêu cầu:** Hãy tính tổng $S = 1 + 2 + \dots + N$ với thời gian chạy tức thì ($< 0.001$ giây) bằng công thức toán học.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** Giá trị tổng $S$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `1000000000` | `500000000500000000` |
* **Gợi ý thuật toán:** Áp dụng công thức Gauss: `S = N * (N + 1) // 2`. Nhờ Python tự động hỗ trợ số nguyên lớn, công thức này tính toán trong 1 phép tính duy nhất!


--------------------------------------------------------------------------------
<!-- Bài 06: lesson-06 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 06: Vòng lặp while và biến cờ

## 1. Tóm tắt kiến thức trọng tâm
- Dùng khi **chưa biết trước số lần lặp**, lặp trong khi điều kiện còn Đúng (`True`).
- Bắt buộc phải có câu lệnh làm thay đổi điều kiện lặp để không bị đơ máy (Infinite loop).
- **`break`:** Dừng và nhảy ra khỏi vòng lặp ngay lập tức.
- **`continue`:** Bỏ qua lần lặp hiện tại, chuyển sang lần lặp kế tiếp.
- **Biến cờ (Flag):** Biến kiểu `bool` (`True`/`False`) dùng đánh dấu phát hiện mục tiêu.

## 2. Mẫu code chuẩn
```python
# Nhập liên tiếp các số nguyên cho đến khi gặp số 0 thì dừng, đếm số lượng số đã nhập
dem = 0
while True:
    x = int(input())
    if x == 0:
        break
    dem += 1
print(dem)
```

---


## 3. Concept quiz: 14 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Vòng lặp `while` sẽ tiếp tục chạy khi nào?
- **A.** Khi điều kiện có giá trị là `False`
- **B.** **[Đáp án đúng]** Khi điều kiện có giá trị là `True`
- **C.** Chỉ chạy đúng 1 lần
- **D.** Khi gặp lệnh `break`
> *Giải thích:* `while` có nghĩa là "trong khi điều kiện còn đúng thì còn lặp".

#### Câu 2: Điều gì xảy ra nếu điều kiện trong `while` luôn luôn đúng và không có lệnh `break`?
- **A.** Chương trình tự động dừng sau 100 lần
- **B.** **[Đáp án đúng]** Bị lặp vô tận (Infinite Loop) khiến chương trình không bao giờ kết thúc
- **C.** Máy tính báo lỗi `SyntaxError`
- **D.** Tự động in ra số 0
> *Giải thích:* Vòng lặp không có lối thoát sẽ chạy mãi mãi.

#### Câu 3: Lệnh nào sau đây dùng để lập tức thoát khỏi vòng lặp `while`?
- **A.** `stop`
- **B.** `exit()`
- **C.** **[Đáp án đúng]** `break`
- **D.** `continue`
> *Giải thích:* Từ khóa `break` dùng để bẻ gãy và thoát ngay khỏi vòng lặp.

#### Câu 4: Đoạn code sau in ra màn hình bao nhiêu số?
```python
x = 1
while x < 5:
    print(x)
    x = x + 2
```
- **A.** 5 số
- **B.** **[Đáp án đúng]** 2 số (gồm số 1 và số 3)
- **C.** 4 số
- **D.** 3 số
> *Giải thích:* Lần 1: $x = 1$ in 1, tăng $x = 3$. Lần 2: $x = 3 < 5$ in 3, tăng $x = 5$. Khi $x = 5$, điều kiện $5 < 5$ bị sai nên dừng. In 2 số.

#### Câu 5: Lệnh `continue` trong vòng lặp có tác dụng gì?
- **A.** Thoát hoàn toàn khỏi chương trình
- **B.** Thoát khỏi vòng lặp
- **C.** **[Đáp án đúng]** Bỏ qua phần còn lại của lần lặp hiện tại và chuyển sang lần lặp tiếp theo
- **D.** Quay lại từ đầu chương trình
> *Giải thích:* `continue` bỏ qua các câu lệnh phía dưới nó trong thân vòng lặp hiện tại.

#### Câu 6: Đoạn code sau in ra giá trị cuối cùng của `k` là bao nhiêu?
```python
k = 10
while k > 0:
    k = k - 3
print(k)
```
- **A.** `1`
- **B.** `0`
- **C.** **[Đáp án đúng]** `-2`
- **D.** `3`
> *Giải thích:* Các giá trị của $k$: $10 \to 7 \to 4 \to 1 \to -2$. Khi $k = -2 \ngtr 0$ thì vòng lặp dừng, in ra $-2$.

#### Câu 7: Vòng lặp sau chạy bao nhiêu lần?
```python
while False:
    print("Python")
```
- **A.** 1 lần
- **B.** Vô tận lần
- **C.** **[Đáp án đúng]** 0 lần (Không chạy lần nào)
- **D.** Báo lỗi cú pháp
> *Giải thích:* Điều kiện là `False` ngay từ đầu nên người lính gác không cho vào vòng lặp lần nào.

#### Câu 8: Đoạn code nào sau đây nhập số từ bàn phím cho đến khi người dùng nhập số 0 thì dừng?
- **A.** `for i in range(0): input()`
- **B.** **[Đáp án đúng]** `while True: x = int(input()); if x == 0: break`
- **C.** `while x == 0: x = int(input())`
- **D.** `while x != 0: break`
> *Giải thích:* Mẫu `while True:` kết hợp với `if x == 0: break` là kỹ thuật nhập dữ liệu chuẩn mực.

#### Câu 9: Muốn gấp đôi số tiền $1000$ đồng cho đến khi số tiền vượt quá $10000$ đồng, ta dùng điều kiện `while` nào?
- **A.** `while tien > 10000:`
- **B.** **[Đáp án đúng]** `while tien <= 10000:`
- **C.** `while tien == 10000:`
- **D.** `while tien >= 1000:`
> *Giải thích:* Trong khi số tiền còn $\le 10000$ thì ta vẫn tiếp tục nhân đôi.

#### Câu 10: Đoạn code sau in ra gì?
```python
i = 0
while i < 3:
    i = i + 1
    if i == 2:
        continue
    print(i, end=" ")
```
- **A.** `1 2 3`
- **B.** `1 2`
- **C.** **[Đáp án đúng]** `1 3`
- **D.** `2 3`
> *Giải thích:* Khi $i = 2$, lệnh `continue` bỏ qua lệnh `print`, nên số 2 không được in.

#### Câu 11: Cho đoạn code sau:
```python
n = 123
dem = 0
while n > 0:
    n = n // 10
    dem = dem + 1
print(dem)
```
Kết quả in ra là gì?
- **A.** `0`
- **B.** `1`
- **C.** `2`
- **D.** **[Đáp án đúng]** `3`
> *Giải thích:* Đây là thuật toán đếm số lượng chữ số! $123 \to 12 \to 1 \to 0$. Lặp đúng 3 lần, đếm được 3 chữ số.

#### Câu 12: So sánh giữa `for` và `while`:
- **A.** `for` mạnh hơn `while`, làm được mọi bài toán mà `while` không làm được
- **B.** `while` không bao giờ dùng được cho dãy số
- **C.** **[Đáp án đúng]** Mọi bài toán dùng `for` đều có thể viết lại được bằng `while`
- **D.** Cả hai lệnh này bắt buộc phải dùng cùng nhau
> *Giải thích:* `while` là vòng lặp tổng quát, có thể mô phỏng lại mọi vòng lặp `for`.

#### Câu 13: Đoạn code sau có bị lặp vô tận không?
```python
x = 5
while x > 0:
    print(x)
    x = x + 1
```
- **A.** Không, nó dừng khi $x = 100$
- **B.** **[Đáp án đúng]** Có, vì $x$ ban đầu bằng 5 và càng ngày càng tăng, nên luôn luôn $> 0$
- **C.** Python tự động dừng sau 1 giây
- **D.** Báo lỗi `MemoryError`
> *Giải thích:* $x$ tăng dần $5, 6, 7, \dots$ nên điều kiện $x > 0$ mãi mãi đúng.

#### Câu 14: Biến cờ (flag) trong lập trình là gì?
- **A.** Một biến để vẽ lá cờ
- **B.** **[Đáp án đúng]** Một biến kiểu `bool` (`True`/`False`) dùng để đánh dấu một sự kiện đã xảy ra hay chưa
- **C.** Một lệnh dừng chương trình
- **D.** Tên một thư viện trong Python
> *Giải thích:* Biến Flag (ví dụ: `tim_thay = False`) dùng như một cột mốc đánh dấu trong vòng lặp.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 06: Vòng lặp while và biến cờ

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L08-P01` | Đếm xuôi bằng while | `Cơ bản` | $1 \le N \le 100$ | Cú pháp `while` cơ bản với biến tăng `i = i + 1` |
| 02 | `PYA-L08-P02` | Rút thăm đến khi trúng | `Cơ bản` | Dãy số kết thúc bằng 7 | Lặp cho đến khi gặp số mục tiêu |
| 03 | `PYA-L08-P03` | Nhập số đến khi gặp số 0 | `Cơ bản` | Số lượng phần tử $\le 1000$ | Đếm số lượng số đã nhập (PYA đà lạt) |
| 04 | `PYA-L08-P04` | Tổng dãy số kết thúc bằng 0 | `Cơ bản` | Mỗi số $\le 10^6$ | Tính tổng các số đã nhập trước khi gặp 0 |
| 05 | `PYA-L08-P05` | Đếm số chẵn đến khi gặp 0 | `Cơ bản` | Số nguyên $\le 10^6$ | Lọc và đếm số chẵn trong luồng nhập (PYA lâm đồng) |
| 06 | `PYA-L08-P06` | Gấp đôi tờ giấy lên mặt trăng | `Luyện tập` | $1 \le H \le 10^9$ | Đếm số lần nhân đôi $2 \times 2 \dots$ vượt ngưỡng $H$ |
| 07 | `PYA-L08-P07` | Ống heo mua xe máy | `Luyện tập` | $1 \le P \le 10^7$ | Tiết kiệm tiền mỗi ngày tăng dần đến khi đủ tiền (PYA) |
| 08 | `PYA-L08-P08` | Tìm lũy thừa của 2 lớn hơn N | `Luyện tập` | $1 \le N \le 10^9$ | Vòng lặp tìm số $2^k > N$ nhỏ nhất |
| 09 | `PYA-L08-P09` | Chú ốc sên leo cột cờ | `Luyện tập` | $1 \le H, A, B \le 10^6 (A > B)$ | Ban ngày leo lên $A$, ban đêm tụt $B$ đến đỉnh $H$ |
| 10 | `PYA-L08-P10` | Đếm số lượng chữ số của N | `Luyện tập` | $1 \le N \le 10^{18}$ | Kỹ thuật chia nguyên liên tiếp `N = N // 10` |
| 11 | `PYA-L08-P11` | Trò chơi đoán số nhị phân | `Vận dụng` | $1 \le N \le 10^6$ | Mô phỏng số bước đoán số tối đa $\log_2 N$ |
| 12 | `PYA-L08-P12` | Dãy số collatz (3n + 1) | `Vận dụng` | $1 \le N \le 10^6$ | Mô phỏng giả thuyết toán học collatz nổi tiếng |

---

### Bài 1 (Cơ bản): Đếm xuôi bằng while (`PYA-L08-P01`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$. Dùng vòng lặp `while`, hãy in ra các số từ $1$ đến $N$ trên một dòng.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 100$).
* **Output:** Dãy số từ 1 đến $N$.
* **Gợi ý:**
  ```python
  N = int(input())
  i = 1
  while i <= N:
      print(i, end=" ")
      i = i + 1
  ```

---

### Bài 2 (Cơ bản): Rút thăm đến khi trúng (`PYA-L08-P02`)

* **Bối cảnh:** Bé Bo bốc thăm từng lá phiếu có ghi số. Bo sẽ dừng lại ngay khi bốc trúng lá phiếu ghi số **7**.
* **Yêu cầu:** Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 7 thì dừng lại. Hãy in ra dòng chữ: `DA TRUNG THUONG!`
* **Input:** Một dãy các số nguyên, số cuối cùng chắc chắn là số 7.
* **Output:** In `DA TRUNG THUONG!` sau khi vòng lặp dừng.

---

### Bài 3 (Cơ bản): Nhập số đến khi gặp số 0 (`PYA-L08-P03`)
*(Lấy cảm hứng từ Bài 6 Đề thi PYA Đà Lạt - Lâm Đồng)*

* **Yêu cầu:** Viết chương trình nhập liên tiếp các số nguyên từ bàn phím. Việc nhập kết thúc khi người dùng nhập số 0. Hãy đếm xem người dùng đã nhập **bao nhiêu số** (không tính số 0 cuối cùng).
* **Input:** Một dãy các số nguyên, kết thúc bằng số 0.
* **Output:** Một số nguyên duy nhất là số lượng các số đã nhập trước số 0.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`12`<br>`8`<br>`0` | `3` | Có 3 số: 5, 12, 8 đã được nhập trước khi gặp 0. |

---

### Bài 4 (Cơ bản): Tổng dãy số kết thúc bằng 0 (`PYA-L08-P04`)

* **Yêu cầu:** Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 0. Hãy tính và in ra **tổng của tất cả các số** đã nhập.
* **Input:** Một dãy số nguyên kết thúc bằng 0.
* **Output:** Tổng các số.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`20`<br>`5`<br>`0` | `35` | $10 + 20 + 5 = 35$. |

---

### Bài 5 (Cơ bản): Đếm số chẵn đến khi gặp 0 (`PYA-L08-P05`)

* **Yêu cầu:** Nhập liên tiếp các số nguyên từ bàn phím cho đến khi nhập số 0. Hãy đếm xem có bao nhiêu số chẵn trong các số đã nhập (không tính số 0).
* **Input:** Dãy số nguyên kết thúc bằng 0.
* **Output:** Số lượng số chẵn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4`<br>`7`<br>`8`<br>`12`<br>`0` | `3` | Có 3 số chẵn là 4, 8, 12. |

---

### Bài 6 (Luyện tập): Gấp đôi tờ giấy lên mặt trăng (`PYA-L08-P06`)

* **Bối cảnh:** Một tờ giấy siêu mỏng ban đầu có độ dày là $1\text{ mm}$. Cứ mỗi lần gấp đôi tờ giấy lại, độ dày của nó lại tăng gấp đôi ($2\text{ mm}, 4\text{ mm}, 8\text{ mm}, \dots$).
* **Yêu cầu:** Hỏi cần phải gấp đôi tờ giấy ít nhất bao nhiêu lần để độ dày của nó đạt hoặc vượt quá độ cao $H\text{ mm}$?
* **Input:** Một số tự nhiên $H$ ($1 \le H \le 10^9$).
* **Output:** Số lần gấp đôi tối thiểu.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `4` | Lần 1: 2mm, lần 2: 4mm, lần 3: 8mm, lần 4: 16mm ($\ge 10$). Cần 4 lần. |

---

### Bài 7 (Luyện tập): Ống heo mua xe máy (`PYA-L08-P07`)
*(Lấy cảm hứng từ Bài 51 Đề thi Scratch PYA Toàn quốc)*

* **Bối cảnh:** Bác Nam muốn tiết kiệm tiền để mua một chiếc xe máy có giá $P$ nghìn đồng.
  * Ngày thứ nhất bác bỏ vào ống heo 1 nghìn đồng.
  * Ngày thứ hai bác bỏ vào 2 nghìn đồng.
  * Ngày thứ $k$ bác bỏ vào đúng $k$ nghìn đồng.
* **Yêu cầu:** Hỏi sau bao nhiêu ngày thì tổng số tiền trong ống heo của bác Nam đạt hoặc vượt quá $P$ nghìn đồng?
* **Input:** Một số tự nhiên $P$ ($1 \le P \le 10^7$).
* **Output:** Số ngày ít nhất.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `15` | `5` | Ngày 1: 1k, ngày 2: 2k (tổng 3k), ngày 3: 3k (tổng 6k), ngày 4: 4k (tổng 10k), ngày 5: 5k (tổng 15k $\ge 15$). Sau 5 ngày. |

---

### Bài 8 (Luyện tập): Tìm lũy thừa của 2 lớn hơn N (`PYA-L08-P08`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$. Hãy tìm số có dạng lũy thừa của 2 ($1, 2, 4, 8, 16, 32, \dots$) **nhỏ nhất mà lớn hơn $N$**.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Số lũy thừa của 2 tìm được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `16` | Lũy thừa của 2 gồm 1, 2, 4, 8, 16... Số nhỏ nhất $> 10$ là 16. |
  | `16` | `32` | Số phải lớn hơn 16 nên là 32. |

---

### Bài 9 (Luyện tập): Chú ốc sên leo cột cờ (`PYA-L08-P09`)

* **Bối cảnh:** Chú ốc sên muốn leo lên đỉnh một cột cờ cao $H$ mét.
  * Ban ngày, chú ốc sên bò lên được $A$ mét.
  * Ban đêm, khi ngủ chú bị tụt xuống $B$ mét ($B < A$).
  * Khi chú chạm tới hoặc vượt qua đỉnh cột cờ vào ban ngày, chú sẽ dừng lại và cắm cờ (không bị tụt nữa).
* **Yêu cầu:** Hỏi chú ốc sên mất bao nhiêu ngày để leo lên tới đỉnh cột cờ?
* **Input:** Ba số tự nhiên $H, A, B$ trên 3 dòng ($1 \le B < A \le H \le 10^6$).
* **Output:** Số ngày để ốc sên chạm đỉnh.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`3`<br>`1` | `2` | Ngày 1: leo lên 3m, đêm tụt 1m còn 2m.<br>Ngày 2: từ 2m leo thêm 3m lên 5m (chạm đỉnh ngay trong ngày!). Vậy mất 2 ngày. |

---

### Bài 10 (Luyện tập): Đếm số lượng chữ số của N (`PYA-L08-P10`)

* **Yêu cầu:** Nhập vào một số nguyên dương $N$. Dùng vòng lặp `while` và phép chia nguyên `// 10`, hãy đếm xem số $N$ có bao nhiêu chữ số.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** Số lượng chữ số của $N$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2026` | `4` |
* **Gợi ý thuật toán:**
  ```python
  N = int(input())
  dem = 0
  while N > 0:
      N = N // 10
      dem = dem + 1
  print(dem)
  ```

---

### Bài 11 (Vận dụng): Trò chơi đoán số nhị phân (`PYA-L08-P11`)

* **Bối cảnh:** Bạn An nghĩ ra một số bí mật từ 1 đến $N$. Bạn Bình dùng chiến thuật "Chặt đôi khoảng tìm kiếm" (Tìm kiếm nhị phân) để đoán số: Mỗi câu hỏi Bình chia đôi khoảng đang xét ($N = N // 2$).
* **Yêu cầu:** Hỏi trong trường hợp xấu nhất, Bình phải đoán **nhiều nhất bao nhiêu lần** thì chắc chắn tìm ra số của An (lặp cho đến khi khoảng chỉ còn 1 số: $N == 1$)?
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Số bước đoán tối đa.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `8` | `4` | Các bước: $8 \to 4 \to 2 \to 1$ (cần 4 bước). |

---

### Bài 12 (Vận dụng): Dãy số collatz (3n + 1) (`PYA-L08-P12`)

* **Bối cảnh:** Giả thuyết Collatz là một bài toán toán học kỳ bí: Bắt đầu từ số tự nhiên $N > 0$:
  * Nếu $N$ là số chẵn: chia đôi $N = N // 2$.
  * Nếu $N$ là số lẻ: nhân ba cộng một $N = 3 \times N + 1$.
  * Lặp lại quy trình trên cho đến khi số $N$ biến thành số $1$ thì dừng lại!
* **Yêu cầu:** Nhập vào số tự nhiên $N$. Hãy in ra số bước biến đổi để $N$ trở thành 1.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^5$).
* **Output:** Số bước biến đổi.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `6` | `8` | Dãy biến đổi: $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$ (qua 8 bước biến đổi). |


================================================================================
# CHƯƠNG 04: BÀI TOÁN SỐ HỌC
================================================================================


--------------------------------------------------------------------------------
<!-- Bài 07: lesson-07 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 07: Quy luật dãy số và tam giác số

## 1. Tóm tắt kiến thức trọng tâm
- **Cấp số cộng:** Số thứ $N$ của dãy có số đầu $u_1$ và khoảng cách $d$ là: $u_N = u_1 + (N - 1) 	\times d$.
- **Dãy Fibonacci:** $1, 1, 2, 3, 5, 8, 13, \dots$ Mỗi số bằng tổng 2 số liền trước. Áp dụng kỹ thuật cuốn chiếu: `a, b = b, a + b`.
- **Tam giác số:** Sử dụng 2 vòng lặp lồng nhau (vòng ngoài điều khiển số hàng, vòng trong điều khiển số cột).

## 2. Mẫu code chuẩn
```python
# In tam giác số tăng dần
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

## 3. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Dãy số $1, 1, 2, 3, 5, 8, 13, \dots$ mang tên nhà toán học nổi tiếng nào?
- **A.** Newton
- **B.** **[Đáp án đúng]** Fibonacci
- **C.** Pythagoras
- **D.** Archimedes
- > *Giải thích:* Đây là dãy số Fibonacci huyền thoại xuất hiện nhiều trong tự nhiên và đề thi lập trình Python.

#### Câu 2: Trong Python, câu lệnh `x, y = 10, 20` có ý nghĩa gì?
- **A.** `x` và `y` đều nhận giá trị 10
- **B.** Máy tính báo lỗi cú pháp
- **C.** **[Đáp án đúng]** `x` nhận giá trị 10 và `y` nhận giá trị 20
- **D.** `x` nhận giá trị 20 và `y` nhận giá trị 10
- > *Giải thích:* Phép gán đồng thời gán lần lượt biến theo thứ tự các giá trị ở vế phải.

#### Câu 3: Cho đoạn code sau:
```python
a = 5
b = 9
a, b = b, a
print(a, b)
```
Kết quả in ra là gì?
- **A.** `5 9`
- **B.** `5 5`
- **C.** **[Đáp án đúng]** `9 5`
- **D.** `9 9`
- > *Giải thích:* Câu lệnh `a, b = b, a` hoán đổi trực tiếp giá trị của 2 biến mà không cần biến phụ.

#### Câu 4: Cho `a = 2, b = 3`. Sau khi thực hiện lệnh `a, b = b, a + b`, giá trị mới của `a` và `b` là:
- **A.** `a = 2, b = 5`
- **B.** **[Đáp án đúng]** `a = 3, b = 5`
- **C.** `a = 5, b = 5`
- **D.** `a = 3, b = 6`
- > *Giải thích:* Giá trị ban đầu của $b$ là 3 (gán cho $a$). Giá trị ban đầu của $a+b$ là $2+3=5$ (gán cho $b$).

#### Câu 5: Số hạng thứ 7 của dãy Fibonacci (bắt đầu bằng $1, 1, 2, \dots$) là:
- **A.** 8
- **B.** 11
- **C.** **[Đáp án đúng]** 13
- **D.** 21
- > *Giải thích:* Các số hạng lần lượt là: $F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=13$.

#### Câu 6: Dãy số $3, 7, 11, 15, 19, \dots$ có công sai (khoảng cách giữa 2 số liền nhau) là bao nhiêu?
- **A.** 3
- **B.** **[Đáp án đúng]** 4
- **C.** 5
- **D.** 7
- > *Giải thích:* $7 - 3 = 4$, $11 - 7 = 4$. Đây là cấp số cộng có khoảng cách bằng 4.

#### Câu 7: Công thức tổng quát của số hạng thứ $n$ trong dãy cấp số cộng có số đầu $u_1$ và khoảng cách $d$ là:
- **A.** $u_n = u_1 + n \times d$
- **B.** **[Đáp án đúng]** $u_n = u_1 + (n - 1) \times d$
- **C.** $u_n = u_1 \times d$
- **D.** $u_n = (u_1 + d) \times n$
- > *Giải thích:* Để đi từ số thứ 1 đến số thứ $n$, ta cần nhảy thêm $(n-1)$ bước nhảy độ dài $d$.

#### Câu 8: Đoạn code sau in ra bao nhiêu dấu hoa thị `*`?
```python
for i in range(3):
    for j in range(2):
        print("*", end="")
```
- **A.** 3
- **B.** 5
- **C.** **[Đáp án đúng]** 6
- **D.** 2
- > *Giải thích:* Vòng lặp ngoài lặp 3 lần, mỗi lần vòng lặp trong chạy 2 lần. Tổng cộng: $3 \times 2 = 6$ lần.

#### Câu 9: Lệnh `print()` rỗng (không có tham số) ở cuối vòng lặp ngoài có tác dụng gì khi in ma trận?
- **A.** Xóa màn hình
- **B.** In ra khoảng trắng
- **C.** **[Đáp án đúng]** Xuống dòng mới
- **D.** Dừng chương trình
- > *Giải thích:* `print()` mặc định kết thúc bằng ký tự xuống dòng `\n`, giúp bắt đầu dòng mới cho hàng kế tiếp.

#### Câu 10: Đoạn code sau in ra hình gì?
```python
for i in range(1, 4):
    print("*" * i)
```
- **A.** Hình vuông $3 \times 3$
- **B.** **[Đáp án đúng]** Tam giác sao tăng dần
- **C.** 3 dòng giống hệt nhau
- **D.** Một hàng ngang duy nhất
- > *Giải thích:* Python hỗ trợ nhân chuỗi: `"*" * 1` là `*`, `"*" * 2` là `**`, `"*" * 3` là `***`.

#### Câu 11: Cho dãy số đan dấu: $1, -2, 3, -4, 5, -6, \dots$. Số thứ 10 của dãy là:
- **A.** 10
- **B.** **[Đáp án đúng]** -10
- **C.** -9
- **D.** 11
- > *Giải thích:* Các vị trí chẵn mang dấu trừ ($-$), số thứ 10 là vị trí chẵn nên là $-10$.

#### Câu 12: Tổng của dãy số đan dấu $S = 1 - 2 + 3 - 4 + \dots + 99 - 100$ bằng bao nhiêu?
- **A.** 0
- **B.** 50
- **C.** **[Đáp án đúng]** -50
- **D.** -100
- > *Giải thích:* Nhóm từng cặp: $(1-2) + (3-4) + \dots + (99-100) = (-1) \times 50 = -50$.

#### Câu 13: Khi giải bài toán tìm số thứ $N$ của dãy số trong phòng thi, nếu $N \le 10^5$ ta có thể dùng vòng lặp, nhưng nếu $N = 10^9$ ta nên ưu tiên điều gì?
- **A.** Chạy vòng lặp thật nhanh
- **B.** **[Đáp án đúng]** Tìm công thức toán học tính trực tiếp $\mathcal{O}(1)$
- **C.** Dùng máy tính mạnh hơn
- **D.** Bỏ qua bài toán
- > *Giải thích:* $10^9$ phép tính vòng lặp sẽ bị quá thời gian (TLE > 1s). Cần dùng công thức giải tích trực tiếp $\mathcal{O}(1)$.

#### Câu 14: Đoạn code sau in ra giá trị gì?
```python
s = 0
for i in range(1, 5):
    s = s + i * (i + 1)
print(s)
```
- **A.** 20
- **B.** 30
- **C.** **[Đáp án đúng]** 40
- **D.** 50
- > *Giải thích:* $1 \times 2 + 2 \times 3 + 3 \times 4 + 4 \times 5 = 2 + 6 + 12 + 20 = 40$.

#### Câu 15: Tam giác pascal hàng thứ 3 (coi hàng đầu là hàng 0: `1`, hàng 1: `1 1`, hàng 2: `1 2 1`) sẽ là:
- **A.** `1 2 2 1`
- **B.** **[Đáp án đúng]** `1 3 3 1`
- **C.** `1 4 4 1`
- **D.** `1 3 4 1`
- > *Giải thích:* Mỗi số bên trong bằng tổng 2 số liền kề ngay trên nó: $1$, $1+2=3$, $2+1=3$, $1$.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 07: Quy luật dãy số và tam giác số

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L09-P01` | Tráo đổi hai chiếc cốc | `Cơ bản` | $-10^9 \le A, B \le 10^9$ | Phép gán hoán đổi `a, b = b, a` |
| 02 | `PYA-L09-P02` | Dãy số nhân đôi | `Cơ bản` | $1 \le N \le 30$ | In dãy $1, 2, 4, 8, 16 \dots$ |
| 03 | `PYA-L09-P03` | Số hạng dãy cấp số cộng | `Cơ bản` | $N, u_1, d \le 10^6$ | Tìm số thứ $N$ của dãy cấp số cộng |
| 04 | `PYA-L09-P04` | Số Fibonacci thứ N | `Cơ bản` | $1 \le N \le 40$ | Thuật toán cuốn chiếu `a, b = b, a + b` |
| 05 | `PYA-L09-P05` | Dãy số đan dấu | `Cơ bản` | $1 \le N \le 10^6$ | Tính $S = 1 - 2 + 3 - 4 \dots \pm N$ |
| 06 | `PYA-L09-P06` | Tổng tích hai số liền nhau | `Luyện tập` | $1 \le N \le 10^5$ | Tính $S = 1\times 2 + 2\times 3 + \dots + N(N+1)$ |
| 07 | `PYA-L09-P07` | Dãy số bội ba bội năm | `Luyện tập` | $1 \le N \le 10^4$ | Dãy số chia hết cho 3 hoặc 5 tăng dần |
| 08 | `PYA-L09-P08` | Tam giác số đơn giản | `Luyện tập` | $1 \le N \le 20$ | Vòng lặp lồng nhau in tháp số tăng dần |
| 09 | `PYA-L09-P09` | Tam giác sao cân | `Luyện tập` | $1 \le N \le 20$ | Căn giữa khoảng trắng và in ký tự sao `*` |
| 10 | `PYA-L09-P10` | Dãy số tam giác (triangular numbers) | `Luyện tập` | $1 \le N \le 10^6$ | Số bi xếp thành tam giác đều $T_n = \frac{n(n+1)}{2}$ |
| 11 | `PYA-L09-P11` | Dãy số tribonacci | `Luyện tập` | $1 \le N \le 35$ | $T_n = T_{n-1} + T_{n-2} + T_{n-3}$ |
| 12 | `PYA-L09-P12` | Ma trận số bàn cờ đan xen | `Vận dụng` | $1 \le N \le 50$ | Ma trận $N \times N$ gồm các số 0 và 1 xen kẽ |
| 13 | `PYA-L09-P13` | Tam giác floyd | `Vận dụng` | $1 \le N \le 20$ | Điền liên tục các số tự nhiên vào tháp tam giác |
| 14 | `PYA-L09-P14` | Tìm vị trí trong dãy tự nhiên dài | `Thử thách` | $1 \le K \le 10^{12}$ | Tìm chữ số thứ $K$ khi viết $123456789101112\dots$ |

---

### Bài 1 (Cơ bản): Tráo đổi hai chiếc cốc (`PYA-L09-P01`)

* **Bối cảnh:** Bạn Bo có 2 chiếc cốc: cốc $A$ đựng nước cam và cốc $B$ đựng nước dưa hấu. Bo muốn đổi nội dung trong 2 cốc cho nhau.
* **Yêu cầu:** Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của chúng và in ra theo thứ tự $A$ trước, $B$ sau.
* **Input:** Hai số nguyên $A$ và $B$ trên một dòng, cách nhau bởi khoảng trắng.
* **Output:** Giá trị mới của $A$ và $B$ sau khi hoán đổi.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5 12` | `12 5` | Ban đầu $A=5, B=12$. Sau khi đổi $A=12, B=5$. |
* **Gợi ý:** Sử dụng cú pháp Python: `a, b = b, a`.

---

### Bài 2 (Cơ bản): Dãy số nhân đôi (`PYA-L09-P02`)

* **Yêu cầu:** Nhập số nguyên $N$ ($1 \le N \le 30$). Hãy in ra $N$ số đầu tiên của dãy số nhân đôi: $1, 2, 4, 8, 16, 32, \dots$ trên cùng một dòng.
* **Input:** Một số nguyên $N$.
* **Output:** Dãy $N$ số, cách nhau bởi dấu cách.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5` | `1 2 4 8 16` |

---

### Bài 3 (Cơ bản): Số hạng dãy cấp số cộng (`PYA-L09-P03`)

* **Yêu cầu:** Cho một dãy số cách đều có số đầu tiên là $u_1$ và khoảng cách giữa 2 số liền kề là $d$. Cho số nguyên dương $N$. Hãy tìm số hạng thứ $N$ của dãy số.
* **Input:** Ba số nguyên $u_1, d, N$ ($1 \le u_1, d, N \le 10^6$).
* **Output:** Một số nguyên là số hạng thứ $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3 4 5` | `19` | Dãy số là: 3, 7, 11, 15, 19. Số thứ 5 là 19. |
* **Công thức toán học:** $u_N = u_1 + (N - 1) \times d$.

---

### Bài 4 (Cơ bản): Số Fibonacci thứ N (`PYA-L09-P04`)

* **Yêu cầu:** Dãy Fibonacci được định nghĩa: $F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2}$ với $n \ge 3$. Nhập vào số tự nhiên $N$. Hãy tìm và in ra số Fibonacci thứ $N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 40$).
* **Output:** Giá trị $F_N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `6` | `8` | Dãy là 1, 1, 2, 3, 5, 8. Số thứ 6 là 8. |

---

### Bài 5 (Cơ bản): Dãy số đan dấu (`PYA-L09-P05`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tính tổng của dãy số đan dấu:
  $$S = 1 - 2 + 3 - 4 + 5 - 6 + \dots + (-1)^{N+1} N$$
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** Giá trị của tổng $S$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5` | `3` | $1 - 2 + 3 - 4 + 5 = 3$. |
  | `6` | `-3` | $1 - 2 + 3 - 4 + 5 - 6 = -3$. |

---

### Bài 6 (Luyện tập): Tổng tích hai số liền nhau (`PYA-L09-P06`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tính tổng:
  $$S = 1 \times 2 + 2 \times 3 + 3 \times 4 + \dots + N \times (N + 1)$$
* **Input:** Một số nguyên dương $N$ ($1 \le N \le 10^5$).
* **Output:** Tổng $S$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3` | `20` | $1 \times 2 + 2 \times 3 + 3 \times 4 = 2 + 6 + 12 = 20$. |

---

### Bài 7 (Luyện tập): Dãy số bội ba bội năm (`PYA-L09-P07`)

* **Yêu cầu:** Xét dãy các số nguyên dương chia hết cho 3 hoặc chia hết cho 5 theo thứ tự tăng dần: $3, 5, 6, 9, 10, 12, 15, \dots$. Cho số tự nhiên $N$. Hãy in ra $N$ số đầu tiên của dãy này.
* **Input:** Một số nguyên dương $N$ ($1 \le N \le 10^4$).
* **Output:** $N$ số đầu tiên của dãy trên một dòng, cách nhau bởi dấu cách.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `6` | `3 5 6 9 10 12` |

---

### Bài 8 (Luyện tập): Tam giác số đơn giản (`PYA-L09-P08`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$ ($1 \le N \le 20$). Hãy in ra tháp tam giác số có $N$ dòng theo quy luật:
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4` | `1`<br>`1 2`<br>`1 2 3`<br>`1 2 3 4` |

---

### Bài 9 (Luyện tập): Tam giác sao cân (`PYA-L09-P09`)

* **Yêu cầu:** Nhập vào độ cao $N$ của tam giác ($1 \le N \le 20$). Hãy in ra một tháp sao tam giác cân đối xứng hoàn hảo.
* **Quy luật:** Dòng thứ $i$ (từ 1 đến $N$) có $(N - i)$ dấu cách phía trước, tiếp theo là $(2i - 1)$ dấu sao `*`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `3` | `  *`<br>` ***`<br>`*****` |

---

### Bài 10 (Luyện tập): Dãy số tam giác (triangular numbers) (`PYA-L09-P10`)

* **Bối cảnh:** Người Hy Lạp cổ đại thường xếp các viên sỏi thành hình tam giác đều:
  * Tầng 1: 1 viên
  * Tầng 2: 1 + 2 = 3 viên
  * Tầng 3: 1 + 2 + 3 = 6 viên
  * Tầng 4: 1 + 2 + 3 + 4 = 10 viên
* **Yêu cầu:** Cho số tự nhiên $K$. Hãy kiểm tra xem $K$ có phải là một "Số tam giác" hay không (nghĩa là có tồn tại số nguyên dương $N$ sao cho $\frac{N(N+1)}{2} = K$)? Nếu có, in ra `YES` và số $N$, ngược lại in `NO`.
* **Input:** Một số nguyên $K$ ($1 \le K \le 10^9$).
* **Output:** `YES <N>` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `10` | `YES 4` |
  | `8` | `NO` |

---

### Bài 11 (Luyện tập): Dãy số tribonacci (`PYA-L09-P11`)

* **Yêu cầu:** Dãy Tribonacci mở rộng từ Fibonacci với 3 số đầu tiên là $1, 1, 2$. Kể từ số thứ tư, mỗi số bằng tổng của 3 số liền kề trước nó:
  $$T_1 = 1, T_2 = 1, T_3 = 2, \quad T_n = T_{n-1} + T_{n-2} + T_{n-3} \quad (n \ge 4)$$
  Nhập vào số tự nhiên $N$ ($1 \le N \le 35$). Hãy in ra số Tribonacci thứ $N$.
* **Input:** Một số nguyên $N$.
* **Output:** Giá trị $T_N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5` | `7` | Dãy là: 1, 1, 2, 4, 7... Số thứ 5 là $1+2+4=7$. |

---

### Bài 12 (Vận dụng): Ma trận số bàn cờ đan xen (`PYA-L09-P12`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$ ($1 \le N \le 50$). Hãy in ra một bảng ma trận vuông kích thước $N \times N$ gồm các số $0$ và $1$ xếp so le giống như các ô trên bàn cờ vua, với ô góc trên cùng bên trái luôn là số $1$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4` | `1 0 1 0`<br>`0 1 0 1`<br>`1 0 1 0`<br>`0 1 0 1` |
* **Gợi ý:** Ô tại dòng $i$, cột $j$ nhận giá trị $(i + j) \% 2 == 0 \implies 1$, ngược lại $\implies 0$ (nếu đánh số từ dòng 1, cột 1).

---

### Bài 13 (Vận dụng): Tam giác floyd (`PYA-L09-P13`)

* **Bối cảnh:** Tam giác Floyd là một tam giác số vuông được điền liên tiếp các số tự nhiên tăng dần bắt đầu từ 1.
* **Yêu cầu:** Nhập vào số nguyên dương $N$ ($1 \le N \le 20$). Hãy in ra tam giác Floyd có $N$ dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4` | `1`<br>`2 3`<br>`4 5 6`<br>`7 8 9 10` |
* **Gợi ý:** Dùng một biến đếm `dem = 1`. Mỗi khi in một số, tăng `dem += 1`.

---

### Bài 14 (Thử thách): Tìm vị trí trong dãy tự nhiên dài (`PYA-L09-P14`)
*(Đề thi Lập trình Python Quốc gia Bảng A)*

* **Bối cảnh:** Bé An viết liên tiếp các số tự nhiên bắt đầu từ 1 thành một dải số vô tận:
  `123456789101112131415161718192021...`
* **Yêu cầu:** Cho số nguyên dương $K$ ($1 \le K \le 10^5$). Hãy xác định chữ số thứ $K$ trong dải số trên là chữ số nào?
* **Input:** Một số nguyên $K$.
* **Output:** Chữ số tại vị trí $K$ (đếm từ 1).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `7` | `7` | Ký tự thứ 7 là số 7. |
  | `11` | `0` | Ký tự thứ 10 là '1', ký tự thứ 11 là '0' (của số 10). |


--------------------------------------------------------------------------------
<!-- Bài 08: lesson-08 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 08: Tách chữ số với chia nguyên và chia dư

## 1. Tóm tắt kiến thức trọng tâm
- Bản chất 2 nhịp vĩnh cửu:
  - `cs = n % 10`: Bóc chữ số hàng đơn vị.
  - `n = n // 10`: Cắt ngắn số đi 1 chữ số.
- Vòng lặp tách số: `while n > 0:`
- **Tạo số đảo ngược:** `dao = dao * 10 + cs`.
- **Số đối xứng (Palindrome):** Số đọc xuôi hay ngược đều giống nhau (`dao == n_goc`).

## 2. Mẫu code chuẩn
```python
# Kiểm tra số đối xứng
n = int(input())
n_goc = n
dao = 0

while n > 0:
    cs = n % 10
    dao = dao * 10 + cs
    n //= 10

if dao == n_goc:
    print("YES")
else:
    print("NO")
```

## 3. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Phép tính `456 % 10` cho kết quả là gì?
- **A.** 4
- **B.** 5
- **C.** **[Đáp án đúng]** 6
- **D.** 45
- > *Giải thích:* Phép chia dư `% 10` luôn trả về chữ số tận cùng (hàng đơn vị).

#### Câu 2: Phép tính `456 // 10` cho kết quả là gì?
- **A.** 6
- **B.** 4.56
- **C.** **[Đáp án đúng]** 45
- **D.** 45.6
- > *Giải thích:* Phép chia nguyên `// 10` cắt bỏ chữ số tận cùng bên phải.

#### Câu 3: Điều kiện dừng của vòng lặp tách chữ số của một số nguyên dương $N$ là gì?
- **A.** Khi `n == 1`
- **B.** **[Đáp án đúng]** Khi `n == 0` (hoặc vòng lặp `while n > 0` kết thúc)
- **C.** Khi `n % 10 == 0`
- **D.** Sau đúng 10 lần lặp
- > *Giải thích:* Khi $N$ bị chia nguyên liên tiếp cho 10 đến khi không còn chữ số nào ($N = 0$) thì dừng.

#### Câu 4: Số $N = 7$ khi thực hiện `7 // 10` sẽ nhận giá trị bằng bao nhiêu?
- **A.** 7
- **B.** **[Đáp án đúng]** 0
- **C.** 1
- **D.** 0.7
- > *Giải thích:* $7$ chia $10$ được thương nguyên là $0$, dư $7$.

#### Câu 5: Số nào sau đây là số đối xứng (palindrome)?
- **A.** 1234
- **B.** 1220
- **C.** **[Đáp án đúng]** 1221
- **D.** 1231
- > *Giải thích:* Số $1221$ đọc từ trái qua phải hay từ phải qua trái đều là $1221$.

#### Câu 6: Đoạn code sau thực hiện điều gì?
```python
dem = 0
while n > 0:
    dem += 1
    n //= 10
```
- **A.** Tính tổng các chữ số của $N$
- **B.** **[Đáp án đúng]** Đếm số lượng chữ số của $N$ (với $N > 0$)
- **C.** Đếm số chữ số chẵn của $N$
- **D.** Tìm chữ số lớn nhất của $N$
- > *Giải thích:* Cứ mỗi lần gọt bỏ 1 chữ số (`n //= 10`), biến `dem` tăng thêm 1.

#### Câu 7: Nếu nhập $N = 0$, đoạn code `while n > 0: dem += 1; n //= 10` sẽ cho kết quả `dem` bằng bao nhiêu?
- **A.** 1
- **B.** **[Đáp án đúng]** 0 (Bẫy số 0!)
- **C.** Báo lỗi
- **D.** Vô tận
- > *Giải thích:* Đây là bẫy kinh điển: Số 0 có 1 chữ số, nhưng điều kiện `0 > 0` bị sai ngay lập tức nên vòng lặp không chạy. Ta phải xử lý riêng nếu $N = 0$ thì `dem = 1`.

#### Câu 8: Muốn kiểm tra chữ số cuối cùng của $N$ có phải là số lẻ hay không, ta viết điều kiện nào?
- **A.** `n % 2 == 0`
- **B.** **[Đáp án đúng]** `(n % 10) % 2 != 0` (hoặc `n % 2 != 0`)
- **C.** `n // 10 % 2 != 0`
- **D.** `n % 10 == 1`
- > *Giải thích:* Một số nguyên lẻ thì chữ số tận cùng của nó cũng là số lẻ.

#### Câu 9: Cho $N = 305$. Tổng các chữ số của $N$ là:
- **A.** 35
- **B.** **[Đáp án đúng]** 8
- **C.** 15
- **D.** 3
- > *Giải thích:* $3 + 0 + 5 = 8$.

#### Câu 10: Đoạn code sau in ra màn hình giá trị gì?
```python
n = 8492
max_cs = 0
while n > 0:
    cs = n % 10
    if cs > max_cs:
        max_cs = cs
    n //= 10
print(max_cs)
```
- **A.** 8
- **B.** 4
- **C.** **[Đáp án đúng]** 9
- **D.** 2
- > *Giải thích:* Thuật toán tìm chữ số lớn nhất trong các chữ số 8, 4, 9, 2 $\implies$ Chữ số 9 lớn nhất.

#### Câu 11: Cho số nguyên dương $N = 12345$. Chữ số hàng chục của $N$ là kết quả của biểu thức nào?
- **A.** `(n % 100) // 10`
- **B.** `(n // 10) % 10`
- **C.** **[Đáp án đúng]** Cả A và B đều đúng
- **D.** `n % 10`
- > *Giải thích:* Cách A: $12345 \% 100 = 45 \implies 45 // 10 = 4$. Cách B: $12345 // 10 = 1234 \implies 1234 \% 10 = 4$. Cả 2 đều cho ra chữ số hàng chục 4.

#### Câu 12: Biểu thức `dao = dao * 10 + cs` với `dao = 35` và `cs = 7` sẽ cho giá trị `dao` mới là:
- **A.** 42
- **B.** 350
- **C.** **[Đáp án đúng]** 357
- **D.** 735
- > *Giải thích:* $35 \times 10 + 7 = 350 + 7 = 357$.

#### Câu 13: Một số tự nhiên được gọi là "toàn chẵn" khi nào?
- **A.** Khi số đó chia hết cho 2
- **B.** **[Đáp án đúng]** Khi TẤT CẢ các chữ số cấu tạo nên số đó đều là chữ số chẵn
- **C.** Khi chữ số đầu tiên là chẵn
- **D.** Khi tổng các chữ số là số chẵn
- > *Giải thích:* Định nghĩa số toàn chẵn (ví dụ: $2468$, $402$) là mọi chữ số của nó đều thuộc tập $\{0, 2, 4, 6, 8\}$.

#### Câu 14: Để kiểm tra số $N$ có toàn chữ số chẵn không, nếu gặp một chữ số `cs % 2 != 0`, ta nên làm gì?
- **A.** Tiếp tục kiểm tra
- **B.** **[Đáp án đúng]** Kết luận ngay là KHÔNG và dùng `break` để thoát vòng lặp
- **C.** Báo lỗi
- **D.** Trừ biến đếm
- > *Giải thích:* Chỉ cần phát hiện 1 chữ số lẻ duy nhất thì số đó lập tức vi phạm điều kiện "toàn chẵn".

#### Câu 15: Tại sao trong các bài toán tách chữ số, ta cần lưu `goc = n` trước khi chạy vòng lặp `while n > 0`?
- **A.** Để làm đẹp code
- **B.** **[Đáp án đúng]** Vì sau khi vòng lặp kết thúc, biến `n` đã bị gọt về $0$
- **C.** Vì Python bắt buộc phải có 2 biến
- **D.** Để tăng tốc độ chương trình
- > *Giải thích:* Vòng lặp thực hiện `n = n // 10` liên tục, khi kết thúc thì $n = 0$. Cần biến `goc` để lưu lại giá trị ban đầu so sánh với số đảo.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 08: Tách chữ số với chia nguyên và chia dư

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L10-P01` | Lấy chữ số đơn vị & chục | `Cơ bản` | $10 \le N \le 99$ | Thuần thục `% 10` và `// 10` với số 2 chữ số |
| 02 | `PYA-L10-P02` | Tổng chữ số của số 3 chữ số | `Cơ bản` | $100 \le N \le 999$ | Tách hàng trăm, chục, đơn vị |
| 03 | `PYA-L10-P03` | Tổng các chữ số của N | `Cơ bản` | $0 \le N \le 10^{18}$ | Vòng lặp `while n > 0` tính tổng chữ số |
| 04 | `PYA-L10-P04` | Đếm số lượng chữ số | `Cơ bản` | $0 \le N \le 10^{18}$ | Đếm số lượng chữ số có xử lý biên $N = 0$ |
| 05 | `PYA-L10-P05` | Tích các chữ số khác không | `Cơ bản` | $1 \le N \le 10^9$ | Bỏ qua chữ số 0 khi nhân dồn |
| 06 | `PYA-L10-P06` | Đếm chữ số chẵn và lẻ | `Luyện tập` | $1 \le N \le 10^{12}$ | Phân loại chẵn/lẻ cho từng chữ số |
| 07 | `PYA-L10-P07` | Chữ số lớn nhất & nhỏ nhất | `Luyện tập` | $1 \le N \le 10^{12}$ | Cập nhật `max` và `min` qua từng chữ số |
| 08 | `PYA-L10-P08` | Số đảo ngược | `Luyện tập` | $1 \le N \le 10^{12}$ | Thuật toán `dao = dao * 10 + cs` |
| 09 | `PYA-L10-P09` | Kiểm tra số đối xứng (palindrome) | `Luyện tập` | $1 \le N \le 10^{15}$ | So sánh số gốc và số đảo ngược |
| 10 | `PYA-L10-P10` | Số toàn chẵn hoặc toàn lẻ | `Luyện tập` | $1 \le N \le 10^{15}$ | Kiểm tra tính đồng nhất của toàn bộ chữ số |
| 11 | `PYA-L10-P11` | Số may mắn chứa số 7 | `Luyện tập` | $1 \le N \le 10^9$ | Kiểm tra sự tồn tại của một chữ số cụ thể |
| 12 | `PYA-L10-P12` | Đếm số lượng số đối xứng trong đoạn | `Vận dụng` | $1 \le A \le B \le 10^5$ | Kết hợp hàm kiểm tra số đối xứng trong đoạn $[A, B]$ |
| 13 | `PYA-L10-P13` | Căn bậc số học (digital root) | `Vận dụng` | $1 \le N \le 10^{18}$ | Tính tổng chữ số liên tục đến khi còn 1 chữ số |
| 14 | `PYA-L10-P14` | Số tăng giảm đẹp | `Thử thách` | $10 \le N \le 10^{12}$ | Kiểm tra các chữ số có tăng dần nghiêm ngặt từ trái qua phải |

---

### Bài 1 (Cơ bản): Lấy chữ số đơn vị & chục (`PYA-L10-P01`)

* **Yêu cầu:** Nhập một số nguyên dương $N$ có đúng 2 chữ số. Hãy in ra chữ số hàng chục và chữ số hàng đơn vị của $N$ trên cùng một dòng, cách nhau một khoảng trắng.
* **Input:** Một số nguyên $N$ ($10 \le N \le 99$).
* **Output:** Chữ số hàng chục, tiếp theo là chữ số hàng đơn vị.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `47` | `4 7` |
* **Gợi ý:** `chuc = n // 10`, `don_vi = n % 10`.

---

### Bài 2 (Cơ bản): Tổng chữ số của số 3 chữ số (`PYA-L10-P02`)

* **Yêu cầu:** Nhập một số nguyên dương $N$ có đúng 3 chữ số. Hãy tính tổng của 3 chữ số đó.
* **Input:** Một số tự nhiên $N$ ($100 \le N \le 999$).
* **Output:** Tổng 3 chữ số.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `358` | `16` | $3 + 5 + 8 = 16$. |

---

### Bài 3 (Cơ bản): Tổng các chữ số của N (`PYA-L10-P03`)

* **Yêu cầu:** Cho một số tự nhiên $N$ bất kỳ. Hãy tính tổng tất cả các chữ số cấu tạo nên số $N$.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^{18}$).
* **Output:** Tổng các chữ số của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `2024` | `8` | $2 + 0 + 2 + 4 = 8$. |
  | `0` | `0` | Chữ số 0 có tổng bằng 0. |

---

### Bài 4 (Cơ bản): Đếm số lượng chữ số (`PYA-L10-P04`)

* **Yêu cầu:** Cho số nguyên không âm $N$. Hãy cho biết số $N$ có bao nhiêu chữ số.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^{18}$).
* **Output:** Số lượng chữ số.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `123456` | `6` | Có 6 chữ số. |
  | `0` | `1` | Số 0 có đúng 1 chữ số. |
* **Lưu ý:** Chú ý xử lý trường hợp đặc biệt $N = 0$.

---

### Bài 5 (Cơ bản): Tích các chữ số khác không (`PYA-L10-P05`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tính tích của tất cả các chữ số **khác 0** của $N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Tích các chữ số khác 0.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `205` | `10` | Bỏ qua chữ số 0, tích là $2 \times 5 = 10$. |

---

### Bài 6 (Luyện tập): Đếm chữ số chẵn và lẻ (`PYA-L10-P06`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy đếm xem trong số $N$ có bao nhiêu chữ số chẵn (0, 2, 4, 6, 8) và bao nhiêu chữ số lẻ (1, 3, 5, 7, 9).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{12}$).
* **Output:** In hai số nguyên cách nhau một khoảng trắng: số lượng chữ số chẵn trước, số lượng chữ số lẻ sau.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `2035` | `2 2` | Chữ số chẵn: 2, 0 (2 số). Chữ số lẻ: 3, 5 (2 số). |

---

### Bài 7 (Luyện tập): Chữ số lớn nhất & nhỏ nhất (`PYA-L10-P07`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tìm chữ số lớn nhất và chữ số nhỏ nhất xuất hiện trong số $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^{12}$).
* **Output:** Chữ số lớn nhất, theo sau là chữ số nhỏ nhất, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `9418` | `9 1` | Chữ số lớn nhất là 9, nhỏ nhất là 1. |

---

### Bài 8 (Luyện tập): Số đảo ngược (`PYA-L10-P08`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy in ra số đảo ngược của $N$ (bỏ qua các chữ số 0 ở đầu nếu có sau khi đảo).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{12}$).
* **Output:** Số đảo ngược.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1234` | `4321` | Đảo ngược các chữ số. |
  | `2500` | `52` | Đảo ngược là 0052, giá trị số học là 52. |

---

### Bài 9 (Luyện tập): Kiểm tra số đối xứng (palindrome) (`PYA-L10-P09`)
*(Đề thi Python Bảng A)*

* **Bối cảnh:** Một số được gọi là số đối xứng (Palindrome) nếu đọc từ trái sang phải hay từ phải sang trái đều thu được số giống hệt nhau (ví dụ: $121$, $1331$, $5$, $88$).
* **Yêu cầu:** Nhập vào số tự nhiên $N$. Kiểm tra xem $N$ có phải số đối xứng không. Nếu có in `YES`, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^{15}$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `12321` | `YES` |
  | `1234` | `NO` |

---

### Bài 10 (Luyện tập): Số toàn chẵn hoặc toàn lẻ (`PYA-L10-P10`)

* **Bối cảnh:** Số "Toàn chẵn" là số mà mọi chữ số của nó đều là số chẵn. Số "Toàn lẻ" là số mà mọi chữ số của nó đều là số lẻ.
* **Yêu cầu:** Nhập số nguyên dương $N$. In ra `TOAN CHAN` nếu $N$ là số toàn chẵn, in `TOAN LE` nếu $N$ toàn lẻ, ngược lại in `BINH THUONG`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{15}$).
* **Output:** `TOAN CHAN`, `TOAN LE` hoặc `BINH THUONG`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2468` | `TOAN CHAN` |
  | `1395` | `TOAN LE` |
  | `2418` | `BINH THUONG` |

---

### Bài 11 (Luyện tập): Số may mắn chứa số 7 (`PYA-L10-P11`)

* **Yêu cầu:** Bé An coi số 7 là con số mang lại may mắn. Một số tự nhiên $N$ được gọi là "May mắn" nếu trong các chữ số của nó có ít nhất một chữ số 7. Cho số $N$, hãy kiểm tra xem $N$ có may mắn không. In `YES` nếu có, `NO` nếu không.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `372` | `YES` |
  | `2024` | `NO` |

---

### Bài 12 (Vận dụng): Đếm số lượng số đối xứng trong đoạn (`PYA-L10-P12`)

* **Yêu cầu:** Cho hai số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^5$). Hãy đếm xem có bao nhiêu số đối xứng nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số nguyên $A, B$ trên cùng một dòng.
* **Output:** Số lượng số đối xứng trong đoạn $[A, B]$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1 20` | `10` | Các số đối xứng là: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 (tổng cộng 10 số). |

---

### Bài 13 (Vận dụng): Căn bậc số học (digital root) (`PYA-L10-P13`)

* **Bối cảnh:** Căn bậc số học của một số tự nhiên là giá trị thu được sau khi cộng dồn liên tục các chữ số của nó cho đến khi chỉ còn lại đúng **một chữ số duy nhất**.
  Ví dụ: $9875 \to 9 + 8 + 7 + 5 = 29 \to 2 + 9 = 11 \to 1 + 1 = 2$. Căn bậc số học của 9875 là 2.
* **Yêu cầu:** Nhập vào số tự nhiên $N$. Hãy tìm căn bậc số học của $N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** Một chữ số duy nhất (từ 1 đến 9).
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `9875` | `2` |

---

### Bài 14 (Thử thách): Số tăng giảm đẹp (`PYA-L10-P14`)
*(Đề thi Lập trình Python cấp Tỉnh/Thành phố)*

* **Bối cảnh:** Một số tự nhiên được gọi là:
  * **Số tăng dần:** Nếu mỗi chữ số đứng sau luôn lớn hơn chữ số đứng trước nó (ví dụ: $1379, 258$).
  * **Số giảm dần:** Nếu mỗi chữ số đứng sau luôn nhỏ hơn chữ số đứng trước nó (ví dụ: $9641, 852$).
* **Yêu cầu:** Cho số $N$. In ra `TANG` nếu $N$ là số tăng dần, in `GIAM` nếu $N$ là số giảm dần, và in `KHONG` nếu không thỏa mãn cả 2 tính chất trên.
* **Input:** Một số nguyên $N$ ($10 \le N \le 10^{12}$).
* **Output:** `TANG`, `GIAM` hoặc `KHONG`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `1379` | `TANG` |
  | `9520` | `GIAM` |
  | `1335` | `KHONG` (Có hai chữ số 3 bằng nhau) |


--------------------------------------------------------------------------------
<!-- Bài 09: lesson-09 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 09: Ước số, bội số và số nguyên tố

## 1. Tóm tắt kiến thức trọng tâm
- Số nguyên tố là số $> 1$, chỉ có 2 ước là 1 và chính nó. Số 0 và 1 không phải là số nguyên tố. Số 2 là số nguyên tố chẵn duy nhất.
- **Thuật toán kiểm tra số nguyên tố tối ưu $\mathcal{O}(\sqrt{N})$:** Chỉ duyệt ước từ 2 đến $\lfloor\sqrt{N}
\rfloor$ (`int(n**0.5)`).
- **ƯCLN và BCNN:**
  ```python
  import math
  ucln = math.gcd(a, b)
  bcnn = (a * b) // ucln
  ```

## 2. Mẫu code chuẩn
```python
# Kiểm tra số nguyên tố
n = int(input())
la_nt = True
if n < 2:
    la_nt = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_nt = False
            break

print("YES" if la_nt else "NO")
```

## 3. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Số nào sau đây là số nguyên tố nhỏ nhất?
- **A.** 0
- **B.** 1
- **C.** **[Đáp án đúng]** 2
- **D.** 3
- > *Giải thích:* Số 2 là số nguyên tố nhỏ nhất và cũng là số nguyên tố chẵn duy nhất.

#### Câu 2: Số 1 có phải là số nguyên tố không?
- **A.** Có, vì 1 chỉ chia hết cho 1
- **B.** **[Đáp án đúng]** Không, vì định nghĩa số nguyên tố bắt buộc phải lớn hơn 1 (có đúng 2 ước phân biệt)
- **C.** Tùy trường hợp
- **D.** Số 1 là số nguyên tố đặc biệt
- > *Giải thích:* Bẫy kinh điển: Số 1 chỉ có đúng 1 ước duy nhất là chính nó nên không phải số nguyên tố.

#### Câu 3: Số 9 có bao nhiêu ước số tự nhiên?
- **A.** 2
- **B.** **[Đáp án đúng]** 3 (gồm 1, 3, 9)
- **C.** 4
- **D.** 1
- > *Giải thích:* Các ước của 9 là 1, 3, 9.

#### Câu 4: Một số tự nhiên có số lượng ước số là một số lẻ thì số đó chắc chắn là:
- **A.** Số lẻ
- **B.** Số nguyên tố
- **C.** **[Đáp án đúng]** Số chính phương
- **D.** Số chẵn
- > *Giải thích:* Các ước thường đi theo cặp $(d, N/d)$. Chỉ có số chính phương khi gặp căn bậc 2 thì $d = N/d$ ghép thành 1 ước đơn, tạo thành số lượng ước lẻ.

#### Câu 5: Số nào sau đây không phải là số nguyên tố?
- **A.** 11
- **B.** 13
- **C.** **[Đáp án đúng]** 15
- **D.** 17
- > *Giải thích:* Số 15 chia hết cho 1, 3, 5, 15 (có 4 ước).

#### Câu 6: Trong Python, để tìm ước chung lớn nhất của 2 số `a` và `b`, ta dùng thư viện nào?
- **A.** `import random`
- **B.** `import time`
- **C.** **[Đáp án đúng]** `import math` và dùng `math.gcd(a, b)`
- **D.** `import turtle`
- > *Giải thích:* `gcd` là viết tắt của Greatest Common Divisor trong thư viện `math`.

#### Câu 7: Bội chung nhỏ nhất (bcnn / lcm) của 2 số $A$ và $B$ liên hệ với ưcln thế nào?
- **A.** $\text{LCM} = A + B - \text{GCD}$
- **B.** **[Đáp án đúng]** $\text{LCM} = (A \times B) // \text{GCD}(A, B)$
- **C.** $\text{LCM} = A \times B \times \text{GCD}$
- **D.** $\text{LCM} = A \times B$
- > *Giải thích:* Tích của hai số bằng tích của ƯCLN và BCNN của chúng: $A \times B = \text{GCD} \times \text{LCM}$.

#### Câu 8: Điều kiện để một số $i$ là ước số của $N$ trong Python được viết là:
- **A.** `n / i == 0`
- **B.** `n // i == 0`
- **C.** **[Đáp án đúng]** `n % i == 0`
- **D.** `i % n == 0`
- > *Giải thích:* Phép chia dư bằng 0 biểu thị phép chia hết.

#### Câu 9: Ước số lớn nhất của số $N$ (với $N > 0$) luôn luôn bằng:
- **A.** $N - 1$
- **B.** **[Đáp án đúng]** Chính nó ($N$)
- **C.** 1
- **D.** $N // 2$
- > *Giải thích:* Mọi số tự nhiên $N > 0$ đều chia hết cho chính nó, và không thể chia hết cho số nào lớn hơn $N$.

#### Câu 10: Ước số dương nhỏ nhất của mọi số tự nhiên $N > 0$ luôn luôn là:
- **A.** 0
- **B.** **[Đáp án đúng]** 1
- **C.** 2
- **D.** Chính nó
- > *Giải thích:* Mọi số tự nhiên đều chia hết cho 1.

#### Câu 11: Có bao nhiêu số nguyên tố nằm trong khoảng từ 1 đến 10?
- **A.** 3
- **B.** **[Đáp án đúng]** 4 (gồm 2, 3, 5, 7)
- **C.** 5
- **D.** 2
- > *Giải thích:* Có 4 số nguyên tố là 2, 3, 5, 7.

#### Câu 12: Để tối ưu hóa thuật toán kiểm tra số nguyên tố $N$, ta chỉ cần cho vòng lặp kiểm tra ước số chạy đến đâu?
- **A.** Đến $N - 1$
- **B.** Đến $N // 2$
- **C.** **[Đáp án đúng]** Đến $\sqrt{N}$ (căn bậc 2 của $N$, tức là `int(n**0.5)`)
- **D.** Đến 100
- > *Giải thích:* Nếu $N$ có ước lớn hơn $\sqrt{N}$ thì chắc chắn phải có ước tương ứng nhỏ hơn $\sqrt{N}$.

#### Câu 13: Đoạn code sau in ra kết quả gì?
```python
n = 16
can = int(n ** 0.5)
if can * can == n:
    print("YES")
else:
    print("NO")
```
- **A.** NO
- **B.** **[Đáp án đúng]** YES
- **C.** Báo lỗi
- **D.** 4
- > *Giải thích:* $16 = 4^2$ là một số chính phương nên in ra YES.

#### Câu 14: Hai số được gọi là "nguyên tố cùng nhau" khi nào?
- **A.** Cả hai số đều là số nguyên tố
- **B.** **[Đáp án đúng]** Ước chung lớn nhất của chúng bằng 1 (`math.gcd(a, b) == 1`)
- **C.** Hai số bằng nhau
- **D.** Tổng của chúng là số nguyên tố
- > *Giải thích:* Định nghĩa 2 số nguyên tố cùng nhau (ví dụ: 8 và 9, dù cả 8 và 9 đều là hợp số nhưng $\text{gcd}(8, 9) = 1$).

#### Câu 15: Một học sinh viết kiểm tra số nguyên tố và bỏ qua trường hợp `n < 2`. Khi người chấm thi nhập vào `n = 1`, chương trình sẽ cho kết quả sai là:
- **A.** Báo lỗi cú pháp
- **B.** **[Đáp án đúng]** Nhận nhầm 1 là số nguyên tố
- **C.** In ra không xác định
- **D.** Lặp vô tận
- > *Giải thích:* Vì vòng lặp `range(2, 1)` sẽ không chạy lần nào, cờ `la_nguyen_to` vẫn giữ nguyên là `True`, dẫn đến kết luận sai rằng 1 là số nguyên tố!

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 09: Ước số, bội số và số nguyên tố

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L11-P01` | Liệt kê tất cả ước số | `Cơ bản` | $1 \le N \le 1000$ | Vòng lặp `for` kiểm tra `N % i == 0` |
| 02 | `PYA-L11-P02` | Đếm số lượng ước số | `Cơ bản` | $1 \le N \le 10^5$ | Đếm số ước của $N$ |
| 03 | `PYA-L11-P03` | Tính tổng các ước số | `Cơ bản` | $1 \le N \le 10^5$ | Cộng dồn các ước số |
| 04 | `PYA-L11-P04` | Kiểm tra số nguyên tố | `Cơ bản` | $0 \le N \le 10^7$ | Thuật toán kiểm tra số nguyên tố chuẩn |
| 05 | `PYA-L11-P05` | Kiểm tra số chính phương | `Cơ bản` | $1 \le N \le 10^9$ | Kiểm tra $N = K^2$ |
| 06 | `PYA-L11-P06` | Ước chung lớn nhất & bcnn | `Luyện tập` | $1 \le A, B \le 10^9$ | Dùng `math.gcd` và công thức bcnn |
| 07 | `PYA-L11-P07` | Đếm ước chẵn của N | `Luyện tập` | $1 \le N \le 10^6$ | Kết hợp `N % i == 0 and i % 2 == 0` |
| 08 | `PYA-L11-P08` | Tìm ước số lớn thứ hai | `Luyện tập` | $2 \le N \le 10^9$ | Tìm ước thực sự lớn nhất khác $N$ |
| 09 | `PYA-L11-P09` | Đếm số nguyên tố trong đoạn | `Luyện tập` | $1 \le A \le B \le 10^4$ | Vòng lặp lồng hoặc hàm đếm số nguyên tố |
| 10 | `PYA-L11-P10` | Hai số nguyên tố cùng nhau | `Luyện tập` | $1 \le A, B \le 10^9$ | Kiểm tra $\text{gcd}(A, B) == 1$ |
| 11 | `PYA-L11-P11` | Cặp số nguyên tố sinh đôi | `Luyện tập` | $1 \le N \le 10^4$ | Tìm các cặp số nguyên tố $(P, P+2) \le N$ |
| 12 | `PYA-L11-P12` | Số siêu nguyên tố (super prime) | `Vận dụng` | $10 \le N \le 10^6$ | Cắt dần bên phải vẫn là số nguyên tố |
| 13 | `PYA-L11-P13` | Phân tích ra thừa số nguyên tố | `Vận dụng` | $2 \le N \le 10^6$ | Phân tích $N = p_1^{a_1} \times p_2^{a_2} \dots$ |
| 14 | `PYA-L11-P14` | Tìm số có đúng 3 ước số | `Thử thách` | $1 \le N \le 10^9$ | Nhận diện bản chất số $P^2$ với $P$ là nguyên tố |

---

### Bài 1 (Cơ bản): Liệt kê tất cả ước số (`PYA-L11-P01`)

* **Yêu cầu:** Nhập một số tự nhiên $N$. Hãy in ra tất cả các ước số nguyên dương của $N$ theo thứ tự tăng dần trên một dòng, cách nhau bởi khoảng trắng.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** Dãy các ước số của $N$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `12` | `1 2 3 4 6 12` |

---

### Bài 2 (Cơ bản): Đếm số lượng ước số (`PYA-L11-P02`)

* **Yêu cầu:** Cho số tự nhiên $N$. Hãy cho biết số $N$ có tất cả bao nhiêu ước số nguyên dương.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^5$).
* **Output:** Một số nguyên duy nhất là số lượng ước số của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `4` | Số 10 có 4 ước: 1, 2, 5, 10. |

---

### Bài 3 (Cơ bản): Tính tổng các ước số (`PYA-L11-P03`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tính tổng tất cả các ước số của $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^5$).
* **Output:** Tổng các ước số của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `6` | `12` | Các ước là 1, 2, 3, 6 $\implies 1 + 2 + 3 + 6 = 12$. |

---

### Bài 4 (Cơ bản): Kiểm tra số nguyên tố (`PYA-L11-P04`)
*(Bài toán nền tảng thi Lập trình Python)*

* **Yêu cầu:** Nhập vào số nguyên $N$. Hãy kiểm tra xem $N$ có phải là số nguyên tố hay không. Nếu có in `YES`, nếu không in `NO`.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^7$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `7` | `YES` |
  | `1` | `NO` |
  | `9` | `NO` |

---

### Bài 5 (Cơ bản): Kiểm tra số chính phương (`PYA-L11-P05`)

* **Bối cảnh:** Số chính phương là số bằng bình phương của một số tự nhiên (ví dụ: $0, 1, 4, 9, 16, 25, \dots$).
* **Yêu cầu:** Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số chính phương không. Nếu đúng in `YES`, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `25` | `YES` |
  | `20` | `NO` |

---

### Bài 6 (Luyện tập): Ước chung lớn nhất & bcnn (`PYA-L11-P06`)

* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$. Hãy tìm Ước chung lớn nhất ($\text{GCD}$) và Bội chung nhỏ nhất ($\text{LCM}$) của 2 số này.
* **Input:** Hai số nguyên $A, B$ cách nhau bởi khoảng trắng ($1 \le A, B \le 10^9$).
* **Output:** Hai số nguyên: $\text{GCD}$ trước, $\text{LCM}$ sau, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12 18` | `6 36` | $\text{GCD}(12, 18) = 6$, $\text{LCM}(12, 18) = (12 \times 18) // 6 = 36$. |

---

### Bài 7 (Luyện tập): Đếm ước chẵn của N (`PYA-L11-P07`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy đếm xem có bao nhiêu ước số của $N$ là số chẵn.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^6$).
* **Output:** Số lượng ước chẵn của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12` | `4` | Các ước của 12 là: 1, 2, 3, 4, 6, 12. Trong đó các ước chẵn là: 2, 4, 6, 12 (có 4 số). |

---

### Bài 8 (Luyện tập): Tìm ước số lớn thứ hai (`PYA-L11-P08`)

* **Yêu cầu:** Cho số nguyên dương $N$ ($N \ge 2$). Ước số lớn nhất của $N$ luôn là chính nó ($N$). Hãy tìm ước số lớn thứ hai của $N$ (tức là ước số lớn nhất nhưng nhỏ hơn $N$).
* **Input:** Một số tự nhiên $N$ ($2 \le N \le 10^9$).
* **Output:** Ước số lớn thứ hai của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `24` | `12` | Ước lớn nhất là 24, lớn thứ hai là 12. |
  | `7` | `1` | Ước của 7 là 1 và 7, lớn thứ hai là 1. |

---

### Bài 9 (Luyện tập): Đếm số nguyên tố trong đoạn (`PYA-L11-P09`)

* **Yêu cầu:** Cho hai số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^4$). Hãy đếm xem có bao nhiêu số nguyên tố nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số $A, B$ trên cùng một dòng.
* **Output:** Số lượng số nguyên tố trong đoạn $[A, B]$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10 20` | `4` | Có 4 số nguyên tố: 11, 13, 17, 19. |

---

### Bài 10 (Luyện tập): Hai số nguyên tố cùng nhau (`PYA-L11-P10`)

* **Bối cảnh:** Hai số $A$ và $B$ được gọi là nguyên tố cùng nhau nếu Ước chung lớn nhất của chúng bằng 1 ($\text{GCD}(A, B) = 1$).
* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng nguyên tố cùng nhau, ngược lại in `NO`.
* **Input:** Hai số $A, B$ ($1 \le A, B \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `8 9` | `YES` |
  | `12 18` | `NO` |

---

### Bài 11 (Luyện tập): Cặp số nguyên tố sinh đôi (`PYA-L11-P11`)

* **Bối cảnh:** Hai số nguyên tố được gọi là "Sinh đôi" (Twin Primes) nếu chúng hơn kém nhau đúng 2 đơn vị (ví dụ: $(3, 5), (5, 7), (11, 13), (17, 19)$).
* **Yêu cầu:** Cho số tự nhiên $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các cặp số nguyên tố sinh đôi $(P, P+2)$ sao cho $P+2 \le N$.
* **Input:** Một số nguyên $N$.
* **Output:** Mỗi dòng in một cặp số nguyên tố sinh đôi cách nhau bởi khoảng trắng, theo thứ tự tăng dần.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `15` | `3 5`<br>`5 7`<br>`11 13` |

---

### Bài 12 (Vận dụng): Số siêu nguyên tố (super prime) (`PYA-L11-P12`)
*(Đề thi Python Bảng A)*

* **Bối cảnh:** Một số tự nhiên được gọi là "Siêu nguyên tố" nếu bản thân nó là số nguyên tố, và khi ta lần lượt xóa bớt chữ số tận cùng bên phải thì các số thu được vẫn luôn là số nguyên tố!
  * Ví dụ: Số $239$ là số nguyên tố.
  * Cắt đuôi 9 còn $23$ (vẫn là số nguyên tố).
  * Cắt đuôi 3 còn $2$ (vẫn là số nguyên tố).
  $\implies 239$ là một Siêu nguyên tố!
* **Yêu cầu:** Cho số tự nhiên $N$. Hãy kiểm tra xem $N$ có phải là Siêu nguyên tố hay không. In `YES` hoặc `NO`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^7$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `239` | `YES` |
  | `23` | `YES` |
  | `27` | `NO` |

---

### Bài 13 (Vận dụng): Phân tích ra thừa số nguyên tố (`PYA-L11-P13`)

* **Yêu cầu:** Mọi số tự nhiên $N \ge 2$ đều có thể phân tích thành tích của các thừa số nguyên tố. Cho số tự nhiên $N$. Hãy in ra dạng phân tích của $N$.
* **Input:** Một số tự nhiên $N$ ($2 \le N \le 10^6$).
* **Output:** Dãy các thừa số nguyên tố tăng dần theo định dạng `p1 * p2 * ...`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `60` | `2 * 2 * 3 * 5` |
  | `17` | `17` |

---

### Bài 14 (Thử thách): Tìm số có đúng 3 ước số (`PYA-L11-P14`)
*(Đề thi Lập trình Python Quốc gia Bảng A)*

* **Bối cảnh:** Một số tự nhiên $X$ có đúng 3 ước số nguyên dương khi và chỉ khi $X$ là bình phương của một số nguyên tố ($X = P^2$, ví dụ: $4 = 2^2, 9 = 3^2, 25 = 5^2, 49 = 7^2$).
* **Yêu cầu:** Cho số nguyên dương $N$. Hãy đếm xem có bao nhiêu số nhỏ hơn hoặc bằng $N$ mà có **đúng 3 ước số**.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Số lượng các số có đúng 3 ước số $\le N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `30` | `3` | Có 3 số là: 4 ($2^2$), 9 ($3^2$), 25 ($5^2$). |


--------------------------------------------------------------------------------
<!-- Bài 10: lesson-10 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 10: Đếm số theo quy luật và số đặc biệt

## 1. Tóm tắt kiến thức trọng tâm
- **Công thức đếm bội số trong đoạn $[A, B]$ với $\mathcal{O}(1)$:**
  $$\mathbf{count(A, B, K) = (B // K) - ((A - 1) // K)}$$
- **Số hoàn hảo:** Tổng các ước nhỏ hơn nó bằng chính nó ($6, 28, 496$).
- **Số chính phương:** Số có căn bậc 2 là số nguyên: `int(n**0.5)**2 == n`.

---


## 2. Concept quiz: 14 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Số hoàn hảo nhỏ nhất là số nào?
- **A.** 1
- **B.** **[Đáp án đúng]** 6
- **C.** 12
- **D.** 28
- > *Giải thích:* Các ước nhỏ hơn 6 là 1, 2, 3 và $1 + 2 + 3 = 6$.

#### Câu 2: Số nào sau đây cũng là một số hoàn hảo?
- **A.** 10
- **B.** 20
- **C.** **[Đáp án đúng]** 28
- **D.** 32
- > *Giải thích:* Các ước nhỏ hơn 28 là 1, 2, 4, 7, 14. Tổng của chúng: $1 + 2 + 4 + 7 + 14 = 28$.

#### Câu 3: Số 153 là số armstrong vì:
- **A.** $153$ chia hết cho 3
- **B.** $153$ là số nguyên tố
- **C.** **[Đáp án đúng]** $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$
- **D.** $1 + 5 + 3 = 9$
- > *Giải thích:* Định nghĩa số Armstrong bậc 3 là bằng tổng lập phương các chữ số của chính nó.

#### Câu 4: Số lượng các số chia hết cho 5 trong đoạn từ 1 đến 100 là:
- **A.** 19
- **B.** **[Đáp án đúng]** 20
- **C.** 21
- **D.** 25
- > *Giải thích:* $100 // 5 = 20$.

#### Câu 5: Số lượng các số chia hết cho 4 trong đoạn từ 10 đến 30 là bao nhiêu?
- **A.** 4
- **B.** **[Đáp án đúng]** 5 (gồm 12, 16, 20, 24, 28)
- **C.** 6
- **D.** 7
- > *Giải thích:* Áp dụng công thức: $(30 // 4) - ((10 - 1) // 4) = 7 - (9 // 4) = 7 - 2 = 5$.

#### Câu 6: Trong đoạn từ $1$ đến $N$, số lượng các số chia hết cho cả 2 và 3 (tức là chia hết cho 6) là:
- **A.** `N // 2 + N // 3`
- **B.** **[Đáp án đúng]** `N // 6`
- **C.** `N // 5`
- **D.** `(N // 2) * (N // 3)`
- > *Giải thích:* Một số chia hết cho cả 2 và 3 khi và chỉ khi nó chia hết cho $\text{BCNN}(2, 3) = 6$.

#### Câu 7: Nguyên lý bao hàm - loại trừ (inclusion-exclusion) dùng để đếm số lượng các số chia hết cho 2 hoặc 3 trong đoạn $[1, N]$ là:
- **A.** `N // 2 + N // 3`
- **B.** **[Đáp án đúng]** `N // 2 + N // 3 - N // 6`
- **C.** `N // 6`
- **D.** `(N // 2) + (N // 3) + (N // 6)`
- > *Giải thích:* Lấy tập chia hết cho 2 cộng tập chia hết cho 3, rồi trừ đi phần giao bị đếm lặp 2 lần (các số chia hết cho 6).

#### Câu 8: Một số được gọi là "số phong phú" (abundant number) nếu tổng các ước nhỏ hơn nó:
- **A.** Bằng chính nó
- **B.** Nhỏ hơn chính nó
- **C.** **[Đáp án đúng]** Lớn hơn chính nó
- **D.** Bằng 0
- > *Giải thích:* Ví dụ số 12: các ước nhỏ hơn nó là 1, 2, 3, 4, 6 có tổng $1+2+3+4+6 = 16 > 12$.

#### Câu 9: Cặp số $(220, 284)$ được gọi là "cặp số thân thiết" (amicable numbers) vì:
- **A.** Cả hai đều chia hết cho 2
- **B.** **[Đáp án đúng]** Tổng các ước của số này bằng số kia và ngược lại
- **C.** Hiệu của chúng bằng 64
- **D.** Tích của chúng là số chính phương
- > *Giải thích:* Tổng các ước nhỏ hơn 220 bằng 284, và tổng các ước nhỏ hơn 284 lại đúng bằng 220.

#### Câu 10: Số chính phương có chữ số tận cùng không thể là chữ số nào sau đây?
- **A.** 1
- **B.** 4
- **C.** 5
- **D.** **[Đáp án đúng]** 2 (hoặc 3, 7, 8)
- > *Giải thích:* Bình phương của một số tự nhiên chỉ có thể tận cùng bằng 0, 1, 4, 5, 6, 9. Không bao giờ tận cùng bằng 2, 3, 7, 8.

#### Câu 11: Để đếm có bao nhiêu số lẻ trong đoạn từ $A$ đến $B$ (với $A \le B$), cách tính tổng quát chuẩn nhất là:
- **A.** `(B - A) // 2`
- **B.** **[Đáp án đúng]** Tổng số phần tử trừ đi số lượng số chẵn trong đoạn
- **C.** Luôn bằng một nửa
- **D.** `(B - A + 1) // 2`
- > *Giải thích:* Đoạn $[A, B]$ có tổng $(B - A + 1)$ số. Số lượng số chẵn là $(B // 2) - ((A - 1) // 2)$. Số lượng số lẻ bằng tổng trừ đi số chẵn.

#### Câu 12: Số tự nhiên $N$ được gọi là "số smith" nếu:
- **A.** $N$ là số nguyên tố
- **B.** **[Đáp án đúng]** $N$ là hợp số và tổng chữ số của nó bằng tổng các chữ số của các thừa số nguyên tố cấu tạo nên nó
- **C.** $N$ chia hết cho 9
- **D.** $N$ là số đối xứng
- > *Giải thích:* Ví dụ $4 \to 2 \times 2$: tổng chữ số 4 bằng $2 + 2 = 4$.

#### Câu 13: Đoạn code sau tính điều gì?
```python
count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        count += 1
print(count)
```
- **A.** Đếm số chia hết cho 15
- **B.** **[Đáp án đúng]** Đếm các số chia hết cho 3 nhưng không chia hết cho 5 trong đoạn 1 đến 100
- **C.** Đếm số chia hết cho 3 hoặc 5
- **D.** Luôn bằng 33
- > *Giải thích:* Biểu thức `i % 3 == 0 and i % 5 != 0` lọc chính xác các bội của 3 loại trừ các bội chung của 3 và 5.

#### Câu 14: Giá trị `count` ở câu 13 bằng bao nhiêu?
- **A.** 33
- **B.** 20
- **C.** **[Đáp án đúng]** 27
- **D.** 30
- > *Giải thích:* Số lượng số chia hết cho 3 là $100 // 3 = 33$. Số lượng số chia hết cho cả 3 và 5 (tức 15) là $100 // 15 = 6$. Vậy $33 - 6 = 27$.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 10: Đếm số theo quy luật và số đặc biệt

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L12-P01` | Đếm số chia hết cho K | `Cơ bản` | $1 \le N, K \le 10^9$ | Phép chia nguyên $N // K$ chuẩn xác |
| 02 | `PYA-L12-P02` | Đếm số lẻ trong đoạn | `Cơ bản` | $1 \le A \le B \le 10^9$ | Đếm số lượng số lẻ trong đoạn $[A, B]$ |
| 03 | `PYA-L12-P03` | Kiểm tra số hoàn hảo | `Cơ bản` | $1 \le N \le 10^6$ | Tính tổng ước nhỏ hơn $N$ và so sánh |
| 04 | `PYA-L12-P04` | Số armstrong ba chữ số | `Cơ bản` | $100 \le N \le 999$ | Kiểm tra $a^3 + b^3 + c^3 = N$ |
| 05 | `PYA-L12-P05` | Tìm tất cả số hoàn hảo nhỏ hơn N | `Cơ bản` | $1 \le N \le 10^4$ | Vòng lặp tìm số hoàn hảo (6, 28, 496...) |
| 06 | `PYA-L12-P06` | Đếm bội của 3 nhưng không chia hết cho 5 | `Luyện tập` | $1 \le A \le B \le 10^{12}$ | Áp dụng trừ tập hợp: Chia 3 trừ chia 15 |
| 07 | `PYA-L12-P07` | Đếm số chia hết cho 2 hoặc 3 | `Luyện tập` | $1 \le N \le 10^{12}$ | Nguyên lý bao hàm - loại trừ $\mathcal{O}(1)$ |
| 08 | `PYA-L12-P08` | Cặp số thân thiết | `Luyện tập` | $1 \le A, B \le 10^5$ | Kiểm tra tổng ước của $A$ bằng $B$ và ngược lại |
| 09 | `PYA-L12-P09` | Số phong phú (abundant number) | `Luyện tập` | $1 \le N \le 10^6$ | Kiểm tra tổng ước thực sự lớn hơn $N$ |
| 10 | `PYA-L12-P10` | Đếm số không chứa chữ số 0 | `Luyện tập` | $1 \le N \le 10^6$ | Đếm các số không chứa chữ số 0 |
| 11 | `PYA-L12-P11` | Đếm số chính phương trong đoạn | `Vận dụng` | $1 \le A \le B \le 10^{14}$ | Đếm số lượng chính phương bằng $\lfloor\sqrt{B}\rfloor - \lfloor\sqrt{A-1}\rfloor$ |
| 12 | `PYA-L12-P12` | Số tự mãn (narcissistic number K chữ số) | `Thử thách` | $1 \le N \le 10^9$ | Tổng lũy thừa bậc $K$ của các chữ số bằng chính nó |

---

### Bài 1 (Cơ bản): Đếm số chia hết cho K (`PYA-L12-P01`)

* **Yêu cầu:** Cho 2 số nguyên dương $N$ và $K$. Hãy đếm xem trong các số từ $1$ đến $N$, có bao nhiêu số chia hết cho $K$.
* **Input:** Hai số nguyên $N$ và $K$ ($1 \le N, K \le 10^9$) cách nhau bởi khoảng trắng.
* **Output:** Một số nguyên duy nhất là số lượng các số chia hết cho $K$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `20 3` | `6` | Có 6 số: 3, 6, 9, 12, 15, 18. |
* **Gợi ý:** Sử dụng công thức `N // K`.

---

### Bài 2 (Cơ bản): Đếm số lẻ trong đoạn (`PYA-L12-P02`)

* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^9$). Hãy đếm xem có bao nhiêu số lẻ nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số $A, B$ trên cùng một dòng.
* **Output:** Số lượng số lẻ.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3 8` | `3` | Có 3 số lẻ là: 3, 5, 7. |

---

### Bài 3 (Cơ bản): Kiểm tra số hoàn hảo (`PYA-L12-P03`)

* **Bối cảnh:** Một số nguyên dương $N$ được gọi là "Số hoàn hảo" nếu tổng tất cả các ước số nguyên dương nhỏ hơn $N$ bằng chính số $N$.
* **Yêu cầu:** Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số hoàn hảo không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `6` | `YES` |
  | `10` | `NO` |

---

### Bài 4 (Cơ bản): Số armstrong ba chữ số (`PYA-L12-P04`)

* **Bối cảnh:** Số Armstrong có 3 chữ số là số tự nhiên có dạng $\overline{abc}$ thỏa mãn $a^3 + b^3 + c^3 = \overline{abc}$.
* **Yêu cầu:** Cho một số có đúng 3 chữ số $N$. Kiểm tra xem $N$ có phải là số Armstrong không. In `YES` hoặc `NO`.
* **Input:** Một số nguyên $N$ ($100 \le N \le 999$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `153` | `YES` |
  | `200` | `NO` |

---

### Bài 5 (Cơ bản): Tìm tất cả số hoàn hảo nhỏ hơn N (`PYA-L12-P05`)

* **Yêu cầu:** Cho số nguyên dương $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các số hoàn hảo nhỏ hơn hoặc bằng $N$ theo thứ tự tăng dần.
* **Input:** Một số nguyên $N$.
* **Output:** Các số hoàn hảo, cách nhau bởi khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `30` | `6 28` |

---

### Bài 6 (Luyện tập): Đếm bội của 3 nhưng không chia hết cho 5 (`PYA-L12-P06`)

* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{12}$). Hãy đếm xem trong đoạn từ $A$ đến $B$ có bao nhiêu số chia hết cho 3 nhưng **không chia hết cho 5**.
* **Input:** Hai số $A$ và $B$ cách nhau bởi khoảng trắng.
* **Output:** Số lượng số thỏa mãn.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `1 30` | `8` |

---

### Bài 7 (Luyện tập): Đếm số chia hết cho 2 hoặc 3 (`PYA-L12-P07`)

* **Yêu cầu:** Cho số nguyên dương $N$ ($1 \le N \le 10^{12}$). Hãy đếm xem từ 1 đến $N$ có bao nhiêu số chia hết cho 2 hoặc chia hết cho 3.
* **Input:** Một số nguyên $N$.
* **Output:** Số lượng số thỏa mãn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `7` | Các số là: 2, 3, 4, 6, 8, 9, 10 (có 7 số). |
* **Gợi ý:** Dùng công thức $N // 2 + N // 3 - N // 6$.

---

### Bài 8 (Luyện tập): Cặp số thân thiết (`PYA-L12-P08`)

* **Bối cảnh:** Hai số $A$ và $B$ ($A \ne B$) được gọi là "Cặp số thân thiết" nếu tổng các ước số nhỏ hơn $A$ bằng $B$, và tổng các ước số nhỏ hơn $B$ bằng $A$.
* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng là cặp số thân thiết, ngược lại in `NO`.
* **Input:** Hai số $A, B$ ($1 \le A, B \le 10^5$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `220 284` | `YES` |
  | `10 20` | `NO` |

---

### Bài 9 (Luyện tập): Số phong phú (abundant number) (`PYA-L12-P09`)

* **Bối cảnh:** Một số tự nhiên được gọi là "Số phong phú" nếu tổng các ước số nhỏ hơn nó lớn hơn chính nó (ví dụ: số 12 có tổng các ước nhỏ hơn nó là $1+2+3+4+6=16 > 12$).
* **Yêu cầu:** Nhập số nguyên dương $N$. Hãy in ra tất cả các số phong phú nhỏ hơn hoặc bằng $N$.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^4$).
* **Output:** Dãy các số phong phú tăng dần trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `20` | `12 18 20` |

---

### Bài 10 (Luyện tập): Đếm số không chứa chữ số 0 (`PYA-L12-P10`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy đếm xem từ 1 đến $N$ có bao nhiêu số mà trong cách ghi thập phân của nó **không chứa bất kỳ chữ số 0 nào**.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** Số lượng số thỏa mãn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `15` | `14` | Từ 1 đến 15 chỉ có duy nhất số 10 chứa chữ số 0. Vậy có $15 - 1 = 14$ số. |

---

### Bài 11 (Vận dụng): Đếm số chính phương trong đoạn (`PYA-L12-P11`)
*(Đề thi Python Bảng A)*

* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{14}$). Hãy đếm xem có bao nhiêu số chính phương nằm trong đoạn từ $A$ đến $B$.
* **Input:** Hai số nguyên $A, B$ trên cùng một dòng.
* **Output:** Số lượng số chính phương trong đoạn $[A, B]$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5 25` | `3` | Có 3 số chính phương là 9, 16, 25. |
* **Gợi ý:** Một số $X$ là số chính phương trong $[A, B]$ thì $K = \sqrt{X}$ thỏa mãn $\sqrt{A} \le K \le \sqrt{B}$. Số lượng $K$ nguyên chính bằng: `int(B**0.5) - int((A - 1)**0.5)`.

---

### Bài 12 (Thử thách): Số tự mãn (narcissistic number K chữ số) (`PYA-L12-P12`)
*(Đề thi Lập trình Python Quốc gia Bảng A)*

* **Bối cảnh:** Một số tự nhiên $N$ có $K$ chữ số được gọi là "Số tự mãn" (Narcissistic number) nếu tổng lũy thừa bậc $K$ của các chữ số của nó đúng bằng chính số $N$.
  Ví dụ:
  * $N = 153$ có 3 chữ số: $1^3 + 5^3 + 3^3 = 153$ $\implies$ Thỏa mãn.
  * $N = 1634$ có 4 chữ số: $1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$ $\implies$ Thỏa mãn.
* **Yêu cầu:** Cho số nguyên dương $N$ ($1 \le N \le 10^9$). Hãy kiểm tra xem $N$ có phải là số tự mãn không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một số nguyên $N$.
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `1634` | `YES` |
  | `2024` | `NO` |


================================================================================
# CHƯƠNG 05: DANH SÁCH (LIST)
================================================================================


--------------------------------------------------------------------------------
<!-- Bài 11: lesson-11 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 11: Danh sách và thao tác cơ bản

## 1. Tóm tắt kiến thức trọng tâm
- Danh sách (List) là tập hợp nhiều phần tử lưu trong dấu ngoặc vuông `[]`.
- Cho phép thay đổi giá trị tại từng vị trí (Mutable): `a[0] = 100`.
- **Cú pháp nhập danh sách số trên 1 dòng chuẩn thi đấu:**
  ```python
  a = list(map(int, input().split()))
  ```
- **Các lệnh thao tác danh sách cơ bản:**
  - `a.append(x)`: Thêm $x$ vào cuối danh sách.
  - `a.remove(x)`: Xóa phần tử đầu tiên có giá trị $x$.
  - `a.insert(i, x)`: Chèn giá trị $x$ vào vị trí index $i$.
  - `len(a)`: Trả về số lượng phần tử.
  - `if x in a:`: Kiểm tra $x$ có nằm trong danh sách không.

## 2. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Để khai báo một danh sách rỗng trong Python, cú pháp nào đúng?
- **A.** `a = ()`
- **B.** `a = {}`
- **C.** **[Đáp án đúng]** `a = []` hoặc `a = list()`
- **D.** `a = ""`
- > *Giải thích:* List trong Python được định nghĩa bằng cặp dấu ngoặc vuông `[]`.

#### Câu 2: Cho `a = [10, 20, 30, 40]`. Phần tử `a[0]` có giá trị là:
- **A.** 20
- **B.** **[Đáp án đúng]** 10
- **C.** 40
- **D.** 0
- > *Giải thích:* Chỉ số index của List trong Python luôn bắt đầu từ số 0.

#### Câu 3: Lệnh nào sau đây dùng để thêm một số `99` vào cuối danh sách `a`?
- **A.** `a.add(99)`
- **B.** `a.push(99)`
- **C.** **[Đáp án đúng]** `a.append(99)`
- **D.** `a.insert(99)`
- > *Giải thích:* Phương thức `append(x)` luôn nối phần tử `x` vào vị trí cuối cùng của List.

#### Câu 4: Cho `a = [1, 2, 3]`. Lệnh `a[1] = 9` sẽ biến danh sách `a` thành:
- **A.** `[9, 2, 3]`
- **B.** **[Đáp án đúng]** `[1, 9, 3]`
- **C.** `[1, 2, 9]`
- **D.** Báo lỗi vì List không thể thay đổi
- > *Giải thích:* Khác với String (bất biến), List là đối tượng thay đổi được (Mutable), ta có thể gán đè giá trị tại bất kỳ index nào.

#### Câu 5: Lệnh `a.pop()` không truyền tham số có tác dụng gì?
- **A.** Xóa phần tử đầu tiên
- **B.** **[Đáp án đúng]** Xóa và trả về phần tử CUỐI CÙNG của danh sách
- **C.** Xóa toàn bộ danh sách
- **D.** Đảo ngược danh sách
- > *Giải thích:* `pop()` mặc định loại bỏ phần tử ở vị trí cuối cùng của danh sách.

#### Câu 6: Dòng code nào sau đây dùng để đọc một mảng các số nguyên cách nhau bởi dấu cách từ bàn phím chuẩn xác nhất?
- **A.** `a = input()`
- **B.** `a = int(input())`
- **C.** **[Đáp án đúng]** `a = list(map(int, input().split()))`
- **D.** `a = list(input())`
- > *Giải thích:* Cú pháp chuẩn trong thi đấu: `input().split()` tách chuỗi, `map(int, ...)` ép kiểu số nguyên, `list(...)` tạo mảng.

#### Câu 7: Cho `a = [5, 8, 12, 20]`. Biểu thức `15 in a` trả về giá trị gì?
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** Báo lỗi
- **D.** 0
- > *Giải thích:* Toán tử `in` kiểm tra sự tồn tại của một giá trị trong List. Số 15 không có trong `a` nên trả về `False`.

#### Câu 8: Cho `a = [1, 2, 3]`. Lệnh `a * 2` sẽ tạo ra kết quả gì?
- **A.** `[2, 4, 6]`
- **B.** **[Đáp án đúng]** `[1, 2, 3, 1, 2, 3]`
- **C.** Báo lỗi
- **D.** `[1, 2, 3, 2]`
- > *Giải thích:* Phép nhân List với một số nguyên $K$ sẽ nhân bản danh sách đó lên $K$ lần (không phải nhân giá trị từng phần tử).

#### Câu 9: Lệnh `a.insert(0, 100)` có tác dụng gì?
- **A.** Gán đè phần tử đầu tiên bằng 100
- **B.** **[Đáp án đúng]** Chèn giá trị 100 vào ĐẦU danh sách (vị trí index 0) và đẩy các phần tử khác lùi về sau
- **C.** Thêm 100 vào cuối
- **D.** Tìm số 100
- > *Giải thích:* `insert(index, value)` chèn phần tử vào vị trí chỉ định và dồn các phần tử sau sang phải.

#### Câu 10: Cho `a = [10, 20, 30, 20]`. Sau khi gọi `a.remove(20)`, danh sách `a` sẽ là:
- **A.** `[10, 30]` (Xóa hết các số 20)
- **B.** **[Đáp án đúng]** `[10, 30, 20]` (Chỉ xóa số 20 ĐẦU TIÊN gặp được)
- **C.** `[10, 20, 30]`
- **D.** Báo lỗi
- > *Giải thích:* `remove(x)` chỉ tìm và xóa phần tử có giá trị $x$ đầu tiên tính từ trái sang phải.

#### Câu 11: Đoạn code sau in ra màn hình bao nhiêu số?
```python
a = [2, 4, 6, 8, 10]
for x in a:
    if x > 5:
        print(x)
```
- **A.** 5 số
- **B.** 2 số
- **C.** **[Đáp án đúng]** 3 số (gồm 6, 8, 10)
- **D.** 4 số
- > *Giải thích:* Các số lớn hơn 5 trong danh sách là 6, 8, 10.

#### Câu 12: Biểu thức `a[-1]` trên một danh sách không rỗng trả về:
- **A.** Phần tử đầu tiên
- **B.** **[Đáp án đúng]** Phần tử cuối cùng của danh sách
- **C.** Báo lỗi chỉ số âm
- **D.** Độ dài danh sách
- > *Giải thích:* Tương tự chuỗi, chỉ số âm `-1` là phần tử cuối cùng của List.

#### Câu 13: Cú pháp slicing `a[1:3]` trên danh sách `a = ['A', 'B', 'C', 'D']` trả về:
- **A.** `['A', 'B']`
- **B.** **[Đáp án đúng]** `['B', 'C']`
- **C.** `['B', 'C', 'D']`
- **D.** `['C', 'D']`
- > *Giải thích:* Lấy từ index 1 (`'B'`) đến index 2 (`'C'`), không lấy index 3.

#### Câu 14: Đoạn code sau in ra giá trị gì?
```python
a = [1, 2, 3]
b = [4, 5]
c = a + b
print(len(c))
```
- **A.** 3
- **B.** 2
- **C.** **[Đáp án đúng]** 5
- **D.** Báo lỗi
- > *Giải thích:* Phép cộng `+` hai danh sách sẽ nối chúng lại thành `[1, 2, 3, 4, 5]` có độ dài 5.

#### Câu 15: Để xóa toàn bộ các phần tử trong danh sách `a` đưa về danh sách rỗng, ta dùng lệnh nào?
- **A.** `a.delete()`
- **B.** **[Đáp án đúng]** `a.clear()`
- **C.** `a.remove_all()`
- **D.** `a = None`
- > *Giải thích:* `clear()` dọn sạch toàn bộ các phần tử trong danh sách.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 11: Danh sách và thao tác cơ bản

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L16-P01` | Nhập dãy số & in phần tử đầu - cuối | `Cơ bản` | $N \le 1000$ | Cú pháp `list(map(int, ...))` và index |
| 02 | `PYA-L16-P02` | Thêm điểm vào danh sách | `Cơ bản` | Số lượng phần tử $\le 100$ | Phương thức `append()` |
| 03 | `PYA-L16-P03` | Tính tổng các phần tử trong dãy | `Cơ bản` | $N \le 10^5, A_i \le 10^9$ | Duyệt `for x in a` cộng dồn |
| 04 | `PYA-L16-P04` | Đếm số lượng số chẵn trong mảng | `Cơ bản` | $N \le 10^5$ | Đếm phần tử thỏa mãn điều kiện |
| 05 | `PYA-L16-P05` | Tìm số lớn nhất & nhỏ nhất | `Cơ bản` | $N \le 10^5$ | Tìm min/max bằng thuật toán duyệt |
| 06 | `PYA-L16-P06` | In dãy số theo thứ tự đảo ngược | `Luyện tập` | $N \le 10^5$ | Đảo ngược mảng `a[::-1]` |
| 07 | `PYA-L16-P07` | Đếm số lần xuất hiện của x | `Luyện tập` | $N \le 10^5$ | Phương thức `a.count(x)` |
| 08 | `PYA-L16-P08` | Tìm vị trí đầu tiên của x | `Luyện tập` | $N \le 10^5$ | Tìm kiếm tuần tự trả về chỉ số index |
| 09 | `PYA-L16-P09` | Tách mảng chẵn và mảng lẻ | `Luyện tập` | $N \le 10^5$ | Phân loại dữ liệu vào 2 danh sách riêng |
| 10 | `PYA-L16-P10` | Xóa phần tử đầu tiên bằng x | `Luyện tập` | $N \le 10^5$ | Sử dụng `a.remove(x)` an toàn |
| 11 | `PYA-L16-P11` | Thay thế tất cả số âm bằng số 0 | `Luyện tập` | $N \le 10^5$ | Cập nhật mảng theo vị trí `a[i]` |
| 12 | `PYA-L16-P12` | Chèn số vào vị trí K | `Vận dụng` | $N \le 1000$ | Thao tác `a.insert(k, x)` |
| 13 | `PYA-L16-P13` | Xoay vòng danh sách sang phải | `Vận dụng` | $N \le 10^5, K \le N$ | Dịch mảng sang phải $K$ vị trí |
| 14 | `PYA-L16-P14` | Cặp số có tổng bằng s | `Thử thách` | $N \le 10^4$ | Tìm 2 phần tử $A_i + A_j = S$ |

---

### Bài 1 (Cơ bản): Nhập dãy số & in phần tử đầu - cuối (`PYA-L16-P01`)

* **Yêu cầu:** Cho một dãy gồm $N$ số nguyên. Hãy in ra phần tử đầu tiên và phần tử cuối cùng của dãy số đó.
* **Input:**
  * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
  * Dòng 2: Gồm $N$ số nguyên cách nhau bởi khoảng trắng.
* **Output:** In phần tử đầu tiên và phần tử cuối cùng trên một dòng, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`10 25 3 47 99` | `10 99` |

---

### Bài 2 (Cơ bản): Thêm điểm vào danh sách (`PYA-L16-P02`)

* **Bối cảnh:** Thầy giáo có một danh sách điểm kiểm tra ban đầu. Sau đó có thêm một bạn học sinh nộp bài muộn và được chấm điểm $X$.
* **Yêu cầu:** Cho danh sách các số nguyên ban đầu và số $X$. Hãy thêm $X$ vào cuối danh sách và in ra toàn bộ danh sách mới.
* **Input:**
  * Dòng 1: Danh sách các số nguyên cách nhau bởi khoảng trắng.
  * Dòng 2: Số nguyên $X$.
* **Output:** Danh sách các số sau khi thêm $X$, cách nhau bởi khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `8 9 7 10`<br>`9` | `8 9 7 10 9` |

---

### Bài 3 (Cơ bản): Tính tổng các phần tử trong dãy (`PYA-L16-P03`)

* **Yêu cầu:** Cho một dãy gồm $N$ số nguyên. Hãy tính tổng tất cả các phần tử trong dãy số.
* **Input:**
  * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).
* **Output:** Tổng các phần tử trong dãy.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4`<br>`10 20 30 40` | `100` |

---

### Bài 4 (Cơ bản): Đếm số lượng số chẵn trong mảng (`PYA-L16-P04`)

* **Yêu cầu:** Cho một dãy gồm $N$ số nguyên dương. Hãy đếm xem có bao nhiêu số chẵn trong dãy.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Số lượng số chẵn.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`2 5 8 10 13` | `3` |

---

### Bài 5 (Cơ bản): Tìm số lớn nhất & nhỏ nhất (`PYA-L16-P05`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn nhất và giá trị nhỏ nhất trong dãy số.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Giá trị lớn nhất, theo sau là giá trị nhỏ nhất, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`12 5 89 3 45` | `89 3` |

---

### Bài 6 (Luyện tập): In dãy số theo thứ tự đảo ngược (`PYA-L16-P06`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy in ra dãy số theo thứ tự ngược lại (từ phần tử cuối cùng về phần tử đầu tiên).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi đảo ngược trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4`<br>`1 2 3 4` | `4 3 2 1` |

---

### Bài 7 (Luyện tập): Đếm số lần xuất hiện của x (`PYA-L16-P07`)

* **Yêu cầu:** Cho dãy $N$ số nguyên và một số nguyên $X$. Hãy đếm xem số $X$ xuất hiện bao nhiêu lần trong dãy số.
* **Input:**
  * Dòng 1: Hai số nguyên $N$ và $X$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Số lần xuất hiện của $X$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `6 5`<br>`5 2 5 7 5 9` | `3` |

---

### Bài 8 (Luyện tập): Tìm vị trí đầu tiên của x (`PYA-L16-P08`)

* **Yêu cầu:** Cho dãy $N$ số nguyên và số $X$. Hãy tìm vị trí (chỉ số index từ 0) xuất hiện **đầu tiên** của số $X$ trong dãy. Nếu số $X$ không có trong dãy, in ra `-1`.
* **Input:**
  * Dòng 1: Hai số nguyên $N$ và $X$.
  * Dòng 2: $N$ số nguyên.
* **Output:** Vị trí index đầu tiên của $X$, hoặc `-1`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5 7`<br>`3 5 7 9 7` | `2` |
  | `4 10`<br>`1 2 3 4` | `-1` |

---

### Bài 9 (Luyện tập): Tách mảng chẵn và mảng lẻ (`PYA-L16-P09`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy tách dãy thành 2 danh sách: một danh sách gồm các số chẵn, một danh sách gồm các số lẻ (giữ nguyên thứ tự xuất hiện ban đầu).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:**
  * Dòng 1: Các số chẵn (cách nhau bởi khoảng trắng).
  * Dòng 2: Các số lẻ (cách nhau bởi khoảng trắng).
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `6`<br>`1 4 7 8 2 9` | `4 8 2`<br>`1 7 9` |

---

### Bài 10 (Luyện tập): Xóa phần tử đầu tiên bằng x (`PYA-L16-P10`)

* **Yêu cầu:** Cho dãy $N$ số nguyên và số $X$. Nếu $X$ có trong dãy, hãy xóa phần tử đầu tiên có giá trị bằng $X$ và in ra dãy số còn lại. Nếu $X$ không có trong dãy, in ra `KHONG CO`.
* **Input:**
  * Dòng 1: Hai số $N, X$.
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi xóa, hoặc `KHONG CO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5 3`<br>`1 3 5 3 7` | `1 5 3 7` |

---

### Bài 11 (Luyện tập): Thay thế tất cả số âm bằng số 0 (`PYA-L16-P11`)

* **Yêu cầu:** Cho dãy $N$ số nguyên gồm cả số âm và số dương. Hãy thay thế toàn bộ các số âm trong dãy bằng số 0 và in ra dãy mới.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi thay thế.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`3 -5 8 -2 0` | `3 0 8 0 0` |

---

### Bài 12 (Vận dụng): Chèn số vào vị trí K (`PYA-L16-P12`)

* **Yêu cầu:** Cho dãy $N$ số nguyên, số nguyên $X$ và vị trí index $K$ ($0 \le K \le N$). Hãy chèn số $X$ vào đúng vị trí $K$ của dãy số và in ra dãy mới gồm $(N + 1)$ phần tử.
* **Input:**
  * Dòng 1: Số nguyên $N$.
  * Dòng 2: $N$ số nguyên.
  * Dòng 3: Hai số nguyên $X$ và $K$.
* **Output:** Dãy số sau khi chèn.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4`<br>`10 20 30 40`<br>`99 1` | `10 99 20 30 40` |

---

### Bài 13 (Vận dụng): Xoay vòng danh sách sang phải (`PYA-L16-P13`)

* **Bối cảnh:** Phép xoay phải danh sách $K$ vị trí là thao tác nhấc $K$ phần tử cuối cùng của mảng đem gắn lên đầu mảng.
* **Yêu cầu:** Cho dãy $N$ số nguyên và số $K$ ($1 \le K \le N \le 10^5$). Hãy in ra dãy số sau khi xoay phải $K$ vị trí.
* **Input:**
  * Dòng 1: Hai số $N$ và $K$.
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi xoay phải.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5 2`<br>`1 2 3 4 5` | `4 5 1 2 3` | Hai phần tử cuối là 4, 5 được đưa lên đầu. |

---

### Bài 14 (Thử thách): Cặp số có tổng bằng s (`PYA-L16-P14`)
*(Đề thi Python Bảng A)*

* **Yêu cầu:** Cho dãy gồm $N$ số nguyên đôi một khác nhau và một số nguyên mục tiêu $S$. Hãy đếm xem có bao nhiêu cặp chỉ số $(i, j)$ với $i < j$ thỏa mãn:
  $$A_i + A_j = S$$
* **Input:**
  * Dòng 1: Hai số nguyên $N$ và $S$ ($1 \le N \le 10^4, |S| \le 10^9$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Số lượng cặp thỏa mãn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5 10`<br>`2 4 6 8 3` | `2` | Có 2 cặp là $(2, 8)$ và $(4, 6)$. |


--------------------------------------------------------------------------------
<!-- Bài 12: lesson-12 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 12: Thống kê danh sách và sắp xếp

## 1. Tóm tắt kiến thức trọng tâm
- **Hàm thống kê tích hợp sẵn:** `max(a)`, `min(a)`, `sum(a)`.
  - Trung bình cộng: `sum(a) / len(a)`.
- **Sắp xếp danh sách:**
  - `a.sort()`: Sắp xếp tăng dần trực tiếp trên mảng `a`.
  - `a.sort(reverse=True)`: Sắp xếp giảm dần.
  - `b = sorted(a)`: Tạo mảng mới `b` đã sắp xếp, giữ nguyên mảng `a`.
- **Lọc phần tử trùng lặp:** `unique = sorted(list(set(a)))`.

## 2. Mẫu code chuẩn
```python
# Nhập mảng số nguyên, in số lớn nhất, nhỏ nhất và mảng sắp xếp tăng dần
a = list(map(int, input().split()))
print("Max:", max(a))
print("Min:", min(a))
a.sort()
print("Sap xep:", *a)
```

---


## 3. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Hàm nào trong Python trả về giá trị lớn nhất trong danh sách số `a`?
- **A.** `a.maximum()`
- **B.** `a.largest()`
- **C.** **[Đáp án đúng]** `max(a)`
- **D.** `top(a)`
- > *Giải thích:* `max()` là hàm tích hợp sẵn trong Python nhận đầu vào là một danh sách.

#### Câu 2: Hàm `sum(a)` trên danh sách `a = [2, 4, 6, 8]` trả về kết quả bằng bao nhiêu?
- **A.** 10
- **B.** **[Đáp án đúng]** 20
- **C.** 4
- **D.** 24
- > *Giải thích:* $2 + 4 + 6 + 8 = 20$.

#### Câu 3: Điểm khác biệt lớn nhất giữa `a.sort()` và `sorted(a)` là gì?
- **A.** `a.sort()` chạy chậm hơn
- **B.** **[Đáp án đúng]** `a.sort()` làm biến đổi trực tiếp danh sách `a` gốc, còn `sorted(a)` tạo ra danh sách mới và giữ nguyên `a` gốc
- **C.** `sorted(a)` chỉ dùng cho chuỗi
- **D.** Không có sự khác biệt
- > *Giải thích:* `a.sort()` là phương thức in-place (tại chỗ), không trả về giá trị (trả về `None`).

#### Câu 4: Để sắp xếp danh sách `a` theo thứ tự giảm dần, cú pháp nào đúng?
- **A.** `a.sort(down=True)`
- **B.** `a.sort(descending=True)`
- **C.** **[Đáp án đúng]** `a.sort(reverse=True)`
- **D.** `a.reverse_sort()`
- > *Giải thích:* Tham số `reverse=True` đảo chiều thứ tự sắp xếp mặc định sang giảm dần.

#### Câu 5: Cho `a = [10, 5, 20, 15]`. Sau khi chạy `a.sort()`, phần tử `a[0]` và `a[-1]` lần lượt là:
- **A.** 10 và 15
- **B.** **[Đáp án đúng]** 5 và 20
- **C.** 20 và 5
- **D.** 5 và 15
- > *Giải thích:* Sau khi sort tăng dần `[5, 10, 15, 20]`: số nhỏ nhất ở đầu `a[0] = 5`, số lớn nhất ở cuối `a[-1] = 20`.

#### Câu 6: Muốn tìm số lớn thứ hai trong danh sách các số đôi một khác nhau `a`, sau khi gọi `a.sort()`, số đó nằm ở vị trí nào?
- **A.** `a[1]`
- **B.** **[Đáp án đúng]** `a[-2]` (Phần tử kế cuối)
- **C.** `a[-1] - 1`
- **D.** `a[len(a)]`
- > *Giải thích:* Trong mảng đã sắp xếp tăng dần, phần tử lớn nhất là `a[-1]`, phần tử lớn thứ nhì là `a[-2]`.

#### Câu 7: Công thức tính trung bình cộng của các số trong danh sách `a` là:
- **A.** `average(a)`
- **B.** `sum(a) // len(a)`
- **C.** **[Đáp án đúng]** `sum(a) / len(a)`
- **D.** `mean(a)`
- > *Giải thích:* Tổng chia cho số lượng phần tử: `sum(a) / len(a)`. Dùng phép chia thực `/` để kết quả chính xác có phần thập phân.

#### Câu 8: Đoạn code sau in ra kết quả gì?
```python
a = [3, 1, 2]
b = a.sort()
print(b)
```
- **A.** `[1, 2, 3]`
- **B.** **[Đáp án đúng]** `None` (Bẫy lỗi kinh điển!)
- **C.** `[3, 1, 2]`
- **D.** Báo lỗi cú pháp
- > *Giải thích:* Bẫy kinh điển: Phương thức `a.sort()` sắp xếp tại chỗ và trả về `None`. Biến `b` sẽ nhận giá trị `None`! Muốn lấy danh sách mới phải dùng `b = sorted(a)`.

#### Câu 9: Lệnh `a.reverse()` có tác dụng gì?
- **A.** Sắp xếp giảm dần
- **B.** **[Đáp án đúng]** Đảo ngược thứ tự các phần tử hiện tại của danh sách (không quan tâm giá trị lớn hay nhỏ)
- **C.** Sắp xếp tăng dần
- **D.** Xóa phần tử cuối
- > *Giải thích:* `reverse()` chỉ lật ngược thứ tự trước sau của mảng hiện tại.

#### Câu 10: Cho danh sách `a = [4, 7, 2, 7, 9, 7]`. Lệnh `a.count(max(a))` trả về:
- **A.** 3
- **B.** **[Đáp án đúng]** 1 (Số lớn nhất là 9, xuất hiện 1 lần)
- **C.** 7
- **D.** 9
- > *Giải thích:* `max(a)` là 9. Số 9 xuất hiện đúng 1 lần trong mảng.

#### Câu 11: Khi sắp xếp danh sách các chuỗi chữ cái `['banana', 'apple', 'cherry']`, Python sẽ sắp xếp theo quy tắc nào?
- **A.** Theo độ dài ngắn của từ
- **B.** **[Đáp án đúng]** Theo thứ tự từ điển (Lexicographical order - tra từ điển A-Z)
- **C.** Theo số lượng nguyên âm
- **D.** Ngẫu nhiên
- > *Giải thích:* Thứ tự từ điển so sánh mã ASCII của từng ký tự từ trái qua phải: `'apple' < 'banana' < 'cherry'`.

#### Câu 12: Đoạn code sau in ra giá trị gì?
```python
a = [10, 20, 30]
print(sum(a) - max(a) - min(a))
```
- **A.** 0
- **B.** 10
- **C.** **[Đáp án đúng]** 20
- **D.** 30
- > *Giải thích:* Tổng $10+20+30=60$. Trừ max (30) trừ min (10) còn lại đúng phần tử ở giữa là 20.

#### Câu 13: Cú pháp nào sau đây dùng để lọc bỏ toàn bộ phần tử trùng lặp và giữ lại các số độc nhất sắp xếp tăng dần?
- **A.** `unique(a)`
- **B.** **[Đáp án đúng]** `sorted(list(set(a)))`
- **C.** `a.distinct()`
- **D.** `a.filter()`
- > *Giải thích:* `set(a)` loại bỏ phần tử trùng lặp, `list(...)` chuyển lại thành danh sách, `sorted(...)` sắp xếp tăng dần.

#### Câu 14: Thuật toán sắp xếp tích hợp sẵn trong Python có tên là gì?
- **A.** Bubble Sort (Sắp xếp nổi bọt)
- **B.** Quick Sort (Sắp xếp nhanh)
- **C.** **[Đáp án đúng]** Timsort (Thuật toán lai ghép tối ưu cực nhanh)
- **D.** Selection Sort (Sắp xếp chọn)
- > *Giải thích:* Timsort do Tim Peters sáng tạo năm 2002, kết hợp Merge Sort và Insertion Sort, có độ phức tạp trung bình $\mathcal{O}(N \log N)$.

#### Câu 15: Cho danh sách `diem = [9.5, 8.0, 10.0, 7.5]`. Để in ra điểm số cao thứ nhì, câu lệnh chuẩn nhất là:
- **A.** `diem.sort(); print(diem[1])`
- **B.** **[Đáp án đúng]** `diem.sort(); print(diem[-2])`
- **C.** `print(max(diem) - 1)`
- **D.** `print(diem[2])`
- > *Giải thích:* Sắp xếp tăng dần: điểm cao nhất ở `diem[-1]`, điểm cao thứ nhì ở `diem[-2]`.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 12: Thống kê danh sách và sắp xếp

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L17-P01` | Điểm số cao nhất & thấp nhất | `Cơ bản` | $N \le 1000$ | Dùng hàm `max()` và `min()` |
| 02 | `PYA-L17-P02` | Sắp xếp tăng dần đơn giản | `Cơ bản` | $N \le 1000$ | Sử dụng `a.sort()` |
| 03 | `PYA-L17-P03` | Điểm trung bình môn học | `Cơ bản` | $N \le 1000$ | Tính `sum(a) / len(a)` làm tròn 2 chữ số |
| 04 | `PYA-L17-P04` | Sắp xếp giảm dần bảng xếp hạng | `Cơ bản` | $N \le 10^5$ | Sử dụng `a.sort(reverse=True)` |
| 05 | `PYA-L17-P05` | Tìm số lớn thứ nhì trong mảng | `Cơ bản` | $N \le 10^5$ | Tìm số lớn thứ hai (loại trừ các số bằng max) |
| 06 | `PYA-L17-P06` | Đếm số lượng học sinh trên điểm trung bình | `Luyện tập` | $N \le 10^5$ | So sánh từng phần tử với giá trị trung bình |
| 07 | `PYA-L17-P07` | Lọc bỏ các số trùng lặp | `Luyện tập` | $N \le 10^5$ | Giữ lại các số độc nhất tăng dần |
| 08 | `PYA-L17-P08` | Điểm Olympic bỏ max bỏ min | `Luyện tập` | $N \ge 3, N \le 1000$ | Bỏ 1 điểm cao nhất và 1 điểm thấp nhất |
| 09 | `PYA-L17-P09` | Sắp xếp tên theo thứ tự bảng chữ cái | `Luyện tập` | $N \le 1000$ từ | Sắp xếp mảng chuỗi |
| 10 | `PYA-L17-P10` | Chênh lệch nhỏ nhất giữa hai số | `Luyện tập` | $N \le 10^5$ | Sắp xếp mảng rồi tìm $\min(A_{i+1} - A_i)$ |
| 11 | `PYA-L17-P11` | Trung vị của dãy số (median) | `Luyện tập` | $N \le 10^5$ | Tìm phần tử chính giữa sau khi sắp xếp |
| 12 | `PYA-L17-P12` | Số xuất hiện nhiều lần nhất (mode) | `Vận dụng` | $N \le 10^5$ | Thống kê tần số xuất hiện cực đại |
| 13 | `PYA-L17-P13` | Ghép hai dãy đã sắp xếp | `Vận dụng` | $N, M \le 10^5$ | Hợp nhất 2 mảng tăng dần thành mảng tăng dần |
| 14 | `PYA-L17-P14` | Xếp hàng mua trà sữa (tổng thời gian chờ ít nhất) | `Thử thách` | $N \le 10^5$ | Thuật toán tham lam (greedy) bằng sắp xếp |

---

### Bài 1 (Cơ bản): Điểm số cao nhất & thấp nhất (`PYA-L17-P01`)

* **Yêu cầu:** Cho danh sách điểm thi của $N$ bạn học sinh. Hãy in ra điểm số cao nhất và điểm số thấp nhất trong danh sách.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
  * Dòng 2: $N$ số nguyên là điểm của các bạn ($0 \le A_i \le 100$).
* **Output:** Điểm cao nhất, theo sau là điểm thấp nhất.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`80 95 60 100 75` | `100 60` |

---

### Bài 2 (Cơ bản): Sắp xếp tăng dần đơn giản (`PYA-L17-P02`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy sắp xếp dãy số theo thứ tự tăng dần và in ra màn hình trên một dòng.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi sắp xếp tăng dần, cách nhau bởi khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`9 2 7 1 5` | `1 2 5 7 9` |

---

### Bài 3 (Cơ bản): Điểm trung bình môn học (`PYA-L17-P03`)

* **Yêu cầu:** Cho danh sách điểm kiểm tra của $N$ bài thi. Hãy tính điểm trung bình cộng của các bài thi và in ra với đúng 2 chữ số sau dấu phẩy.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
  * Dòng 2: $N$ số thực hoặc số nguyên là điểm các bài thi.
* **Output:** Điểm trung bình cộng (định dạng `f"{tb:.2f}"`).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4`<br>`8 9 7 10` | `8.50` | $(8 + 9 + 7 + 10) / 4 = 8.5$. |

---

### Bài 4 (Cơ bản): Sắp xếp giảm dần bảng xếp hạng (`PYA-L17-P04`)

* **Yêu cầu:** Cho danh sách điểm số của $N$ thí sinh tham gia cuộc thi. Hãy sắp xếp bảng điểm theo thứ tự từ cao xuống thấp (giảm dần) để trao giải.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Bảng điểm sắp xếp giảm dần trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`20 80 40 100 60` | `100 80 60 40 20` |

---

### Bài 5 (Cơ bản): Tìm số lớn thứ nhì trong mảng (`PYA-L17-P05`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn thứ nhì trong dãy số (nghĩa là giá trị lớn nhất trong số các phần tử nhỏ hơn giá trị cực đại). Nếu tất cả các phần tử trong mảng đều bằng nhau, in ra `KHONG CO`.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Giá trị lớn thứ nhì, hoặc `KHONG CO`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`10 20 20 15 5` | `15` | Số lớn nhất là 20. Số lớn thứ hai nhỏ hơn 20 là 15. |
  | `3`<br>`5 5 5` | `KHONG CO` | Tất cả bằng nhau. |

---

### Bài 6 (Luyện tập): Đếm số lượng học sinh trên điểm trung bình (`PYA-L17-P06`)

* **Yêu cầu:** Cho điểm thi của $N$ học sinh. Hãy đếm xem có bao nhiêu bạn học sinh có điểm số lớn hơn hoặc bằng điểm trung bình cộng của cả lớp.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số thực.
* **Output:** Số lượng học sinh đạt điểm $\ge$ điểm trung bình.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4`<br>`8 6 10 4` | `2` | Điểm TB: $(8+6+10+4)/4 = 7.0$. Các bạn có điểm $\ge 7$ là 8 và 10 (có 2 bạn). |

---

### Bài 7 (Luyện tập): Lọc bỏ các số trùng lặp (`PYA-L17-P07`)

* **Yêu cầu:** Cho dãy gồm $N$ số nguyên có thể chứa nhiều số bị trùng lặp. Hãy lọc bỏ các phần tử trùng lặp và in ra các số độc nhất theo thứ tự tăng dần.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Các số độc nhất sắp xếp tăng dần trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `7`<br>`3 1 4 1 5 9 2` | `1 2 3 4 5 9` |

---

### Bài 8 (Luyện tập): Điểm Olympic bỏ max bỏ min (`PYA-L17-P08`)

* **Bối cảnh:** Trong hội thi Bơi lội Olympic, có $N$ giám khảo chấm điểm ($N \ge 3$). Để đảm bảo công bằng tuyệt đối, điểm số chính thức của vận động viên là trung bình cộng sau khi đã **bỏ đi một điểm cao nhất và một điểm thấp nhất**.
* **Yêu cầu:** Cho $N$ điểm số. Hãy tính điểm chính thức của vận động viên (làm tròn 2 chữ số thập phân).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($3 \le N \le 1000$).
  * Dòng 2: $N$ số thực cách nhau bởi khoảng trắng.
* **Output:** Điểm trung bình sau khi loại bỏ 1 điểm max và 1 điểm min.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`7.0 9.0 8.0 10.0 6.0` | `8.00` | Bỏ min là 6.0, bỏ max là 10.0. Còn lại: 7.0, 8.0, 9.0. Trung bình là 8.00. |

---

### Bài 9 (Luyện tập): Sắp xếp tên theo thứ tự bảng chữ cái (`PYA-L17-P09`)

* **Yêu cầu:** Cho danh sách gồm $N$ từ tiếng Anh. Hãy sắp xếp danh sách từ theo thứ tự từ điển A-Z (tăng dần).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
  * Dòng 2: $N$ từ viết thường cách nhau bởi khoảng trắng.
* **Output:** Danh sách từ sau khi sắp xếp trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4`<br>`orange apple banana grape` | `apple banana grape orange` |

---

### Bài 10 (Luyện tập): Chênh lệch nhỏ nhất giữa hai số (`PYA-L17-P10`)
*(Đề thi Python Bảng A)*

* **Yêu cầu:** Cho dãy $N$ số nguyên đôi một khác nhau. Hãy tìm độ chênh lệch nhỏ nhất giữa 2 phần tử bất kỳ trong dãy (tức là giá trị $|A_i - A_j|$ nhỏ nhất với $i \ne j$).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Độ chênh lệch nhỏ nhất.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4`<br>`10 1 8 15` | `2` | Sắp xếp: [1, 8, 10, 15]. Chênh lệch giữa 8 và 10 là $|10 - 8| = 2$ (nhỏ nhất). |

---

### Bài 11 (Luyện tập): Trung vị của dãy số (median) (`PYA-L17-P11`)

* **Bối cảnh:** Cho một dãy gồm $N$ số nguyên lẻ phần tử ($N$ là số lẻ). Trung vị của dãy là phần tử nằm chính giữa sau khi dãy đã được sắp xếp tăng dần.
* **Yêu cầu:** Cho dãy $N$ số nguyên ($N$ lẻ). Hãy tìm số trung vị của dãy số.
* **Input:**
  * Dòng 1: Số nguyên lẻ $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Giá trị trung vị.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`10 2 8 4 6` | `6` | Sắp xếp: [2, 4, 6, 8, 10]. Số chính giữa là 6. |

---

### Bài 12 (Vận dụng): Số xuất hiện nhiều lần nhất (mode) (`PYA-L17-P12`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy tìm số xuất hiện nhiều lần nhất trong dãy. Nếu có nhiều số có cùng số lần xuất hiện nhiều nhất, hãy in ra số có giá trị nhỏ nhất trong các số đó.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Số xuất hiện nhiều nhất.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `7`<br>`2 3 5 2 3 7 2` | `2` |

---

### Bài 13 (Vận dụng): Ghép hai dãy đã sắp xếp (`PYA-L17-P13`)

* **Yêu cầu:** Cho hai dãy số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy ghép hai dãy lại thành một dãy duy nhất gồm $(N + M)$ phần tử cũng được sắp xếp tăng dần.
* **Input:**
  * Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 10^5$).
  * Dòng 2: $N$ số nguyên của dãy $A$.
  * Dòng 3: $M$ số nguyên của dãy $B$.
* **Output:** Dãy hợp nhất gồm $(N + M)$ phần tử tăng dần trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `3 4`<br>`1 4 7`<br>`2 3 5 8` | `1 2 3 4 5 7 8` |

---

### Bài 14 (Thử thách): Xếp hàng mua trà sữa (greedy) (`PYA-L17-P14`)
*(Đề thi Lập trình Python Quốc gia Bảng A)*

* **Bối cảnh:** Có $N$ bạn học sinh cùng xếp hàng mua trà sữa. Bạn thứ $i$ cần $T_i$ phút để người bán hàng pha chế xong cốc trà sữa của mình.
  Tổng thời gian chờ đợi của tất cả các bạn sẽ là tổng thời gian mà mỗi bạn phải đứng xếp hàng chờ cho đến khi nhận được trà sữa.
* **Yêu cầu:** Hãy tìm cách sắp xếp thứ tự các bạn vào mua trà sữa sao cho **tổng thời gian chờ đợi của tất cả các bạn là NHỎ NHẤT CÓ THỂ**. Hãy in ra tổng thời gian chờ đợi nhỏ nhất đó.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên $T_i$ ($1 \le T_i \le 1000$).
* **Output:** Một số nguyên duy nhất là tổng thời gian chờ đợi nhỏ nhất.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`3 1 2` | `10` | Sắp xếp người làm nhanh lên trước: thời gian làm lần lượt là 1, 2, 3.<br>- Bạn 1 chờ 1 phút.<br>- Bạn 2 chờ $1 + 2 = 3$ phút.<br>- Bạn 3 chờ $1 + 2 + 3 = 6$ phút.<br>Tổng thời gian chờ: $1 + 3 + 6 = 10$ phút (tối ưu nhất). |


================================================================================
# CHƯƠNG 06: XỬ LÝ CHUỖI & KÝ TỰ
================================================================================


--------------------------------------------------------------------------------
<!-- Bài 13: lesson-13 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 13: Chỉ số và cắt lát chuỗi

## 1. Tóm tắt kiến thức trọng tâm
- Chuỗi ký tự (String) đánh chỉ số bắt đầu từ **0**.
  - Ký tự đầu tiên: `s[0]`.
  - Ký tự cuối cùng: `s[-1]`.
  - Độ dài chuỗi: `len(s)`.
- **Cắt lát chuỗi (Slicing) `s[start:stop]`:** Lấy từ `start` đến `stop - 1`.
  - Lấy $K$ ký tự đầu: `s[:K]`.
  - Lấy từ vị trí $K$ đến hết: `s[K:]`.
  - **Đảo ngược chuỗi tức thì:** `s[::-1]`.
- Chuỗi trong Python là **bất biến (Immutable)**: Không thể gán sửa trực tiếp `s[0] = 'X'`.

## 2. Concept quiz: 14 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Ký tự đầu tiên của chuỗi `s = "VIETNAM"` có chỉ số index là bao nhiêu?
- **A.** 1
- **B.** **[Đáp án đúng]** 0
- **C.** -1
- **D.** Không có chỉ số
- > *Giải thích:* Trong Python và khoa học máy tính, chỉ số chuỗi luôn bắt đầu từ 0.

#### Câu 2: Biểu thức `s[-1]` dùng để làm gì?
- **A.** Lấy ký tự đầu tiên
- **B.** Xóa một ký tự
- **C.** **[Đáp án đúng]** Lấy ký tự cuối cùng của chuỗi
- **D.** Đếm số ký tự
- > *Giải thích:* Chỉ số âm đếm ngược từ phải sang trái, `-1` là phần tử cuối cùng.

#### Câu 3: Cho chuỗi `s = "TIN HOC"`. Hàm `len(s)` trả về kết quả là:
- **A.** 6
- **B.** **[Đáp án đúng]** 7
- **C.** 8
- **D.** 5
- > *Giải thích:* Dấu cách (khoảng trắng) cũng được tính là một ký tự: 'T','I','N',' ','H','O','C' = 7.

#### Câu 4: Cho `s = "PYTHON"`. Lệnh `print(s[6])` sẽ dẫn đến điều gì?
- **A.** In ra chữ cái cuối cùng
- **B.** In ra khoảng trắng
- **C.** **[Đáp án đúng]** Báo lỗi `IndexError: string index out of range`
- **D.** In ra số 6
- > *Giải thích:* Độ dài chuỗi là 6 thì chỉ số lớn nhất chỉ là 5. Gọi `s[6]` là vượt quá giới hạn.

#### Câu 5: Cho chuỗi `s = "HELLO"`. Kết quả của `s[1:4]` là gì?
- **A.** `"HEL"`
- **B.** `"HELL"`
- **C.** **[Đáp án đúng]** `"ELL"`
- **D.** `"ELLO"`
- > *Giải thích:* Lấy từ index 1 (`'E'`), 2 (`'L'`), 3 (`'L'`). Không lấy index 4.

#### Câu 6: Cú pháp nào sau đây giúp đảo ngược toàn bộ chuỗi `s` trong Python?
- **A.** `s.reverse()`
- **B.** `s[0:-1]`
- **C.** **[Đáp án đúng]** `s[::-1]`
- **D.** `s[1:len(s)]`
- > *Giải thích:* `s[::-1]` là cú pháp slicing với bước nhảy `-1` lùi từ cuối về đầu.

#### Câu 7: Chuỗi trong Python có cho phép gán đè ký tự trực tiếp như `s[0] = 'A'` không?
- **A.** Có, thay đổi bình thường
- **B.** **[Đáp án đúng]** Không, chuỗi trong Python là kiểu bất biến (Immutable), lệnh này báo lỗi `TypeError`
- **C.** Chỉ đổi được nếu chuỗi viết hoa
- **D.** Tự động thêm vào cuối
- > *Giải thích:* Chuỗi là đối tượng bất biến (Immutable) trong Python, không thể gán lại từng ký tự qua index.

#### Câu 8: Cho `s = "ABCDEF"`. Lệnh `s[::2]` sẽ in ra:
- **A.** `"ABC"`
- **B.** `"DEF"`
- **C.** **[Đáp án đúng]** `"ACE"`
- **D.** `"BDF"`
- > *Giải thích:* Bước nhảy `step = 2`: lấy vị trí 0 (`'A'`), vị trí 2 (`'C'`), vị trí 4 (`'E'`).

#### Câu 9: Cho `s = "KHOAHOC"`. Biểu thức `s[:4]` tương đương với:
- **A.** `s[0:4]`
- **B.** **[Đáp án đúng]** Lấy 4 ký tự đầu tiên (`"KHOA"`)
- **C.** Cả A và B đều đúng
- **D.** `s[1:4]`
- > *Giải thích:* Khuyết `start` mặc định là từ đầu (index 0).

#### Câu 10: Cho `s = "LAPTRINH"`. Biểu thức `s[3:]` cho kết quả:
- **A.** `"LAP"`
- **B.** **[Đáp án đúng]** `"TRINH"`
- **C.** `"PTRINH"`
- **D.** `"TRIN"`
- > *Giải thích:* Bắt đầu từ index 3 (chữ `'T'`) và lấy đến hết chuỗi.

#### Câu 11: Cho đoạn code sau:
```python
s = "12345"
print(s[1] + s[2])
```
Kết quả in ra là gì?
- **A.** 5
- **B.** **[Đáp án đúng]** `"23"`
- **C.** 23 (số nguyên)
- **D.** Báo lỗi
- > *Giải thích:* `s` là chuỗi nên `s[1]` là `'2'` và `s[2]` là `'3'`. Phép cộng chuỗi nối thành `"23"`.

#### Câu 12: Biểu thức kiểm tra một từ `w` có phải là từ đối xứng (palindrome) hay không là:
- **A.** `w == w`
- **B.** `len(w) % 2 == 0`
- **C.** **[Đáp án đúng]** `w == w[::-1]`
- **D.** `w[0] == w[-1]`
- > *Giải thích:* Từ đối xứng khi đọc ngược lại giống hệt từ ban đầu.

#### Câu 13: Cho `s = "iKHEDU"`. Lệnh `s[-3:]` trả về:
- **A.** `"iKH"`
- **B.** **[Đáp án đúng]** `"EDU"`
- **C.** `"ED"`
- **D.** `"DU"`
- > *Giải thích:* Index -3 là chữ `'E'`, lấy đến hết chuỗi là `"EDU"`.

#### Câu 14: Biểu thức `s[:-1]` có tác dụng gì?
- **A.** Lấy ký tự cuối cùng
- **B.** **[Đáp án đúng]** Cắt bỏ đi ký tự cuối cùng của chuỗi (lấy từ đầu đến sát cuối)
- **C.** Đảo ngược chuỗi
- **D.** Báo lỗi cú pháp
- > *Giải thích:* Cắt từ đầu đến trước vị trí `-1`, tức là bỏ đi ký tự cuối cùng.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 13: Chỉ số và cắt lát chuỗi

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L13-P01` | Ký tự đầu & ký tự cuối | `Cơ bản` | Độ dài chuỗi $\le 100$ | Truy xuất `s[0]` và `s[-1]` |
| 02 | `PYA-L13-P02` | Độ dài của chuỗi | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Sử dụng hàm `len(s)` |
| 03 | `PYA-L13-P03` | Cắt ba ký tự đầu tiên | `Cơ bản` | Chuỗi có $\ge 3$ ký tự | Slicing tiền tố `s[:3]` |
| 04 | `PYA-L13-P04` | Đảo ngược tên riêng | `Cơ bản` | Độ dài chuỗi $\le 100$ | Slicing đảo chuỗi `s[::-1]` |
| 05 | `PYA-L13-P05` | Kiểm tra từ đối xứng (palindrome) | `Cơ bản` | Độ dài chuỗi $\le 1000$ | `if s == s[::-1]` |
| 06 | `PYA-L13-P06` | Cắt đôi chuỗi ký tự | `Luyện tập` | Độ dài chuỗi chẵn $\le 1000$ | Cắt nửa đầu và nửa sau `s[:n//2]` và `s[n//2:]` |
| 07 | `PYA-L13-P07` | Rút trích tên miền email | `Luyện tập` | Chuỗi email hợp lệ | Cắt chuỗi sau ký tự `@` |
| 08 | `PYA-L13-P08` | Ký tự ở vị trí chẵn | `Luyện tập` | Độ dài chuỗi $\le 1000$ | Slicing bước nhảy `s[::2]` |
| 09 | `PYA-L13-P09` | Hoán đổi nửa đầu nửa sau | `Luyện tập` | Độ dài chuỗi chẵn $\le 10^5$ | Nối chuỗi `s[n//2:] + s[:n//2]` |
| 10 | `PYA-L13-P10` | Xóa ký tự ở vị trí K | `Luyện tập` | Độ dài chuỗi $\le 1000$ | Ghép `s[:k] + s[k+1:]` |
| 11 | `PYA-L13-P11` | Dịch chuyển vòng quanh (left rotation) | `Vận dụng` | $N \le 10^5, K \le N$ | Dịch trái chuỗi $K$ vị trí `s[k:] + s[:k]` |
| 12 | `PYA-L13-P12` | Chuỗi con đối xứng dài nhất | `Thử thách` | Độ dài chuỗi $\le 200$ | Duyệt mọi chuỗi con và tìm đối xứng cực đại |

---

### Bài 1 (Cơ bản): Ký tự đầu & ký tự cuối (`PYA-L13-P01`)

* **Yêu cầu:** Nhập vào một chuỗi ký tự $S$ không chứa dấu cách. Hãy in ra ký tự đầu tiên và ký tự cuối cùng của chuỗi $S$, cách nhau bởi một dấu cách.
* **Input:** Một chuỗi ký tự $S$ ($1 \le |S| \le 100$).
* **Output:** Ký tự đầu và ký tự cuối.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `PYTHON` | `P N` |

---

### Bài 2 (Cơ bản): Độ dài của chuỗi (`PYA-L13-P02`)

* **Yêu cầu:** Nhập một dòng văn bản $S$ từ bàn phím. Hãy đếm và in ra xem chuỗi $S$ có bao nhiêu ký tự (tính cả các ký tự khoảng trắng nếu có).
* **Input:** Một chuỗi ký tự $S$.
* **Output:** Một số nguyên là độ dài chuỗi.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Lap trinh` | `11` |

---

### Bài 3 (Cơ bản): Cắt ba ký tự đầu tiên (`PYA-L13-P03`)

* **Yêu cầu:** Nhập vào một chuỗi $S$ có ít nhất 3 ký tự. Hãy in ra 3 ký tự đầu tiên của chuỗi đó.
* **Input:** Một chuỗi $S$ ($3 \le |S| \le 100$).
* **Output:** 3 ký tự đầu tiên.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `VIETNAM` | `VIE` |
* **Gợi ý:** Sử dụng `print(s[:3])`.

---

### Bài 4 (Cơ bản): Đảo ngược tên riêng (`PYA-L13-P04`)

* **Bối cảnh:** Bé Bo muốn tạo ra một biệt danh bí mật bằng cách đọc ngược tên của mình.
* **Yêu cầu:** Nhập một chuỗi ký tự $S$. Hãy in ra chuỗi đảo ngược của $S$.
* **Input:** Một chuỗi ký tự $S$.
* **Output:** Chuỗi $S$ sau khi đảo ngược.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `DORAEMON` | `NOMEAROD` |

---

### Bài 5 (Cơ bản): Kiểm tra từ đối xứng (palindrome) (`PYA-L13-P05`)
*(Bài toán kinh điển Python Bảng A)*

* **Bối cảnh:** Một từ được gọi là từ đối xứng nếu đọc xuôi hay đọc ngược đều hoàn toàn giống nhau (ví dụ: `radar`, `level`, `madam`, `noon`).
* **Yêu cầu:** Cho một từ $S$. Kiểm tra xem $S$ có phải từ đối xứng không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một chuỗi $S$ viết liền ($1 \le |S| \le 1000$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `RADAR` | `YES` |
  | `ROBOT` | `NO` |

---

### Bài 6 (Luyện tập): Cắt đôi chuỗi ký tự (`PYA-L13-P06`)

* **Yêu cầu:** Cho một chuỗi $S$ có độ dài chẵn. Hãy chia chuỗi $S$ thành 2 nửa bằng nhau và in mỗi nửa trên một dòng.
* **Input:** Một chuỗi $S$ có độ dài chẵn ($2 \le |S| \le 1000$).
* **Output:** Dòng 1 in nửa đầu, dòng 2 in nửa sau.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `PYTHON` | `PYT`<br>`HON` |

---

### Bài 7 (Luyện tập): Rút trích tên miền email (`PYA-L13-P07`)

* **Bối cảnh:** Trong địa chỉ thư điện tử dạng `tentaikhoan@domain.com`, phần đứng sau ký tự `@` được gọi là tên miền (domain).
* **Yêu cầu:** Cho một địa chỉ email hợp lệ. Hãy in ra phần tên miền của địa chỉ đó.
* **Input:** Một chuỗi email chứa đúng 1 ký tự `@`.
* **Output:** Phần tên miền đứng sau `@`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `hocsinh@ikhedu.vn` | `ikhedu.vn` |
* **Gợi ý:** Dùng `vitri = s.find('@')` sau đó cắt `s[vitri + 1:]`.

---

### Bài 8 (Luyện tập): Ký tự ở vị trí chẵn (`PYA-L13-P08`)

* **Yêu cầu:** Cho một chuỗi $S$. Hãy tạo ra một chuỗi mới chỉ gồm các ký tự nằm ở **chỉ số index chẵn** ($0, 2, 4, 6 \dots$) của chuỗi $S$.
* **Input:** Một chuỗi ký tự $S$ ($1 \le |S| \le 1000$).
* **Output:** Chuỗi mới thu được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `ABCDEF` | `ACE` | Lấy các vị trí 0 ('A'), 2 ('C'), 4 ('E'). |

---

### Bài 9 (Luyện tập): Hoán đổi nửa đầu nửa sau (`PYA-L13-P09`)

* **Yêu cầu:** Cho chuỗi ký tự $S$ có độ dài chẵn $2N$. Hãy hoán đổi vị trí của nửa đầu chuỗi và nửa sau chuỗi với nhau.
* **Input:** Một chuỗi $S$ có độ dài chẵn ($2 \le |S| \le 10^5$).
* **Output:** Chuỗi sau khi hoán đổi 2 nửa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `ABCDEF` | `DEFABC` |

---

### Bài 10 (Luyện tập): Xóa ký tự ở vị trí K (`PYA-L13-P10`)

* **Bối cảnh:** Chuỗi trong Python là bất biến (không thể dùng lệnh xóa trực tiếp `del s[k]`). Ta phải dùng kỹ thuật cắt lát ghép chuỗi.
* **Yêu cầu:** Cho chuỗi $S$ và chỉ số nguyên $K$ ($0 \le K < |S|$). Hãy xóa ký tự tại vị trí $K$ và in ra chuỗi còn lại.
* **Input:** Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số nguyên $K$.
* **Output:** Chuỗi sau khi xóa ký tự thứ $K$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `PYTHON`<br>`2` | `PYHON` | Xóa ký tự tại index 2 là chữ 'T'. |
* **Gợi ý:** Sử dụng `s[:k] + s[k+1:]`.

---

### Bài 11 (Vận dụng): Dịch chuyển vòng quanh (left rotation) (`PYA-L13-P11`)

* **Bối cảnh:** Phép dịch trái chuỗi $K$ vị trí là thao tác nhấc $K$ ký tự đầu tiên của chuỗi đem gắn ra phía sau cùng.
  Ví dụ: Chuỗi `ABCDE` dịch trái 2 ký tự sẽ thành `CDEAB`.
* **Yêu cầu:** Cho chuỗi $S$ và số nguyên $K$ ($1 \le K \le |S| \le 10^5$). Hãy in ra chuỗi $S$ sau khi dịch trái $K$ vị trí.
* **Input:** Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số $K$.
* **Output:** Chuỗi sau khi dịch.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `ABCDE`<br>`2` | `CDEAB` |
* **Gợi ý:** `s[k:] + s[:k]`.

---

### Bài 12 (Thử thách): Chuỗi con đối xứng dài nhất (`PYA-L13-P12`)
*(Đề thi Học sinh giỏi Tin học Bảng A)*

* **Bối cảnh:** Một chuỗi con là một đoạn các ký tự liên tiếp nhau của chuỗi ban đầu.
* **Yêu cầu:** Cho một chuỗi ký tự $S$. Hãy tìm độ dài của chuỗi con liên tiếp đối xứng dài nhất nằm trong chuỗi $S$.
* **Input:** Một chuỗi ký tự $S$ ($1 \le |S| \le 200$).
* **Output:** Độ dài lớn nhất tìm được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `ABCBADE` | `5` | Chuỗi con đối xứng dài nhất là `ABCBA` có độ dài 5. |


--------------------------------------------------------------------------------
<!-- Bài 14: lesson-14 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 14: Duyệt chuỗi, biến đổi ký tự và tách từ

## 1. Tóm tắt kiến thức trọng tâm
- Duyệt từng ký tự: `for ch in s:`
- **Hàm kiểm tra:** `ch.isdigit()` (chữ số), `ch.isalpha()` (chữ cái), `ch.isupper()` (chữ hoa), `ch.islower()` (chữ thường).
- **Hàm biến đổi:** `s.upper()` (chuyển sang chữ hoa), `s.lower()` (chuyển sang chữ thường), `s.replace(old, new)`.
- **Tách từ và ghép từ:**
  - Tách các từ trong câu (tự động xóa dấu cách thừa): `danh_sach_tu = s.split()`
  - Ghép lại bằng 1 khoảng trắng: `" ".join(danh_sach_tu)`
- **Mã ASCII (`ord` và `chr`):**
  - `ord('A') == 65`, `ord('a') == 97`, `ord('0') == 48`.
  - `chr(65) == 'A'`.

---


## 2. Concept quiz: 26 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Vòng lặp `for ch in "ABC":` sẽ lặp lại bao nhiêu lần?
- **A.** 1 lần
- **B.** 2 lần
- **C.** **[Đáp án đúng]** 3 lần
- **D.** Vô tận
- > *Giải thích:* Chuỗi có 3 ký tự nên vòng lặp chạy đúng 3 lần, mỗi lần `ch` nhận một ký tự.

#### Câu 2: Kết quả của biểu thức `'9'.isdigit()` là gì?
- **A.** 9 (số nguyên)
- **B.** `False`
- **C.** **[Đáp án đúng]** `True`
- **D.** Báo lỗi
- > *Giải thích:* Ký tự `'9'` là một chữ số nên phương thức `isdigit()` trả về `True`.

#### Câu 3: Kết quả của biểu thức `'A'.islower()` là gì?
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `'a'`
- **D.** Báo lỗi
- > *Giải thích:* `'A'` là chữ in hoa, không phải chữ thường nên `islower()` trả về `False`.

#### Câu 4: Cho chuỗi `s = "Tin Hoc"`. Kết quả của `s.upper()` là:
- **A.** `"Tin Hoc"`
- **B.** `"tin hoc"`
- **C.** **[Đáp án đúng]** `"TIN HOC"`
- **D.** `"TINHOC"`
- > *Giải thích:* `upper()` chuyển toàn bộ các chữ cái trong chuỗi thành chữ in hoa.

#### Câu 5: Phương thức `s.count('a')` trên chuỗi `s = "Ha Noi Mua Thu"` trả về kết quả bằng bao nhiêu?
- **A.** 0
- **B.** **[Đáp án đúng]** 1 (Bẫy chữ hoa / chữ thường!)
- **C.** 2
- **D.** 3
- > *Giải thích:* Python phân biệt chữ hoa và chữ thường! Chữ `'H'` trong `"Ha"` đi kèm với chữ `'a'` thường (1 chữ). Trong chuỗi không còn chữ `'a'` thường nào khác.

#### Câu 6: Phương thức `ch.isalpha()` trả về `True` khi nào?
- **A.** Khi `ch` là một số
- **B.** **[Đáp án đúng]** Khi `ch` là một chữ cái trong bảng chữ cái (a-z hoặc A-Z)
- **C.** Khi `ch` là dấu cách
- **D.** Khi `ch` là ký tự đặc biệt
- > *Giải thích:* `isalpha` kiểm tra xem ký tự có phải là chữ cái (alphabet) hay không.

#### Câu 7: Đoạn code sau in ra kết quả gì?
```python
s = "A1B2C3"
kq = ""
for ch in s:
    if ch.isalpha():
        kq += ch
print(kq)
```
- **A.** `"123"`
- **B.** **[Đáp án đúng]** `"ABC"`
- **C.** `"A1B2C3"`
- **D.** Báo lỗi
- > *Giải thích:* Chỉ lọc và giữ lại các ký tự là chữ cái (`isalpha()`), loại bỏ các số 1, 2, 3.

#### Câu 8: Hàm nào sau đây dùng để chuyển một ký tự số như `'7'` thành số nguyên $7$?
- **A.** `str('7')`
- **B.** **[Đáp án đúng]** `int('7')`
- **C.** `float('7')`
- **D.** `chr('7')`
- > *Giải thích:* Hàm `int()` chuyển đổi chuỗi chứa số thành số nguyên để tính toán.

#### Câu 9: Cho `s = "hello"`. Câu lệnh `s.upper()` có làm thay đổi trực tiếp chuỗi `s` gốc không?
- **A.** Có, `s` biến thành `"HELLO"`
- **B.** **[Đáp án đúng]** Không, `s.upper()` chỉ tạo ra một chuỗi mới, chuỗi `s` gốc vẫn là `"hello"` (do chuỗi bất biến)
- **C.** Xóa chuỗi `s`
- **D.** Báo lỗi cú pháp
- > *Giải thích:* Để lưu lại chuỗi in hoa, ta phải gán lại: `s = s.upper()`.

#### Câu 10: Biểu thức kiểm tra một ký tự `ch` có phải là dấu cách (khoảng trắng) hay không là:
- **A.** `ch == ""`
- **B.** **[Đáp án đúng]** `ch == " "` hoặc `ch.isspace()`
- **C.** `ch == None`
- **D.** `len(ch) == 0`
- > *Giải thích:* Khoảng trắng là một ký tự chứa đúng một dấu cách `" "`.

#### Câu 11: Đoạn code sau làm công việc gì?
```python
s = "Covid-19"
dem = 0
for ch in s:
    if ch.isupper():
        dem += 1
print(dem)
```
- **A.** Đếm số chữ số
- **B.** **[Đáp án đúng]** Đếm số chữ cái in hoa (kết quả là 1 vì có chữ 'C')
- **C.** Đếm số ký tự
- **D.** Đếm dấu gạch nối
- > *Giải thích:* Duyệt chuỗi và đếm các ký tự thỏa mãn `isupper()`. Trong chuỗi chỉ có chữ 'C' là in hoa.

#### Câu 12: Ký tự `' '` (khoảng trắng) khi gọi `.isalpha()` sẽ trả về:
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** Báo lỗi
- **D.** `None`
- > *Giải thích:* Khoảng trắng không phải là chữ cái nên `isalpha()` trả về `False`.

#### Câu 13: Đoạn code sau tính điều gì?
```python
s = "2024"
tong = 0
for ch in s:
    tong += int(ch)
print(tong)
```
- **A.** Ghép thành `"2024"`
- **B.** **[Đáp án đúng]** Tính tổng các chữ số trong chuỗi ($2 + 0 + 2 + 4 = 8$)
- **C.** Báo lỗi kiểu dữ liệu
- **D.** Đếm số lượng chữ số
- > *Giải thích:* `int(ch)` chuyển từng ký tự số thành giá trị số học và cộng dồn vào `tong`.

#### Câu 14: Để thay thế tất cả chữ cái `'a'` thành `'o'` trong chuỗi `s`, ta dùng phương thức nào?
- **A.** `s.change('a', 'o')`
- **B.** **[Đáp án đúng]** `s.replace('a', 'o')`
- **C.** `s.swap('a', 'o')`
- **D.** `s.delete('a')`
- > *Giải thích:* Phương thức `replace(old, new)` thay thế các chuỗi con khớp với `old` bằng `new`.

#### Câu 15: Phương thức `s.split()` mặc định cắt chuỗi theo ký tự gì?
- **A.** Dấu phẩy
- **B.** **[Đáp án đúng]** Khoảng trắng (khoảng trắng đơn, nhiều khoảng trắng, dấu tab, xuống dòng)
- **C.** Dấu chấm
- **D.** Chữ cái đầu tiên
- > *Giải thích:* `split()` không truyền tham số sẽ tự động phân tách theo mọi khoảng trắng liên tiếp.

#### Câu 16: Cho `s = "An   Binh    Cuong"`. Biểu thức `len(s.split())` trả về:
- **A.** 3
- **B.** **[Đáp án đúng]** 3 (Bất chấp có bao nhiêu dấu cách giữa các từ!)
- **C.** 15
- **D.** 6
- > *Giải thích:* `split()` tự động gộp các khoảng trắng thừa thành một dấu phân cách duy nhất, danh sách còn đúng 3 từ.

#### Câu 17: Hàm `ord('A')` trong Python trả về giá trị là:
- **A.** 0
- **B.** 1
- **C.** **[Đáp án đúng]** 65
- **D.** 97
- > *Giải thích:* Mã ASCII của chữ cái 'A' in hoa là 65.

#### Câu 18: Hàm `chr(66)` trong Python trả về ký tự nào?
- **A.** `'A'`
- **B.** **[Đáp án đúng]** `'B'`
- **C.** `'6'`
- **D.** `'b'`
- > *Giải thích:* Mã ASCII 65 là 'A' nên mã 66 là 'B'.

#### Câu 19: Khoảng cách mã ASCII giữa chữ thường `'a'` và chữ hoa `'A'` (`ord('a') - ord('A')`) luôn bằng bao nhiêu?
- **A.** 26
- **B.** **[Đáp án đúng]** 32
- **C.** 10
- **D.** 48
- > *Giải thích:* $97 - 65 = 32$. Đây là hằng số dùng để chuyển đổi hoa-thường thủ công!

#### Câu 20: Cho `words = ['Python', 'la', 'so', '1']`. Biểu thức `" ".join(words)` tạo ra chuỗi gì?
- **A.** `"Pythonlaso1"`
- **B.** **[Đáp án đúng]** `"Python la so 1"`
- **C.** `['Python la so 1']`
- **D.** `"Python-la-so-1"`
- > *Giải thích:* `join()` lấy chuỗi phân cách đứng trước (ở đây là dấu cách `" "`) nối các phần tử lại với nhau.

#### Câu 21: Mã ASCII của ký tự chữ số `'0'` là bao nhiêu?
- **A.** 0
- **B.** **[Đáp án đúng]** 48
- **C.** 1
- **D.** 32
- > *Giải thích:* Ký tự `'0'` có mã ASCII là 48. Vì vậy `ord(ch) - 48` là cách chuyển ký tự số sang số nguyên nhanh!

#### Câu 22: Cho `ch = 'Z'`. Nếu dịch chuyển sang ký tự tiếp theo trong vòng tròn 26 chữ cái tiếng anh, ký tự đó là:
- **A.** `'['`
- **B.** **[Đáp án đúng]** `'A'`
- **C.** `'Z'`
- **D.** Không tồn tại
- > *Giải thích:* Trong mật mã Caesar xoay vòng (Modulo 26), sau 'Z' sẽ quay trở lại 'A'.

#### Câu 23: Đoạn code sau in ra từ nào?
```python
cau = "Ha Noi mua thu dep lam"
ds = cau.split()
print(ds[-1])
```
- **A.** `"Ha"`
- **B.** `"Noi"`
- **C.** **[Đáp án đúng]** `"lam"`
- **D.** `"dep"`
- > *Giải thích:* `ds[-1]` lấy phần tử cuối cùng trong danh sách các từ, đó là từ `"lam"`.

#### Câu 24: Phương thức `s.strip()` có tác dụng gì?
- **A.** Xóa tất cả các chữ cái
- **B.** **[Đáp án đúng]** Cắt bỏ toàn bộ các khoảng trắng thừa ở ĐẦU và ĐUÔI của chuỗi
- **C.** Đảo ngược chuỗi
- **D.** In hoa chuỗi
- > *Giải thích:* `strip()` dọn dẹp các khoảng trắng ở hai đầu chuỗi văn bản.

#### Câu 25: Biểu thức `chr(ord('c') - 32)` cho kết quả là gì?
- **A.** `'a'`
- **B.** `'d'`
- **C.** **[Đáp án đúng]** `'C'`
- **D.** `'c'`
- > *Giải thích:* Lấy mã ASCII của 'c' (99) trừ đi 32 được 67, là mã của chữ hoa 'C'.

#### Câu 26: Đoạn code sau in ra màn hình giá trị gì?
```python
cau = "lap trinh lap trinh Python"
ds = cau.split()
max_len = 0
for tu in ds:
    if len(tu) > max_len:
        max_len = len(tu)
print(max_len)
```
- **A.** 3
- **B.** 4
- **C.** **[Đáp án đúng]** 5
- **D.** 6
- > *Giải thích:* Độ dài các từ: 'lap' (3), 'trinh' (5), 'tin' (3), 'hoc' (3), 'tre' (3). Từ dài nhất có độ dài 5.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 14: Duyệt chuỗi, biến đổi ký tự và tách từ

---

## Bảng ma trận bài tập (24 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L14-P01` | In từng chữ cái xuống dòng | `Cơ bản` | Độ dài chuỗi $\le 100$ | Vòng lặp duyệt cơ bản `for ch in s` |
| 02 | `PYA-L14-P02` | Chuyển toàn bộ thành chữ hoa | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Sử dụng phương thức `s.upper()` |
| 03 | `PYA-L14-P03` | Đếm ký tự 'A' (cả hoa lẫn thường) | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Đếm với `ch.upper() == 'A'` |
| 04 | `PYA-L14-P04` | Đếm chữ cái in hoa & in thường | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Sử dụng `ch.isupper()` và `ch.islower()` |
| 05 | `PYA-L14-P05` | Tách riêng chữ số ra khỏi văn bản | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Lọc các ký tự thỏa mãn `ch.isdigit()` |
| 06 | `PYA-L14-P06` | Tính tổng các chữ số trong chuỗi | `Luyện tập` | Độ dài chuỗi $\le 10^5$ | Chuyển `int(ch)` và cộng dồn |
| 07 | `PYA-L14-P07` | Đổi chữ hoa thành thường & ngược lại | `Luyện tập` | Độ dài chuỗi $\le 1000$ | Đảo ngược trạng thái chữ (swap case) |
| 08 | `PYA-L14-P08` | Thay thế ký tự bí mật | `Luyện tập` | Độ dài chuỗi $\le 1000$ | Sử dụng phương thức `s.replace()` |
| 09 | `PYA-L14-P09` | Xóa bỏ toàn bộ dấu cách | `Luyện tập` | Độ dài chuỗi $\le 10^5$ | Lọc bỏ `ch == " "` |
| 10 | `PYA-L14-P10` | Đếm số lượng nguyên âm | `Luyện tập` | Độ dài chuỗi $\le 1000$ | Đếm các chữ cái thuộc tập `u, e, o, a, i` |
| 11 | `PYA-L14-P11` | Nén chuỗi ký tự (run-length encoding) | `Vận dụng` | Độ dài chuỗi $\le 1000$ | Đếm số ký tự liên tiếp giống nhau `AAABBC \to A3B2C1` |
| 12 | `PYA-L14-P12` | Trích xuất số lớn nhất trong văn bản | `Thử thách` | Độ dài chuỗi $\le 1000$ | Gom các cụm chữ số liên tiếp thành số nguyên |
| 13 | `PYA-L15-P01` | Đếm số từ trong câu | `Cơ bản` | Dòng văn bản $\le 1000$ ký tự | Sử dụng `len(s.split())` |
| 14 | `PYA-L15-P02` | Từ đầu tiên & từ cuối cùng | `Cơ bản` | Câu có ít nhất 1 từ | Truy xuất `ds[0]` và `ds[-1]` |
| 15 | `PYA-L15-P03` | Mã ASCII của ký tự | `Cơ bản` | 1 ký tự duy nhất | Hàm `ord(ch)` |
| 16 | `PYA-L15-P04` | Ký tự kế tiếp trong bảng chữ cái | `Cơ bản` | Ký tự từ 'A' đến 'y' | `chr(ord(ch) + 1)` |
| 17 | `PYA-L15-P05` | Tìm từ dài nhất trong câu | `Cơ bản` | Dòng văn bản $\le 1000$ ký tự | So sánh độ dài các từ sau `split()` |
| 18 | `PYA-L15-P06` | Chuẩn hóa khoảng trắng | `Luyện tập` | Dòng văn bản có nhiều dấu cách | `" ".join(s.split())` |
| 19 | `PYA-L15-P07` | Viết hoa chữ cái đầu mỗi từ (title case) | `Luyện tập` | Dòng văn bản $\le 1000$ ký tự | Chuẩn hóa họ và tên người |
| 20 | `PYA-L15-P08` | Đảo ngược từng từ trong câu | `Luyện tập` | Dòng văn bản $\le 1000$ ký tự | Đảo ngược từng từ giữ nguyên thứ tự từ |
| 21 | `PYA-L15-P09` | Mật mã Caesar dịch chuyển K | `Luyện tập` | Chuỗi in hoa, $1 \le K \le 25$ | Thuật toán mã hóa Caesar cổ điển |
| 22 | `PYA-L15-P10` | Giải mã mật thư Caesar | `Luyện tập` | Chuỗi in hoa, $1 \le K \le 25$ | Dịch ngược $K$ vị trí để tìm thông điệp gốc |
| 23 | `PYA-L15-P11` | Từ xuất hiện nhiều nhất trong đoạn | `Vận dụng` | Văn bản $\le 10^4$ ký tự | Đếm tần suất xuất hiện của từng từ |
| 24 | `PYA-L15-P12` | Mật mã thay thế hoán vị (anagram) | `Thử thách` | Hai chuỗi $\le 10^5$ ký tự | Kiểm tra 2 từ cấu tạo từ cùng tập ký tự |

---

### Bài 1 (Cơ bản): In từng chữ cái xuống dòng (`PYA-L14-P01`)

* **Yêu cầu:** Nhập vào một từ $S$. Hãy in ra từng chữ cái của từ đó, mỗi chữ cái nằm trên một dòng riêng biệt.
* **Input:** Một chuỗi ký tự $S$ ($1 \le |S| \le 100$).
* **Output:** Mỗi ký tự trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `CAT` | `C`<br>`A`<br>`T` |

---

### Bài 2 (Cơ bản): Chuyển toàn bộ thành chữ hoa (`PYA-L14-P02`)

* **Yêu cầu:** Nhập một dòng văn bản $S$. Hãy chuyển tất cả các chữ cái trong $S$ thành chữ in hoa và in ra màn hình.
* **Input:** Một dòng văn bản $S$.
* **Output:** Chuỗi sau khi đã in hoa toàn bộ.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `ikhedu vietnam` | `IKHEDU VIETNAM` |

---

### Bài 3 (Cơ bản): Đếm ký tự 'A' (cả hoa lẫn thường) (`PYA-L14-P03`)

* **Yêu cầu:** Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu chữ cái `'A'` hoặc `'a'` xuất hiện trong chuỗi $S$.
* **Input:** Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng chữ cái 'A' hoặc 'a'.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `An va Ba hoc bai` | `4` | Gồm chữ 'A' (1 lần) và 'a' (3 lần trong 'va', 'Ba', 'bai'). |

---

### Bài 4 (Cơ bản): Đếm chữ cái in hoa & in thường (`PYA-L14-P04`)

* **Yêu cầu:** Cho một chuỗi $S$. Hãy đếm xem có bao nhiêu chữ cái in hoa và bao nhiêu chữ cái in thường trong chuỗi đó.
* **Input:** Chuỗi ký tự $S$.
* **Output:** Hai số nguyên cách nhau một khoảng trắng: số lượng chữ in hoa trước, số lượng chữ in thường sau.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `Lap Trinh Python` | `3 11` | Chữ in hoa: 'L', 'T', 'P' (3 chữ). |

---

### Bài 5 (Cơ bản): Tách riêng chữ số ra khỏi văn bản (`PYA-L14-P05`)

* **Bối cảnh:** Trong một văn bản mật mã có các chữ số bị giấu lẫn vào giữa các chữ cái.
* **Yêu cầu:** Cho chuỗi $S$. Hãy nhặt ra toàn bộ các ký tự là chữ số ('0' - '9') và ghép chúng lại theo thứ tự ban đầu để in ra màn hình. Nếu không có chữ số nào, in ra `KHONG CO`.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Chuỗi các chữ số ghép lại, hoặc `KHONG CO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Toi sinh nam 2014 vao thang 08` | `201408` |

---

### Bài 6 (Luyện tập): Tính tổng các chữ số trong chuỗi (`PYA-L14-P06`)

* **Yêu cầu:** Cho một chuỗi văn bản $S$. Hãy tính tổng giá trị của tất cả các chữ số xuất hiện trong chuỗi đó.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 10^5$).
* **Output:** Một số nguyên duy nhất là tổng các chữ số.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `A1B2C3D4` | `10` | $1 + 2 + 3 + 4 = 10$. |

---

### Bài 7 (Luyện tập): Đổi chữ hoa thành thường & ngược lại (`PYA-L14-P07`)

* **Yêu cầu:** Cho chuỗi ký tự $S$. Hãy biến đổi chuỗi bằng quy tắc: chữ hoa đổi thành chữ thường, chữ thường đổi thành chữ hoa, các ký tự khác (số, dấu câu, khoảng trắng) giữ nguyên.
* **Input:** Một chuỗi văn bản $S$.
* **Output:** Chuỗi sau khi biến đổi.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Hello World 123` | `hELLO wORLD 123` |
* **Gợi ý:** Có thể dùng `s.swapcase()` hoặc duyệt từng ký tự.

---

### Bài 8 (Luyện tập): Thay thế ký tự bí mật (`PYA-L14-P08`)

* **Yêu cầu:** Nhập một chuỗi $S$. Hãy thay thế tất cả các ký tự khoảng trắng `" "` trong $S$ bằng dấu gạch dưới `"_"` và in ra kết quả.
* **Input:** Một chuỗi $S$.
* **Output:** Chuỗi sau khi thay thế.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `hoc lap trinh de vui` | `hoc_lap_trinh_de_vui` |
* **Gợi ý:** Dùng `s.replace(" ", "_")`.

---

### Bài 9 (Luyện tập): Xóa bỏ toàn bộ dấu cách (`PYA-L14-P09`)

* **Yêu cầu:** Cho một dòng văn bản $S$. Hãy xóa bỏ tất cả các ký tự khoảng trắng trong chuỗi để thu được một chuỗi viết liền hoàn toàn.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 10^5$).
* **Output:** Chuỗi viết liền không còn khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Lap Trinh Python Bang A` | `LapTrinhPythonBangA` |

---

### Bài 10 (Luyện tập): Đếm số lượng nguyên âm (`PYA-L14-P10`)

* **Bối cảnh:** Trong tiếng Anh, 5 chữ cái: `A, E, I, O, U` (cả hoa lẫn thường) được gọi là nguyên âm (vowels).
* **Yêu cầu:** Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu ký tự nguyên âm trong chuỗi $S$.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng nguyên âm.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `EDUCATION` | `5` | Các nguyên âm: E, U, A, I, O (có 5 nguyên âm). |

---

### Bài 11 (Vận dụng): Nén chuỗi ký tự (run-length encoding) (`PYA-L14-P11`)
*(Đề thi Python Bảng A)*

* **Bối cảnh:** Thuật toán nén chuỗi đơn giản thay thế một dãy các ký tự giống nhau liên tiếp bằng ký tự đó kèm theo số lần lặp lại.
  Ví dụ: `AAABBC` nén thành `A3B2C1`.
* **Yêu cầu:** Cho một chuỗi $S$ chỉ gồm các chữ cái in hoa. Hãy in ra dạng nén của chuỗi $S$.
* **Input:** Một chuỗi $S$ ($1 \le |S| \le 1000$).
* **Output:** Chuỗi sau khi nén.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `AAABBCCCC` | `A3B2C4` |

---

### Bài 12 (Thử thách): Trích xuất số lớn nhất trong văn bản (`PYA-L14-P12`)
*(Đề thi Lập trình Python cấp Tỉnh/Thành phố Bảng A)*

* **Bối cảnh:** Trong một bài báo cáo có các con số nằm rải rác giữa các câu chữ. Một con số có thể có nhiều chữ số liên tiếp nhau.
* **Yêu cầu:** Cho chuỗi văn bản $S$. Hãy tìm và in ra giá trị của **con số nguyên lớn nhất** xuất hiện trong chuỗi đó. Dữ liệu đảm bảo có ít nhất 1 chữ số.
* **Input:** Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số nguyên lớn nhất tìm được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `Lop 5A co 38 hoc sinh va 105 quyen sach` | `105` | Các con số xuất hiện là: 5, 38, 105. Số lớn nhất là 105. |

### Bài 13 (Cơ bản): Đếm số từ trong câu (`PYA-L15-P01`)

* **Yêu cầu:** Nhập một dòng văn bản $S$ có thể chứa nhiều khoảng trắng thừa ở đầu, cuối hoặc giữa các từ. Hãy đếm xem câu văn đó có bao nhiêu từ.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng từ trong câu.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `  Chuc   mung nam   moi   ` | `4` | Có 4 từ: 'Chuc', 'mung', 'nam', 'moi'. |

---

### Bài 14 (Cơ bản): Từ đầu tiên & từ cuối cùng (`PYA-L15-P02`)

* **Yêu cầu:** Cho một câu văn $S$. Hãy in ra từ đầu tiên và từ cuối cùng của câu văn đó trên 2 dòng riêng biệt.
* **Input:** Một dòng văn bản có ít nhất 1 từ.
* **Output:** Dòng 1 in từ đầu tiên, dòng 2 in từ cuối cùng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Hoc lap trinh Python cuc vui` | `Hoc`<br>`vui` |

---

### Bài 15 (Cơ bản): Mã ASCII của ký tự (`PYA-L15-P03`)

* **Yêu cầu:** Nhập một ký tự bất kỳ từ bàn phím. Hãy in ra mã số ASCII của ký tự đó.
* **Input:** Một ký tự duy nhất $C$.
* **Output:** Một số nguyên là mã ASCII.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `A` | `65` |
  | `a` | `97` |

---

### Bài 16 (Cơ bản): Ký tự kế tiếp trong bảng chữ cái (`PYA-L15-P04`)

* **Yêu cầu:** Nhập vào một chữ cái in hoa từ `'A'` đến `'Y'`. Hãy in ra chữ cái đứng ngay liền sau nó trong bảng chữ cái tiếng Anh.
* **Input:** Một ký tự in hoa $C \in ['A' \dots 'Y']$.
* **Output:** Chữ cái liền sau.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `C` | `D` |
* **Gợi ý:** `chr(ord(c) + 1)`.

---

### Bài 17 (Cơ bản): Tìm từ dài nhất trong câu (`PYA-L15-P05`)

* **Yêu cầu:** Cho một câu văn $S$. Hãy tìm và in ra từ có độ dài dài nhất trong câu. Nếu có nhiều từ cùng độ dài dài nhất, in ra từ đầu tiên xuất hiện.
* **Input:** Một dòng văn bản $S$.
* **Output:** Từ dài nhất tìm được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `Hoc lap trinh rat thu vi` | `trinh` | Từ 'trinh' có 5 chữ cái (dài nhất). |

---

### Bài 18 (Luyện tập): Chuẩn hóa khoảng trắng (`PYA-L15-P06`)

* **Bối cảnh:** Khi đánh máy, một bạn học sinh lỡ tay bấm rất nhiều dấu cách thừa giữa các từ và ở hai đầu câu văn.
* **Yêu cầu:** Cho chuỗi văn bản $S$. Hãy chuẩn hóa câu văn sao cho: không còn khoảng trắng ở đầu và cuối câu, giữa mỗi từ chỉ có duy nhất **một dấu cách**.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Câu văn chuẩn hóa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `   Python     rat   la     tuyet      ` | `Python rat la tuyet` |
* **Gợi ý:** Dùng `" ".join(s.split())`.

---

### Bài 19 (Luyện tập): Viết hoa chữ cái đầu mỗi từ (title case) (`PYA-L15-P07`)

* **Yêu cầu:** Nhập họ và tên của một bạn học sinh viết chưa đúng quy tắc (ví dụ: `nguyen van an`). Hãy chuẩn hóa họ tên bằng cách viết hoa chữ cái đầu tiên của mỗi từ và viết thường các chữ cái còn lại.
* **Input:** Một chuỗi họ tên.
* **Output:** Họ tên sau khi chuẩn hóa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `nguyen van an` | `Nguyen Van An` |

---

### Bài 20 (Luyện tập): Đảo ngược từng từ trong câu (`PYA-L15-P08`)

* **Yêu cầu:** Cho một câu văn. Hãy đảo ngược thứ tự các chữ cái trong từng từ một, nhưng giữ nguyên vị trí của các từ trong câu.
* **Input:** Một dòng văn bản.
* **Output:** Câu văn mới với từng từ bị đảo ngược.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `Toi yeu Viet Nam` | `ioT uey teiV maN` | 'Toi' -> 'ioT', 'yeu' -> 'uey'... |

---

### Bài 21 (Luyện tập): Mật mã Caesar dịch chuyển K (`PYA-L15-P09`)
*(Bài toán kinh điển Python Bảng A)*

* **Bối cảnh:** Hoàng đế Caesar mã hóa bức thư gồm các chữ cái in hoa (`'A'` đến `'Z'`) bằng cách dịch chuyển mỗi chữ cái sang phải $K$ bước theo vòng tròn 26 chữ cái ($A \to B \dots Z \to A$).
* **Yêu cầu:** Cho chuỗi $S$ chỉ gồm các chữ cái in hoa và số nguyên $K$ ($1 \le K \le 25$). Hãy in ra bản mật mã sau khi mã hóa.
* **Input:** Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số $K$.
* **Output:** Chuỗi sau khi mã hóa.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `ABCXYZ`<br>`3` | `DEFABC` | 'A'->'D', 'B'->'E', 'X'->'A', 'Y'->'B', 'Z'->'C'. |
* **Công thức toán học:** `chr((ord(ch) - ord('A') + k) % 26 + ord('A'))`.

---

### Bài 22 (Luyện tập): Giải mã mật thư Caesar (`PYA-L15-P10`)

* **Yêu cầu:** Cho một bản mật mã $S$ (chỉ gồm các chữ cái in hoa) đã bị mã hóa Caesar với bước nhảy $K$. Hãy giải mã để tìm lại thông điệp ban đầu.
* **Input:** Dòng 1 chứa bản mật mã $S$. Dòng 2 chứa số nguyên $K$ ($1 \le K \le 25$).
* **Output:** Thông điệp ban đầu trước khi mã hóa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `DEFABC`<br>`3` | `ABCXYZ` |

---

### Bài 23 (Vận dụng): Từ xuất hiện nhiều nhất trong đoạn (`PYA-L15-P11`)

* **Yêu cầu:** Cho một đoạn văn bản chỉ gồm các từ cách nhau bởi khoảng trắng. Hãy tìm xem từ nào xuất hiện nhiều lần nhất trong đoạn văn đó và xuất hiện bao nhiêu lần. Dữ liệu đảm bảo chỉ có 1 từ xuất hiện nhiều nhất.
* **Input:** Một đoạn văn bản $S$ gồm các chữ cái viết thường.
* **Output:** Từ xuất hiện nhiều nhất và số lần xuất hiện, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `cam quyt mit dua cam xoai cam dua` | `cam 3` |

---

### Bài 24 (Thử thách): Mật mã thay thế hoán vị (anagram) (`PYA-L15-P12`)
*(Đề thi Python Bảng A)*

* **Bối cảnh:** Hai từ được gọi là "Anagram" (hoán vị ký tự của nhau) nếu chúng có thể tạo thành từ nhau bằng cách xáo trộn lại thứ tự các chữ cái (ví dụ: `silent` và `listen`, `heart` và `earth`).
* **Yêu cầu:** Cho 2 từ $S_1$ và $S_2$. Kiểm tra xem chúng có phải là Anagram của nhau không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Hai dòng, mỗi dòng chứa một từ viết thường ($1 \le |S_1|, |S_2| \le 10^5$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `listen`<br>`silent` | `YES` |
  | `hello`<br>`world` | `NO` |
* **Gợi ý:** Kiểm tra nếu `sorted(s1) == sorted(s2)`.


================================================================================
# CHƯƠNG 07: LUYỆN ĐỀ THI
================================================================================


--------------------------------------------------------------------------------
<!-- Bài 15: lesson-15 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 15: Chiến lược giải đề Python Bảng A

## 1. Bản đồ 5 bước tác chiến trong phòng thi
```
BƯỚC 1: Đọc đề cẩn thận (Tối thiểu 2 lần, gạch chân Ràng buộc dữ liệu & Input/Output)
   │
BƯỚC 2: Nháp thuật toán & Dry Run tay với Sample Test trên giấy
   │
BƯỚC 3: Liệt kê các "Bẫy hiểm độc" (Edge Cases: N = 0, N = 1, số âm, số cực lớn)
   │
BƯỚC 4: Lập trình sạch sẽ, dùng đúng kiểu dữ liệu, in đúng từng chữ hoa/thường
   │
BƯỚC 5: Tự kiểm thử (Self-Testing) với test nhỏ nhất, test biên và test lớn nhất trước khi nộp!
```

## 2. Các tử huyệt làm mất điểm oan
- In thừa chữ dẫn dắt: Đề chỉ yêu cầu in `15`, viết `print("Ket qua la:", 15)` sẽ bị chấm `Wrong Answer (WA)` ngay lập tức.
- Không để ý giới hạn $N$: Nếu $N \le 10^5$ thì vòng lặp `for` an toàn. Nếu $N \ge 10^9$ bắt buộc phải dùng công thức giải tích $\mathcal{O}(1)$.

## 3. Concept quiz: 12 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Khi đề bài yêu cầu "in ra kết quả trên một dòng", nếu in thêm dòng chữ `"Ket qua la:"` thì hệ thống chấm thi tự động sẽ đánh giá thế nào?
- **A.** Vẫn được điểm tối đa vì code chạy đúng logic
- **B.** Được cộng điểm vì giải thích rõ ràng
- **C.** **[Đáp án đúng]** Bị chấm `Wrong Answer (WA)` (0 điểm) vì output không khớp chính xác với định dạng của đề bài
- **D.** Được nửa số điểm
- > *Giải thích:* Hệ thống chấm tự động so sánh từng ký tự trong file output của thí sinh với đáp án chuẩn. Mọi ký tự thừa hay thiếu đều bị coi là sai.

#### Câu 2: Khi đánh giá số vòng lặp trong chương trình Python, cách suy nghĩ nào phù hợp nhất?
- **A.** Chỉ nhìn vào số biến trong chương trình
- **B.** **[Đáp án đúng]** Ước lượng số lần lặp theo giới hạn dữ liệu và kiểm tra bằng test phù hợp
- **C.** Luôn chọn vòng lặp dài nhất
- **D.** Bỏ qua giới hạn thời gian
- > *Giải thích:* Tốc độ phụ thuộc vào môi trường, thao tác và dữ liệu. Điều cần làm là phân tích độ phức tạp, giới hạn đề bài và kiểm tra thực tế khi cần.

#### Câu 3: Nếu dữ liệu đầu vào cho $N \le 10^9$, thuật toán có độ phức tạp thời gian nào sau đây sẽ chắc chắn bị lỗi `Time Limit Exceeded` (tle)?
- **A.** $\mathcal{O}(1)$ (Công thức toán)
- **B.** **[Đáp án đúng]** $\mathcal{O}(N)$ (Vòng lặp chạy từ 1 đến $N$)
- **C.** $\mathcal{O}(\sqrt{N})$ (Vòng lặp chạy đến $\sqrt{N} \approx 31622$)
- **D.** $\mathcal{O}(\log N)$
- > *Giải thích:* Khi $N$ rất lớn, một vòng lặp tuyến tính có thể vượt giới hạn thời gian. Cần xem giới hạn cụ thể và tìm công thức hoặc cách giảm số bước nếu phù hợp.

#### Câu 4: Khi giải bài toán liên quan đến số tự nhiên $N$, các "test biên" (edge cases) bắt buộc phải tự kiểm tra tay trước tiên là:
- **A.** $N = 100$
- **B.** **[Đáp án đúng]** $N = 0$, $N = 1$, và giá trị $N$ nhỏ nhất / lớn nhất trong phạm vi đề bài cho
- **C.** $N = 50$
- **D.** $N$ là số ngẫu nhiên
- > *Giải thích:* Các bài toán tin học thường gài bẫy tại các điểm biên như 0, 1 hoặc giới hạn cực đại.

#### Câu 5: Dòng lệnh nào sau đây giúp đọc trọn vẹn cả một dòng văn bản chứa cả khoảng trắng trong Python?
- **A.** `input().split()`
- **B.** **[Đáp án đúng]** `s = input()`
- **C.** `s = int(input())`
- **D.** `s = input().strip().split()`
- > *Giải thích:* Hàm `input()` đọc nguyên vẹn cả dòng cho đến khi gặp phím Enter.

#### Câu 6: Trong Python, số nguyên có bị giới hạn kích thước tối đa là 32-bit hay 64-bit như trong pascal hay C++ không?
- **A.** Có, tối đa là $2 \times 10^9$
- **B.** Có, tối đa là $9 \times 10^{18}$
- **C.** **[Đáp án đúng]** Không, Python hỗ trợ số nguyên lớn (Arbitrary-precision integers) có thể chứa hàng nghìn chữ số mà không bao giờ bị tràn số
- **D.** Tối đa 100 chữ số
- > *Giải thích:* Đây là lợi thế cực lớn của Python so với các ngôn ngữ khác trong kỳ thi Lập trình Python Phổ thông: Không bao giờ lo bị tràn số!

#### Câu 7: Khi gặp một bài toán khó chưa nghĩ ra cách làm tối ưu $\mathcal{O}(1)$ hay $\mathcal{O}(N)$, chiến thuật khôn ngoan nhất trong phòng thi là gì?
- **A.** Bỏ bài đó để đi về sớm
- **B.** Ngồi nghĩ đến hết giờ
- **C.** **[Đáp án đúng]** Viết lời giải đơn giản trước, kiểm tra đúng đắn rồi cải thiện nếu giới hạn dữ liệu yêu cầu
- **D.** Viết ngẫu nhiên một câu lệnh print
- > *Giải thích:* Chiến thuật "vét điểm từng test": 50% điểm của một bài khó quý giá hơn là bỏ trắng 0 điểm.

#### Câu 8: Khi nộp bài lên hệ thống thi đấu, nếu nhận được thông báo lỗi `Memory Limit Exceeded` (mle), nguyên nhân là gì?
- **A.** Chạy quá thời gian quy định
- **B.** In ra sai đáp án
- **C.** **[Đáp án đúng]** Chương trình tiêu thụ quá nhiều bộ nhớ RAM (vượt mức 256MB quy định)
- **D.** Lỗi cú pháp
- > *Giải thích:* MLE xảy ra khi tạo mảng quá lớn hoặc để đệ quy quá sâu.

#### Câu 9: Để in ra số thực $X$ với đúng 2 chữ số sau dấu phẩy (làm tròn chuẩn), câu lệnh nào chuẩn xác nhất?
- **A.** `print(round(X, 2))`
- **B.** **[Đáp án đúng]** `print(f"{X:.2f}")`
- **C.** `print(int(X))`
- **D.** `print(X)`
- > *Giải thích:* `round(5.0, 2)` có thể chỉ in `5.0`. Dùng f-string định dạng `{X:.2f}` đảm bảo luôn in đủ 2 chữ số phần thập phân như `5.00`.

#### Câu 10: Tên file nộp bài trong các kỳ thi thường có định dạng như thế nào?
- **A.** Tên bất kỳ do thí sinh chọn
- **B.** **[Đáp án đúng]** Bắt buộc phải trùng khớp với mã bài toán theo quy định của ban tổ chức (ví dụ: `BAI1.PY`)
- **C.** Luôn luôn là `main.py`
- **D.** Tên của thí sinh
- > *Giải thích:* Đặt sai tên file hoặc sai phần mở rộng sẽ khiến máy chấm không tìm thấy bài và bị 0 điểm.

#### Câu 11: Trước khi nộp bài 5 phút, thí sinh nên làm việc gì nhất?
- **A.** Viết lại toàn bộ code của bài khó nhất
- **B.** **[Đáp án đúng]** Rà soát lại tất cả các dòng `print` thừa dùng để debug, kiểm tra tên file và bấm nộp thử lại toàn bộ các bài
- **C.** Tắt máy tính đi ra ngoài
- **D.** Sửa đổi các biến số
- > *Giải thích:* Rất nhiều thí sinh bị mất điểm vì quên xóa các dòng `print("debug: ...")` dẫn đến bị máy chấm bắt lỗi output thừa.

#### Câu 12: Phẩm chất quan trọng nhất của một tuyển thủ Lập trình Python xuất sắc là gì?
- **A.** Gõ bàn phím thật nhanh
- **B.** **[Đáp án đúng]** Tính kiên trì, tư duy cẩn trọng, đọc kỹ đề bài và không bao giờ bỏ cuộc
- **C.** Thuộc lòng code mẫu
- **D.** Chỉ làm các bài dễ
- > *Giải thích:* Sự kiên trì và tư duy logic sắc bén là chìa khóa mở cánh cửa đến với mọi thành công trong công nghệ và cuộc sống.

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 15: Chiến lược giải đề Python Bảng A

---

## 3 bộ đề thi thử Python Bảng A toàn diện (12 bài toán phân tầng chuẩn đề thi quốc gia)

Mỗi đề thi mô phỏng chính xác cấu trúc và thời gian làm bài của kỳ thi Python Bảng A (Phổ thông): thời gian 90 phút, gồm 4 bài toán từ khởi động đến phân loại học sinh giỏi.

---

### Phần 1: Đề thi thử số 01 (mô phỏng đề PYA thành phố hà nội / tp. Hồ chí minh)

#### Bài 1 (30 điểm): Mua bút tặng bạn (`PYA-L18-P01`)
* **Bối cảnh:** Đầu năm học mới, cửa hàng văn phòng phẩm có chương trình khuyến mãi: Mỗi chiếc bút có giá $P$ đồng. Nếu mua từ 5 chiếc bút trở lên, mỗi chiếc bút sẽ được giảm giá $10\%$. Nếu mua từ 10 chiếc bút trở lên, mỗi chiếc bút sẽ được giảm giá $20\%$.
* **Yêu cầu:** Cho số lượng bút cần mua $N$ và đơn giá $P$. Hãy tính tổng số tiền bạn Lan phải trả (kết quả là số nguyên).
* **Input:** Hai số nguyên dương $N$ và $P$ ($1 \le N \le 1000, 1000 \le P \le 100000$).
* **Output:** Tổng số tiền phải thanh toán.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `6 10000` | `54000` | Mua 6 chiếc ($\ge 5$), giá mỗi chiếc là $9000$ đ. Tổng tiền: $6 \times 9000 = 54000$ đ. |

---

#### Bài 2 (30 điểm): Cặp số bạn bè (`PYA-L18-P02`)
* **Bối cảnh:** Hai số tự nhiên được gọi là "Cặp số bạn bè" nếu tổng các chữ số của chúng bằng nhau.
  Ví dụ: $25$ ($2+5=7$) và $34$ ($3+4=7$) là một cặp số bạn bè.
* **Yêu cầu:** Cho hai số nguyên dương $A$ và $B$. Hãy kiểm tra xem $A$ và $B$ có phải là cặp số bạn bè không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Hai số nguyên $A, B$ ($1 \le A, B \le 10^{18}$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `123 51` | `YES` (Cùng có tổng chữ số là 6) |
  | `102 301` | `NO` |

---

#### Bài 3 (25 điểm): Chuẩn hóa mã thí sinh (`PYA-L18-P03`)
* **Bối cảnh:** Mã thí sinh trong kỳ thi gồm 2 phần: chữ cái viết tắt của tỉnh và số báo danh (ví dụ: `HN025`, `DN007`). Do sơ suất, người nhập liệu gõ nhầm chữ thường và các khoảng trắng thừa: `  hn  25  `.
* **Yêu cầu:** Cho chuỗi nhập liệu gồm chữ viết tắt và số. Hãy chuẩn hóa thành chuỗi viết hoa, bỏ mọi khoảng trắng và nếu phần số có ít hơn 3 chữ số thì thêm các chữ số 0 vào trước để phần số luôn đủ 3 chữ số.
* **Input:** Một dòng văn bản gồm chữ cái và số nguyên $K$.
* **Output:** Mã thí sinh chuẩn hóa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `hn 5` | `HN005` |
  | `HCM 12` | `HCM012` |

---

#### Bài 4 (15 điểm - phân loại): Chú kiến tha mồi về tổ (`PYA-L18-P04`)
* **Bối cảnh:** Một chú kiến đứng tại tọa độ $0$ trên một trục số thẳng. Mục tiêu của chú là di chuyển đến vị trí $X$. Chú kiến có thể nhảy mỗi bước dài tùy ý từ $1$ đến $5$ mét ($1, 2, 3, 4$ hoặc $5$).
* **Yêu cầu:** Hãy tìm số bước nhảy ít nhất để chú kiến đến được đúng vị trí $X$.
* **Input:** Một số nguyên dương $X$ ($1 \le X \le 10^9$).
* **Output:** Số bước nhảy tối thiểu.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12` | `3` | Nhảy $5 + 5 + 2 = 12$ mét (cần 3 bước). |
* **Gợi ý:** Công thức toán học $\mathcal{O}(1)$: `(X + 4) // 5` hoặc dùng `math.ceil(X / 5)`.

---

### Phần 2: Đề thi thử số 02 (mô phỏng đề PYA lâm đồng / đà lạt)

#### Bài 1 (30 điểm): Thu hoạch dâu tây đà lạt (`PYA-L18-P05`)
* **Bối cảnh:** Nông trại dâu tây thu hoạch được $K$ kg dâu. Dâu được đóng vào 2 loại hộp: Hộp lớn chứa được $5\text{ kg}$ và Hộp nhỏ chứa được $1\text{ kg}$. Để tiết kiệm chi phí đóng gói, chủ nông trại muốn dùng nhiều hộp lớn nhất có thể.
* **Yêu cầu:** Cho số nguyên $K$. Hãy in ra số hộp lớn và số hộp nhỏ cần dùng.
* **Input:** Một số nguyên $K$ ($1 \le K \le 10^6$).
* **Output:** Hai số nguyên: số hộp lớn trước, số hộp nhỏ sau.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `23` | `4 3` |

---

#### Bài 2 (30 điểm): Số đặc biệt chia hết cho tổng chữ số (harshad number) (`PYA-L18-P06`)
* **Bối cảnh:** Một số tự nhiên $N$ được gọi là số Harshad nếu nó chia hết cho chính tổng các chữ số của nó.
  Ví dụ: Số 18 có tổng các chữ số là $1 + 8 = 9$. Vì 18 chia hết cho 9 nên 18 là số Harshad.
* **Yêu cầu:** Cho số $N$. In `YES` nếu $N$ là số Harshad, ngược lại in `NO`.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `18` | `YES` |
  | `19` | `NO` ($1+9=10$, 19 không chia hết cho 10) |

---

#### Bài 3 (25 điểm): Đếm số lần xuất hiện của tên bạn thân (`PYA-L18-P07`)
* **Bối cảnh:** Cho một bài văn miêu tả kỷ niệm tuổi học trò. Bé An muốn đếm xem tên của người bạn thân tên là `BIN` xuất hiện bao nhiêu lần trong bài văn (không phân biệt chữ in hoa hay in thường: `Bin`, `BIN`, `bin` đều được tính).
* **Yêu cầu:** Cho chuỗi văn bản $S$. Hãy đếm số lần từ `bin` xuất hiện như một từ độc lập.
* **Input:** Dòng văn bản $S$ ($1 \le |S| \le 10^4$).
* **Output:** Số lần xuất hiện.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Hom nay Bin va bin di choi cung ban BIN` | `3` |

---

#### Bài 4 (15 điểm - phân loại): Dãy số bội chung của 3 và 5 đẹp mắt (`PYA-L18-P08`)
* **Bối cảnh:** Xét dãy số tự nhiên tăng dần gồm các số chia hết cho 3 HOẶC chia hết cho 5: $3, 5, 6, 9, 10, 12, 15, 18, 20 \dots$
* **Yêu cầu:** Cho số nguyên dương $K$ ($1 \le K \le 10^5$). Hãy tìm số hạng thứ $K$ của dãy số này.
* **Input:** Một số nguyên $K$.
* **Output:** Giá trị số hạng thứ $K$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `7` | `15` | Số thứ 7 là 15. |

---

### Phần 3: Đề thi thử số 03 (mô phỏng vòng chung kết toàn quốc Bảng A)

#### Bài 1 (30 điểm): Đồng hồ cát kỳ diệu (`PYA-L18-P09`)
* **Bối cảnh:** Đồng hồ cát có thể đo được các khoảng thời gian. Một nhà thiên văn học bắt đầu quan sát bầu trời từ $0$ giờ $0$ phút $0$ giây. Sau đúng $S$ giây, buổi quan sát kết thúc.
* **Yêu cầu:** Hãy đổi $S$ giây thành định dạng chuẩn: `HH:MM:SS` (Giờ:Phút:Giây), mỗi thành phần luôn có 2 chữ số (ví dụ: `05:08:09`).
* **Input:** Một số nguyên $S$ ($0 \le S < 86400$).
* **Output:** Chuỗi giờ phút giây định dạng `HH:MM:SS`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `3665` | `01:01:05` |

---

#### Bài 2 (30 điểm): Số nguyên tố đối xứng (`PYA-L18-P10`)
* **Bối cảnh:** Một số tự nhiên được gọi là "Nguyên tố đối xứng" (Palindromic Prime) nếu nó vừa là số nguyên tố, vừa là số đối xứng (ví dụ: $11, 101, 131, 151, 181, 191, \dots$).
* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tìm số nguyên tố đối xứng nhỏ nhất nhưng **lớn hơn hoặc bằng** $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^5$).
* **Output:** Số nguyên tố đối xứng tìm được.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `100` | `101` |
  | `12` | `101` |

---

#### Bài 3 (25 điểm): Bảng điểm thi khảo sát năng khiếu (`PYA-L18-P11`)
* **Bối cảnh:** Có $N$ học sinh tham gia thi tuyển chọn. Mỗi học sinh có một điểm số nguyên từ 0 đến 100. Ban giám khảo quyết định chọn ra $K$ bạn có điểm cao nhất để vào đội tuyển chính thức.
* **Yêu cầu:** Cho danh sách điểm của $N$ bạn và số $K$. Hãy in ra điểm số của $K$ bạn được chọn theo thứ tự giảm dần từ cao xuống thấp.
* **Input:**
  * Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên là điểm của các thí sinh.
* **Output:** $K$ điểm số cao nhất cách nhau bởi khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `6 3`<br>`70 95 85 60 90 85` | `95 90 85` |

---

#### Bài 4 (15 điểm - phân loại): Dãy con liên tiếp tăng dài nhất (`PYA-L18-P12`)
*(Bài toán phân loại Huy chương Vàng Bảng A toàn quốc)*

* **Bối cảnh:** Cho một dãy gồm $N$ số nguyên. Một "dãy con liên tiếp tăng" là một đoạn các phần tử đứng cạnh nhau mà phần tử đứng sau luôn lớn hơn phần tử đứng ngay trước nó ($A_i < A_{i+1} < A_{i+2} \dots$).
* **Yêu cầu:** Hãy tìm độ dài của dãy con liên tiếp tăng dài nhất trong dãy số đã cho.
* **Input:**
  * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).
* **Output:** Một số nguyên duy nhất là độ dài lớn nhất tìm được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `6`<br>`1 3 5 2 4 7` | `3` | Dãy con tăng dài nhất có độ dài 3 (đoạn `1 3 5` hoặc `2 4 7`). |


--------------------------------------------------------------------------------
<!-- Bài 16: lesson-16 -->
--------------------------------------------------------------------------------

## Lý thuyết và Concept Quiz

# Bài 16: Đề thi thử Python Bảng A

Mỗi đề thi chuẩn gồm 4 bài toán phân bổ theo thời gian 90 phút:

## ĐỀ THI THỬ SỐ 01 (MÔ PHỎNG ĐỀ PYA THÀNH PHỐ)

### Bài 1 (30 điểm): Mua dụng cụ học tập
- **Yêu cầu:** Mua $N$ quyển vở giá $P$ đồng/quyển. Mua từ 10 quyển trở lên giảm $10\%$. Tính số tiền phải trả (số nguyên).
- **Code mẫu:**
  ```python
  n, p = map(int, input().split())
  tong = n * p
  if n >= 10:
      tong = int(tong * 0.9)
  print(tong)
  ```

### Bài 2 (30 điểm): Số lộc phát đối xứng
- **Yêu cầu:** Số lộc phát đối xứng là số đối xứng và chỉ chứa các chữ số 6 hoặc 8. Kiểm tra số $N$.
- **Code mẫu:**
  ```python
  s = input()
  if s == s[::-1] and all(c in '68' for c in s):
      print("YES")
  else:
      print("NO")
  ```

### Bài 3 (25 điểm): Đếm từ độc nhất trong văn bản
- **Yêu cầu:** Cho câu văn. Đếm xem có bao nhiêu từ khác nhau xuất hiện (không phân biệt hoa thường).
- **Code mẫu:**
  ```python
  s = input().lower()
  tu = s.split()
  print(len(set(tu)))
  ```

### Bài 4 (15 điểm - Phân loại): Bước nhảy chú cào cào
- **Yêu cầu:** Chú cào cào xuất phát từ 0 nhảy đến vị trí $X$. Mỗi bước nhảy xa tối đa $K$ mét. Hỏi số bước nhảy ít nhất?
- **Code mẫu:**
  ```python
  x, k = map(int, input().split())
  ans = (x + k - 1) // k
  print(ans)
  ```

## Bài tập lesson

# Hệ thống bài tập thực hành — bài 16: Đề thi thử Python Bảng A

---

## Ma trận 12 bài thi thử (phong cách contest: giấu pattern, có subtask)

| STT | Mã bài | Tên | Cấp độ | Ràng buộc | Mục tiêu |
|---|---|---|---|---|---|
| 01 | PYA-L16-P15 | Heo Đất Tiết Kiệm | Dễ | $N \le 10^6$ | Rèn vòng lặp có điều kiện và phép đếm ngày chẵn |
| 02 | PYA-L16-P16 | Vé Số May Mắn | Dễ | $N \le 10^{18}$ | Rèn tách chữ số và kiểm tra chia hết |
| 03 | PYA-L16-P17 | Bảng Điểm Lớp Học | Dễ | $N \le 10^5$ | Rèn đọc danh sách và thống kê cơ bản |
| 04 | PYA-L16-P18 | Mật Khẩu Bị Ẩn | Dễ | $\|S\| \le 10^5$ | Rèn duyệt chuỗi và phân loại ký tự |
| 05 | PYA-L16-P19 | Đếm Kẹo Chẵn Lẻ | Dễ | $N \le 10^5$ | Rèn phép chia dư và bộ đếm đôi |
| 06 | PYA-L16-P20 | Tổng Chữ Số Lớn Nhất | Trung bình | $N \le 10^5$ | Rèn tổng chữ số và chọn cực trị có điều kiện phụ |
| 07 | PYA-L16-P21 | Số Ghế Đối Xứng | Trung bình | $N \le 10^{18}$ | Rèn đảo ngược số và so sánh chuỗi |
| 08 | PYA-L16-P22 | Xếp Hàng Chiều Cao | Trung bình | $N \le 10^5$ | Rèn sắp xếp danh sách |
| 09 | PYA-L16-P23 | Thưởng Đọc Sách | Trung bình | $N \le 10^{12}$ | Rèn công thức toán thay vòng lặp chậm |
| 10 | PYA-L16-P24 | Đếm Từ Dài | Trung bình | $\|S\| \le 10^4$ | Rèn tách từ bằng split và so sánh độ dài |
| 11 | PYA-L16-P25 | Đếm Sao Nguyên Tố | Khó | $N \le 10^6$ | Rèn kiểm tra nguyên tố và vét điểm subtask nhỏ |
| 12 | PYA-L16-P26 | Chuyến Tàu Vượt Đèo | Khó | $N \le 10^5$ | Rèn giữ giá trị lớn nhất hiện tại trong một lượt duyệt |

---

### Bài 1 (Dễ): Heo Đất Tiết Kiệm (PYA-L16-P15)

* **Bối cảnh:** Bé Na bỏ vào heo mỗi ngày $A$ đồng, riêng các ngày chẵn được mẹ thưởng thêm $B$ đồng. Sau $N$ ngày, trong heo có bao nhiêu tiền?
* **Yêu cầu:** Cho $N, A, B$. Tính tổng số tiền sau $N$ ngày.
* **Input:** Ba số nguyên $N, A, B$ ($1 \le N \le 10^6$).
* **Output:** Tổng số tiền.
* **Ví dụ mẫu:**

  | Input | Output | Giải thích |
  |---|---|---|
  | `5 10 3` | `56` | $5 \times 10 + 2 \times 3 = 56$. |

### Bài 2 (Dễ): Vé Số May Mắn (PYA-L16-P16)

* **Bối cảnh:** Vé số được gọi là may mắn nếu tổng các chữ số của nó chia hết cho $7$. Tấm vé $1234$ có trúng thưởng không?
* **Yêu cầu:** Cho số $N$. In `YES` nếu là vé may mắn, ngược lại in `NO`.
* **Input:** Số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `1234` | `NO` |

### Bài 3 (Dễ): Bảng Điểm Lớp Học (PYA-L16-P17)

* **Bối cảnh:** Cô giáo nhờ bé Na tìm điểm cao nhất, điểm thấp nhất và điểm trung bình của $N$ bạn để ghi vào sổ thi đua.
* **Yêu cầu:** Cho điểm của $N$ bạn. In điểm cao nhất, thấp nhất và trung bình (1 chữ số thập phân).
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($0 \le A_i \le 10$).
* **Output:** 3 dòng: điểm cao nhất, điểm thấp nhất, điểm trung bình.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `5`<br>`8 7 10 6 9` | `10`<br>`6`<br>`8.0` |

### Bài 4 (Dễ): Mật Khẩu Bị Ẩn (PYA-L16-P18)

* **Bối cảnh:** Mật khẩu nhật ký của bé Bo gồm chữ cái và chữ số như `Abc123x`. Có bao nhiêu ký tự là chữ số?
* **Yêu cầu:** Cho chuỗi $S$. Đếm ký tự là chữ số từ `0` đến `9`.
* **Input:** Chuỗi $S$ ($1 \le \|S\| \le 10^5$).
* **Output:** Số lượng chữ số.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `Abc123x` | `3` |

### Bài 5 (Dễ): Đếm Kẹo Chẵn Lẻ (PYA-L16-P19)

* **Bối cảnh:** Cô giáo chia $N$ gói kẹo thành mâm gói chẵn và mâm gói lẻ. Mỗi mâm có bao nhiêu gói?
* **Yêu cầu:** Cho $N$ số nguyên. Đếm số chẵn và số lẻ, in trên một dòng.
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($0 \le A_i \le 10^9$).
* **Output:** Hai số: số lượng số chẵn trước, số lượng số lẻ sau.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `6`<br>`1 2 3 4 5 6` | `3 3` |

### Bài 6 (Trung bình): Tổng Chữ Số Lớn Nhất (PYA-L16-P20)

* **Bối cảnh:** Bạn nào có tổng các chữ số của số báo danh lớn nhất sẽ làm lớp trưởng. Nếu hòa thì bạn có số báo danh nhỏ hơn thắng.
* **Yêu cầu:** Cho $N$ số báo danh. Tìm số của bạn thắng cuộc.
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số tự nhiên ($0 \le A_i \le 10^{18}$).
* **Output:** Số báo danh thắng cuộc.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `5`<br>`12 99 45 100 38` | `99` |

### Bài 7 (Trung bình): Số Ghế Đối Xứng (PYA-L16-P21)

* **Bối cảnh:** Ghế vàng trong rạp xiếc mang số đối xứng (đọc xuôi ngược đều giống nhau như 121). Ghế số $N$ có phải ghế vàng không?
* **Yêu cầu:** Cho số $N$. In `YES` nếu đối xứng, ngược lại in `NO`.
* **Input:** Số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `121` | `YES` |

### Bài 8 (Trung bình): Xếp Hàng Chiều Cao (PYA-L16-P22)

* **Bối cảnh:** Thầy thể dục nhờ bé Na xếp $N$ bạn thành hàng từ thấp đến cao để tập đội hình.
* **Yêu cầu:** Cho chiều cao của $N$ bạn. In ra theo thứ tự tăng dần.
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($100 \le A_i \le 200$).
* **Output:** $N$ số tăng dần trên một dòng.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `5`<br>`160 150 175 165 155` | `150 155 160 165 175` |

### Bài 9 (Trung bình): Thưởng Đọc Sách (PYA-L16-P23)

* **Bối cảnh:** Đọc hết $N$ quyển sách sẽ được thưởng sao: quyển thứ 1 được 1 sao, quyển thứ 2 được 2 sao, tới quyển thứ $N$ được $N$ sao. Tổng cộng được bao nhiêu sao?
* **Yêu cầu:** Cho $N$. Tính tổng từ 1 đến $N$.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^{12}$).
* **Output:** Tổng số sao.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `5` | `15` |

### Bài 10 (Trung bình): Đếm Từ Dài (PYA-L16-P24)

* **Bối cảnh:** Cô giáo đố: trong câu văn $S$ có bao nhiêu từ dài hơn $K$ ký tự? Từ là nhóm ký tự liền nhau, cách nhau bởi dấu cách.
* **Yêu cầu:** Cho $K$ và câu $S$. Đếm số từ có độ dài lớn hơn $K$.
* **Input:**
  * Dòng 1: số nguyên $K$ ($0 \le K \le 100$).
  * Dòng 2: câu văn $S$ ($1 \le \|S\| \le 10^4$).
* **Output:** Số từ thỏa mãn.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `3`<br>`Hom nay Bin di hoc cung ban Na` | `1` |

### Bài 11 (Khó): Đếm Sao Nguyên Tố (PYA-L16-P25)

* **Bối cảnh:** Trên bầu trời giấy có $N$ ngôi sao đánh số từ 1 đến $N$. Có bao nhiêu ngôi sao mang số nguyên tố? (Số 1 không phải số nguyên tố.)
* **Yêu cầu:** Cho $N$. Đếm số nguyên tố từ 1 đến $N$.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** Số lượng số nguyên tố.
* **Ví dụ mẫu:**

  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `4` | Các số 2, 3, 5, 7. |

### Bài 12 (Khó): Chuyến Tàu Vượt Đèo (PYA-L16-P26)

* **Bối cảnh:** Tàu đồ chơi chạy qua $N$ ngọn đèo cao $A_i$ mét. Bé lái tàu reo lên mỗi khi chinh phục ngọn đèo cao hơn tất cả các ngọn đã qua (ngọn đầu tiên luôn được reo một lần). Bé reo tất cả bao nhiêu lần?
* **Yêu cầu:** Cho dãy $N$ số. Đếm số lần phần tử lớn hơn mọi phần tử đứng trước nó.
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($\|A_i\| \le 10^9$).
* **Output:** Số lần reo.
* **Ví dụ mẫu:**

  | Input | Output | Giải thích |
  |---|---|---|
  | `6`<br>`1 3 5 2 4 7` | `4` | Các kỷ lục là 1, 3, 5, 7. |
