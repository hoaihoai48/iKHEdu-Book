# Bài 04: Cấu trúc rẽ nhánh

## 1. Bản chất của cấu trúc rẽ nhánh trong khoa học máy tính

Trong chương trình tuần tự, các dòng lệnh được máy tính nạp vào và thực thi từ trên xuống dưới một cách máy móc. Tuy nhiên, trong thế giới thực cũng như trong các bài toán thực tế, máy tính cần có khả năng **ra quyết định**: *Nếu điều kiện này đúng thì thực hiện công việc A, nếu sai thì chuyển sang thực hiện công việc B*.

Cấu trúc cho phép máy tính thay đổi dòng chảy thực thi dựa trên điều kiện được gọi là **Cấu trúc rẽ nhánh**.

![Sơ đồ luồng rẽ nhánh if-else](../../assets/l04_branching_visual.svg?v=1788575106)

---

## 2. Thiết lập điều kiện so sánh trong câu lệnh `if`

Ở Bài 02, chúng ta đã làm quen với các phép toán so sánh trả về kết quả Đúng (`True`) hoặc Sai (`False`). Trong cấu trúc rẽ nhánh, biểu thức so sánh đóng vai trò là **"người gác cổng"** quyết định máy tính có bước vào thực thi khối lệnh hay không:

| Phép so sánh | Ký hiệu | Cú pháp trong `if` | Ý nghĩa điều kiện |
|:---:|:---:|---|---|
| **Bằng nhau** | `==` | `if n == 0:` | Đúng khi giá trị của `n` bằng 0 |
| **Khác nhau** | `!=` | `if n != 0:` | Đúng khi giá trị của `n` khác 0 |
| **Lớn hơn** | `>` | `if diem > 5:` | Đúng khi `diem` lớn hơn 5 |
| **Nhỏ hơn** | `<` | `if diem < 5:` | Đúng khi `diem` nhỏ hơn 5 |
| **Lớn hơn hoặc bằng** | `>=` | `if tuoi >= 18:` | Đúng khi `tuoi` từ 18 trở lên |
| **Nhỏ hơn hoặc bằng** | `<=` | `if tuoi <= 10:` | Đúng khi `tuoi` từ 10 trở xuống |

> ❌ **TỬ HUYỆT BẮT BUỘC PHẢI NHỚ: NHẦM LẪN GIỮA DẤU GÁN `=` VÀ DẤU SO SÁNH `==`**
>
> * Dấu `=` (Một dấu bằng): Là **phép gán giá trị** từ vế phải vào biến ở vế trái (`x = 10`).
> * Dấu `==` (Hai dấu bằng liền nhau): Là **phép so sánh bằng**, trả về `True` hoặc `False`.
> * Nếu viết `if a = 5:` $\implies$ Máy tính sẽ báo lỗi cú pháp ngay lập tức: `SyntaxError: invalid syntax`.

---

## 3. Quy tắc Thụt lề — Linh hồn của cú pháp Python

Trong nhiều ngôn ngữ lập trình như C++ hay Pascal, người ta dùng cặp ngoặc nhọn `{ }` hoặc cặp từ khóa `begin ... end` để gom các dòng lệnh thành một khối. 

Trong Python, nhà thiết kế ngôn ngữ đã loại bỏ hoàn toàn các cặp ngoặc rườm rà này và sử dụng **quy tắc Thụt lề**:
* Tất cả các dòng lệnh thuộc cùng một khối lệnh con **bắt buộc phải được thụt vào trong cùng một khoảng cách** (chuẩn quốc tế là **4 dấu cách / 1 phím Tab**).
* Khi hết khối lệnh con, dòng lệnh tiếp theo được lùi ra ngoài bằng lề với câu lệnh cha.
* Dấu hai chấm `:` ở cuối dòng lệnh điều kiện là **bắt buộc**, báo hiệu cho Python biết rằng chuẩn bị bắt đầu một khối lệnh thụt lề mới.

```python
diem = 8
if diem >= 5:
    print("Chuc mung!")       # Thuộc khối lệnh IF (Thụt lề 4 dấu cách)
    print("Ban da qua mon.")  # Thuộc khối lệnh IF (Thụt lề 4 dấu cách)
print("Ket thuc chuong trinh.") # Không thuộc IF, luôn luôn được in
```

---

## 4. 3 Dạng cấu trúc rẽ nhánh từ cơ bản đến phức tạp

### 4.1. Dạng 1: Cấu trúc `if` đơn (Khuyết thiếu)
Dùng khi chỉ muốn thực hiện một hành động nếu điều kiện thỏa mãn; nếu không thỏa mãn thì bỏ qua và đi tiếp.

```python
n = int(input())
if n < 0:
    n = -n  # Nếu n là số âm, đổi dấu thành số dương
print(n)
```

### 4.2. Dạng 2: Cấu trúc `if - else` (Đầy đủ)
Hai nhánh đối lập loại trừ lẫn nhau: Nếu điều kiện `True` thì thực hiện khối `if`, ngược lại nếu điều kiện `False` thì thực hiện khối `else`.

```python
n = int(input())
if n % 2 == 0:
    print("CHAN")
else:
    print("LE")
```

### 4.3. Dạng 3: Cấu trúc đa nhánh `if - elif - else`
Dùng khi có từ 3 lựa chọn trở lên. Từ khóa `elif` là viết tắt của *Else If (Nếu không thì xét tiếp)*:
* Python duyệt các điều kiện lần lượt từ trên xuống dưới.
* Ngay khi gặp điều kiện đầu tiên thỏa mãn `True`, Python thực thi khối lệnh tương ứng và **bỏ qua toàn bộ các nhánh `elif` và `else` còn lại bên dưới**.

```python
# Ví dụ: Xếp loại học tập theo thang điểm
diem = float(input())
if diem >= 8.0:
    print("GIOI")
elif diem >= 6.5:
    print("KHA")
elif diem >= 5.0:
    print("TRUNG BINH")
else:
    print("YEU")
```

---

## 5. Kỹ thuật ghép nhiều điều kiện: `and`, `or`, `not`

Khi một quyết định trong câu lệnh rẽ nhánh đòi hỏi kết hợp nhiều yếu tố, ta sử dụng các liên từ logic đã học ở Bài 02 để kết nối các biểu thức điều kiện:

| Liên từ | Ý nghĩa trong `if` | Khi nào nhánh `if` được chạy? | Ví dụ thực tế |
|:---:|---|---|---|
| **`and`** | **ĐỒNG THỜI** (Và) | Khi **tất cả** các điều kiện con đều đúng | `if diem >= 8 and hanh_kiem == "Tot":` |
| **`or`** | **HOẶC** (Ít nhất một) | Khi **có ít nhất một** điều kiện con đúng | `if thu == "Bay" or thu == "Chu Nhat":` |
| **`not`** | **PHỦ ĐỊNH** (Đảo ngược) | Khi điều kiện bên trong bị sai | `if not hop_le:` |

### Thứ tự ưu tiên logic:
1. Phép so sánh số học: `>`, `<`, `==`, ...
2. `not`
3. `and`
4. `or`
* **Lời khuyên an toàn:** Luôn dùng cặp ngoặc tròn `( )` để gom nhóm các điều kiện logic phức tạp, giúp code trong sáng và không bị hiểu nhầm thứ tự ưu tiên (ví dụ: `if (a > 0 and b > 0) or c > 0:`).

---

## 6. Các bài toán thuật toán kinh điển khi làm bài

### 6.1. Tìm số lớn nhất giữa 2 số
```python
a, b = map(int, input().split())
if a > b:
    max_val = a
else:
    max_val = b
print(max_val)
```

### 6.2. Tìm số lớn nhất giữa 3 số (Kỹ thuật Lính canh - Sentinel)
```python
a, b, c = map(int, input().split())
# Đặt a làm lính canh giữ ngôi vị lớn nhất tạm thời
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print(max_val)
```

### 6.3. Kiểm tra 3 cạnh có tạo thành tam giác hợp lệ
Theo định lý Bất đẳng thức tam giác, 3 cạnh $a, b, c$ ($a, b, c > 0$) tạo thành một tam giác khi và chỉ khi **tổng của hai cạnh bất kỳ luôn lớn hơn cạnh còn lại**:
$$\begin{cases} a + b > c \\ a + c > b \\ b + c > a \end{cases}$$

```python
a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    print("HOP LE")
else:
    print("KHONG HOP LE")
```

### 6.4. Bài toán kiểm tra Năm Nhuận
Quy ước lịch thiên văn quốc tế: Một năm $Y$ là năm nhuận khi và chỉ khi:
* Năm đó chia hết cho 400.
* **HOẶC** (Năm đó chia hết cho 4 và không chia hết cho 100).

```python
nam = int(input())
if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    print("NAM NHUAN")
else:
    print("KHONG NHUAN")
```

---

## 7. Bảng mô phỏng biến thiên ô nhớ

Xét đoạn chương trình xếp loại học lực với `diem = 7.2`:
```python
diem = 7.2
if diem >= 8.0:
    loai = "GIOI"
elif diem >= 6.5:
    loai = "KHA"
elif diem >= 5.0:
    loai = "TB"
else:
    loai = "YEU"
```

### Bảng theo dõi luồng điều khiển của CPU:

| Bước | Điều Kiện Được Đánh Giá | Biểu Thức Tính Toán | Kết Quả Boolean | Hành Động Của CPU |
|:---:|---|---|:---:|---|
| **1** | Nhánh `if diem >= 8.0` | `7.2 >= 8.0` | `False` | Bỏ qua khối lệnh `"GIOI"`, nhảy xuống xét nhánh `elif` kế tiếp |
| **2** | Nhánh `elif diem >= 6.5` | `7.2 >= 6.5` | **`True`** | **Khớp điều kiện!** Thực thi lệnh `loai = "KHA"` |
| **3** | Các nhánh còn lại bên dưới | `diem >= 5.0`, `else` | *(Bỏ qua)* | **Thoát ngay lập tức khỏi toàn bộ cấu trúc if**, không xét tiếp |

$$\implies \text{Kết quả cuối cùng lưu trong biến } loai = \text{"KHA"}$$

---

## 8. Tử huyệt và Bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: QUÊN DẤU HAI CHẤM `:` Ở ĐẦU CÂU LỆNH**
> * Viết `if x > 0` $\implies$ Báo lỗi `SyntaxError: expected ':'`.

> ❌ **BẪY LỖI 2: THỤT LỀ KHÔNG ĐỒNG ĐỀU (`IndentationError`)**
> * Dòng trên thụt 4 dấu cách, dòng dưới thụt 2 dấu cách trong cùng một khối lệnh sẽ bị chương trình kiểm tra dừng ngay lập tức: `IndentationError: unindent does not match any outer indentation level`.

> ❌ **BẪY LỖI 3: DÙNG NHIỀU `if` ĐỘC LẬP THAY VÌ CHUỖI `elif`**
> * Hãy xem đoạn code sai lầm sau:
>   ```python
>   if diem >= 5.0:
>       print("DAT")
>   if diem >= 8.0:
>       print("XUAT SAC")
>   ```
>   Nếu học sinh được `9.0` điểm, chương trình sẽ in ra **CẢ HAI DÒNG**: `DAT` và `XUAT SAC`!
> * **Cách viết đúng:** Luôn dùng chuỗi `if - elif` để đảm bảo các điều kiện được sắp xếp theo thứ tự phân loại chặt chẽ.

---

## 9. Mẫu code thường gặp

```python
# Mẫu kiểm tra số chẵn lẻ và số âm dương
n = int(input())
if n > 0:
    if n % 2 == 0:
        print("DUONG CHAN")
    else:
        print("DUONG LE")
elif n < 0:
    print("SO AM")
else:
    print("SO KHONG")
```

---

## 10. Concept Quiz: 24 câu trắc nghiệm kiểm tra sâu khái niệm

#### Câu 1 (Bản chất cú pháp rẽ nhánh):
Ký tự nào sau đây **BẮT BUỘC** phải có ở cuối dòng lệnh `if` hoặc `else` trong Python?
- **A.** Dấu chấm phẩy `;`
- **B.** **[Đáp án đúng]** Dấu hai chấm `:`
- **C.** Dấu ngoặc nhọn `{`
- **D.** Dấu chấm `.`
> *Giải thích:* Trong Python, dấu hai chấm `:` bắt buộc phải có ở cuối câu lệnh rẽ nhánh để mở ra khối lệnh con.

#### Câu 2 (Bắt bẫy dấu so sánh):
Để kiểm tra xem giá trị của biến `x` có bằng 10 hay không, câu lệnh nào sau đây là đúng?
- **A.** `if x = 10:`
- **B.** **[Đáp án đúng]** `if x == 10:`
- **C.** `if x := 10:`
- **D.** `if x equals 10:`
> *Giải thích:* Phép so sánh bằng trong Python sử dụng hai dấu bằng liên tiếp `==`. Một dấu `=` là phép gán.

#### Câu 3 (Quy tắc thụt lề):
Các câu lệnh nằm bên trong khối lệnh `if` phải được thụt lề vào trong bao nhiêu khoảng trắng theo chuẩn PEP 8?
- **A.** 1 khoảng trắng
- **B.** 2 khoảng trắng
- **C.** **[Đáp án đúng]** 4 khoảng trắng (hoặc 1 phím Tab)
- **D.** Không cần thụt lề
> *Giải thích:* Chuẩn mực quốc tế của Python là 4 khoảng trắng cho mỗi cấp độ thụt lề.

#### Câu 4 (Dự đoán output — if-else):
Đoạn code sau đây sẽ in ra kết quả gì?
```python
n = 15
if n % 2 == 0:
    print("CHAN")
else:
    print("LE")
```
- **A.** `CHAN`
- **B.** **[Đáp án đúng]** `LE`
- **C.** `CHAN LE`
- **D.** Báo lỗi cú pháp
> *Giải thích:* $15 \% 2 = 1 \ne 0$, do đó nhánh `if` là `False`, chương trình nhảy vào nhánh `else` in ra `LE`.

#### Câu 5 (Toán tử logic AND):
Biểu thức logic `(5 > 3) and (10 < 8)` có giá trị là:
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `None`
- **D.** `Error`
> *Giải thích:* Biểu thức thứ nhất `5 > 3` là `True`, nhưng biểu thức thứ hai `10 < 8` là `False`. Toán tử `and` yêu cầu cả hai đều phải đúng mới ra `True`.

#### Câu 6 (Toán tử logic OR):
Biểu thức logic `(5 > 3) or (10 < 8)` có giá trị là:
- **A.** **[Đáp án đúng]** `True`
- **B.** `False`
- **C.** `1`
- **D.** `0`
> *Giải thích:* Toán tử `or` chỉ cần ít nhất 1 vế đúng thì toàn bộ biểu thức sẽ là `True`. Vì `5 > 3` đúng nên kết quả là `True`.

#### Câu 7 (Toán tử logic NOT):
Giá trị của biểu thức `not (4 == 4)` là:
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `4`
- **D.** Báo lỗi cú pháp
> *Giải thích:* `4 == 4` là `True`. Lệnh `not True` sẽ đảo ngược thành `False`.

#### Câu 8 (Dự đoán output — Chuỗi if-elif):
Cho đoạn chương trình sau:
```python
x = 7
if x > 10:
    print("A")
elif x > 5:
    print("B")
elif x > 0:
    print("C")
else:
    print("D")
```
Màn hình sẽ hiển thị ký tự nào?
- **A.** `A`
- **B.** **[Đáp án đúng]** `B`
- **C.** `C`
- **D.** `B` và `C`
> *Giải thích:* Điều kiện `x > 5` đúng đầu tiên $\implies$ In ra `B` và thoát ngay khỏi cấu trúc rẽ nhánh, không xét nhánh `x > 0`.

#### Câu 9 (Bắt bẫy nhiều if rời rạc):
Nếu thay các chữ `elif` ở Câu 8 thành các chữ `if` độc lập:
```python
x = 7
if x > 10:
    print("A")
if x > 5:
    print("B")
if x > 0:
    print("C")
```
Màn hình sẽ in ra:
- **A.** `B`
- **B.** **[Đáp án đúng]** Hai dòng: `B` và `C`
- **C.** `C`
- **D.** `A B C`
> *Giải thích:* Vì đây là các câu lệnh `if` độc lập nên cả 2 điều kiện `x > 5` và `x > 0` đều được kiểm tra và thỏa mãn.

#### Câu 10 (Điều kiện số chẵn và chia hết cho 3):
Biểu thức nào sau đây kiểm tra một số nguyên $N$ vừa là số chẵn vừa chia hết cho 3?
- **A.** `N % 2 == 0 or N % 3 == 0`
- **B.** **[Đáp án đúng]** `N % 2 == 0 and N % 3 == 0`
- **C.** `N % 6 != 0`
- **D.** `N // 6 == 0`
> *Giải thích:* Yêu cầu thỏa mãn đồng thời cả 2 điều kiện nên phải dùng toán tử `and`. (Tương đương `N % 6 == 0`).

#### Câu 11 (Thuật toán tìm Max 2 số):
Đoạn code sau nhằm tìm giá trị lớn nhất giữa `a` và `b`. Chỗ trống `...` cần điền là:
```python
if a > b:
    ans = a
else:
    ans = ...
```
- **A.** `a`
- **B.** **[Đáp án đúng]** `b`
- **C.** `a + b`
- **D.** `0`
> *Giải thích:* Nếu `a > b` sai thì `b` lớn hơn hoặc bằng `a`, do đó giá trị lớn nhất là `b`.

#### Câu 12 (Điều kiện tam giác hợp lệ):
Cho 3 số dương $a, b, c$. Điều kiện nào sau đây đảm bảo 3 số này là độ dài 3 cạnh của một tam giác?
- **A.** `a + b > c or a + c > b or b + c > a`
- **B.** **[Đáp án đúng]** `a + b > c and a + c > b and b + c > a`
- **C.** `a + b + c > 0`
- **D.** `a == b and b == c`
> *Giải thích:* Định lý bất đẳng thức tam giác bắt buộc cả 3 bất đẳng thức phải đồng thời thỏa mãn.

#### Câu 13 (Kiểm tra năm nhuận):
Năm nào sau đây là năm nhuận theo quy tắc lịch quốc tế?
- **A.** 1900
- **B.** 2021
- **C.** **[Đáp án đúng]** 2000
- **D.** 2022
> *Giải thích:* Năm 2000 chia hết cho 400 nên là năm nhuận. Năm 1900 chia hết cho 100 nhưng không chia hết cho 400 nên không nhuận.

#### Câu 14 (Thứ tự ưu tiên toán tử logic):
Biểu thức `True or False and False` có giá trị là:
- **A.** **[Đáp án đúng]** `True`
- **B.** `False`
- **C.** Báo lỗi
- **D.** `None`
> *Giải thích:* Toán tử `and` có ưu tiên cao hơn `or`. Do đó tính `False and False = False` trước. Sau đó `True or False = True`.

#### Câu 15 (Bẫy so sánh chuỗi):
Kết quả của phép so sánh `"10" > "2"` trong Python là gì?
- **A.** `True` (vì số 10 lớn hơn số 2)
- **B.** **[Đáp án đúng]** `False` (vì so sánh theo bảng chữ cái, ký tự `'1'` đứng trước ký tự `'2'`)
- **C.** Báo lỗi `TypeError`
- **D.** `0`
> *Giải thích:* Hai chuỗi ký tự được so sánh theo thứ tự từ điển. Ký tự đầu tiên `'1'` có mã nhỏ hơn `'2'` nên `"10" < "2"`. Đây là lý do vì sao luôn phải ép kiểu số trước khi so sánh.

#### Câu 16 (Dự đoán output — Khối if lồng nhau):
Cho đoạn code sau:
```python
x = 12
if x > 0:
    if x % 2 == 0:
        print("DUONG CHAN")
    else:
        print("DUONG LE")
```
Màn hình sẽ in ra:
- **A.** `DUONG LE`
- **B.** **[Đáp án đúng]** `DUONG CHAN`
- **C.** Không in gì cả
- **D.** `DUONG CHAN DUONG LE`
> *Giải thích:* $x = 12 > 0$ và $12 \% 2 = 0$, thỏa mãn cả hai cấp độ điều kiện.

#### Câu 17 (Kiểm tra số có 2 chữ số):
Để kiểm tra số nguyên dương $N$ có đúng 2 chữ số, biểu thức nào là chuẩn xác nhất?
- **A.** `N > 10 and N < 100`
- **B.** **[Đáp án đúng]** `N >= 10 and N <= 99`
- **C.** `N // 100 == 0`
- **D.** `10 < N < 99`
> *Giải thích:* Các số có 2 chữ số chạy từ 10 đến 99, bao gồm cả hai đầu mút: `N >= 10 and N <= 99` (hoặc viết gọn `10 <= N <= 99`).

#### Câu 18 (Toán tử 3 ngôi — Ternary Operator):
Cú pháp viết ngắn gọn của việc tìm số lớn nhất `max_val = a if a > b else b` có ý nghĩa là:
- **A.** Nếu `a > b` thì gán `max_val = b`, ngược lại gán `a`.
- **B.** **[Đáp án đúng]** Nếu `a > b` thì gán `max_val = a`, ngược lại gán `b`.
- **C.** Luôn luôn gán `max_val = a`.
- **D.** Báo lỗi cú pháp trong Python.
> *Giải thích:* Đây là biểu thức điều kiện chuẩn của Python.

#### Câu 19 (So sánh chuỗi liên tiếp):
Trong Python, biểu thức toán học `1 <= x <= 10` có hợp lệ không?
- **A.** Không hợp lệ, phải viết là `1 <= x and x <= 10`.
- **B.** **[Đáp án đúng]** Hoàn toàn hợp lệ, Python hỗ trợ cú pháp so sánh chuỗi liên tiếp.
- **C.** Báo lỗi `SyntaxError`.
- **D.** Luôn luôn trả về `True`.
> *Giải thích:* Python là ngôn ngữ hiếm hoi cho phép viết chuỗi so sánh kép `1 <= x <= 10` rất tự nhiên giống như trong toán học.

#### Câu 20 (Nhận diện lỗi thụt lề):
Lỗi nào sau đây sẽ xảy ra nếu một câu lệnh trong khối `if` không được thụt lề?
- **A.** `ValueError`
- **B.** `TypeError`
- **C.** **[Đáp án đúng]** `IndentationError: expected an indented block`
- **D.** `NameError`
> *Giải thích:* Python kiểm tra cấu trúc khối lệnh bằng thụt lề, nếu thiếu sẽ báo `IndentationError`.

#### Câu 21 (Bắt bẫy điều kiện phủ định):
Phủ định của mệnh đề `x >= 10` là:
- **A.** `x <= 10`
- **B.** **[Đáp án đúng]** `x < 10`
- **C.** `x > 10`
- **D.** `not x`
> *Giải thích:* Phủ định của "lớn hơn hoặc bằng" là "nhỏ hơn nghiêm ngặt" ($<$).

#### Câu 22 (Kiểm tra chia hết cho 5 nhưng không chia hết cho 2):
Biểu thức logic biểu diễn "Số $N$ chia hết cho 5 nhưng là số lẻ" là:
- **A.** `N % 5 == 0 or N % 2 != 0`
- **B.** **[Đáp án đúng]** `N % 5 == 0 and N % 2 != 0`
- **C.** `N % 10 == 0`
- **D.** `N % 5 == 0 and N % 2 == 0`
> *Giải thích:* Chia hết cho 5: `N % 5 == 0`, là số lẻ: `N % 2 != 0`. Cần thỏa mãn đồng thời dùng `and`.

#### Câu 23 (Dự đoán output — Câu lệnh pass):
Từ khóa `pass` trong khối lệnh `if` có tác dụng gì?
- **A.** Thoát khỏi chương trình ngay lập tức.
- **B.** **[Đáp án đúng]** Giữ chỗ rỗng hợp lệ khi chưa muốn thực hiện lệnh nào, tránh bị báo lỗi cú pháp.
- **C.** In chữ "pass" ra màn hình.
- **D.** Đổi điều kiện thành `True`.
> *Giải thích:* `pass` là câu lệnh rỗng, dùng khi cú pháp đòi hỏi có khối lệnh nhưng logic chưa cần làm gì.

#### Câu 24 (Tư duy khi làm bài):
Khi so sánh tìm số lớn nhất giữa 3 số `a, b, c`, cách viết nào tối ưu và ít bị lỗi nhánh nhất?
- **A.** Liệt kê tất cả các cặp bằng nhiều câu lệnh `if a > b and a > c: ... elif b > a and b > c: ...`
- **B.** **[Đáp án đúng]** Dùng kỹ thuật Lính canh: Khởi tạo `max_val = a`, sau đó lần lượt so sánh với `b` và `c`.
- **C.** Sắp xếp cả 3 số vào danh sách rồi lấy phần tử cuối.
- **D.** Dùng phép chia để tìm thương số lớn hơn 1.
> *Giải thích:* Kỹ thuật Lính canh là mẫu thuật toán tối ưu, rõ ràng, an toàn nhất và dễ dàng mở rộng cho $N$ số.
