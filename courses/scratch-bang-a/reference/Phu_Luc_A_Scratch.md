# Phụ lục A: Cẩm nang Khối lệnh & Nền tảng Thuật toán Scratch 3.0

Phụ lục này tổng hợp toàn bộ các bảng tra cứu cú pháp khối lệnh Tiếng Việt, công thức toán học hình học, hệ tọa độ sân khấu và các mẫu thuật toán kinh điển trong chương trình lập trình Scratch 3.0.

---

## 1. KHUNG TƯ DUY GIẢI QUYẾT BÀI TOÁN LẬP TRÌNH (MÔ HÌNH I - P - O)

Mọi bài toán lập trình khối lệnh đều vận hành theo chu trình 3 bước cốt lõi:

| Giai đoạn | Nhiệm vụ của học sinh | Khối lệnh Scratch tương ứng |
|---|---|---|
| **1. Đầu vào (Input)** | Xác định dữ liệu người dùng cung cấp hoặc đọc từ bàn phím. | Khối `hỏi [Nhập n:] và đợi`, lưu giá trị vào `câu trả lời`. |
| **2. Xử lý (Process)** | Tính toán theo công thức, dùng biến đếm, rẽ nhánh hoặc lặp. | Các khối `toán tử`, khối `đặt [biến] thành (...)`, khối `lặp lại (...)`. |
| **3. Đầu ra (Output)** | Hiển thị kết quả ra sân khấu hoặc vẽ hình tương ứng. | Khối `nói (...) trong (2) giây`, khối `nói (...)`, hoặc vẽ bằng `bút vẽ`. |

---

## 2. HỆ TRỤC TỌA ĐỘ OXY & LA BÀN HƯỚNG TRÊN SÂN KHẤU SCRATCH

Sân khấu Scratch 3.0 là mặt phẳng hình chữ nhật kích thước $480 \times 360$ bước chân:

| Thành phần | Ý nghĩa không gian | Giá trị cực tiểu | Trung tâm | Giá trị cực đại |
|---|---|:---:|:---:|:---:|
| **Trục X (Ngang)** | Trái $\longleftrightarrow$ Phải | $x = -240$ (Mép trái) | $x = 0$ (Tâm) | $x = 240$ (Mép phải) |
| **Trục Y (Dọc)** | Dưới $\longleftrightarrow$ Trên | $y = -180$ (Mép dưới) | $y = 0$ (Tâm) | $y = 180$ (Mép trên) |

### Bảng góc quay la bàn hướng nhìn nhân vật
- **Hướng $90^\circ$ (Mặc định)**: Nhân vật nhìn sang phải.
- **Hướng $0^\circ$**: Nhân vật nhìn thẳng lên trên.
- **Hướng $180^\circ$**: Nhân vật nhìn thẳng xuống dưới.
- **Hướng $-90^\circ$ (hoặc $270^\circ$)**: Nhân vật nhìn sang trái.

---

## 3. BẢNG CÔNG THỨC VẼ HÌNH ĐỒ HỌA BÚT VẼ (PEN)

### Cụm lệnh chuẩn bị giấy bút (Bắt buộc đầu bài vẽ hình)

![Cụm lệnh chuẩn bị giấy bút Scratch](courses/scratch-bang-a/assets/rendered_blocks/phu_luc_a_setup_pen.png)


### Bảng góc quay và bước đi của các đa giác đều
Công thức tính góc quay ngoài: **`Góc quay = 360 / Số_cạnh`**

| Hình đa giác đều | Số cạnh ($N$) | Vòng lặp | Góc xoay phải / trái | Công thức chu vi ($P$) |
|---|:---:|---|:---:|---|
| **Tam giác đều** | $3$ | `lặp lại (3) lần` | $120^\circ$ ($360 / 3$) | $P = 3 \times a$ |
| **Hình vuông** | $4$ | `lặp lại (4) lần` | $90^\circ$ ($360 / 4$) | $P = 4 \times a$ |
| **Ngũ giác đều** | $5$ | `lặp lại (5) lần` | $72^\circ$ ($360 / 5$) | $P = 5 \times a$ |
| **Lục giác đều** | $6$ | `lặp lại (6) lần` | $60^\circ$ ($360 / 6$) | $P = 6 \times a$ |
| **Bát giác đều** | $8$ | `lặp lại (8) lần` | $45^\circ$ ($360 / 8$) | $P = 8 \times a$ |
| **Ngôi sao 5 cánh nét liền** | $5$ | `lặp lại (5) lần` | $144^\circ$ ($720 / 5$) | Đi thẳng $a$, xoay $144^\circ$ |
| **Hình tròn xấp xỉ** | $360$ | `lặp lại (360) lần` | $1^\circ$ | Đi $(2 \times 3.14 \times R) / 360$, xoay $1^\circ$ |

---

## 4. BẢNG TOÁN TỬ VÀ CÁC PHÉP TÍNH CỐT LÕI

| Phép tính | Khối lệnh Scratch 3.0 | Ý nghĩa toán học | Ví dụ kết quả |
|---|---|---|---|
| **Cộng** | `(...) + (...)` | Phép cộng hai số $A + B$ | `5 + 3 = 8` |
| **Trừ** | `(...) - (...)` | Phép trừ hai số $A - B$ | `10 - 4 = 6` |
| **Nhân** | `(...) * (...)` | Phép nhân hai số $A \times B$ | `6 * 7 = 42` |
| **Chia thực** | `(...) / (...)` | Phép chia thập phân $A : B$ | `7 / 2 = 3.5` |
| **Chia lấy dư (Mod)** | `(...) mod (...)` | Số dư của phép chia nguyên | `17 mod 5 = 2` |
| **Chia lấy nguyên (Floor)** | `làm tròn xuống của ((A) / (B))` | Phần nguyên của phép chia | `làm tròn xuống của (17 / 5) = 3` |
| **Giá trị tuyệt đối** | `trị tuyệt đối của (...)` | Tính $\|A\|$ | `trị tuyệt đối của (-8) = 8` |
| **Căn bậc hai** | `căn bậc hai của (...)` | Tính $\sqrt{A}$ | `căn bậc hai của (25) = 5` |
| **Nối chuỗi chữ** | `kết hợp (...) và (...)` | Ghép hai đoạn văn bản | `kết hợp [Xin] và [chao] = Xinchao` |

---

## 5. CẤU TRÚC ĐIỀU KHIỂN & VÒNG LẶP KINH ĐIỂN

| Cấu trúc thuật toán | Khối lệnh Scratch | Khi nào sử dụng? |
|---|---|---|
| **Rẽ nhánh khuyết** | `nếu <điều kiện> thì` | Chỉ thực hiện khi điều kiện ĐÚNG, nếu SAI thì bỏ qua. |
| **Rẽ nhánh đủ** | `nếu <điều kiện> thì ... không thì` | Chọn 1 trong 2 nhánh hành động tùy thuộc điều kiện ĐÚNG hay SAI. |
| **Lặp xác định số lần** | `lặp lại (n) lần` | Đã biết trước chính xác số lần cần lặp (ví dụ lặp 10 lần, lặp N lần). |
| **Lặp có điều kiện dừng** | `lặp lại cho đến khi <điều kiện>` | Chưa biết trước số lần lặp, lặp liên tục cho tới khi điều kiện trở thành ĐÚNG. |
| **Vòng lặp vô tận** | `liên tục` | Dùng trong trò chơi hoặc hoạt hình cần nhân vật phản hồi mãi mãi. |

---

## 6. CÁC MẪU THUẬT TOÁN KINH ĐIỂN TRONG LẬP TRÌNH SCRATCH 3.0

### 6.1. Thuật toán bóc tách từng chữ số của số nguyên N
Dùng để tính tổng các chữ số, đếm số lượng chữ số hoặc đảo ngược số:

![Thuật toán bóc tách từng chữ số](courses/scratch-bang-a/assets/rendered_blocks/phu_luc_a_tach_chu_so.png)

### 6.2. Thuật toán kiểm tra số nguyên tố tối ưu ($i \times i \le N$)

![Thuật toán kiểm tra số nguyên tố](courses/scratch-bang-a/assets/rendered_blocks/phu_luc_a_so_nguyen_to.png)

### 6.3. Thuật toán tìm phần tử lớn nhất (Max) trong Danh sách

![Thuật toán tìm giá trị lớn nhất trong danh sách](courses/scratch-bang-a/assets/rendered_blocks/phu_luc_a_max_list.png)

### 6.4. Thuật toán đảo ngược chuỗi ký tự

![Thuật toán đảo ngược chuỗi ký tự](courses/scratch-bang-a/assets/rendered_blocks/phu_luc_a_dao_chuoi.png)

