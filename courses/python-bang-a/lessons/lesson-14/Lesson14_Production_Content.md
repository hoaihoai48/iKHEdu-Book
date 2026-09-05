# Bài 14: Duyệt chuỗi, biến đổi ký tự và tách từ

## 1. Khái niệm & Bản chất của Xử lý chuỗi nâng cao

Trong bài trước, ta đã làm quen với việc đánh chỉ số và cắt lát chuỗi (`s[i]`, `s[a:b]`). Tuy nhiên, trong các bài toán lập trình thi đấu thực tế, chuỗi ký tự thường là dữ liệu văn bản phức tạp: mật mã, câu văn, danh sách từ ngữ, dữ liệu số lẫn lộn chữ cái. 

Để giải quyết triệt để các dạng toán này, ta cần làm chủ 4 kỹ năng cốt lõi:
1. **Duyệt từng ký tự**: Kiểm tra từng ký tự trong chuỗi xem là chữ cái, chữ số hay ký tự đặc biệt.
2. **Biến đổi ký tự**: Chuyển đổi qua lại giữa chữ hoa và chữ thường, thay thế ký tự.
3. **Bản chất mã ASCII**: Hiểu rõ mối liên hệ giữa ký tự và mã số nguyên trong bộ nhớ máy tính (`ord` và `chr`).
4. **Tách từ và chuẩn hóa văn bản**: Sử dụng `split()` và `join()` để bóc tách từ ngữ từ một câu văn hoàn chỉnh.

![Bản chất xử lý chuỗi nâng cao](../../assets/l14_string_ascii_methods.svg?v=1788575106)

---

## 2. Kiểm tra và phân loại ký tự

Python cung cấp sẵn các phương thức kiểm tra ký tự cực kỳ mạnh mẽ, trả về giá trị kiểu Logic (`True` hoặc `False`):

| Phương thức | Ý nghĩa kỹ thuật | Ví dụ kiểm tra | Kết quả |
|---|---|---|:---:|
| `ch.isdigit()` | Ký tự `ch` có phải là chữ số (`'0'` đến `'9'`) không? | `'7'.isdigit()` | `True` |
| `ch.isalpha()` | Ký tự `ch` có phải là chữ cái (`'a'-'z'`, `'A'-'Z'`) không? | `'k'.isalpha()` | `True` |
| `ch.isupper()` | Ký tự `ch` có phải là chữ cái in hoa không? | `'A'.isupper()` | `True` |
| `ch.islower()` | Ký tự `ch` có phải là chữ cái in thường không? | `'b'.islower()` | `True` |
| `ch.isspace()` | Ký tự `ch` có phải là khoảng trắng (space, tab, enter) không? | `' '.isspace()` | `True` |

> ⚠️ **Lưu ý tử huyệt:** Các phương thức trên chỉ hoạt động chính xác khi `ch` là một ký tự đơn hoặc một chuỗi con không chứa ký tự khác loại. Nếu chuỗi rỗng `""`, tất cả các hàm trên đều trả về `False`. Khoảng trắng `' '` không phải là chữ cái cũng không phải là chữ số!

### Ứng dụng: Lọc và trích xuất chữ số từ văn bản hỗn hợp
```python
s = input()
chu_so = ""
for ch in s:
    if ch.isdigit():
        chu_so += ch
print(chu_so)
```

---

## 3. Biến đổi ký tự và chuỗi

Vì chuỗi trong Python mang tính chất **bất biến**, các hàm biến đổi **không bao giờ làm thay đổi chuỗi gốc**, mà luôn trả về một **chuỗi mới hoàn toàn**:

### 3.1. Chuyển đổi hoa — thường
* `s.upper()`: Tạo chuỗi mới với toàn bộ chữ cái được chuyển thành **in hoa**.
* `s.lower()`: Tạo chuỗi mới với toàn bộ chữ cái được chuyển thành **in thường**.
* `s.swapcase()`: Đảo ngược trạng thái: chữ hoa hóa thường, chữ thường hóa hoa.

```python
s = "Python 2026"
print(s.upper())     # "PYTHON 2026"
print(s.lower())     # "python 2026"
print(s.swapcase())  # "pYTHON 2026"
print(s)             # Vẫn là "Python 2026" (chuỗi gốc không đổi)
```

### 3.2. Thay thế chuỗi con với `s.replace(old, new)`
* Cú pháp: `s.replace(chuoi_cu, chuoi_moi)`
* Thay thế tất cả các lần xuất hiện của `chuoi_cu` bằng `chuoi_moi`:
```python
s = "lap-trinh-python"
s_moi = s.replace("-", " ")
print(s_moi)  # "lap trinh python"
```

---

## 4. Bản chất mã ASCII: Cầu nối giữa Chữ cái và Con số

Trong bộ nhớ máy tính, mỗi ký tự đều được biểu diễn bởi một số nguyên từ $0$ đến $127$ (gọi là mã ASCII — American Standard Code for Information Interchange).

### 4.1. Bảng mã ASCII chuẩn mực cần nhớ nằm lòng

| Ký tự | Mã ASCII (`ord`) | Quy luật & Ứng dụng |
|:---:|:---:|---|
| `'0'` đến `'9'` | $48$ đến $57$ | Muốn đổi ký tự số sang số nguyên: `int(ch)` hoặc `ord(ch) - 48` |
| `'A'` đến `'Z'` | $65$ đến $90$ | Chữ hoa liên tiếp cách nhau đúng 1 đơn vị |
| `'a'` đến `'z'` | $97$ đến $122$ | Chữ thường liên tiếp cách nhau đúng 1 đơn vị |
| `' '` (space) | $32$ | Khoảng trắng |

> 💡 **Hằng số vàng 32:** 
> $$\mathbf{ord('a') - ord('A') = 97 - 65 = 32}$$
> Chữ thường luôn có mã ASCII lớn hơn chữ hoa tương ứng đúng **32 đơn vị**. 
> Do đó:
> * Đổi hoa sang thường: `chr(ord(ch) + 32)`
> * Đổi thường sang hoa: `chr(ord(ch) - 32)`

### 4.2. Hai hàm chuyển đổi: `ord()` và `chr()`
* `ord(ch)`: Nhận vào **1 ký tự**, trả về **mã số nguyên ASCII** của nó.
* `chr(code)`: Nhận vào **mã số nguyên**, trả về **ký tự** tương ứng.

```python
print(ord('A'))         # In ra: 65
print(chr(65))          # In ra: 'A'
print(chr(ord('A') + 1)) # In ra: 'B' (Ký tự kế tiếp)
```

---

## 5. Tách từ (`split`) và Ghép từ (`join`) — Chuẩn hóa câu văn

Xử lý từ ngữ là một trong những dạng toán thi đấu kinh điển: đếm số từ, tìm từ dài nhất, đảo ngược từ trong câu.

### 5.1. Phương thức `s.split()` thần thánh
* Khi gọi `s.split()` không truyền tham số, Python sẽ:
  1. Tự động tìm tất cả các cụm khoảng trắng (bao gồm 1 khoảng trắng, nhiều khoảng trắng liên tiếp, dấu cách ở đầu/đuôi).
  2. Bóc tách câu thành một **danh sách (`list`) các từ riêng biệt**.

```python
s = "   Ha    Noi   mua    thu   "
danh_sach_tu = s.split()
print(danh_sach_tu)      # ['Ha', 'Noi', 'mua', 'thu']
print(len(danh_sach_tu)) # In ra: 4 (Đếm số từ cực kỳ chính xác!)
```

### 5.2. Phương thức ghép chuỗi `sep.join(list)`
* Nối tất cả các chuỗi trong một danh sách lại với nhau, phân cách bằng chuỗi `sep`:
```python
tu = ['Python', 'la', 'ngon', 'ngu', 'tuyet', 'voi']
cau = " ".join(tu)
print(cau)  # "Python la ngon ngu tuyet voi"
```

---

## 6. Bảng mô phỏng biến thiên ô nhớ

### Chương trình: Tính tổng các chữ số xuất hiện trong một chuỗi hỗn hợp

```python
s = "A3B7C2"
tong = 0
for ch in s:
    if ch.isdigit():
        tong += int(ch)
print(tong)
```

| Bước | Vòng lặp `ch` | `ch.isdigit()`? | Thao tác thực hiện | Giá trị `tong` trong RAM |
|:---:|:---:|:---:|---|:---:|
| Khởi tạo | — | — | Khởi tạo biến tích lũy `tong = 0` | $0$ |
| $1$ | `'A'` | `False` | Không phải số, bỏ qua | $0$ |
| $2$ | `'3'` | `True` | `tong += int('3')` $\implies 0 + 3 = 3$ | $3$ |
| $3$ | `'B'` | `False` | Không phải số, bỏ qua | $3$ |
| $4$ | `'7'` | `True` | `tong += int('7')` $\implies 3 + 7 = 10$ | $10$ |
| $5$ | `'C'` | `False` | Không phải số, bỏ qua | $10$ |
| $6$ | `'2'` | `True` | `tong += int('2')` $\implies 10 + 2 = 12$ | $12$ |
| **Kết thúc** | — | — | In giá trị `tong` ra màn hình | **In: $12$** |

---

## 7. Tử huyệt và Bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: NỐI CHUỖI THAY VÌ CỘNG SỐ**
> * Khi duyệt qua các ký tự số, nếu viết:
>   ```python
>   tong += ch  # ch vẫn là kiểu chuỗi '3', '7'
>   ```
>   Thì máy tính sẽ thực hiện phép ghép chuỗi: `"0" + "3" + "7" = "037"`, không phải phép cộng số học!
> * **Cách viết an toàn:** Luôn ép kiểu `int(ch)` trước khi cộng: `tong += int(ch)`.

> ❌ **BẪY LỖI 2: ĐẾM SỐ TỪ BẰNG CÁCH ĐẾM DẤU CÁCH**
> * Nhiều học sinh ngây thơ dùng thuật toán: `so_tu = s.count(' ') + 1`.
> * Nếu văn bản có 2 dấu cách liên tiếp `"Ha  Noi"`, thuật toán trên đếm ra 3 từ $\implies$ **SAI HOÀN TOÀN!**
> * **Quy tắc vàng:** Luôn dùng `len(s.split())` để đếm từ chuẩn xác 100%.

> ❌ **BẪY LỖI 3: QUÊN RẰNG `s.upper()` KHÔNG LÀM ĐỔI CHUỖI GỐC**
> * Viết:
>   ```python
>   s = "abc"
>   s.upper()
>   print(s)  # Vẫn in ra: "abc"
>   ```
> * **Bắt buộc gán lại:** `s = s.upper()`.

---

## 8. Mẫu code chuẩn thi đấu

### 8.1. Đếm số lượng chữ cái in hoa, in thường và chữ số
```python
s = input()
hoa = 0
thuong = 0
so = 0

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1

print(hoa, thuong, so)
```

### 8.2. Chuẩn hóa câu văn (Xóa khoảng trắng thừa, viết hoa chữ cái đầu)
```python
s = input()
tu = s.split()
tu_chuan = [w.capitalize() for w in tu]
print(" ".join(tu_chuan))
```

---

## 9. Concept Quiz: 26 câu trắc nghiệm bắt bẫy củng cố khái niệm

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
- **B.** 1
- **C.** **[Đáp án đúng]** 2
- **D.** 3
- > *Giải thích:* Python phân biệt chữ hoa và chữ thường! Chữ `'a'` thường xuất hiện ở vị trí `H[a]` trong `"Ha"` và `M[a]` trong `"Mua"` → tổng cộng 2 lần. Chữ `'A'` in hoa trong `"Ha"` không được tính.

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
cau = "lap trinh python nang cao"
ds = cau.split()
max_len = 0
for tu in ds:
    if len(tu) > max_len:
        max_len = len(tu)
print(max_len)
```
- **A.** 3
- **B.** 4
- **C.** 5
- **D.** **[Đáp án đúng]** 6
- > *Giải thích:* Độ dài các từ: 'lap' (3), 'trinh' (5), 'python' (6), 'nang' (4), 'cao' (3). Từ dài nhất là 'python' có độ dài 6.
