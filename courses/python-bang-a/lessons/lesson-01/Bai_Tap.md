# Hệ thống bài tập thực hành — bài 01: Lệnh xuất nhập và biến số

---

## Bảng ma trận bài tập (10 bài tập phân tầng cơ bản → luyện tập)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L01-P01` | Lời chào robot | `Cơ bản` | Không có input | Lệnh `print()` in chuỗi ký tự cơ bản |
| 02 | `PYA-L01-P02` | Tấm danh thiếp thông minh | `Cơ bản` | Chuỗi $S$ không quá 50 ký tự | Lệnh `input()` chuỗi và in kèm thông điệp |
| 03 | `PYA-L01-P03` | Tuổi của bé sau 5 năm | `Cơ bản` | $1 \le N \le 12$ | Nhập số nguyên `int(input())`, phép cộng cơ bản |
| 04 | `PYA-L01-P04` | Cặp số nhân đôi | `Cơ bản` | $0 \le A \le 10^6$ | Phép nhân số nguyên và in kết quả |
| 05 | `PYA-L01-P05` | Đổi thước kẻ milimet | `Cơ bản` | $1 \le a, b \le 1000$ | Nhập 2 dòng số nguyên, chuyển đổi đơn vị đo |
| 06 | `PYA-L01-P06` | Cửa hàng bánh rán | `Luyện tập` | $1 \le a, b \le 100$ | Nhập đơn giá và số lượng, tính tổng số tiền |
| 07 | `PYA-L01-P07` | Chiếc hộp hoán đổi bí mật | `Luyện tập` | $0 \le A, B \le 10^9$ | Tư duy biến trung gian / hoán đổi giá trị 2 biến |
| 08 | `PYA-L01-P08` | Đoàn tàu toa xe ghép số | `Luyện tập` | $1 \le a, b \le 100$ | Phân biệt phép cộng số học và phép ghép chữ |
| 09 | `PYA-L01-P09` | Vé tham quan chùa hương | `Luyện tập` | $0 < a, b, x, y, n, m < 100$ | Bài toán thực tế nhiều biến, tổ chức luồng tính toán |
| 10 | `PYA-L01-P10` | Cỗ máy thời gian 3 thế hệ | `Luyện tập` | $1 \le a, b, c \le 100$ | Biến phụ thuộc, thiết lập quan hệ toán học giữa các biến |

---

### Bài 1 (Cơ bản): Lời chào robot (`PYA-L01-P01`)

* **Bối cảnh:** Bạn Robot vừa được khởi động trong phòng thí nghiệm iKHEDU. Em hãy giúp Robot phát ra lời chào mừng đến các bạn nhỏ.
* **Yêu cầu:** Viết chương trình in ra chính xác dòng chữ sau trên một dòng:
  ```text
  Xin chao cac ban! Toi la Robot Python.
  ```
* **Đầu vào (Input):** Không có dữ liệu vào.
* **Đầu ra (Output):** In ra một dòng chứa câu chào theo đúng mẫu.
* **Gợi ý thuật toán:** Sử dụng lệnh `print("...")`. Lưu ý gõ đúng từng chữ cái, dấu chấm và khoảng trắng.

---

### Bài 2 (Cơ bản): Tấm danh thiếp thông minh (`PYA-L01-P02`)

* **Bối cảnh:** Robot muốn làm quen với từng bạn nhỏ. Robot sẽ hỏi tên của bạn và in ra một câu chào thân thiện.
* **Yêu cầu:** Nhập vào tên của bạn nhỏ (một từ hoặc cụm từ), sau đó in ra câu chào theo mẫu: `Xin chao ban [Ten]!`
* **Đầu vào (Input):** Một dòng duy nhất chứa chuỗi ký tự tên của bạn nhỏ.
* **Đầu ra (Output):** In ra dòng thông điệp: `Xin chao ban <Ten>!` (giữa chữ `ban` và tên cách nhau một dấu cách, cuối câu có dấu chấm than `!`).
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Nam` | `Xin chao ban Nam!` |
  | `Bao Anh` | `Xin chao ban Bao Anh!` |
* **Gợi ý thuật toán:**
  ```python
  ten = input()
  print("Xin chao ban", ten + "!")
  ```

---

### Bài 3 (Cơ bản): Tuổi của bé sau 5 năm (`PYA-L01-P03`)

* **Bối cảnh:** Bé Bo năm nay tròn $N$ tuổi. Bé rất tò mò muốn biết sau 5 năm nữa thì bé sẽ bao nhiêu tuổi.
* **Yêu cầu:** Nhập vào số tuổi hiện tại $N$ của bé Bo. Hãy tính và in ra số tuổi của bé sau 5 năm nữa.
* **Đầu vào (Input):** Một dòng duy nhất chứa số tự nhiên $N$ ($1 \le N \le 12$).
* **Đầu ra (Output):** Một số nguyên duy nhất là số tuổi của bé Bo sau 5 năm.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `8` | `13` | Bé 8 tuổi, sau 5 năm nữa bé: $8 + 5 = 13$ tuổi |
* **Gợi ý thuật toán:** Bắt buộc phải ép kiểu số nguyên: `N = int(input())` rồi in `N + 5`.

---

### Bài 4 (Cơ bản): Cặp số nhân đôi (`PYA-L01-P04`)

* **Bối cảnh:** Trong trò chơi ảo thuật, nhà ảo thuật đặt một số nguyên $A$ vào chiếc hộp ma thuật. Khi mở hộp ra, số lượng viên ngọc sẽ được nhân lên gấp đôi.
* **Yêu cầu:** Nhập vào số nguyên $A$. Hãy in ra số lượng viên ngọc sau khi được nhân đôi.
* **Đầu vào (Input):** Gồm một số tự nhiên $A$ ($0 \le A \le 10^6$).
* **Đầu ra (Output):** In ra một số nguyên là kết quả nhân đôi ($A \times 2$).
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `15` | `30` |
  | `0` | `0` |
* **Gợi ý thuật toán:** `A = int(input()); print(A * 2)`.

---

### Bài 5 (Cơ bản): Đổi thước kẻ milimet (`PYA-L01-P05`)
*(Lấy cảm hứng từ Bài 2 Đề thi Tin học trẻ TP Bắc Ninh)*

* **Bối cảnh:** Bạn An có một chiếc thước kẻ dài $a\text{ cm}$ và thêm một đoạn nhỏ dài $b\text{ mm}$. Em hãy giúp An đổi toàn bộ chiều dài chiếc thước đó ra đơn vị milimet ($\text{mm}$).
* **Biết rằng:** $1\text{ cm} = 10\text{ mm}$.
* **Đầu vào (Input):**
  * Dòng 1: Chứa số tự nhiên $a$ ($1 \le a \le 1000$).
  * Dòng 2: Chứa số tự nhiên $b$ ($1 \le b \le 1000$).
* **Đầu ra (Output):** Một số tự nhiên duy nhất là độ dài của thước tính theo đơn vị milimet ($\text{mm}$).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `2`<br>`5` | `25` | $2\text{ cm} = 20\text{ mm}$. Tổng cộng là: $20 + 5 = 25\text{ mm}$. |
* **Gợi ý thuật toán:** Đọc lần lượt 2 dòng:
  ```python
  a = int(input())
  b = int(input())
  ket_qua = a * 10 + b
  print(ket_qua)
  ```

---

### Bài 6 (Luyện tập): Cửa hàng bánh rán (`PYA-L01-P06`)

* **Bối cảnh:** Chú mèo máy Doraemon đi mua bánh rán. Mỗi chiếc bánh rán có giá $a$ nghìn đồng. Doraemon muốn mua đúng $b$ chiếc bánh rán.
* **Yêu cầu:** Hãy tính số tiền (nghìn đồng) mà Doraemon cần phải trả cho người bán hàng.
* **Đầu vào (Input):** Nhập vào 2 số tự nhiên $a$ và $b$ mỗi số trên một dòng ($1 \le a \le 100, 1 \le b \le 100$).
* **Đầu ra (Output):** In ra số tiền Doraemon cần trả.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12`<br>`5` | `60` | Mua 5 chiếc bánh, mỗi chiếc 12 nghìn đồng: $12 \times 5 = 60$. |

---

### Bài 7 (Luyện tập): Chiếc hộp hoán đổi bí mật (`PYA-L01-P07`)

* **Bối cảnh:** Bạn Tèo có hai chiếc hộp: hộp $A$ đựng số kẹo của Tèo, hộp $B$ đựng số kẹo của Tí. Bây giờ hai bạn muốn đổi kẹo cho nhau (số kẹo trong hộp $A$ chuyển sang hộp $B$, và số kẹo trong hộp $B$ chuyển sang hộp $A$).
* **Yêu cầu:** Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của 2 biến và in ra giá trị mới của $A$ và $B$ sau khi hoán đổi (cách nhau một dấu cách).
* **Đầu vào (Input):** Dòng 1 chứa số $A$, dòng 2 chứa số $B$ ($0 \le A, B \le 10^9$).
* **Đầu ra (Output):** In ra hai số $A$ và $B$ sau khi hoán đổi trên cùng một dòng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `7`<br>`12` | `12 7` | Ban đầu $A=7, B=12$. Sau khi đổi: $A=12, B=7$. |
* **Gợi ý thuật toán:**
  * Cách 1 (Dùng biến trung gian): `tam = a; a = b; b = tam`
  * Cách 2 (Đặc quyền Python): `a, b = b, a`
  * Sau đó in: `print(a, b)`

---

### Bài 8 (Luyện tập): Đoàn tàu toa xe ghép số (`PYA-L01-P08`)

* **Bối cảnh:** Ga xe lửa có 2 toa xe mang 2 con số $a$ và $b$. Bác trưởng ga muốn nhìn thấy cả hai kết quả:
  1. Nếu ghép 2 toa tàu lại thành một dãy số (Ghép chữ).
  2. Nếu cộng giá trị của 2 toa tàu lại với nhau (Cộng số học).
* **Yêu cầu:** Nhập vào 2 số tự nhiên $a$ và $b$. Dòng 1 in ra kết quả khi ghép chuỗi chữ. Dòng 2 in ra kết quả khi cộng số.
* **Đầu vào (Input):** Nhập 2 số tự nhiên $a, b$ ($1 \le a, b \le 100$) trên 2 dòng.
* **Đầu ra (Output):**
  * Dòng 1: Chuỗi ghép dính $a$ và $b$.
  * Dòng 2: Tổng giá trị số học $a + b$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `25`<br>`30` | `2530`<br>`55` | Dòng 1 ghép chữ: `"25" + "30" = "2530"`.<br>Dòng 2 cộng số: $25 + 30 = 55$. |
* **Gợi ý thuật toán:**
  ```python
  s1 = input()
  s2 = input()
  print(s1 + s2)
  print(int(s1) + int(s2))
  ```

---

### Bài 9 (Luyện tập): Vé tham quan chùa hương (`PYA-L01-P09`)
*(Lấy cảm hứng từ Bài 4 Đề thi Tin học trẻ Thị xã Thái Hòa - Nghệ An)*

* **Bối cảnh:** Một đoàn khách chuẩn bị đi tham quan Chùa Hương Tích. Để lên chùa, đoàn phải đi thuyền và đi cáp treo:
  * Vé thuyền: người lớn $a$ nghìn đồng/người, trẻ em $b$ nghìn đồng/người.
  * Vé cáp treo: người lớn $x$ nghìn đồng/người, trẻ em $y$ nghìn đồng/người.
  * Đoàn khách có tổng cộng $n$ người, trong đó có $m$ trẻ em.
* **Yêu cầu:** Em hãy tính tổng số tiền (đơn vị nghìn đồng) cần chuẩn bị để mua toàn bộ vé thuyền và vé cáp treo cho cả đoàn khách.
* **Đầu vào (Input):** Gồm 6 dòng lần lượt chứa các số tự nhiên: $a, b, x, y, n, m$ ($0 < a, b, x, y < 100$; $0 \le m \le n < 100$).
* **Đầu ra (Output):** In ra một số nguyên duy nhất là tổng số tiền cần chuẩn bị.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `20`<br>`10`<br>`50`<br>`30`<br>`10`<br>`4` | `580` | - Số trẻ em: $4$, số người lớn: $10 - 4 = 6$ người.<br>- Tiền thuyền: $6 \times 20 + 4 \times 10 = 120 + 40 = 160$.<br>- Tiền cáp treo: $6 \times 50 + 4 \times 30 = 300 + 120 = 420$.<br>- Tổng tiền: $160 + 420 = 580$ nghìn đồng. |
* **Gợi ý thuật toán:**
  * Số người lớn: `nguoi_lon = n - m`
  * Tiền người lớn: `nguoi_lon * (a + x)`
  * Tiền trẻ em: `m * (b + y)`
  * Tổng tiền là tổng 2 khoản trên.

---

### Bài 10 (Luyện tập): Cỗ máy thời gian 3 thế hệ (`PYA-L01-P10`)

* **Bối cảnh:** Trong gia đình bạn Nam có 3 thế hệ: Nam, Bố của Nam và Ông nội của Nam.
  * Nam năm nay $a$ tuổi.
  * Bố hơn Nam $b$ tuổi.
  * Ông nội hơn Bố $c$ tuổi.
* **Yêu cầu:** Nhập vào 3 số tự nhiên $a, b, c$ lần lượt trên 3 dòng. Hãy tính và in ra:
  * Dòng 1: Tuổi của Bố.
  * Dòng 2: Tuổi của Ông nội.
  * Dòng 3: Tổng số tuổi của cả ba người.
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số nguyên $a, b, c$ ($1 \le a \le 20, 20 \le b \le 40, 20 \le c \le 40$).
* **Đầu ra (Output):** Gồm 3 dòng tương ứng với 3 yêu cầu của bài toán.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`30`<br>`25` | `40`<br>`65`<br>`115` | - Tuổi Nam: $10$.<br>- Tuổi Bố: $10 + 30 = 40$.<br>- Tuổi Ông: $40 + 25 = 65$.<br>- Tổng cả 3 người: $10 + 40 + 65 = 115$. |
* **Gợi ý thuật toán:** Sử dụng các biến liên kết:
  ```python
  nam = int(input())
  b = int(input())
  c = int(input())
  bo = nam + b
  ong = bo + c
  tong = nam + bo + ong
  print(bo)
  print(ong)
  print(tong)
  ```
