# Bài 06: Vòng lặp while và biến cờ

## 1. Bản chất của vòng lặp `while` trong khoa học máy tính

Vòng lặp `for` rất hợp khi các em **đã biết trước chính xác số lần lặp**. Nhưng thực tế có nhiều việc **chưa biết trước số lần lặp**:
* Chơi một trò chơi đến khi nào thua thì dừng lại.
* Nhập các số liên tiếp đến khi nào gặp số 0 thì kết thúc.
* Rút tiền cho đến khi số dư không còn đủ.
* Chia một số cho 10 liên tục cho đến khi số đó chỉ còn bằng 0.

Ở các việc trên, khi nào dừng không do một con số cố định quyết định, mà do **một điều kiện** quyết định. Công cụ chuẩn cho trường hợp này là **vòng lặp `while` (lặp khi điều kiện còn đúng)**.

![Chu trình vòng lặp while](../../assets/l06_while_loop.svg?v=1788575106)

---

## 2. Cấu trúc 3 thành phần bắt buộc của vòng lặp `while`

Mọi vòng lặp `while` chuẩn đều gồm **3 bộ phận**:

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
 1. Trước khi vào vòng lặp, máy kiểm tra điều kiện sau từ khóa `while`.
 2. Nếu điều kiện là `True`, toàn bộ thân lệnh bên trong được chạy.
 3. Chạy xong, máy **quay lại đầu câu lệnh `while`** để kiểm tra lại điều kiện.
 4. Điều kiện còn `True` thì lặp tiếp. Điều kiện thành `False` thì dừng và chạy lệnh tiếp theo bên dưới.

---

## 3. Thảm họa Vòng lặp vô tận

> **LỖI NGUY HIỂM NHẤT CỦA VÒNG LẶP WHILE:**
> Hãy quan sát đoạn mã sai lầm sau:
> ```python
> i = 1
> while i <= 5:
>     print(i)
>     # QUÊN LỆNH: i += 1 !
> ```
> * **Hiện tượng:** Biến `i` mãi giữ giá trị bằng `1`. Điều kiện `1 <= 5` luôn là `True`!
> * **Hậu quả:** Chương trình in số `1` liên tục không bao giờ dừng, máy tính bị treo.
> * **Quy tắc an toàn:** Mỗi khi viết lệnh `while`, điều đầu tiên cần tự hỏi là: *"Câu lệnh nào bên trong vòng lặp sẽ làm cho điều kiện này trở thành False để thoát ra?"*

---

## 4. Hai lệnh điều khiển luồng lặp mạnh mẽ: `break` và `continue`

Khi vòng lặp đang chạy, các em có thể can thiệp bằng hai từ khóa đặc biệt:

### 4.1. Lệnh `break` (Bẻ gãy và Thoát vòng lặp ngay lập tức)
Gặp lệnh `break`, Python **hủy ngay vòng lặp hiện tại** và nhảy ra ngoài, dù điều kiện của `while` vẫn đang là `True`.

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
Gặp lệnh `continue`, Python **bỏ qua mọi câu lệnh còn lại bên dưới** của vòng hiện tại và nhảy ngay lên đầu để bắt đầu lượt tiếp theo.

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
Biến cờ là biến kiểu `bool` (thường đặt tên là `found`, `co_hieu`, `da_tim_thay`), dùng để ghi nhận xem **một việc đặc biệt đã xảy ra hay chưa**.

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
Bài toán: Đọc liên tiếp các số nguyên cho đến khi gặp số 0 thì dừng, in ra tổng các số vừa nhập.

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

## 7. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: ĐẶT SAI VỊ TRÍ CỦA LỆNH TĂNG BIẾN ĐIỀU KHIỂN KHI DÙNG CONTINUE**
> * Quan sát đoạn code bị treo vô tận:
>  ```python
>   i = 0
>   while i < 5:
>       if i == 3:
>           continue  # Nhảy lên đầu vòng lặp ngay!
>       i += 1        # Khi i == 3, dòng này KHÔNG BAO GIỜ được chạy tới!
>   ```
> * **Hậu quả:** Khi $i = 3$, lệnh `continue` nhảy ngay lên kiểm tra điều kiện, bỏ qua lệnh tăng `i += 1`. Biến $i$ mãi bằng 3 $\implies$ Treo máy!
> * **Khắc phục:** Luôn cập nhật biến điều khiển `i += 1` trước câu lệnh `continue`.

> **BẪY LỖI 2: NHẦM LẪN GIỮA ĐIỀU KIỆN TIẾP TỤC VÀ ĐIỀU KIỆN DỪNG**
> * Trong tiếng Việt ta nói: *"Lặp cho đến khi $x > 10$ thì dừng"*.
> * Rất nhiều bạn viết nhầm thành: `while x > 10:`.
> * **Bản chất của while:** Vòng lặp chạy khi điều kiện **ĐÚNG**. Muốn dừng khi $x > 10$, nghĩa là phải chạy khi $x \le 10$:
>  $$\mathbf{while \ x <= 10:}$$

---

## 8. Mẫu code thường gặp

```python
# Mẫu đếm số chữ số của một số nguyên dương N
n = int(input())
dem = 0

while n > 0:
    dem += 1
    n //= 10

print(dem)
```
