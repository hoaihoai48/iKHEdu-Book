# Bài 14: Duyệt chuỗi, biến đổi ký tự và tách từ

## 1. Khái niệm & Bản chất của Xử lý chuỗi nâng cao

Ở bài trước, ta đã biết đánh chỉ số và cắt lát chuỗi (`s[i]`, `s[a:b]`). Nhưng văn bản thực tế thường rối hơn: mật mã, câu văn, cụm từ, số lẫn chữ cái.

Để làm tốt dạng này, em cần nắm 4 kỹ năng chính:
1. **Duyệt từng ký tự**: Xem từng ký tự là chữ cái, chữ số hay ký hiệu đặc biệt.
2. **Biến đổi ký tự**: Đổi qua lại giữa chữ hoa và chữ thường, thay ký tự.
3. **Bản chất mã ASCII**: Hiểu mối liên hệ giữa ký tự và số nguyên trong máy (`ord` và `chr`).
4. **Tách từ và chuẩn hóa văn bản**: Dùng `split()` và `join()` để tách từ trong câu.

![Bản chất xử lý chuỗi nâng cao](../../assets/l14_string_ascii_methods.svg?v=1788575106)

---

## 2. Kiểm tra và phân loại ký tự

Python có sẵn các cách kiểm tra ký tự rất tiện, trả về `True` hoặc `False`:

| Phương thức | Ý nghĩa kỹ thuật | Ví dụ kiểm tra | Kết quả |
|---|---|---|:---:|
| `ch.isdigit()` | Ký tự `ch` có phải là chữ số (`'0'` đến `'9'`) không? | `'7'.isdigit()` | `True` |
| `ch.isalpha()` | Ký tự `ch` có phải là chữ cái (`'a'-'z'`, `'A'-'Z'`) không? | `'k'.isalpha()` | `True` |
| `ch.isupper()` | Ký tự `ch` có phải là chữ cái in hoa không? | `'A'.isupper()` | `True` |
| `ch.islower()` | Ký tự `ch` có phải là chữ cái in thường không? | `'b'.islower()` | `True` |
| `ch.isspace()` | Ký tự `ch` có phải là khoảng trắng (space, tab, enter) không? | `' '.isspace()` | `True` |

> **Lưu ý quan trọng:** Các cách kiểm tra trên chỉ đúng khi `ch` là một ký tự đơn hoặc chuỗi con cùng loại. Chuỗi rỗng `""` luôn cho `False`. Dấu cách `' '` không phải chữ cái, cũng không phải chữ số!

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

Vì chuỗi trong Python **không đổi được trực tiếp**, các phép biến đổi **không sửa chuỗi gốc**, mà luôn tạo ra một **chuỗi mới**:

### 3.1. Chuyển đổi hoa — thường
* `s.upper()`: Tạo chuỗi mới, mọi chữ cái thành **in hoa**.
* `s.lower()`: Tạo chuỗi mới, mọi chữ cái thành **in thường**.
* `s.swapcase()`: Đảo lại: hoa thành thường, thường thành hoa.

```python
s = "Python 2026"
print(s.upper())     # "PYTHON 2026"
print(s.lower())     # "python 2026"
print(s.swapcase())  # "pYTHON 2026"
print(s)             # Vẫn là "Python 2026" (chuỗi gốc không đổi)
```

### 3.2. Thay thế chuỗi con với `s.replace(old, new)`
* Cú pháp: `s.replace(chuoi_cu, chuoi_moi)`
* Thay mọi chỗ `chuoi_cu` bằng `chuoi_moi`:
```python
s = "lap-trinh-python"
s_moi = s.replace("-", " ")
print(s_moi)  # "lap trinh python"
```

---

## 4. Bản chất mã ASCII: Cầu nối giữa Chữ cái và Con số

Trong máy, mỗi ký tự được ghi bằng một số nguyên từ $0$ đến $127$ (gọi là mã ASCII).

### 4.1. Bảng mã ASCII chuẩn mực cần nhớ nằm lòng

| Ký tự | Mã ASCII (`ord`) | Quy luật & Ứng dụng |
|:---:|:---:|---|
| `'0'` đến `'9'` | $48$ đến $57$ | Muốn đổi ký tự số sang số nguyên: `int(ch)` hoặc `ord(ch) - 48` |
| `'A'` đến `'Z'` | $65$ đến $90$ | Chữ hoa liên tiếp cách nhau đúng 1 đơn vị |
| `'a'` đến `'z'` | $97$ đến $122$ | Chữ thường liên tiếp cách nhau đúng 1 đơn vị |
| `' '` (space) | $32$ | Khoảng trắng |

> 💡 **Hằng số vàng 32:**
> $$\mathbf{ord('a') - ord('A') = 97 - 65 = 32}$$
> Chữ thường luôn lớn hơn chữ hoa tương ứng đúng **32 đơn vị**.
> Do đó:
> * Đổi hoa sang thường: `chr(ord(ch) + 32)`
> * Đổi thường sang hoa: `chr(ord(ch) - 32)`

### 4.2. Hai hàm chuyển đổi: `ord()` và `chr()`
* `ord(ch)`: Nhận **1 ký tự**, trả về **mã số ASCII** của nó.
* `chr(code)`: Nhận **mã số**, trả về **ký tự** tương ứng.

```python
print(ord('A'))         # In ra: 65
print(chr(65))          # In ra: 'A'
print(chr(ord('A') + 1)) # In ra: 'B' (Ký tự kế tiếp)
```

---

## 5. Tách từ (`split`) và Ghép từ (`join`) — Chuẩn hóa câu văn

Xử lý từ ngữ là dạng bài quen thuộc: đếm số từ, tìm từ dài nhất, đảo từ trong câu.

### 5.1. Phương thức `s.split()` thần thánh
* Khi gọi `s.split()` không kèm gì thêm, Python sẽ:
  1. Tự tìm mọi cụm khoảng trắng (1 dấu cách, nhiều dấu cách liền nhau, cách ở đầu/cuối).
  2. Tách câu thành một **danh sách (`list`) các từ riêng**.

```python
s = "   Ha    Noi   mua    thu   "
danh_sach_tu = s.split()
print(danh_sach_tu)      # ['Ha', 'Noi', 'mua', 'thu']
print(len(danh_sach_tu)) # In ra: 4 (Đếm số từ cực kỳ chính xác!)
```

### 5.2. Phương thức ghép chuỗi `sep.join(list)`
* Nối mọi chuỗi trong danh sách lại, ngăn cách bằng `sep`:
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

## 7. Lỗi hay gặp và bẫy lỗi kinh điển

> **Lỗi hay gặp 1: Nối chuỗi thay vì cộng số**
> * Khi duyệt các ký tự số, nếu viết:
>   ```python
>   tong += ch  # ch vẫn là kiểu chuỗi '3', '7'
>   ```
>   Thì máy sẽ ghép chuỗi: `"0" + "3" + "7" = "037"`, chứ không cộng số!
> * **Cách viết an toàn:** Luôn đổi kiểu `int(ch)` trước khi cộng: `tong += int(ch)`.

> **Lỗi hay gặp 2: Đếm số từ bằng cách đếm dấu cách**
> * Có bạn dùng cách: `so_tu = s.count(' ') + 1`.
> * Nếu văn bản có 2 dấu cách liền nhau `"Ha  Noi"`, cách trên đếm ra 3 từ — **sai hẳn!**
> * **Quy tắc vàng:** Luôn dùng `len(s.split())` để đếm từ đúng hẳn.

> **Lỗi hay gặp 3: Quên rằng `s.upper()` không đổi chuỗi gốc**
> * Viết:
>   ```python
>   s = "abc"
>   s.upper()
>   print(s)  # Vẫn in ra: "abc"
>   ```
> * **Nhớ gán lại:** `s = s.upper()`.

---

## 8. Mẫu code thường gặp

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
