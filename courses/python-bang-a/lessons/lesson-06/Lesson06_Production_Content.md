# Bài 06: Điều kiện ghép với and-or-not

---

## 1. Khởi động: Khi một điều kiện là chưa đủ!

Trong cuộc sống, có những việc chỉ xảy ra khi **thỏa mãn đồng thời nhiều điều kiện**:
* Để được đi tàu lượn siêu tốc: Em phải **trên 10 tuổi VÀ cao trên 130cm**.
* Em được nghỉ học vào **Thứ Bảy HOẶC Chủ Nhật**.
* Muốn tạo thành một hình tam giác hợp lệ: **Tổng hai cạnh bất kỳ phải luôn LỚN HƠN cạnh còn lại**.
* Một năm là **Năm nhuận** nếu: Năm đó chia hết cho 400, **HOẶC** chia hết cho 4 nhưng **KHÔNG ĐƯỢC** chia hết cho 100.

Để kết hợp nhiều điều kiện logic phức tạp lại với nhau trong một dòng lệnh duy nhất, Python cung cấp **bộ ba liên minh quyền năng: `and`, `or` và `not`**!

---

## 2. Bảng chân lý của 3 hiệp sĩ logic: `and`, `or`, `not`

Python dùng chính các từ tiếng Anh thông dụng để viết logic, cực kỳ dễ nhớ đối với học sinh:

### 2.1. Boolean expression tạo ra `True` hoặc `False`

Một phép so sánh như `a > b` không chỉ là một câu hỏi; nó là một **biểu thức Boolean** có kết quả là `True` hoặc `False`. Lệnh `if` dùng kết quả đó để chọn nhánh chạy. Các toán tử `and`, `or`, `not` ghép hoặc đảo những kết quả Boolean này.

```python
a = 8
b = 5
kiem_tra = a > b
print(kiem_tra)  # True
```

| Toán tử logic | Tên gọi tiếng Việt | Quy tắc hoạt động bản chất | Ví dụ kiểm tra | Kết quả |
|:---:|:---:|---|---|:---:|
| **`and`** | **VÀ** <br> *(Đồng thời)* | **Bắt buộc TẤT CẢ phải ĐÚNG** thì mới ĐÚNG. Chỉ cần có 1 điều kiện SAI là toàn bộ SAI ngay. | `(5 > 3) and (2 < 4)` <br> `(5 > 3) and (2 > 4)` | `True` <br> `False` |
| **`or`** | **HOẶC** <br> *(Lựa chọn)* | **Chỉ cần ÍT NHẤT 1 điều kiện ĐÚNG** là ĐÚNG. Chỉ SAI khi tất cả đều SAI. | `(5 > 3) or (2 > 4)` <br> `(5 < 3) or (2 > 4)` | `True` <br> `False` |
| **`not`** | **KHÔNG** <br> *(Phủ định)* | **Đảo ngược sự thật**: Biến ĐÚNG thành SAI, biến SAI thành ĐÚNG. | `not (5 > 3)` <br> `not (5 < 3)` | `False` <br> `True` |

---

## 3. Hai bài toán "vàng" kinh điển trong các đề thi Tin học trẻ

### 3.1. Bài toán 1: Kiểm tra tam giác hợp lệ (định lý bất đẳng thức tam giác)
Cho 3 số dương $a, b, c$. Ba số này có thể tạo thành 3 cạnh của một hình tam giác hay không?
* **Định lý toán học:** Trong một tam giác, tổng độ dài hai cạnh bất kỳ bao giờ cũng lớn hơn độ dài cạnh còn lại.
* **Cần thỏa mãn đồng thời 3 điều kiện:**
  1. $a + b > c$
  2. $a + c > b$
  3. $b + c > a$

```python
a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    print("TAM GIAC HOP LE")
else:
    print("KHONG PHAI TAM GIAC")
```

### 3.2. Bài toán 2: Quy luật năm nhuận (leap year)
Năm nhuận là năm có 366 ngày (tháng 2 có 29 ngày). Làm sao để máy tính biết năm $Y$ có phải năm nhuận không?
* **Quy tắc Thiên văn học:**
  * Năm chia hết cho 400 $\implies$ Chắc chắn là năm nhuận! (Ví dụ: năm 2000, 2400).
  * Năm chia hết cho 4 nhưng **không chia hết cho 100** $\implies$ Là năm nhuận! (Ví dụ: năm 2024, 2028).
  * Các năm còn lại $\implies$ Không phải năm nhuận.

```python
nam = int(input())

if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print("NAM NHUAN")
else:
    print("NAM THUONG")
```

---

## 4. Cú pháp so sánh chuỗi kẹp (chained comparison) — đặc quyền chỉ có ở Python!

Trong các ngôn ngữ khác như C++ hay Pascal, khi muốn kiểm tra xem $x$ có nằm trong đoạn từ 1 đến 10 hay không, em phải viết: `(x >= 1) and (x <= 10)`.
Nhưng trong Python, em được phép viết y hệt như trong sách giáo khoa Toán:
```python
if 1 <= x <= 10:
    print("x nam trong khoang tu 1 den 10")
```
Cú pháp này cực kỳ trực quan và tự nhiên cho các bạn học sinh Tiểu học!

---

## 5. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Biểu thức `(True and False)` cho kết quả là gì?
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `None`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Phép `and` đòi hỏi cả 2 vế phải cùng là `True`. Có 1 vế `False` thì kết quả là `False`.

#### Câu 2: Biểu thức `(True or False)` cho kết quả là gì?
- **A.** **[Đáp án đúng]** `True`
- **B.** `False`
- **C.** `None`
- **D.** Báo lỗi
> *Giải thích:* Phép `or` chỉ cần ít nhất 1 vế là `True` thì kết quả sẽ là `True`.

#### Câu 3: Kết quả của biểu thức `not (10 > 5)` là:
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `10 < 5`
- **D.** `None`
> *Giải thích:* $10 > 5$ là `True`. Phép `not True` đảo ngược lại thành `False`.

#### Câu 4: Cú pháp nào sau đây kiểm tra số $x$ là số chẵn và lớn hơn 10?
- **A.** `x % 2 == 0 or x > 10`
- **B.** **[Đáp án đúng]** `x % 2 == 0 and x > 10`
- **C.** `x % 2 == 0 not x > 10`
- **D.** `x % 2 == 0 & x > 10`
> *Giải thích:* Từ khóa `and` dùng để kết hợp hai điều kiện cần xảy ra đồng thời.

#### Câu 5: Năm nào sau đây là năm nhuận?
- **A.** 1900
- **B.** 2021
- **C.** 2023
- **D.** **[Đáp án đúng]** 2024
> *Giải thích:* 2024 chia hết cho 4 và không chia hết cho 100 nên là năm nhuận. Năm 1900 chia hết cho 100 nhưng không chia hết cho 400 nên không phải năm nhuận.

#### Câu 6: Điều kiện tồn tại tam giác với 3 cạnh $a, b, c$ là:
- **A.** `a + b + c > 0`
- **B.** `a + b > c or a + c > b or b + c > a`
- **C.** **[Đáp án đúng]** `a + b > c and a + c > b and b + c > a`
- **D.** `a * a + b * b == c * c`
> *Giải thích:* Bắt buộc cả 3 bất đẳng thức phải cùng thỏa mãn (`and`).

#### Câu 7: Đoạn code sau in ra gì?
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

#### Câu 8: Đoạn code sau in ra gì?
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

#### Câu 9: Thứ tự ưu tiên giữa các toán tử logic trong Python là:
- **A.** `or` trước, `and` sau, `not` cuối
- **B.** **[Đáp án đúng]** `not` ưu tiên cao nhất, sau đó đến `and`, cuối cùng là `or`
- **C.** Từ trái sang phải, cái nào đứng trước làm trước
- **D.** `and` và `or` ngang hàng nhau
> *Giải thích:* Quy tắc chuẩn: `not` > `and` > `or`. (Tuy nhiên nên dùng ngoặc `( ... )` để code rõ ràng nhất).

#### Câu 10: Biểu thức `not False and True` tương đương với:
- **A.** `not (False and True)`
- **B.** **[Đáp án đúng]** `(not False) and True` $\implies$ `True and True` = `True`
- **C.** `False`
- **D.** Báo lỗi
> *Giải thích:* `not` có ưu tiên cao hơn `and`, nên `not False` được tính trước thành `True`, sau đó `True and True` ra `True`.

#### Câu 11: Làm sao để kiểm tra tháng $M$ có 31 ngày?
- **A.** `M in (1, 3, 5, 7, 8, 10, 12)`
- **B.** `M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12`
- **C.** **[Đáp án đúng]** Cả A và B đều đúng
- **D.** `M % 2 != 0`
> *Giải thích:* Cả hai cách viết đều đúng logic các tháng có 31 ngày trong năm.

#### Câu 12: Biểu thức nào kiểm tra một điểm tọa độ $(x, y)$ nằm ở góc phần tư thứ nhất (cả $x$ và $y$ đều dương)?
- **A.** `x > 0 or y > 0`
- **B.** **[Đáp án đúng]** `x > 0 and y > 0`
- **C.** `x * y > 0`
- **D.** `x + y > 0`
> *Giải thích:* Góc phần tư thứ nhất yêu cầu cả hoành độ và tung độ đều phải dương.

#### Câu 13: Bẫy lỗi: Đoạn code `if a == 1 or 2:` có ý nghĩa là gì?
- **A.** Kiểm tra xem `a` có bằng 1 hoặc bằng 2 không
- **B.** **[Đáp án đúng]** Luôn luôn đúng (`True`) vì số 2 khác 0 được Python coi là `True`!
- **C.** Báo lỗi cú pháp
- **D.** Kiểm tra `a == 3`
> *Giải thích:* Đây là bẫy lỗi kinh điển! Phải viết đầy đủ: `if a == 1 or a == 2:`. Nếu viết `or 2`, Python sẽ xét giá trị độc lập của số 2, mà số khác 0 luôn là `True`, dẫn đến câu `if` luôn chạy!

#### Câu 14: Đoạn code sau in ra gì?
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

#### Câu 15: Kiểm tra số tự nhiên $N$ có đúng 2 chữ số:
- **A.** `N >= 10 and N <= 99`
- **B.** `10 <= N <= 99`
- **C.** **[Đáp án đúng]** Cả A và B đều hoàn toàn chính xác
- **D.** `N // 10 > 0`
> *Giải thích:* Cả hai cách viết đều giới hạn chính xác các số nguyên từ 10 đến 99.
