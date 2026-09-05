## I. Tử huyệt và lỗi thường gặp

### 1.1. Toán tử lũy thừa: `**` không phải `^`

#### Bản chất kỹ thuật
Trong toán học, ta quen tay viết $2^3$ hoặc gõ `2 ^ 3` để biểu diễn $2^3$. Tuy nhiên trong Python:
* Ký hiệu `^` là **phép toán logic trên bit (Bitwise XOR)**.
* Lệnh `print(2 ^ 3)` sẽ in ra số `1` (do $0010_2 \oplus 0011_2 = 0001_2$).
* Rất nhiều học sinh gõ `a ^ 2` để tính $a^2$ và nhận kết quả sai hoàn toàn mà không hiểu vì sao!

#### Quy tắc vàng
Muốn tính lũy thừa $A^B$, **bắt buộc dùng hai dấu sao liền nhau: `**`**.

```python
# SAI:
dien_tich = a ^ 2     # Nhận kết quả XOR bitwise, sai bản chất

# ĐÚNG:
dien_tich = a ** 2    # Lũy thừa bậc hai chính xác
the_tich = a ** 3     # Lũy thừa bậc ba chính xác
```

---

### 1.2. Phép chia: Phân biệt `/` và `//`

* **Phép chia thực `/`:** Luôn luôn trả về kiểu số thực (`float`), kể cả khi chia hết.
  - Ví dụ: `10 / 2` cho kết quả `5.0`. Nếu in ra khi đề bài yêu cầu số nguyên, máy chấm sẽ báo lỗi kết quả sai (Wrong Answer).
* **Phép chia lấy phần nguyên `//`:** Lấy số nguyên lớn nhất không vượt quá thương số.
  - Ví dụ: `10 // 2 = 5`, `17 // 5 = 3`.
* **Phép chia lấy phần dư `%`:** Lấy phần còn dư sau phép chia nguyên.
  - Ví dụ: `17 % 5 = 2`.
  - Định lý bất biến: $A = (A // B) \times B + (A \% B)$ với $0 \le A \% B < B$.

---

### 1.3. Hàm `range(start, stop, step)`: Cận trên bị loại trừ

Hàm `range()` trong vòng lặp `for` **luôn luôn loại trừ cận trên (`stop`)**:
* `range(1, 10)` chỉ chạy các số từ $1$ đến $9$ (dừng trước $10$).
* Muốn duyệt đủ từ $1$ đến $N$, bắt buộc viết: `range(1, n + 1)`.

---

### 1.4. Lệnh `input()`: Luôn trả về chuỗi ký tự

* Lệnh `input()` luôn trả về kiểu chuỗi ký tự (`str`).
* Nếu không chuyển đổi kiểu dữ liệu, phép cộng `"5" + "3"` sẽ cho ra `"53"`, không phải `8`.
* **Cú pháp chuẩn:**
  - Đọc một số nguyên: `n = int(input())`
  - Đọc hai số nguyên trên cùng một dòng: `a, b = map(int, input().split())`
  - Đọc danh sách số nguyên trên một dòng: `arr = list(map(int, input().split()))`

---

## II. Công thức và bảng tra cứu

### 2.1. Tháp thứ tự ưu tiên toán tử trong biểu thức

Khi tính toán biểu thức phức tạp, máy tính tuân theo thứ tự từ trên xuống dưới:
1. **Cặp ngoặc tròn `( )`:** Được tính toán trước tiên.
2. **Phép lũy thừa `**`:** Tính kết hợp từ phải qua trái (`2 ** 3 ** 2 = 2 ** 9 = 512`).
3. **Nhóm nhân, chia, chia nguyên, chia dư `*`, `/`, `//`, `%`:** Tính từ trái qua phải.
4. **Nhóm cộng, trừ `+`, `-`:** Tính từ trái qua phải.

> 💡 **Quy tắc phân số đại số:** Khi chuyển phân số $\frac{a + b}{c + d}$ sang Python, **bắt buộc bọc ngoặc tròn** cả tử và mẫu: `(a + b) / (c + d)`.

---

### 2.2. Công thức hình học cơ bản trong lập trình

Trước khi áp dụng công thức, **tất cả các kích thước bắt buộc phải cùng đơn vị đo**.

| Hình học | Chu vi ($P$) | Diện tích ($S$) | Mã lệnh Python |
|---|---|---|---|
| **Hình vuông** (cạnh $a$) | $P = 4a$ | $S = a^2$ | `p = 4 * a`<br>`s = a ** 2` |
| **Hình chữ nhật** (dài $a$, rộng $b$) | $P = 2(a + b)$ | $S = a \times b$ | `p = (a + b) * 2`<br>`s = a * b` |
| **Tam giác** (đáy $a$, cao $h$) | $P = a + b + c$ | $S = \frac{a \times h}{2}$ | `p = a + b + c`<br>`s = (a * h) / 2` |
| **Hình thang** (đáy $a, b$, cao $h$) | — | $S = \frac{(a + b) \times h}{2}$ | `s = ((a + b) * h) / 2` |

---

### 2.3. Bảng đổi đơn vị và thuật toán tách thời gian

#### 2.3.1. Bảng quy đổi chiều dài và khối lượng
* **Chiều dài:** $1\text{m} = 100\text{cm} = 1000\text{mm}$; $1\text{km} = 1000\text{m}$.
* **Khối lượng:** $1\text{tấn} = 10\text{tạ} = 1000\text{kg}$; $1\text{kg} = 1000\text{g}$.

#### 2.3.2. Thuật toán đổi tổng số giây $T$ ra Giờ - Phút - Giây
* $1\text{ giờ} = 3600\text{ giây}$, $1\text{ phút} = 60\text{ giây}$.
```python
T = int(input())
gio = T // 3600
phut = (T % 3600) // 60
giay = T % 60
print(f"{gio} gio {phut} phut {giay} giay")
```

#### 2.3.3. Định dạng số thực 2 chữ số thập phân
* **Dùng f-string:** `print(f"{x:.2f}")` (tự động làm tròn và bù đủ 2 chữ số thập phân chuẩn thi đấu).
