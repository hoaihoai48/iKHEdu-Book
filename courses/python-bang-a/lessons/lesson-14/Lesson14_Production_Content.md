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
cau = "lap trinh tin hoc tre"
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
