# Bài 06: Vòng lặp while và biến cờ

## 1. Bản chất của vòng lặp `while` trong khoa học máy tính

Nếu như vòng lặp `for` là công cụ tối ưu khi ta **đã biết trước chính xác số lần lặp**, thì trong thực tế ta thường xuyên đối mặt với những tình huống **hoàn toàn chưa biết trước số lần lặp**:
* Người dùng chơi một trò chơi đến khi nào thua thì dừng lại.
* Nhập các số từ bàn phím liên tiếp đến khi nào gặp số 0 thì kết thúc.
* Rút tiền từ tài khoản cho đến khi số dư không còn đủ.
* Chia một số cho 10 liên tục cho đến khi số đó chỉ còn bằng 0.

Trong tất cả các bài toán trên, điều kiện dừng không phụ thuộc vào một chiếc thước đo cố định, mà phụ thuộc vào **một điều kiện logic**. Công cụ điều khiển chuẩn mực trong trường hợp này chính là **Vòng lặp `while` (Lặp khi điều kiện còn đúng)**.

![Chu trình vòng lặp while](../../assets/l06_while_loop.svg?v=1788575106)

---

## 2. Cấu trúc 3 thành phần bắt buộc của vòng lặp `while`

Mọi vòng lặp `while` chuẩn mực đều bắt buộc phải được xây dựng từ **3 bộ phận cốt tử**:

```python
# THÀNH PHẦN 1: Khởi tạo biến điều khiển trước vòng lặp
i = 1

# THÀNH PHẦN 2: Điều kiện duy trì vòng lặp (Kiểm tra ở đầu mỗi vòng)
while i <= 5:
    print(i)
    # THÀNH PHẦN 3: Cập nhật biến điều khiển bên trong thân vòng lặp
    i += 1
```

* **Cơ chế hoạt động:**
  1. Trước khi bước vào vòng lặp, máy tính kiểm tra điều kiện sau từ khóa `while`.
  2. Nếu điều kiện trả về `True`, toàn bộ thân lệnh bên trong được thực thi.
  3. Sau khi thực thi xong, máy tính **quay trở lại đầu câu lệnh `while`** để kiểm tra lại điều kiện.
  4. Nếu điều kiện vẫn `True`, vòng lặp tiếp tục. Ngay khi điều kiện chuyển sang `False`, vòng lặp lập tức kết thúc và chương trình nhảy xuống thực thi lệnh tiếp theo bên dưới.

---

## 3. Thảm họa Vòng lặp vô tận

> ❌ **TỬ HUYỆT LẬP TRÌNH LỚN NHẤT CỦA VÒNG LẶP WHILE:**
> Hãy quan sát đoạn mã sai lầm sau:
> ```python
> i = 1
> while i <= 5:
>     print(i)
>     # QUÊN LỆNH: i += 1 !
> ```
> * **Hiện tượng:** Biến `i` mãi mãi giữ giá trị bằng `1`. Điều kiện `1 <= 5` luôn luôn là `True` trong mọi thời điểm!
> * **Hậu quả:** Chương trình sẽ in ra số `1` liên tục hàng triệu lần, máy tính bị treo, quạt tản nhiệt quay ầm ầm. Khi nộp bài lên hệ thống thi đấu DKOJ/Themis, máy chấm sẽ dừng chương trình và đánh lỗi **Time Limit Exceeded (TLE) - Tràn giới hạn thời gian**.
> * **Quy tắc an toàn:** Mỗi khi viết lệnh `while`, điều đầu tiên cần tự hỏi bản thân là: *"Câu lệnh nào bên trong vòng lặp sẽ làm cho điều kiện này trở thành False để thoát ra?"*

---

## 4. Hai lệnh điều khiển luồng lặp mạnh mẽ: `break` và `continue`

Trong quá trình vòng lặp đang chạy, ta có thể chủ động can thiệp vào tiến trình bằng hai từ khóa đặc biệt:

### 4.1. Lệnh `break` (Bẻ gãy và Thoát vòng lặp ngay lập tức)
Khi gặp lệnh `break`, Python sẽ **ngay lập tức hủy bỏ vòng lặp hiện tại** và nhảy ra khỏi vòng lặp, bất chấp điều kiện lặp của `while` vẫn đang là `True`.

```python
# Tìm số đầu tiên chia hết cho 7 lớn hơn 50:
n = 51
while True:  # Vòng lặp vô tận có chủ đích
    if n % 7 == 0:
        print("So tim thay la:", n)
        break  # Đã tìm thấy, thoát vòng lặp ngay lập tức!
    n += 1
```
*Kết quả in ra:* `So tim thay la: 56`

### 4.2. Lệnh `continue` (Bỏ qua lượt lặp hiện tại)
Khi gặp lệnh `continue`, Python sẽ **bỏ qua tất cả các câu lệnh còn lại bên dưới** của vòng lặp hiện tại và nhảy ngay lên đầu để bắt đầu lượt lặp kế tiếp.

```python
# In các số từ 1 đến 5, trừ số 3:
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Bỏ qua số 3, không in
    print(i, end=" ")
```
*Kết quả in ra:* `1 2 4 5 `

---

## 5. Kỹ thuật Biến cờ và Lính canh

### 5.1. Kỹ thuật Biến cờ
Biến cờ là một biến thuộc kiểu logic `bool` (thường đặt tên là `found`, `co_hieu`, `da_tim_thay`), dùng để ghi nhận xem **một sự kiện đặc biệt đã xảy ra hay chưa**.

```python
# Kiểm tra xem số N có phải là số nguyên tố hay không bằng biến cờ:
n = int(input())
la_nguyen_to = True  # Cắm cờ ban đầu: Giả định n là số nguyên tố

if n < 2:
    la_nguyen_to = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            la_nguyen_to = False  # Hạ cờ: Đã tìm thấy ước số
            break
        i += 1

if la_nguyen_to:
    print("YES")
else:
    print("NO")
```

### 5.2. Kỹ thuật Lính canh dừng nhập
Bài toán: Đọc liên tiếp các số nguyên từ bàn phím cho đến khi gặp số 0 thì dừng lại, in ra tổng của các số vừa nhập.

```python
tong = 0
while True:
    x = int(input())
    if x == 0:  # Số 0 đóng vai trò lính canh báo hiệu kết thúc
        break
    tong += x

print(tong)
```

---

## 6. Bảng mô phỏng từng bước

Xét thuật toán tính tổng các chữ số của $N = 258$ bằng vòng lặp `while`:
```python
n = 258
tong = 0
while n > 0:
    chu_so = n % 10
    tong += chu_so
    n //= 10
```

### Bảng theo dõi biến thiên ô nhớ RAM qua từng vòng lặp:

| Vòng Lặp | Điều Kiện `n > 0` | Tách Chữ Số Cuối `chu_so = n % 10` | Tích Lũy `tong += chu_so` | Cắt Bỏ Chữ Số Cuối `n //= 10` |
|:---:|:---:|:---:|:---:|:---:|
| **Khởi tạo** | *(Bắt đầu)* | Chưa có | `tong = 0` | `n = 258` |
| **Vòng 1** | `258 > 0` (True) | `258 % 10 = 8` | `tong = 0 + 8 = 8` | `n = 258 // 10 = 25` |
| **Vòng 2** | `25 > 0` (True) | `25 % 10 = 5` | `tong = 8 + 5 = 13` | `n = 25 // 10 = 2` |
| **Vòng 3** | `2 > 0` (True) | `2 % 10 = 2` | `tong = 13 + 2 = 15` | `n = 2 // 10 = 0` |
| **Vòng 4** | `0 > 0` (**False!**) | *(Dừng lặp, thoát ra ngoài)* | Giữ nguyên `15` | Giữ nguyên `0` |

$$\implies \text{Tổng các chữ số thu được: } 8 + 5 + 2 = \mathbf{15}$$

---

## 7. Tử huyệt và Bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: ĐẶT SAI VỊ TRÍ CỦA LỆNH TĂNG BIẾN ĐIỀU KHIỂN KHI DÙNG CONTINUE**
> * Quan sát đoạn code bị treo vô tận:
>   ```python
>   i = 0
>   while i < 5:
>       if i == 3:
>           continue  # Nhảy lên đầu vòng lặp ngay!
>       i += 1        # Khi i == 3, dòng này KHÔNG BAO GIỜ được chạy tới!
>   ```
> * **Hậu quả:** Khi $i = 3$, lệnh `continue` nhảy ngay lên kiểm tra điều kiện, bỏ qua lệnh tăng `i += 1`. Biến $i$ mãi mãi bằng 3 $\implies$ Treo máy!
> * **Khắc phục:** Luôn cập nhật biến điều khiển `i += 1` trước câu lệnh `continue`.

> ❌ **BẪY LỖI 2: NHẦM LẪN GIỮA ĐIỀU KIỆN TIẾP TỤC VÀ ĐIỀU KIỆN DỪNG**
> * Trong tiếng Việt ta nói: *"Lặp cho đến khi $x > 10$ thì dừng"*.
> * Rất nhiều học sinh viết nhầm thành: `while x > 10:`.
> * **Bản chất của while:** Vòng lặp chạy khi điều kiện **ĐÚNG**. Muốn dừng khi $x > 10$, nghĩa là phải duy trì chạy khi $x \le 10$:
>   $$\mathbf{while \ x <= 10:}$$

---

## 8. Mẫu code chuẩn thi đấu

```python
# Mẫu đếm số chữ số của một số nguyên dương N
n = int(input())
dem = 0

while n > 0:
    dem += 1
    n //= 10

print(dem)
```

---

## 9. Concept Quiz: 20 câu trắc nghiệm kiểm tra sâu khái niệm

#### Câu 1 (Bản chất vòng lặp while):
Vòng lặp `while` trong Python sẽ tiếp tục thực thi phần thân lệnh khi nào?
- **A.** Khi điều kiện trả về `False`
- **B.** **[Đáp án đúng]** Khi điều kiện trả về `True`
- **C.** Khi điều kiện bằng 0
- **D.** Chạy đúng một số lần cố định
> *Giải thích:* Vòng lặp `while` duy trì lặp lại chừng nào điều kiện kiểm tra còn mang giá trị `True`.

#### Câu 2 (Nguyên nhân vòng lặp vô tận):
Đoạn mã nào sau đây chắc chắn sẽ rơi vào vòng lặp vô tận?
- **A.** `i = 1; while i <= 5: i += 1`
- **B.** **[Đáp án đúng]** `i = 1; while i <= 5: print(i)`
- **C.** `i = 5; while i > 0: i -= 1`
- **D.** `i = 10; while i < 5: i += 1`
> *Giải thích:* Đáp án B không có lệnh tăng `i`, do đó $i = 1$ mãi mãi thỏa mãn điều kiện $i \le 5$.

#### Câu 3 (Tác dụng của lệnh break):
Câu lệnh `break` khi được thực thi bên trong vòng lặp sẽ có tác dụng gì?
- **A.** Bỏ qua lượt lặp hiện tại và chuyển sang lượt kế tiếp
- **B.** **[Đáp án đúng]** Thoát ngay lập tức khỏi vòng lặp gần nhất chứa nó
- **C.** Tạm dừng chương trình 1 giây
- **D.** Khởi động lại vòng lặp từ đầu
> *Giải thích:* Lệnh `break` lập tức phá vỡ và chấm dứt vòng lặp.

#### Câu 4 (Tác dụng của lệnh continue):
Câu lệnh `continue` có chức năng gì?
- **A.** Thoát khỏi toàn bộ chương trình
- **B.** **[Đáp án đúng]** Bỏ qua các câu lệnh còn lại của vòng hiện tại và nhảy ngay sang lượt lặp kế tiếp
- **C.** Tiếp tục lặp vô tận
- **D.** In ra chữ "continue"
> *Giải thích:* `continue` kết thúc sớm vòng lặp hiện tại để chuyển sang lượt lặp mới.

#### Câu 5 (Dự đoán output — Đếm số bước lặp):
Đoạn code sau đây sẽ in ra bao nhiêu số?
```python
k = 1
while k < 8:
    print(k, end=" ")
    k += 2
```
- **A.** 3 số
- **B.** **[Đáp án đúng]** 4 số (`1 3 5 7`)
- **C.** 5 số
- **D.** Vô tận số
> *Giải thích:* Các giá trị của $k$ lần lượt là 1, 3, 5, 7. Khi $k = 9$ điều kiện $9 < 8$ sai nên dừng.

#### Câu 6 (Bẫy lặp không chạy):
Vòng lặp sau sẽ thực thi bao nhiêu lần?
```python
x = 10
while x < 5:
    print(x)
    x += 1
```
- **A.** 5 lần
- **B.** **[Đáp án đúng]** 0 lần
- **C.** 1 lần
- **D.** Báo lỗi cú pháp
> *Giải thích:* Ngay từ đầu $x = 10$, điều kiện $10 < 5$ đã là `False` nên khối lệnh bên trong không được chạy lần nào.

#### Câu 7 (Ứng dụng đếm số chữ số):
Để đếm xem số nguyên $N = 3456$ có bao nhiêu chữ số, ta chia nguyên liên tiếp cho 10:
```python
dem = 0
while n > 0:
    dem += 1
    n //= 10
```
Sau khi vòng lặp kết thúc, `dem` bằng:
- **A.** 3
- **B.** **[Đáp án đúng]** 4
- **C.** 5
- **D.** 6
> *Giải thích:* Số 3456 có 4 chữ số, cần 4 lần chia nguyên cho 10 để $n$ giảm về 0.

#### Câu 8 (Kỹ thuật cờ hiệu Boolean):
Một biến được dùng để ghi nhận trạng thái tìm kiếm (ví dụ `da_tim_thay = False`) được gọi là:
- **A.** Biến tích lũy
- **B.** **[Đáp án đúng]** Biến cờ
- **C.** Biến lặp
- **D.** Biến hằng
> *Giải thích:* Biến mang giá trị `True/False` đánh dấu trạng thái được gọi là Biến cờ.

#### Câu 9 (Bẫy điều kiện phủ định):
Để vòng lặp dừng lại khi biến `tuoi` lớn hơn 18, điều kiện duy trì sau từ khóa `while` phải là:
- **A.** `tuoi > 18`
- **B.** **[Đáp án đúng]** `tuoi <= 18`
- **C.** `tuoi == 18`
- **D.** `tuoi < 18`
> *Giải thích:* Muốn dừng khi $> 18$ thì phải tiếp tục lặp khi $\le 18$.

#### Câu 10 (Dự đoán output — Lệnh break):
Đoạn code sau in ra gì?
```python
i = 1
while i <= 10:
    if i == 4:
        break
    print(i, end=" ")
    i += 1
```
- **A.** `1 2 3 4`
- **B.** **[Đáp án đúng]** `1 2 3 `
- **C.** `1 2 3 4 5`
- **D.** `4`
> *Giải thích:* Khi $i = 4$, lệnh `break` thoát ngay lập tức trước khi lệnh `print(4)` được gọi.

#### Câu 11 (Bẫy toán tử chia nguyên n //= 2):
Nếu $N = 16$, cần bao nhiêu lần thực hiện lệnh `N //= 2` để $N$ giảm về $1$?
- **A.** 3 lần
- **B.** **[Đáp án đúng]** 4 lần ($16 \to 8 \to 4 \to 2 \to 1$)
- **C.** 5 lần
- **D.** 2 lần
> *Giải thích:* $16 = 2^4$, do đó cần đúng 4 lần chia đôi để về 1.

#### Câu 12 (Dự đoán output — Vòng lặp lồng while):
Đoạn code sau in ra kết quả gì?
```python
a = 1
while a <= 2:
    b = 1
    while b <= 2:
        print(a * b, end=" ")
        b += 1
    a += 1
```
- **A.** `1 2 2 4 `
- **B.** **[Đáp án đúng]** `1 2 2 4 `
- **C.** `1 2 3 4 `
- **D.** `2 4 `
> *Giải thích:* Với $a=1: b=1 \to 1, b=2 \to 2$. Với $a=2: b=1 \to 2, b=2 \to 4$.

#### Câu 13 (Nhập dữ liệu với lính canh 0):
Đoạn code sau dừng lại khi nào?
```python
while True:
    x = int(input())
    if x == 0:
        break
```
- **A.** Khi nhập vào số âm
- **B.** **[Đáp án đúng]** Khi người dùng nhập vào số 0
- **C.** Sau đúng 10 lần nhập
- **D.** Khi gặp số nguyên lớn
> *Giải thích:* Số 0 kích hoạt lệnh `break` thoát khỏi vòng lặp vô tận.

#### Câu 14 (Dự đoán output — Cập nhật biến):
Giá trị của `x` sau đoạn code sau:
```python
x = 100
while x > 10:
    x //= 3
```
- **A.** `11`
- **B.** **[Đáp án đúng]** `3`
- **C.** `1`
- **D.** `33`
> *Giải thích:* $100 \to 33 \to 11 \to 3$. Khi $x = 3 \ngtr 10$ nên vòng lặp dừng lại.

#### Câu 15 (So sánh giữa for và while):
Khi nào ta **BẮT BUỘC** hoặc nên ưu tiên sử dụng vòng lặp `while` thay vì `for`?
- **A.** Khi muốn duyệt qua một danh sách
- **B.** **[Đáp án đúng]** Khi chưa biết trước số lần lặp và phụ thuộc vào điều kiện dừng
- **C.** Khi muốn tính tổng từ 1 đến 10
- **D.** Khi chỉ muốn chạy đúng 5 lần
> *Giải thích:* `while` sinh ra chuyên biệt cho các tình huống lặp không xác định trước số lần.

#### Câu 16 (Bẫy điều kiện logic kép trong while):
Vòng lặp `while a > 0 and b > 0:` sẽ dừng lại khi nào?
- **A.** Khi cả `a` và `b` đều $\le 0$
- **B.** **[Đáp án đúng]** Khi **chỉ cần ít nhất một trong hai biến** $a \le 0$ hoặc $b \le 0$
- **C.** Khi `a == b`
- **D.** Không bao giờ dừng
> *Giải thích:* Điều kiện duy trì là cả hai cùng dương. Chỉ cần 1 bên không còn dương là điều kiện `and` sai $\implies$ dừng lặp.

#### Câu 17 (Bẫy thứ tự lệnh bên trong thân lặp):
Đoạn code sau:
```python
i = 1
while i <= 3:
    i += 1
    print(i, end=" ")
```
sẽ in ra:
- **A.** `1 2 3 `
- **B.** **[Đáp án đúng]** `2 3 4 `
- **C.** `1 2 3 4 `
- **D.** `2 3 `
> *Giải thích:* Lệnh `i += 1` được thực hiện trước lệnh `print(i)`, do đó in từ 2 đến 4.

#### Câu 18 (Tìm ước chung lớn nhất Euclid):
Thuật toán Euclid tìm $\gcd(A, B)$ dùng vòng lặp `while` dựa trên nguyên lý:
```python
while b != 0:
    r = a % b
    a = b
    b = r
```
Sau khi vòng lặp dừng, ước chung lớn nhất nằm ở biến:
- **A.** **[Đáp án đúng]** `a`
- **B.** `b`
- **C.** `r`
- **D.** `a + b`
> *Giải thích:* Khi $b = 0$, số chia cuối cùng được gán vào `a`, do đó $\gcd(A, B) = a$.

#### Câu 19 (Tách từng chữ số theo thứ tự từ phải sang trái):
Khi dùng `while n > 0:` kết hợp `chu_so = n % 10` và `n //= 10`, các chữ số của $N$ được tách ra theo thứ tự nào?
- **A.** Từ trái sang phải (hàng lớn nhất trước)
- **B.** **[Đáp án đúng]** Từ phải sang trái (hàng đơn vị trước)
- **C.** Ngẫu nhiên
- **D.** Tăng dần theo giá trị
> *Giải thích:* Phép chia dư `% 10` luôn bóc tách chữ số hàng đơn vị trước tiên.

#### Câu 20 (Quy tắc phòng thi lập trình):
Khi một bài toán có thể giải bằng cả công thức toán $\mathcal{O}(1)$ và vòng lặp `while`, thí sinh nên chọn cách nào?
- **A.** Dùng vòng lặp `while` vì dễ viết hơn
- **B.** **[Đáp án đúng]** Áp dụng công thức toán $\mathcal{O}(1)$ để đạt tốc độ chạy tức thì và tránh nguy cơ lặp vô tận
- **C.** Dùng cả hai cách trong cùng một file nộp
- **D.** Dùng phép đệ quy
> *Giải thích:* Công thức toán $\mathcal{O}(1)$ là tối ưu tuyệt đối, không tiêu tốn tài nguyên thời gian và an toàn 100%.
