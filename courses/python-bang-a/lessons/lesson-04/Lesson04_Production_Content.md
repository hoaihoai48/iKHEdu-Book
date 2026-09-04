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
