# iKHEDU PYTHON — NỘI DUNG BÀI HỌC (LEVEL 1)

> Tài liệu nội dung bài học dành cho học sinh Phổ thông ôn luyện kỳ thi Python.
> Cấu trúc chuẩn hóa: Kiến thức trọng tâm, Bảng công thức ghi nhớ, Bẫy lỗi phòng thi, Code mẫu chuẩn và Hệ thống bài tập phân tầng.

---

## MỤC LỤC CHƯƠNG TRÌNH

### Chương 1: TÍNH TOÁN CƠ BẢN
- **Bài 01:** Lệnh xuất nhập và biến số
- **Bài 02:** Phép toán số học, chia nguyên và chia dư *(Chuyên sâu & Bài tập thực chiến)*
- **Bài 03:** Công thức tính toán, hình học và đổi đơn vị *(Chuyên sâu & Bài tập thực chiến)*

### Chương 2: TƯ DUY RẼ NHÁNH & ĐIỀU KIỆN LOGIC
- **Bài 04:** Cấu trúc rẽ nhánh `if - elif - else` và Điều kiện ghép `and - or - not`

### Chương 3: VÒNG LẶP
- **Bài 05:** Vòng lặp `for` và hàm `range`
- **Bài 06:** Vòng lặp `while` và kỹ thuật điều khiển luồng (`break`, `continue`, cờ hiệu)

### Chương 4: BÀI TOÁN SỐ HỌC
- **Bài 07:** Quy luật dãy số và tam giác số
- **Bài 08:** Tách chữ số với chia nguyên và chia dư
- **Bài 09:** Ước số, bội số và số nguyên tố
- **Bài 10:** Đếm số theo quy luật và số đặc biệt

### Chương 5: DANH SÁCH (LIST), XỬ LÝ CHUỖI & LUYỆN THI
- **Bài 11:** Danh sách và thao tác cơ bản
- **Bài 12:** Thống kê danh sách và sắp xếp
- **Bài 13:** Chỉ số và cắt lát chuỗi (Indexing & Slicing)
- **Bài 14:** Duyệt chuỗi, biến đổi ký tự và xử lý từ
- **Bài 15:** Chiến lược làm bài, phân tích test biên & tối ưu thời gian

---

# PHẦN I: THẺ NHỚ THUẬT TOÁN DÙNG XUYÊN SUỐT (ALGORITHM PATTERNS)

| STT | Mẫu thuật toán | Mục đích & Ứng dụng | Cấu trúc code mẫu chuẩn |
|:---:|---|---|---|
| **1** | **Input → Process → Output** | Đọc dữ liệu, tính theo công thức, in kết quả | `n = int(input())`<br>`ans = n * 2`<br>`print(ans)` |
| **2** | **Counting (Đếm)** | Đếm số lượng phần tử thỏa mãn điều kiện | `cnt = 0`<br>`for x in day:`<br>`    if dieu_kien(x): cnt += 1` |
| **3** | **Accumulator (Tổng dồn)** | Tích lũy tổng từ đầu đến cuối dãy | `tong = 0`<br>`for x in day:`<br>`    tong += x` |
| **4** | **Max / Min (Cực trị)** | Tìm phần tử lớn nhất hoặc nhỏ nhất | `max_val = day[0]`<br>`for x in day[1:]:`<br>`    if x > max_val: max_val = x` |
| **5** | **Flag (Cờ hiệu)** | Đánh dấu sự kiện đã xảy ra để dừng sớm | `found = False`<br>`for x in day:`<br>`    if dieu_kien(x): found = True; break` |
| **6** | **Digit Extraction** | Bóc tách từng chữ số của một số tự nhiên | `while n > 0:`<br>`    cs = n % 10`<br>`    n //= 10` |
| **7** | **Rolling Variables** | Biến cuốn chiếu lưu trạng thái trước (Fibonacci) | `a, b = b, a + b` |
| **8** | **List Traversal** | Duyệt giá trị hoặc cập nhật qua chỉ số mảng | `for x in a:` hoặc `for i in range(len(a)): a[i] = f(a[i])` |
| **9** | **String Slicing** | Trích xuất hoặc đảo ngược chuỗi | `s[start:stop]`, `s[::-1]` |
| **10**| **Formula $\mathcal{O}(1)$** | Tính toán trực tiếp không dùng vòng lặp | `(B // K) - ((A - 1) // K)`, `N * (N + 1) // 2` |

---

# PHẦN II: NỘI DUNG CHI TIẾT 5 CHƯƠNG BÀI HỌC

---

# CHƯƠNG 1: TÍNH TOÁN CƠ BẢN

---

## BÀI 01: LỆNH XUẤT NHẬP VÀ BIẾN SỐ

### 1. Tóm tắt kiến thức trọng tâm
- **Lệnh in ra màn hình `print()`:**
  - In chữ / văn bản: Đặt trong nháy kép `"` hoặc nháy đơn `'` (Ví dụ: `print("Xin chao")`).
  - In số hoặc biểu thức tính: Không dùng nháy (Ví dụ: `print(2026)` hoặc `print(10 + 5)`).
  - In nhiều món đồ trên 1 dòng: Ngăn cách bởi dấu phẩy `,`. Python tự chèn 1 khoảng trắng ở giữa.
- **Biến số (Variable):**
  - Biến số là ô nhớ lưu dữ liệu: `ten_bien = gia_tri`. Dấu `=` là phép gán.
  - Quy tắc đặt tên biến: Chỉ dùng chữ cái tiếng Anh (`a-z`, `A-Z`), chữ số (`0-9`) và dấu gạch dưới `_`. Không bắt đầu bằng chữ số, không chứa dấu cách, không trùng từ khóa Python.
- **Lệnh nhập dữ liệu `input()` & Ép kiểu:**
  - `input()` luôn trả về kiểu chuỗi (`str`).
  - Khi cần tính toán số học, bắt buộc phải ép kiểu số nguyên `int(input())` hoặc số thực `float(input())`.

### 2. Bảng công thức & Quy tắc ghi nhớ
| Thao tác | Cú pháp Python | Kết quả / Ý nghĩa |
|---|---|---|
| In chuỗi và số | `print("Ket qua:", a + b)` | In chữ kèm kết quả tính toán |
| Nhập số nguyên | `n = int(input())` | Đọc 1 dòng từ bàn phím và ép sang số nguyên |
| Nhập số thực | `x = float(input())` | Đọc 1 dòng từ bàn phím và ép sang số thực |
| Hoán đổi 2 biến | `a, b = b, a` | Đổi chỗ 2 biến mà không cần biến phụ |

### 3. Bẫy lỗi phòng thi
- ❌ **Quên ép kiểu `int()`:** `a = input()`, `b = input()` rồi `print(a + b)` sẽ thành phép ghép chữ (Ví dụ: `"5" + "3" = "53"` thay vì số 8).
- ❌ **Đặt nháy kép quanh phép tính:** `print("5 + 3")` in ra chữ `5 + 3`, phải viết `print(5 + 3)` mới ra 8.
- ❌ **Tên biến sai quy tắc:** Viết `1diem = 10` hoặc `diem toan = 10` sẽ bị báo lỗi `SyntaxError`.

### 4. Mẫu code chuẩn
```python
# Mẫu nhập 2 số nguyên trên 2 dòng và in tổng
a = int(input())
b = int(input())
tong = a + b
print(tong)
```

---

## BÀI 02: PHÉP TOÁN SỐ HỌC, CHIA NGUYÊN VÀ CHIA DƯ *(BÀI TRỌNG TÂM CHI TIẾT)*

### 1. Kiến thức chuyên sâu dành cho học sinh Phổ thông
Python cung cấp 7 phép toán số học. Trong đó, bộ đôi **Chia lấy phần nguyên (`//`)** và **Chia lấy phần dư (`%`)** là nền tảng cốt lõi của mọi bài thi Lập trình Python:

```
Phép chia: A : B  (Ví dụ: 17 chia cho 5)
17 = 5 x 3 + 2
       │     │
       │     └─► 17 % 5  = 2 (Số dư - Modulo)
       └───────► 17 // 5 = 3 (Thương nguyên - Floor Division)
```

#### A. Phép chia thực (`/`)
- Ký hiệu một dấu gạch chéo `/`.
- **Đặc điểm sống còn:** Kết quả luôn luôn là số thực (`float`), kể cả khi chia hết. Ví dụ: `8 / 2` cho ra `4.0` chứ không phải `4`. Nếu đề bài yêu cầu in ra số nguyên, dùng `/` sẽ bị trừ điểm!

#### B. Phép chia lấy phần nguyên (`//`)
- Ký hiệu hai dấu gạch chéo liền nhau `//`.
- **Ý nghĩa:** Trả lời câu hỏi *"Có thể chia được trọn vẹn bao nhiêu phần bằng nhau?"*.
- Bỏ hoàn toàn phần thập phân, chỉ giữ lại số nguyên: `19 // 4 = 4` (vì $19 : 4 = 4.75$, lấy phần nguyên là $4$).

#### C. Phép chia lấy phần dư (`%`)
- Ký hiệu dấu phần trăm `%`.
- **Ý nghĩa:** Trả lời câu hỏi *"Sau khi chia đều hết mức có thể, còn thừa ra bao nhiêu?"*.
- `19 % 4 = 3` (vì $4 	imes 4 = 16$, còn dư $19 - 16 = 3$).

#### D. Định lý chia có dư Toán Phổ thông trong Python
$$\mathbf{A} = (\mathbf{A} // \mathbf{B}) 	imes \mathbf{B} + (\mathbf{A} \% \mathbf{B})$$

#### E. Thứ tự ưu tiên tính toán (Quy tắc PEMDAS)
$$	ext{Ngoặc } () \longrightarrow 	ext{Lũy thừa } ** \longrightarrow 	ext{Nhân, Chia } (*, /, //, \%) \longrightarrow 	ext{Cộng, Trừ } (+, -)$$
*Lưu ý:* Các phép toán cùng cấp độ được thực hiện lần lượt từ **Trái sang Phải**.

### 2. Sổ tay 6 kỹ thuật ứng dụng thực chiến của `//` và `%`

#### Kỹ thuật 1: Kiểm tra tính chẵn lẻ
- Số chẵn là số chia hết cho 2 (dư 0): `n % 2 == 0`.
- Số lẻ là số chia cho 2 dư 1: `n % 2 == 1` (hoặc `n % 2 != 0`).

#### Kỹ thuật 2: Kiểm tra tính chia hết
- Số $A$ là bội số của $B$ (hay $A$ chia hết cho $B$): `A % B == 0`.

#### Kỹ thuật 3: Bóc tách chữ số hàng đơn vị và hàng chục
- Lấy chữ số hàng đơn vị (chữ số cuối cùng): `don_vi = n % 10`.
- Gọt bỏ chữ số hàng đơn vị: `tam = n // 10`.
- Lấy chữ số hàng chục của số $N$: `chuc = (n // 10) % 10`.

#### Kỹ thuật 4: Kỹ thuật làm tròn lên (Ceiling Division)
- *Bài toán:* Có $N$ học sinh, cần thuê xe chở học sinh, mỗi xe chở được $K$ bạn. Cần ít nhất bao nhiêu xe để không bạn nào bị bỏ lại?
- Nếu dùng `N // K`, với $N = 25, K = 10$ sẽ ra $2$ (thiếu 1 xe chở 5 bạn còn lại!).
- **Công thức làm tròn lên chuẩn:**
  $$\mathbf{so\_xe = (N + K - 1) // K}$$
  *Kiểm tra:* $(25 + 10 - 1) // 10 = 34 // 10 = 3$ xe (Tuyệt đối chính xác!).

#### Kỹ thuật 5: Bài toán chu kỳ vòng tròn (Đồng hồ, Vòng chạy)
- Một vòng có $M$ trạng thái (từ 0 đến $M-1$). Di chuyển thêm $K$ bước:
  $$\mathbf{vi\_tri\_moi = (vi\_tri\_cu + K) \% M}$$
- Đồng hồ 12 giờ: Sau $K$ giờ nữa kim chỉ số mấy?
  `gio_moi = (gio_hien_tai + K) % 12`. Nếu `gio_moi == 0` thì kết quả là `12`.
  *Hoặc mẹo 1 dòng:* `(gio_hien_tai + K - 1) % 12 + 1`.

#### Kỹ thuật 6: Đổi số thứ tự $K$ sang tọa độ (Hàng, Cột) trên bàn cờ
- Một bảng ô vuông có chiều rộng mỗi hàng là $W$ ô. Ô thứ $K$ ($K$ tính từ 1):
  - `idx = K - 1` (Chuyển về mốc 0)
  - `hang = (idx // W) + 1`
  - `cot = (idx % W) + 1`

### 3. Bảng bẫy lỗi phòng thi thường gặp
| Code sai | Báo lỗi / Hiện tượng | Nguyên nhân | Cách sửa đúng |
|---|---|---|---|
| `a / b` | In ra `3.0` thay vì `3` | Dùng chia thực `/` | Dùng chia nguyên `a // b` |
| `a % 0` hoặc `a // 0` | `ZeroDivisionError` | Mẫu số chia bằng 0 | Đảm bảo mẫu số $> 0$ |
| `a ^ b` | Kết quả sai hoàn toàn | `^` là phép XOR bit, không phải mũ | Viết `a ** b` |
| `a x b` | `SyntaxError` | Dùng chữ `x` làm dấu nhân | Viết `a * b` |

### 4. Hệ thống 15 bài tập thực hành phân tầng chi tiết

#### Nhóm 1: Cơ bản — Nhận biết và tính toán trực tiếp
* **Bài 1.1 (Chia kẹo công bằng):** Mẹ có $a$ chiếc kẹo chia đều cho $b$ bạn nhỏ. In ra 2 số trên một dòng: số kẹo mỗi bạn nhận được và số kẹo còn thừa.
  * *Input:* `17` và `5` $
ightarrow$ *Output:* `3 2`.
* **Bài 1.2 (Số ngày và tuần):** Một kỳ nghỉ hè kéo dài $N$ ngày. Hãy cho biết kỳ nghỉ đó gồm bao nhiêu tuần trọn vẹn và còn lẻ mấy ngày?
  * *Input:* `25` $
ightarrow$ *Output:* `3 4` (3 tuần 4 ngày).
* **Bài 1.3 (Nhân đôi lũy thừa):** Một tế bào ban đầu sau mỗi giờ sẽ tự nhân đôi. Hỏi sau $n$ giờ ($1 \le n \le 30$) có bao nhiêu tế bào?
  * *Input:* `5` $
ightarrow$ *Output:* `32` (Tính $2^5$).
* **Bài 1.4 (Bội chung đơn giản):** Nhập 2 số $A$ và $B$. In ra số dư khi lấy $A$ chia cho $B$.
  * *Input:* `100 8` $
ightarrow$ *Output:* `4`.
* **Bài 1.5 (Tính trung bình cộng nguyên):** Nhập 3 số nguyên $a, b, c$. Biết tổng của chúng chia hết cho 3. Hãy in ra trung bình cộng dạng số nguyên của 3 số đó.
  * *Input:* `4 7 10` $
ightarrow$ *Output:* `7` (Viết `(a + b + c) // 3`).

#### Nhóm 2: Luyện tập — Biến đổi số học và tách số
* **Bài 1.6 (Tách hai chữ số):** Nhập số nguyên dương $N$ có đúng 2 chữ số ($10 \le N \le 99$). In ra chữ số hàng chục và chữ số hàng đơn vị cách nhau dấu cách.
  * *Input:* `83` $
ightarrow$ *Output:* `8 3`.
* **Bài 1.7 (Đảo ngược số 2 chữ số):** Nhập số $N$ ($10 \le N \le 99$). In ra số sau khi hoán đổi vị trí hàng chục và hàng đơn vị.
  * *Input:* `49` $
ightarrow$ *Output:* `94`.
* **Bài 1.8 (Chữ số hàng chục của số 3 chữ số):** Nhập số nguyên $N$ ($100 \le N \le 999$). Hãy tìm và in ra chữ số hàng chục của $N$.
  * *Input:* `752` $
ightarrow$ *Output:* `5`.
* **Bài 1.9 (Tổng 3 chữ số):** Nhập số $N$ ($100 \le N \le 999$). Hãy tính tổng 3 chữ số cấu tạo nên số $N$.
  * *Input:* `345` $
ightarrow$ *Output:* `12` ($3 + 4 + 5 = 12$).
* **Bài 1.10 (Bàn cờ ca-rô):** Bàn cờ vô tận có mỗi hàng gồm $W$ ô. Ô thứ $K$ nằm ở hàng mấy, cột mấy?
  * *Input:* `K = 11, W = 4` $
ightarrow$ *Output:* `3 3`.

#### Nhóm 3: Vận dụng — Bài toán thực tế đời sống
* **Bài 1.11 (Thuê xe du lịch - Làm tròn lên):** Khối 5 có $N$ học sinh đi tham quan. Mỗi xe buýt chở được tối đa $K$ học sinh. Cần thuê ít nhất bao nhiêu xe để chở hết học sinh?
  * *Input:* `25 10` $
ightarrow$ *Output:* `3` (Áp dụng `(N + K - 1) // K`).
* **Bài 1.12 (Kim đồng hồ 12 giờ):** Đồng hồ đang chỉ $H$ giờ. Sau đúng $K$ giờ nữa, kim giờ chỉ vào số mấy (từ 1 đến 12)?
  * *Input:* `H = 10, K = 5` $
ightarrow$ *Output:* `3`.
* **Bài 1.13 (Vận động viên chạy vòng quanh sân):** Đường chạy dài $400	ext{m}$. Vận động viên chạy được quãng đường $D$ mét. Hỏi vận động viên đã chạy được bao nhiêu vòng trọn vẹn và đang cách vạch xuất phát bao nhiêu mét?
  * *Input:* `1450` $
ightarrow$ *Output:* `3 250`.
* **Bài 1.14 (Trồng cây có đầu mút):** Đại lộ dài $L$ mét. Cứ cách $K$ mét người ta trồng một cây bóng mát, bắt đầu trồng cây đầu tiên ngay tại vạch 0 mét. Hỏi trồng được tất cả bao nhiêu cây?
  * *Input:* `10 3` $
ightarrow$ *Output:* `4` (Các vị trí 0, 3, 6, 9 $\implies (L // K) + 1$).
* **Bài 1.15 (Xếp hàng mua vé):** Trong rạp chiếu phim, các ghế được đánh số liên tiếp từ 1. Mỗi dãy ghế có đúng 8 chỗ ngồi. Bạn An có vé số $N$. An ngồi ở dãy ghế thứ mấy?
  * *Input:* `20` $
ightarrow$ *Output:* `3` (Áp dụng làm tròn lên: `(20 + 8 - 1) // 8 = 3`).

---

## BÀI 03: CÔNG THỨC TÍNH TOÁN, HÌNH HỌC VÀ ĐỔI ĐƠN VỊ *(BÀI TRỌNG TÂM CHI TIẾT)*

### 1. Kiến thức chuyên sâu dành cho học sinh Phổ thông

#### A. Các công thức hình học nền tảng
* **Hình chữ nhật:**
  - Chu vi: $P = (a + b) 	imes 2 \implies$ Code: `(a + b) * 2` *(Bắt buộc phải có dấu ngoặc tròn)*.
  - Diện tích: $S = a 	imes b \implies$ Code: `a * b`.
  - Nửa chu vi: $P_{nua} = P // 2$.
  - Tìm một cạnh khi biết chu vi $P$ và một cạnh $a$: $b = (P // 2) - a$.
* **Hình vuông:**
  - Chu vi: $P = a 	imes 4 \implies$ Code: `a * 4`.
  - Cạnh hình vuông từ chu vi: $a = P // 4$.
  - Diện tích: $S = a 	imes a = a^2 \implies$ Code: `a * a` hoặc `a ** 2`.
* **Tam giác vuông:**
  - Diện tích khi biết 2 cạnh góc vuông $a$ và $b$: $S = rac{a 	imes b}{2} \implies$ Code: `(a * b) // 2` (nếu tích chia hết cho 2).
* **Hình thang:**
  - Diện tích: $S = rac{(a + b) 	imes h}{2} \implies$ Code: `((a + b) * h) // 2`.

#### B. Bài toán diện tích hình học lồng ghép (Trừ phần giao / Phần còn lại)
* *Mô hình:* Có một khu đất lớn diện tích $S_1$, bên trong xây một công trình có diện tích $S_2$. Diện tích đất còn lại là:
  $$\mathbf{S_{con\_lai} = S_1 - S_2}$$
* *Bài toán bờ hồ & hòn đảo:* Hồ hình vuông cạnh $A$, đảo hình chữ nhật $B 	imes C$:
  `mat_nuoc = (A * A) - (B * C)`.

#### C. Thuật toán phân rã đơn vị thời gian (Từ giây sang Giờ — Phút — Giây)
Biết rằng: $1	ext{ giờ} = 60	ext{ phút} = 3600	ext{ giây}$, $1	ext{ phút} = 60	ext{ giây}$.
Cho trước $S$ giây, quy trình phân rã gồm 3 bước:
1. **Tính số giờ:** `gio = S // 3600`
2. **Lấy số giây còn dư sau khi tính giờ:** `giay_du = S % 3600`
3. **Tính số phút và giây từ phần dư:**
   - `phut = giay_du // 60`
   - `giay = giay_du % 60`

#### D. Kỹ thuật in số thập phân và làm tròn
- Làm tròn 2 chữ số thập phân: `round(x, 2)`.
- **In chuẩn định dạng bằng f-string:** `print(f"{x:.2f}")` (Đảm bảo số `5` sẽ in ra đủ `5.00`).
- **In bù số 0 ở đầu (Ví dụ: in 5 giây thành `05`):** `print(f"{giay:02d}")`.

### 2. Bảng công thức quy đổi đơn vị đo lường cần thuộc lòng
| Tên đơn vị | Quy đổi xuôi | Lưu ý khi tính diện tích |
|---|---|---|
| Độ dài | $1	ext{ m} = 10	ext{ dm} = 100	ext{ cm} = 1000	ext{ mm}$ | $1	ext{ km} = 1000	ext{ m}$ |
| Diện tích | $1	ext{ m}^2 = 100	ext{ dm}^2 = 10,000	ext{ cm}^2$ | **Độ dài nhân 10 thì diện tích nhân 100!** |
| Khối lượng | $1	ext{ tấn} = 10	ext{ tạ} = 1000	ext{ kg}$; $1	ext{ kg} = 1000	ext{ g}$ | Luôn đổi về cùng đơn vị nhỏ nhất trước |

### 3. Bẫy lỗi phòng thi
- ❌ **Quên đổi về cùng đơn vị:** Dài $2	ext{ m}$, rộng $30	ext{ cm}$ mà tính diện tích $2 	imes 30 = 60$ là sai! Phải đổi $2	ext{ m} = 200	ext{ cm}$, diện tích là $200 	imes 30 = 6000	ext{ cm}^2$.
- ❌ **Thiếu ngoặc phép tính nửa chu vi:** Viết `P // 2 - a` thì đúng, nhưng viết `P - a // 2` là sai hoàn toàn!

### 4. Hệ thống 15 bài tập thực hành phân tầng chi tiết

#### Nhóm 1: Cơ bản — Hình học trực tiếp
* **Bài 3.1 (Mảnh vườn chữ nhật):** Nhập chiều dài $a$ và chiều rộng $b$. In ra chu vi và diện tích trên cùng 1 dòng cách nhau dấu cách.
  * *Input:* `10 6` $
ightarrow$ *Output:* `32 60`.
* **Bài 3.2 (Khung tranh hình vuông):** Nhập cạnh tranh $a$ (cm). In ra độ dài khung gỗ cần mua (chu vi) và diện tích tấm kính bảo vệ bề mặt.
  * *Input:* `8` $
ightarrow$ *Output:* `32 64`.
* **Bài 3.3 (Chu vi tam giác):** Nhập 3 cạnh của tam giác $a, b, c$. Tính chu vi tam giác đó.
  * *Input:* `3 4 5` $
ightarrow$ *Output:* `12`.
* **Bài 3.4 (Cạnh ao còn lại):** Một cái ao hình chữ nhật có chu vi $P = 30	ext{m}$, một cạnh đã biết là $5	ext{m}$. Tìm độ dài cạnh còn lại.
  * *Input:* `P = 30, a = 5` $
ightarrow$ *Output:* `10` (Công thức: `(P // 2) - a`).
* **Bài 3.5 (Diện tích tam giác vuông):** Nhập 2 cạnh góc vuông $a$ và $b$ (biết tích $a 	imes b$ là số chẵn). Tính diện tích tam giác.
  * *Input:* `6 8` $
ightarrow$ *Output:* `24`.

#### Nhóm 2: Luyện tập — Đổi đơn vị và Phân rã thời gian
* **Bài 3.6 (Đổi giây sang phút giây):** Nhập số giây $S$ ($S < 3600$). Hãy đổi ra xem gồm bao nhiêu phút và bao nhiêu giây.
  * *Input:* `125` $
ightarrow$ *Output:* `2 5` (2 phút 5 giây).
* **Bài 3.7 (Phân rã thời gian trọn vẹn):** Nhập tổng số giây $S$. In ra 3 số `Gio Phut Giay` tương ứng.
  * *Input:* `3665` $
ightarrow$ *Output:* `1 1 5` (1 giờ 1 phút 5 giây).
* **Bài 3.8 (Đổi thước kẻ milimet):** Chiếc thước dài $a	ext{ cm}$ và thêm $b	ext{ mm}$. Đổi toàn bộ độ dài thước ra milimet.
  * *Input:* `a = 2, b = 5` $
ightarrow$ *Output:* `25` (Vì $2	ext{ cm} = 20	ext{ mm} \implies 20 + 5 = 25$).
* **Bài 3.9 (Thời gian chạy đua):** Vận động viên chạy xuất phát lúc $H_1$ giờ $M_1$ phút và về đích lúc $H_2$ giờ $M_2$ phút (cùng ngày, $H_2 > H_1$). Tính tổng thời gian chạy ra đơn vị phút.
  * *Input:* `8 15` và `10 45` $
ightarrow$ *Output:* `150` phút.
* **Bài 3.10 (Đồng hồ điện tử format đẹp):** Nhập vào số phút $M$ và số giây $S$. Hãy in ra dạng chuẩn điện tử `MM:SS` có chèn số 0 ở đầu nếu nhỏ hơn 10.
  * *Input:* `M = 5, S = 8` $
ightarrow$ *Output:* `05:08` (Dùng `f"{M:02d}:{S:02d}"`).

#### Nhóm 3: Vận dụng — Hình học ghép và bài toán thực tế
* **Bài 3.11 (Hồ cá sấu và đảo nổi):** Một hồ nuôi cá sấu hình vuông cạnh $A$. Giữa hồ có đảo nhỏ hình chữ nhật kích thước $B 	imes C$. Tính diện tích phần mặt nước.
  * *Input:* `A = 10, B = 3, C = 4` $
ightarrow$ *Output:* `88` ($100 - 12 = 88$).
* **Bài 3.12 (Lát gạch sân trường):** Sân trường hình chữ nhật kích thước $D 	imes R$ mét. Dùng các viên gạch hình vuông cạnh $K$ mét để lát kín sân ($D, R$ chia hết cho $K$). Tính số viên gạch cần mua.
  * *Input:* `D = 20, R = 10, K = 2` $
ightarrow$ *Output:* `50` viên ($200 // 4 = 50$).
* **Bài 3.13 (Rào quanh vườn hoa chừa cổng):** Vườn hoa hình chữ nhật kích thước $a 	imes b$ mét. Người ta làm hàng rào bao quanh vườn, nhưng chừa lại một cửa đi rộng $c$ mét (không rào). Tính chiều dài hàng rào cần làm.
  * *Input:* `a = 12, b = 8, c = 2` $
ightarrow$ *Output:* `38` (Chu vi 40 trừ cửa 2).
* **Bài 3.14 (Bồn hoa chữ thập):** Bồn hoa hình chữ thập (dấu cộng) tạo bởi hai hình chữ nhật $a 	imes b$ đè lên nhau, phần giao nhau ở giữa là hình vuông $b 	imes b$. Tính diện tích thực tế của bồn hoa.
  * *Input:* `a = 10, b = 3` $
ightarrow$ *Output:* `51` ($2 	imes (10 	imes 3) - 3 	imes 3 = 51$).
* **Bài 3.15 (Hai bạn đạp xe gặp nhau):** Thuận ở vị trí $x$, Ánh ở vị trí $y$ ($x < y$). Thuận đạp xe về phía Ánh với vận tốc $v	ext{ km/h}$. Biết khoảng cách chia hết cho $v$. Sau bao nhiêu giờ hai bạn gặp nhau?
  * *Input:* `x = 10, y = 70, v = 15` $
ightarrow$ *Output:* `4` (Công thức: `(y - x) // v`).

---

# CHƯƠNG 2: TƯ DUY RẼ NHÁNH & ĐIỀU KIỆN LOGIC

---

## BÀI 04: CẤU TRÚC RẼ NHÁNH `IF - ELIF - ELSE` VÀ ĐIỀU KIỆN GHÉP `AND - OR - NOT` *(GỘP TRỌNG TÂM)*

### 1. Tóm tắt kiến thức trọng tâm
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
  - `not`: Đảo ngược Đúng $\leftrightarrow$ Sai.
  - Cú pháp so sánh kẹp tiện lợi trong Python: `10 <= x <= 99`.

### 2. Sổ tay các biểu thức logic hay thi
- Kiểm tra tam giác hợp lệ: `(a + b > c) and (a + c > b) and (b + c > a)`
- Kiểm tra năm nhuận: `(nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)`
- Kiểm tra số có 2 chữ số: `10 <= n <= 99`

### 3. Bẫy lỗi phòng thi
- ❌ Nhầm `==` (so sánh) thành `=` (gán): `if a = 5:` $\implies$ Báo lỗi `SyntaxError`.
- ❌ Bẫy viết tắt sai: `if a == 1 or 2:` $\implies$ Python hiểu là `if (a == 1) or (2)`, số 2 khác 0 luôn là `True` nên câu `if` luôn chạy sai! Phải viết: `if a == 1 or a == 2:`.

### 4. Mẫu code chuẩn
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

### 5. Hệ thống bài tập thực hành tăng cường (14 bài)
* **Bài 4.1 (Số lớn nhất 2 số):** Nhập 2 số nguyên $a, b$. In ra số lớn hơn.
* **Bài 4.2 (Kiểm tra chẵn lẻ):** Nhập $N$. In `CHAN` hoặc `LE`.
* **Bài 4.3 (Vé vào cổng công viên):** Cao từ $130	ext{ cm}$ trở lên mua `VE NGUOI LON`, dưới $130	ext{ cm}$ mua `VE TRE EM`.
* **Bài 4.4 (Số lớn nhất trong 3 số):** Nhập $a, b, c$. In ra giá trị lớn nhất (Dùng `max(a, b, c)` hoặc cấu trúc lính canh).
* **Bài 4.5 (Dấu của số nguyên):** Nhập $N$. In `DUONG`, `AM` hoặc `KHONG`.
* **Bài 4.6 (Xếp loại học lực):** Điểm $\ge 9.0$: `XUAT SAC`; $\ge 8.0$: `GIOI`; $\ge 6.5$: `KHA`; còn lại: `CAN CO GANG`.
* **Bài 4.7 (Cước taxi bậc thang):** $1	ext{ km}$ đầu giá 10k; từ km 2 đến 10 giá 8k/km; từ km 11 trở đi giá 6k/km. Tính tổng tiền đi $N$ km.
* **Bài 4.8 (Kiểm tra tam giác hợp lệ):** Cho 3 số dương $a, b, c$. Kiểm tra xem có tạo thành tam giác không. In `YES` hoặc `NO`.
* **Bài 4.9 (Kiểm tra năm nhuận):** Cho năm dương lịch $Y$. In `NAM NHUAN` hoặc `NAM THUONG`.
* **Bài 4.10 (Số ngày trong tháng):** Cho tháng $M$ và năm $Y$. In ra số ngày của tháng đó (chú ý tháng 2 năm nhuận có 29 ngày).
* **Bài 4.11 (Tam giác vuông):** Cho 3 cạnh $a, b, c$. Kiểm tra có phải tam giác vuông theo Pytago không.
* **Bài 4.12 (Thẻ may mắn):** Số $N$ may mắn nếu chia hết cho 7 HOẶC tận cùng bằng 7. In `TRUNG THUONG` hoặc `CHUC MAY MAN`.
* **Bài 4.13 (Cặp số cùng dấu hay trái dấu):** Nhập 2 số nguyên khác 0. In `CUNG DAU` hoặc `TRAI DAU`.
* **Bài 4.14 (Trò chơi kéo búa bao):** Nhập lựa chọn của 2 người chơi (1: Búa, 2: Kéo, 3: Bao). Xác định người thắng hoặc hòa.

---

# CHƯƠNG 3: VÒNG LẶP

---

## BÀI 05: VÒNG LẶP FOR VÀ HÀM RANGE

### 1. Tóm tắt kiến thức trọng tâm
- Dùng khi **đã biết trước số lần lặp cụ thể**.
- Cú pháp: `for <bien> in range(start, stop, step):`
- Cận dừng `stop` không bao giờ được lấy tới (máy dừng ngay trước `stop`).
- **Mẫu tích lũy ống heo (Accumulator):** Khởi tạo `tong = 0` trước vòng lặp, mỗi lượt cộng dồn `tong += i`.

### 2. Bảng công thức ghi nhớ
| Cú pháp | Dãy số sinh ra |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, N + 1)` | `1, 2, 3, ..., N` |
| `range(2, N + 1, 2)` | Các số chẵn từ 2 đến $N$ |
| `range(N, 0, -1)` | Đếm lùi từ $N$ về 1 |

### 3. Mẫu code chuẩn
```python
# Tính tổng các số chẵn từ A đến B
a = int(input())
b = int(input())
tong = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        tong += i
print(tong)
```

---

## BÀI 06: VÒNG LẶP WHILE VÀ KỸ THUẬT ĐIỀU KHIỂN LUỒNG

### 1. Tóm tắt kiến thức trọng tâm
- Dùng khi **chưa biết trước số lần lặp**, lặp trong khi điều kiện còn Đúng (`True`).
- Bắt buộc phải có câu lệnh làm thay đổi điều kiện lặp để không bị đơ máy (Infinite loop).
- **`break`:** Dừng và nhảy ra khỏi vòng lặp ngay lập tức.
- **`continue`:** Bỏ qua lần lặp hiện tại, chuyển sang lần lặp kế tiếp.
- **Biến cờ (Flag):** Biến kiểu `bool` (`True`/`False`) dùng đánh dấu phát hiện mục tiêu.

### 2. Mẫu code chuẩn
```python
# Nhập liên tiếp các số nguyên cho đến khi gặp số 0 thì dừng, đếm số lượng số đã nhập
dem = 0
while True:
    x = int(input())
    if x == 0:
        break
    dem += 1
print(dem)
```

---

# CHƯƠNG 4: BÀI TOÁN SỐ HỌC

---

## BÀI 07: QUY LUẬT DÃY SỐ VÀ TAM GIÁC SỐ *(CHUYỂN TỪ BÀI 9 SANG)*

### 1. Tóm tắt kiến thức trọng tâm
- **Cấp số cộng:** Số thứ $N$ của dãy có số đầu $u_1$ và khoảng cách $d$ là: $u_N = u_1 + (N - 1) 	imes d$.
- **Dãy Fibonacci:** $1, 1, 2, 3, 5, 8, 13, \dots$ Mỗi số bằng tổng 2 số liền trước. Áp dụng kỹ thuật cuốn chiếu: `a, b = b, a + b`.
- **Tam giác số:** Sử dụng 2 vòng lặp lồng nhau (vòng ngoài điều khiển số hàng, vòng trong điều khiển số cột).

### 2. Mẫu code chuẩn
```python
# In tam giác số tăng dần
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

## BÀI 08: TÁCH CHỮ SỐ VỚI CHIA NGUYÊN VÀ CHIA DƯ

### 1. Tóm tắt kiến thức trọng tâm
- Bản chất 2 nhịp vĩnh cửu:
  - `cs = n % 10`: Bóc chữ số hàng đơn vị.
  - `n = n // 10`: Cắt ngắn số đi 1 chữ số.
- Vòng lặp tách số: `while n > 0:`
- **Tạo số đảo ngược:** `dao = dao * 10 + cs`.
- **Số đối xứng (Palindrome):** Số đọc xuôi hay ngược đều giống nhau (`dao == n_goc`).

### 2. Mẫu code chuẩn
```python
# Kiểm tra số đối xứng
n = int(input())
n_goc = n
dao = 0

while n > 0:
    cs = n % 10
    dao = dao * 10 + cs
    n //= 10

if dao == n_goc:
    print("YES")
else:
    print("NO")
```

---

## BÀI 09: ƯỚC SỐ, BỘI SỐ VÀ SỐ NGUYÊN TỐ

### 1. Tóm tắt kiến thức trọng tâm
- Số nguyên tố là số $> 1$, chỉ có 2 ước là 1 và chính nó. Số 0 và 1 không phải là số nguyên tố. Số 2 là số nguyên tố chẵn duy nhất.
- **Thuật toán kiểm tra số nguyên tố tối ưu $\mathcal{O}(\sqrt{N})$:** Chỉ duyệt ước từ 2 đến $\lfloor\sqrt{N}
floor$ (`int(n**0.5)`).
- **ƯCLN và BCNN:**
  ```python
  import math
  ucln = math.gcd(a, b)
  bcnn = (a * b) // ucln
  ```

### 2. Mẫu code chuẩn
```python
# Kiểm tra số nguyên tố
n = int(input())
la_nt = True
if n < 2:
    la_nt = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_nt = False
            break

print("YES" if la_nt else "NO")
```

---

## BÀI 10: ĐẾM SỐ THEO QUY LUẬT VÀ SỐ ĐẶC BIỆT

### 1. Tóm tắt kiến thức trọng tâm
- **Công thức đếm bội số trong đoạn $[A, B]$ với $\mathcal{O}(1)$:**
  $$\mathbf{count(A, B, K) = (B // K) - ((A - 1) // K)}$$
- **Số hoàn hảo:** Tổng các ước nhỏ hơn nó bằng chính nó ($6, 28, 496$).
- **Số chính phương:** Số có căn bậc 2 là số nguyên: `int(n**0.5)**2 == n`.

---

## BÀI 11: DANH SÁCH VÀ THAO TÁC CƠ BẢN

### 1. Tóm tắt kiến thức trọng tâm
- Danh sách (List) là tập hợp nhiều phần tử lưu trong dấu ngoặc vuông `[]`.
- Cho phép thay đổi giá trị tại từng vị trí (Mutable): `a[0] = 100`.
- **Cú pháp nhập danh sách số trên 1 dòng:**
  ```python
  a = list(map(int, input().split()))
  ```
- **Các lệnh thao tác danh sách cơ bản:**
  - `a.append(x)`: Thêm $x$ vào cuối danh sách.
  - `a.remove(x)`: Xóa phần tử đầu tiên có giá trị $x$.
  - `a.insert(i, x)`: Chèn giá trị $x$ vào vị trí index $i$.
  - `len(a)`: Trả về số lượng phần tử.
  - `if x in a:`: Kiểm tra $x$ có nằm trong danh sách không.

---

## BÀI 12: THỐNG KÊ DANH SÁCH VÀ SẮP XẾP

### 1. Tóm tắt kiến thức trọng tâm
- **Hàm thống kê tích hợp sẵn:** `max(a)`, `min(a)`, `sum(a)`.
  - Trung bình cộng: `sum(a) / len(a)`.
- **Sắp xếp danh sách:**
  - `a.sort()`: Sắp xếp tăng dần trực tiếp trên mảng `a`.
  - `a.sort(reverse=True)`: Sắp xếp giảm dần.
  - `b = sorted(a)`: Tạo mảng mới `b` đã sắp xếp, giữ nguyên mảng `a`.
- **Lọc phần tử trùng lặp:** `unique = sorted(list(set(a)))`.

### 2. Mẫu code chuẩn
```python
# Nhập mảng số nguyên, in số lớn nhất, nhỏ nhất và mảng sắp xếp tăng dần
a = list(map(int, input().split()))
print("Max:", max(a))
print("Min:", min(a))
a.sort()
print("Sap xep:", *a)
```

---

# CHƯƠNG 5: DANH SÁCH (LIST), XỬ LÝ CHUỖI & LUYỆN THI

---

## BÀI 13: CHỈ SỐ VÀ CẮT LÁT CHUỖI

### 1. Tóm tắt kiến thức trọng tâm
- Chuỗi ký tự (String) đánh chỉ số bắt đầu từ **0**.
  - Ký tự đầu tiên: `s[0]`.
  - Ký tự cuối cùng: `s[-1]`.
  - Độ dài chuỗi: `len(s)`.
- **Cắt lát chuỗi (Slicing) `s[start:stop]`:** Lấy từ `start` đến `stop - 1`.
  - Lấy $K$ ký tự đầu: `s[:K]`.
  - Lấy từ vị trí $K$ đến hết: `s[K:]`.
  - **Đảo ngược chuỗi tức thì:** `s[::-1]`.
- Chuỗi trong Python là **bất biến (Immutable)**: Không thể gán sửa trực tiếp `s[0] = 'X'`.

---

## BÀI 14: DUYỆT CHUỖI, BIẾN ĐỔI KÝ TỰ VÀ XỬ LÝ TỪ

### 1. Tóm tắt kiến thức trọng tâm
- Duyệt từng ký tự: `for ch in s:`
- **Hàm kiểm tra:** `ch.isdigit()` (chữ số), `ch.isalpha()` (chữ cái), `ch.isupper()` (chữ hoa), `ch.islower()` (chữ thường).
- **Hàm biến đổi:** `s.upper()` (chuyển sang chữ hoa), `s.lower()` (chuyển sang chữ thường), `s.replace(old, new)`.
- **Tách từ và ghép từ:**
  - Tách các từ trong câu (tự động xóa dấu cách thừa): `danh_sach_tu = s.split()`
  - Ghép lại bằng 1 khoảng trắng: `" ".join(danh_sach_tu)`
- **Mã ASCII (`ord` và `chr`):**
  - `ord('A') == 65`, `ord('a') == 97`, `ord('0') == 48`.
  - `chr(65) == 'A'`.

---

## BÀI 15: CHIẾN LƯỢC LÀM BÀI, PHÂN TÍCH TEST BIÊN & TỐI ƯU THỜI GIAN

### 1. Bản đồ 5 bước tác chiến trong phòng thi
```
BƯỚC 1: Đọc đề cẩn thận (Tối thiểu 2 lần, gạch chân Ràng buộc dữ liệu & Input/Output)
   │
BƯỚC 2: Nháp thuật toán & Dry Run tay với Sample Test trên giấy
   │
BƯỚC 3: Liệt kê các "Bẫy hiểm độc" (Edge Cases: N = 0, N = 1, số âm, số cực lớn)
   │
BƯỚC 4: Lập trình sạch sẽ, dùng đúng kiểu dữ liệu, in đúng từng chữ hoa/thường
   │
BƯỚC 5: Tự kiểm thử (Self-Testing) với test nhỏ nhất, test biên và test lớn nhất trước khi nộp!
```

### 2. Các tử huyệt làm mất điểm oan
- In thừa chữ dẫn dắt: Đề chỉ yêu cầu in `15`, viết `print("Ket qua la:", 15)` sẽ bị chấm `Wrong Answer (WA)` ngay lập tức.
- Không để ý giới hạn $N$: Nếu $N \le 10^5$ thì vòng lặp `for` an toàn. Nếu $N \ge 10^9$ bắt buộc phải dùng công thức giải tích $\mathcal{O}(1)$.

---

