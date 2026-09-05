# Bài 13: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự

## 1. Bản chất khoa học máy tính: Chuỗi ký tự trong bộ nhớ RAM

Trong khoa học máy tính, chuỗi ký tự (`str`) là một **dãy hữu hạn các ký tự được xếp liền kề nhau có thứ tự** trong bộ nhớ RAM. Khác với số nguyên hay số thực là một giá trị đơn lẻ, một chuỗi ký tự là một tập hợp tuần tự các phần tử con.

Mỗi ký tự trong chuỗi được gắn một vị trí cố định gọi là **chỉ số (index)**. Python hỗ trợ hệ thống hai chiều chỉ số vô cùng linh hoạt:
* **Chỉ số dương (Chỉ số xuôi):** Bắt đầu từ $0$ tại ký tự đầu tiên bên trái, tăng dần đến $\text{len}(s) - 1$ ở ký tự cuối cùng.
* **Chỉ số âm (Chỉ số ngược):** Bắt đầu từ $-1$ tại ký tự cuối cùng bên phải, giảm dần về $-\text{len}(s)$ ở ký tự đầu tiên.

![Hệ thống chỉ số dương và âm của chuỗi ký tự](../../assets/l13_string_indexing.svg?v=1788575106)

### Bảng tra cứu chỉ số chuỗi với ví dụ `s = "PYTHON"`:

| Chiều duyệt | Ký tự 1 | Ký tự 2 | Ký tự 3 | Ký tự 4 | Ký tự 5 | Ký tự 6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Ký tự thực tế** | `'P'` | `'Y'` | `'T'` | `'H'` | `'O'` | `'N'` |
| **Chỉ số dương (Từ trái sang phải)** | `0` | `1` | `2` | `3` | `4` | `5` |
| **Chỉ số âm (Từ phải sang trái)** | `-6` | `-5` | `-4` | `-3` | `-2` | `-1` |

### Các cú pháp truy cập cơ bản:

```python
s = "PYTHON"

print(s[0])     # In ra: 'P'  (Ký tự đầu tiên)
print(s[5])     # In ra: 'N'  (Ký tự cuối cùng: index = len(s) - 1)
print(s[-1])    # In ra: 'N'  (Ký tự cuối cùng dùng chỉ số âm)
print(s[-2])    # In ra: 'O'  (Ký tự áp chót)
print(len(s))   # In ra: 6    (Độ dài chuỗi - tổng số lượng ký tự)
```

> ⚠️ **Tử huyệt bắt buộc phải nhớ: Lỗi vượt quá chỉ số (`IndexError`)**
> * Nếu chuỗi có độ dài $N = \text{len}(s)$, chỉ số dương hợp lệ chỉ nằm trong đoạn $[0, N - 1]$.
> * Truy cập vào `s[N]` hoặc `s[len(s)]` sẽ khiến chương trình bị dừng đột ngột với lỗi: `IndexError: string index out of range`.
> * Với chuỗi rỗng `s = ""`, độ dài bằng 0, mọi thao tác truy cập `s[0]` đều gây lỗi ngay lập tức.

---

## 2. Kỹ thuật cắt lát chuỗi — Trích xuất chuỗi con

Cắt lát là kỹ thuật mạnh mẽ nhất của Python cho phép trích xuất một đoạn ký tự liên tiếp hoặc cách quãng từ chuỗi ban đầu để tạo thành một chuỗi con mới.

### Cú pháp tổng quát:
$$\mathbf{s[\text{start} : \text{stop} : \text{step}]}$$

* `start`: Vị trí chỉ số bắt đầu lấy (mặc định là $0$ nếu để trống).
* `stop`: Vị trí chỉ số kết thúc (nhưng **luôn bị loại trừ**, tức chỉ lấy đến chỉ số $\text{stop} - 1$).
* `step`: Bước nhảy (mặc định là $1$ nếu để trống). Bước nhảy âm mang ý nghĩa duyệt lùi.

### Bảng các mẫu cắt lát kinh điển trong phòng thi:

| Cú pháp cắt lát | Quy tắc trích xuất | Ví dụ với `s = "ABCDEFGH"` | Chuỗi con kết quả |
|---|---|---|:---:|
| `s[2:5]` | Lấy từ vị trí $2$ đến vị trí $4$ | `s[2:5]` | `"CDE"` |
| `s[:4]` | Bỏ trống `start`: Lấy từ đầu đến vị trí $3$ | `s[:4]` | `"ABCD"` |
| `s[3:]` | Bỏ trống `stop`: Lấy từ vị trí $3$ đến hết chuỗi | `s[3:]` | `"DEFGH"` |
| `s[::2]` | Lấy từ đầu đến cuối với bước nhảy $2$ | `s[::2]` | `"ACEG"` |
| `s[1::2]` | Lấy từ vị trí $1$ với bước nhảy $2$ (vị trí lẻ) | `s[1::2]` | `"BDFH"` |
| `s[::-1]` | **Bí thuật đảo ngược chuỗi**: Bước nhảy $-1$ | `s[::-1]` | `"HGFEDCBA"` |

```python
s = "iKHEDU2026"

print(s[0:6])   # "iKHEDU" (Lấy 6 ký tự đầu tiên)
print(s[:6])    # "iKHEDU" (Cách viết gọn tương đương)
print(s[6:])    # "2026"   (Lấy từ vị trí thứ 6 đến hết)
print(s[::-1])  # "6202UDEHKi" (Đảo ngược toàn bộ chuỗi)
```

> 💡 **Quy tắc khoảng bán mở $[start, stop)$:**
> Trong Python, quy tắc cận trên `stop` bị loại trừ áp dụng đồng nhất từ hàm `range(start, stop)` cho đến cú pháp cắt lát `s[start:stop]`. Số lượng ký tự được trích xuất khi `step = 1` luôn bằng đúng công thức: $\text{stop} - \text{start}$.

---

## 3. Đặc tính bất biến của chuỗi ký tự

Đây là một trong những khái niệm quan trọng nhất phân biệt kiểu chuỗi ký tự (`str`) với kiểu danh sách (`list`):

* **Chuỗi ký tự trong Python là bất biến:** Một khi chuỗi đã được tạo ra trong bộ nhớ RAM, ta **không thể thay đổi, sửa đổi hay gán đè trực tiếp** bất kỳ ký tự nào tại từng vị trí của nó.

```python
s = "HELLO"

# Cố gắng sửa chữ 'H' thành chữ 'J':
# s[0] = "J"
# ❌ Báo lỗi nghiêm trọng: TypeError: 'str' object does not support item assignment
```

### Cách xử lý chuẩn xác khi muốn thay đổi ký tự trong chuỗi:
Ta bắt buộc phải **tạo ra một chuỗi hoàn toàn mới** bằng phép ghép chuỗi (`+`) hoặc cắt lát:

```python
s = "HELLO"

# ✅ ĐÚNG: Ghép ký tự mới với phần đuôi còn lại của chuỗi
s = "J" + s[1:]
print(s)  # In ra: "JELLO"
```

---

## 4. Các phương thức duyệt chuỗi bằng vòng lặp

Duyệt chuỗi là thao tác ghé thăm từng ký tự một để kiểm tra, đếm số lượng hoặc thực hiện phép tính toán.

### 4.1. Duyệt trực tiếp từng ký tự bằng `for ... in`
Dùng khi bài toán chỉ quan tâm đến giá trị của từng ký tự mà không cần biết ký tự đó đứng ở thứ hạng (chỉ số) bao nhiêu:

```python
s = input()
for ch in s:
    print(ch)
```

### 4.2. Duyệt qua chỉ số bằng `for i in range(len(s))`
Dùng khi bài toán yêu cầu xử lý dựa trên vị trí, ví dụ: kiểm tra ký tự đứng cạnh nhau, đổi chỗ, hoặc chỉ xét các vị trí chẵn/lẻ:

```python
s = input()
for i in range(len(s)):
    # s[i] là ký tự tại vị trí thứ i
    if i % 2 == 0:
        print(f"Ký tự tại vị trí chẵn {i}: {s[i]}")
```

### 4.3. Duyệt cặp ký tự liền kề
Mẫu thuật toán kiểm tra hai ký tự giống nhau đứng cạnh nhau:

```python
s = input()
dem_trung = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        dem_trung += 1
print(dem_trung)
```

---

## 5. Bảng mô phỏng biến thiên ô nhớ

### Thuật toán: Kiểm tra chuỗi có đối xứng hay không bằng hai con trỏ

```python
s = "RADAR"
la_doi_xung = True
n = len(s)

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        la_doi_xung = False
        break

if la_doi_xung:
    print("YES")
else:
    print("NO")
```

| Bước | Vòng lặp `i` | So sánh `s[i]` và `s[n - 1 - i]` | Kết quả so sánh | Biến `la_doi_xung` | Trạng thái thực thi |
|:---:|:---:|:---:|:---:|:---:|---|
| Khởi tạo | — | — | — | `True` | $n = 5$, vòng lặp chạy $i \in [0, 1]$ |
| 1 | $i = 0$ | `s[0]` ('R') so với `s[4]` ('R') | `'R' == 'R'` | `True` | Thỏa mãn, tiếp tục vòng lặp |
| 2 | $i = 1$ | `s[1]` ('A') so với `s[3]` ('A') | `'A' == 'A'` | `True` | Thỏa mãn, tiếp tục vòng lặp |
| Kết thúc | — | — | — | `True` | Hết vòng lặp, in ra `YES` |

---

## 6. Tử huyệt và bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: TÌM KIẾM BẰNG `find()` TRẢ VỀ `-1`**
> * Hàm `s.find(sub)` tìm vị trí xuất hiện đầu tiên của `sub` trong `s`. Nếu không tìm thấy, hàm trả về `-1` (không gây lỗi chương trình).
> * Nếu học sinh viết `if s.find("a"):` $\implies$ Sai nghiêm trọng! Vì trong Python, số `-1` được xem là `True` trong biểu thức logic.
> * **Cách viết an toàn:** `if s.find("a") != -1:` hoặc dùng toán tử trực tiếp: `if "a" in s:`.

> ❌ **BẪY LỖI 2: NHẦM LẪN GIỮA PHÉP NỐI CHUỖI VÀ CỘNG SỐ**
> * Khi đọc dữ liệu bằng `input()`, nếu người dùng nhập số `12` thì kiểu dữ liệu nhận được vẫn là chuỗi `"12"`.
> * Phép tính `"12" + "34"` sẽ cho ra `"1234"` (ghép hai chuỗi).
> * **Cách viết an toàn:** Phải đổi kiểu dữ liệu thành số nguyên bằng `int()` trước khi tính toán.

> ❌ **BẪY LỖI 3: PHÂN BIỆT CHỮ HOA VÀ CHỮ THƯỜNG TRONG PHÉP SO SÁNH**
> * Trong Python, `'A' == 'a'` luôn trả về `False`.
> * Khi đề bài yêu cầu không phân biệt chữ hoa thường, luôn chuẩn hóa về cùng một dạng: `if s1.lower() == s2.lower():`.

---

## 7. Mẫu code chuẩn thi đấu

### 7.1. Mẫu kiểm tra chuỗi đối xứng
```python
s = input()
if s == s[::-1]:
    print("YES")
else:
    print("NO")
```

### 7.2. Mẫu xóa bỏ ký tự tại vị trí chỉ định $K$
```python
s = input()
k = int(input())
# Trích xuất đoạn trước k và đoạn sau k rồi ghép lại
ket_qua = s[:k] + s[k + 1:]
print(ket_qua)
```

### 7.3. Mẫu đếm số lần xuất hiện của một ký tự bằng vòng lặp
```python
s = input()
ky_tu_can_tim = input()
dem = 0

for ch in s:
    if ch == ky_tu_can_tim:
        dem += 1

print(dem)
```

---

## 8. Concept Quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Ký tự đầu tiên của chuỗi `s = "PYTHON"` có chỉ số bằng bao nhiêu?
- **A.** 1
- **B.** **[Đáp án đúng]** 0
- **C.** -1
- **D.** Không có chỉ số
- > *Giải thích:* Trong Python, chỉ số của chuỗi luôn được đánh số bắt đầu từ 0.

#### Câu 2: Lệnh `print("HELLO"[-1])` sẽ hiển thị ký tự nào ra màn hình?
- **A.** `'H'`
- **B.** `'E'`
- **C.** **[Đáp án đúng]** `'O'`
- **D.** Báo lỗi chỉ số âm
- > *Giải thích:* Chỉ số `-1` đại diện cho ký tự cuối cùng của chuỗi.

#### Câu 3: Cho chuỗi `s = "TIN HOC"`. Hàm `len(s)` trả về kết quả bằng bao nhiêu?
- **A.** 6
- **B.** **[Đáp án đúng]** 7
- **C.** 5
- **D.** 8
- > *Giải thích:* Ký tự khoảng trắng giữa `"TIN"` và `"HOC"` cũng được tính là một ký tự trong chuỗi.

#### Câu 4: Kết quả của biểu thức cắt lát `"VIETNAM"[1:4]` là gì?
- **A.** `"VIET"`
- **B.** `"IETN"`
- **C.** **[Đáp án đúng]** `"IET"`
- **D.** `"VIE"`
- > *Giải thích:* Cắt lát lấy từ chỉ số 1 đến chỉ số $4 - 1 = 3$. Các ký tự tại vị trí 1, 2, 3 là `'I'`, `'E'`, `'T'`.

#### Câu 5: Cách viết nào sau đây giúp đảo ngược chuỗi `s` nhanh nhất trong Python?
- **A.** `s.reverse()`
- **B.** **[Đáp án đúng]** `s[::-1]`
- **C.** `reverse(s)`
- **D.** `s[-1:0]`
- > *Giải thích:* `s[::-1]` là kỹ thuật cắt lát bước nhảy $-1$. Phương thức `.reverse()` chỉ dùng cho danh sách (`list`), không dùng được cho chuỗi.

#### Câu 6: Tính chất bất biến của chuỗi trong Python có nghĩa là gì?
- **A.** Không thể in chuỗi ra màn hình
- **B.** Không thể ghép hai chuỗi lại với nhau
- **C.** **[Đáp án đúng]** Không thể sửa đổi trực tiếp giá trị của một ký tự tại vị trí bất kỳ (`s[i] = ...` gây lỗi)
- **D.** Chuỗi không thể chứa số
- > *Giải thích:* Khi chuỗi được nạp vào bộ nhớ, các phần tử của nó không thể bị gán đè tại chỗ.

#### Câu 7: Biểu thức `"BANANAS".count("AN")` trả về kết quả bằng bao nhiêu?
- **A.** 1
- **B.** **[Đáp án đúng]** 2
- **C.** 3
- **D.** 0
- > *Giải thích:* Chuỗi con `"AN"` xuất hiện 2 lần trong `"BANANAS"` (tại vị trí 1 và 3).

#### Câu 8: Lệnh `print("HELLO"[10])` sẽ dẫn đến hiện tượng gì?
- **A.** In ra khoảng trắng
- **B.** In ra giá trị `None`
- **C.** **[Đáp án đúng]** Báo lỗi `IndexError: string index out of range`
- **D.** In ra chữ `'O'`
- > *Giải thích:* Chuỗi `"HELLO"` chỉ có độ dài 5 (chỉ số lớn nhất là 4). Truy cập chỉ số 10 vượt quá phạm vi bộ nhớ của chuỗi.

#### Câu 9: Cho `s = "ABCDE"`. Biểu thức `s[2:]` cho kết quả là gì?
- **A.** `"AB"`
- **B.** `"BC"`
- **C.** **[Đáp án đúng]** `"CDE"`
- **D.** `"CD"`
- > *Giải thích:* Bỏ trống tham số `stop` đồng nghĩa với việc lấy từ vị trí bắt đầu (chỉ số 2 là `'C'`) đến hết chuỗi.

#### Câu 10: Biểu thức `"Python".find("th")` trả về giá trị gì?
- **A.** `True`
- **B.** 1
- **C.** **[Đáp án đúng]** 2
- **D.** 3
- > *Giải thích:* Chuỗi con `"th"` bắt đầu xuất hiện tại vị trí chỉ số 2 của `"Python"`.

#### Câu 11: Nếu chuỗi con không tồn tại trong chuỗi gốc, phương thức `find()` sẽ trả về:
- **A.** `0`
- **B.** `False`
- **C.** **[Đáp án đúng]** `-1`
- **D.** Báo lỗi chương trình
- > *Giải thích:* Đây là quy ước của Python giúp phân biệt với vị trí 0 (đầu chuỗi).

#### Câu 12: Biểu thức `"HA NOI"[::2]` trả về chuỗi nào?
- **A.** `"H NO"`
- **B.** **[Đáp án đúng]** `"H OI"`
- **C.** `"A NI"`
- **D.** `"HA NOI"`
- > *Giải thích:* Lấy các ký tự tại chỉ số chẵn 0, 2, 4, 6: `'H'`, `' '`, `'O'`, `'I'` $\implies$ `"H OI"`.

#### Câu 13: Đoạn code sau in ra gì?
```python
s = "A"
s = s * 3
print(s)
```
- **A.** `AAA`
- **B.** `AA`
- **C.** **[Đáp án đúng]** `AAA`
- **D.** `3A`
- > *Giải thích:* Toán tử nhân `*` giữa chuỗi và số nguyên thực hiện phép lặp lại chuỗi đó: `"A" * 3` = `"AAA"`.

#### Câu 14: Chuỗi `s = "12321"` có phải là chuỗi đối xứng không?
- **A.** Không
- **B.** **[Đáp án đúng]** Có (vì `s == s[::-1]` trả về `True`)
- **C.** Chỉ đối xứng khi chứa chữ cái
- **D.** Báo lỗi cú pháp
- > *Giải thích:* Đọc xuôi hay đọc ngược đều thu được dãy `"12321"`.

#### Câu 15: Cho chuỗi `s = "KHOA HOC"`. Kết quả của `s[:4]` là:
- **A.** `"KHO"`
- **B.** **[Đáp án đúng]** `"KHOA"`
- **C.** `"KHOA "`
- **D.** `"HOA "`
- > *Giải thích:* Lấy từ đầu đến chỉ số $4 - 1 = 3$, gồm 4 ký tự `'K'`, `'H'`, `'O'`, `'A'`.
