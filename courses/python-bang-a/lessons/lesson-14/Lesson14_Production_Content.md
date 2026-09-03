# Bài 14: Duyệt chuỗi và biến đổi ký tự

---

## 1. Khởi động: Chiếc kính lúp soi từng chữ cái

Ở Bài 13, chúng ta đã biết cách lấy một ký tự cụ thể hoặc cắt một lát chuỗi bằng Indexing và Slicing.
Nhưng giả sử bác bảo vệ giao cho em một văn bản rất dài và hỏi:
* *"Văn bản này có bao nhiêu chữ cái in hoa?"*
* *"Có bao nhiêu chữ số từ '0' đến '9' bị lẫn vào trong tên người?"*
* *"Hãy đổi toàn bộ các chữ cái thường thành chữ IN HOA để in lên tấm băng rôn cổ vũ!"*

Làm sao để làm được điều đó? Chúng ta cần một **chiếc kính lúp** soi lần lượt từng chữ cái từ đầu đến cuối chuỗi.
Trong Python, cú pháp duyệt chuỗi đẹp và tự nhiên như ngôn ngữ nói hàng ngày:
```python
for ky_tu in chuoi:
    # Làm việc với từng ky_tu
```

---

## 2. Hai cách duyệt chuỗi trong Python

### Cách 1: Duyệt trực tiếp từng phần tử (`for ch in s`) — đơn giản nhất!
```python
s = "iKHEDU"
for ch in s:
    print(ch)  # Lần lượt in ra: 'i', 'K', 'H', 'E', 'D', 'U'
```

### Cách 2: Duyệt qua chỉ số index (`for i in range(len(s))`) — khi cần biết vị trí!
```python
s = "PYTHON"
for i in range(len(s)):
    print("Vi tri", i, "la ky tu", s[i])
```

---

## 3. Bộ công cụ nhận diện & biến đổi ký tự thần kỳ

Python trang bị sẵn cho chúng ta những phương thức kiểm tra và biến đổi cực kỳ quyền năng:

| Lệnh / Phương thức | Ý nghĩa | Ví dụ thực tế |
|---|---|---|
| `ch.isupper()` | Kiểm tra có phải **chữ HOA** không? | `'A'.isupper() \to True`, `'a'.isupper() \to False` |
| `ch.islower()` | Kiểm tra có phải **chữ thường** không? | `'b'.islower() \to True` |
| `ch.isdigit()` | Kiểm tra có phải **chữ số ('0'-'9')** không? | `'5'.isdigit() \to True`, `'A'.isdigit() \to False` |
| `ch.isalpha()` | Kiểm tra có phải **chữ cái** không? | `'x'.isalpha() \to True`, `'?'.isalpha() \to False` |
| `s.upper()` | Biến toàn bộ chuỗi thành **IN HOA** | `"python".upper() \to "PYTHON"` |
| `s.lower()` | Biến toàn bộ chuỗi thành **chữ thường** | `"HELLO".lower() \to "hello"` |
| `s.count(x)` | Đếm số lần xuất hiện của ký tự `x` | `"BANANA".count('A') \to 3` |

### Ví dụ mẫu: Đếm số chữ số xuất hiện trong một dòng chữ
```python
s = input()
dem_so = 0

for ch in s:
    if ch.isdigit():
        dem_so += 1

print("So luong chu so trong van ban la:", dem_so)
```

---

## 4. Concept quiz: 14 câu trắc nghiệm bắt bẫy củng cố khái niệm

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
