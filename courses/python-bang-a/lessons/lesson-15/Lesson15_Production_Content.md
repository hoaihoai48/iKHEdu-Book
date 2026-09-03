# Bài 15: Tách từ và mã hóa thay thế

---

## 1. Khởi động: Chiếc kéo chia câu & mật thư của julius Caesar

* Khi đọc một câu văn dài như: `"Hoc lap trinh Python rat vui"`, làm sao để máy tính biết câu này có **bao nhiêu từ**, và từ nào là từ dài nhất?
* Thời La Mã cổ đại, vị hoàng đế vĩ đại **Julius Caesar** khi gửi thư cho các tướng lĩnh đã nghĩ ra một cách mã hóa bí mật: Mỗi chữ cái trong bức thư được **dịch chuyển về phía sau 3 vị trí trong bảng chữ cái**!
  Ví dụ: Chữ `'A'` dịch thành `'D'`, chữ `'B'` dịch thành `'E'`. Kẻ địch bắt được lá thư chỉ thấy toàn chữ cái kỳ quái vô nghĩa!

Trong bài học hôm nay, chúng ta sẽ làm chủ **nghệ thuật tách từ `split()`** và giải mã các bức mật thư bằng **bảng mã ASCII (`ord` và `chr`)**!

---

## 2. Kỹ thuật tách từ siêu tốc: `split()` và nối lại bằng `join()`

### 2.1. Phép màu của `split()`
Phương thức `s.split()` giống như một chiếc kéo tự động: Nó sẽ tìm tất cả các khoảng trắng (dù là 1 dấu cách hay 10 dấu cách liên tiếp) để cắt dòng văn bản thành một **danh sách (list) các từ riêng biệt**!

```python
cau = "Hoc lap trinh Python rat vui"
danh_sach_tu = cau.split()

print(danh_sach_tu)
# In ra: ['Hoc', 'lap', 'trinh', 'Python', 'rat', 'vui']

print("So tu trong cau la:", len(danh_sach_tu)) # In ra: 6
```

### 2.2. Ghép các từ lại bằng `join()`
Muốn nối các từ lại với nhau bằng một dấu gạch nối `"-"` hay một dấu cách:
```python
ket_qua = "-".join(danh_sach_tu)
print(ket_qua) # In ra: 'Hoc-lap-trinh-Python-rat-vui'
```

---

## 3. Bảng mã số bí mật của máy tính: `ord()` và `chr()`

Máy tính thực ra không hiểu chữ cái `'A'` hay `'B'`. Bên trong chip xử lý, mọi ký tự đều được quy ước bằng một con số nguyên duy nhất gọi là **Mã ASCII**:
* Chữ cái in hoa `'A'` có mã số là **$65$**, `'B'` là $66$, ..., `'Z'` là **$90$**.
* Chữ cái in thường `'a'` có mã số là **$97$**, `'b'` là $98$, ..., `'z'` là **$122$**.
* Chữ số `'0'` có mã số là **$48$**, ..., `'9'` là **$57$**.

### Hai hàm ma thuật trong Python:
* **`ord(ch)`**: Đưa vào một ký tự $\implies$ Trả về **mã số nguyên** của nó.
  Ví dụ: `ord('A') \to 65`.
* **`chr(code)`**: Đưa vào một con số nguyên $\implies$ Trả về **ký tự** tương ứng.
  Ví dụ: `chr(65) \to 'A'`.

### Ứng dụng: Mã hóa Caesar dịch chuyển $K$ bước
```python
ch = 'A'
k = 3
ma_moi = ord(ch) + k
ky_tu_moi = chr(ma_moi)
print(ky_tu_moi) # In ra 'D'
```

---

## 4. Concept quiz: 12 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Phương thức `s.split()` mặc định cắt chuỗi theo ký tự gì?
- **A.** Dấu phẩy
- **B.** **[Đáp án đúng]** Khoảng trắng (khoảng trắng đơn, nhiều khoảng trắng, dấu tab, xuống dòng)
- **C.** Dấu chấm
- **D.** Chữ cái đầu tiên
- > *Giải thích:* `split()` không truyền tham số sẽ tự động phân tách theo mọi khoảng trắng liên tiếp.

#### Câu 2: Cho `s = "An   Binh    Cuong"`. Biểu thức `len(s.split())` trả về:
- **A.** 3
- **B.** **[Đáp án đúng]** 3 (Bất chấp có bao nhiêu dấu cách giữa các từ!)
- **C.** 15
- **D.** 6
- > *Giải thích:* `split()` tự động gộp các khoảng trắng thừa thành một dấu phân cách duy nhất, danh sách còn đúng 3 từ.

#### Câu 3: Hàm `ord('A')` trong Python trả về giá trị là:
- **A.** 0
- **B.** 1
- **C.** **[Đáp án đúng]** 65
- **D.** 97
- > *Giải thích:* Mã ASCII của chữ cái 'A' in hoa là 65.

#### Câu 4: Hàm `chr(66)` trong Python trả về ký tự nào?
- **A.** `'A'`
- **B.** **[Đáp án đúng]** `'B'`
- **C.** `'6'`
- **D.** `'b'`
- > *Giải thích:* Mã ASCII 65 là 'A' nên mã 66 là 'B'.

#### Câu 5: Khoảng cách mã ASCII giữa chữ thường `'a'` và chữ hoa `'A'` (`ord('a') - ord('A')`) luôn bằng bao nhiêu?
- **A.** 26
- **B.** **[Đáp án đúng]** 32
- **C.** 10
- **D.** 48
- > *Giải thích:* $97 - 65 = 32$. Đây là hằng số dùng để chuyển đổi hoa-thường thủ công!

#### Câu 6: Cho `words = ['Python', 'la', 'so', '1']`. Biểu thức `" ".join(words)` tạo ra chuỗi gì?
- **A.** `"Pythonlaso1"`
- **B.** **[Đáp án đúng]** `"Python la so 1"`
- **C.** `['Python la so 1']`
- **D.** `"Python-la-so-1"`
- > *Giải thích:* `join()` lấy chuỗi phân cách đứng trước (ở đây là dấu cách `" "`) nối các phần tử lại với nhau.

#### Câu 7: Mã ASCII của ký tự chữ số `'0'` là bao nhiêu?
- **A.** 0
- **B.** **[Đáp án đúng]** 48
- **C.** 1
- **D.** 32
- > *Giải thích:* Ký tự `'0'` có mã ASCII là 48. Vì vậy `ord(ch) - 48` là cách chuyển ký tự số sang số nguyên nhanh!

#### Câu 8: Cho `ch = 'Z'`. Nếu dịch chuyển sang ký tự tiếp theo trong vòng tròn 26 chữ cái tiếng anh, ký tự đó là:
- **A.** `'['`
- **B.** **[Đáp án đúng]** `'A'`
- **C.** `'Z'`
- **D.** Không tồn tại
- > *Giải thích:* Trong mật mã Caesar xoay vòng (Modulo 26), sau 'Z' sẽ quay trở lại 'A'.

#### Câu 9: Đoạn code sau in ra từ nào?
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

#### Câu 10: Phương thức `s.strip()` có tác dụng gì?
- **A.** Xóa tất cả các chữ cái
- **B.** **[Đáp án đúng]** Cắt bỏ toàn bộ các khoảng trắng thừa ở ĐẦU và ĐUÔI của chuỗi
- **C.** Đảo ngược chuỗi
- **D.** In hoa chuỗi
- > *Giải thích:* `strip()` dọn dẹp các khoảng trắng ở hai đầu chuỗi văn bản.

#### Câu 11: Biểu thức `chr(ord('c') - 32)` cho kết quả là gì?
- **A.** `'a'`
- **B.** `'d'`
- **C.** **[Đáp án đúng]** `'C'`
- **D.** `'c'`
- > *Giải thích:* Lấy mã ASCII của 'c' (99) trừ đi 32 được 67, là mã của chữ hoa 'C'.

#### Câu 12: Đoạn code sau in ra màn hình giá trị gì?
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
