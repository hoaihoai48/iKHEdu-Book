# Bài 04: Cấu trúc rẽ nhánh

## 1. Bản chất của cấu trúc rẽ nhánh trong khoa học máy tính

Trong chương trình tuần tự, các dòng lệnh được máy tính thực thi từ trên xuống dưới một cách máy móc. Nhưng trong thực tế, máy tính cần biết **ra quyết định**: *nếu điều kiện đúng thì làm việc A, nếu sai thì làm việc B*.

Cấu trúc cho phép máy tính đổi hướng thực thi dựa trên điều kiện gọi là **cấu trúc rẽ nhánh**.

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

> **LỖI BẮT BUỘC PHẢI NHỚ: NHẦM LẪN GIỮA DẤU GÁN `=` VÀ DẤU SO SÁNH `==`**
>
> * Dấu `=` (Một dấu bằng): Là **phép gán giá trị** từ vế phải vào biến ở vế trái (`x = 10`).
> * Dấu `==` (Hai dấu bằng liền nhau): Là **phép so sánh bằng**, trả về `True` hoặc `False`.
> * Nếu viết `if a = 5:` $\implies$ Máy tính sẽ báo lỗi cú pháp ngay lập tức: `SyntaxError: invalid syntax`.

---

## 3. Quy tắc Thụt lề — Linh hồn của cú pháp Python

Trong nhiều ngôn ngữ khác, người ta dùng cặp ngoặc nhọn `{ }` hoặc cặp từ khóa `begin ... end` để gom các dòng lệnh thành một khối.

Python bỏ hết các cặp ngoặc rườm rà này và dùng **quy tắc Thụt lề**:
* Các dòng lệnh trong cùng một khối lệnh con **bắt buộc thụt vào trong cùng một khoảng cách** (chuẩn là **4 dấu cách / 1 phím Tab**).
* Hết khối lệnh con, dòng tiếp theo lùi ra bằng lề với câu lệnh cha.
* Dấu hai chấm `:` cuối dòng điều kiện là **bắt buộc**, báo cho Python biết sắp bắt đầu một khối lệnh thụt lề mới.

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
Chỉ làm một việc khi điều kiện đúng; nếu sai thì bỏ qua và đi tiếp.

```python
n = int(input())
if n < 0:
    n = -n  # Nếu n là số âm, đổi dấu thành số dương
print(n)
```

### 4.2. Dạng 2: Cấu trúc `if - else` (Đầy đủ)
Hai nhánh đối lập nhau: điều kiện `True` thì làm khối `if`, `False` thì làm khối `else`.

```python
n = int(input())
if n % 2 == 0:
    print("CHAN")
else:
    print("LE")
```

### 4.3. Dạng 3: Cấu trúc đa nhánh `if - elif - else`
Dùng khi có từ 3 lựa chọn trở lên. Từ khóa `elif` là viết tắt của *Else If (Nếu không thì xét tiếp)*:
* Python xét các điều kiện lần lượt từ trên xuống dưới.
* Gặp điều kiện đúng đầu tiên, Python chạy khối lệnh đó rồi **bỏ qua toàn bộ các nhánh `elif` và `else` còn lại**.

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

Khi một quyết định đòi hỏi kết hợp nhiều yếu tố, ta dùng các liên từ logic đã học ở Bài 02 để nối các biểu thức điều kiện:

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
* **Lời khuyên an toàn:** Luôn dùng ngoặc tròn `( )` để gom nhóm các điều kiện phức tạp, giúp đoạn lệnh trong sáng và không bị hiểu nhầm thứ tự ưu tiên (ví dụ: `if (a > 0 and b > 0) or c > 0:`).

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
Theo định lý Bất đẳng thức tam giác, 3 cạnh $a, b, c$ ($a, b, c > 0$) tạo thành một tam giác khi **tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại**:
$$\begin{cases} a + b > c \\ a + c > b \\ b + c > a \end{cases}$$

```python
a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    print("HOP LE")
else:
    print("KHONG HOP LE")
```

### 6.4. Bài toán kiểm tra Năm Nhuận
Một năm $Y$ là năm nhuận khi và chỉ khi:
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

## 8. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: QUÊN DẤU HAI CHẤM `:` Ở ĐẦU CÂU LỆNH**
> * Viết `if x > 0` $\implies$ Báo lỗi `SyntaxError: expected ':'`.

> **BẪY LỖI 2: THỤT LỀ KHÔNG ĐỒNG ĐỀU (`IndentationError`)**
> * Dòng trên thụt 4 dấu cách, dòng dưới thụt 2 dấu cách trong cùng một khối lệnh sẽ bị chương trình kiểm tra dừng ngay lập tức: `IndentationError: unindent does not match any outer indentation level`.

> **BẪY LỖI 3: DÙNG NHIỀU `if` ĐỘC LẬP THAY VÌ CHUỖI `elif`**
> * Hãy xem đoạn code sai lầm sau:
>  ```python
>   if diem >= 5.0:
>       print("DAT")
>   if diem >= 8.0:
>       print("XUAT SAC")
>   ```
>  Nếu học sinh được `9.0` điểm, chương trình sẽ in ra **CẢ HAI DÒNG**: `DAT` và `XUAT SAC`!
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
