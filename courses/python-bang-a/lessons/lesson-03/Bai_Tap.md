# Hệ thống bài tập thực hành — bài 03: Công thức tính toán, hình học và đổi đơn vị

---

## Bảng ma trận bài tập (10 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L03-P01` | Mảnh vườn chữ nhật | `Cơ bản` | $1 \le a, b \le 10^4$ | Tính chu vi và diện tích hình chữ nhật |
| 02 | `PYA-L03-P02` | Khung tranh hình vuông | `Cơ bản` | $1 \le a \le 10^4$ | Tính chu vi và diện tích hình vuông |
| 03 | `PYA-L03-P03` | Chu vi tam giác abc | `Cơ bản` | $1 \le a, b, c \le 10^8$ | Tổng 3 cạnh tam giác, số lớn (THT hà tĩnh) |
| 04 | `PYA-L03-P04` | Cạnh còn lại của hình chữ nhật | `Cơ bản` | $10 < P \le 10^6, a < P // 2$ | Tìm cạnh từ chu vi và một cạnh (THT bắc giang) |
| 05 | `PYA-L03-P05` | Hồ cá sấu và đảo nhỏ | `Luyện tập` | $1 \le A, B, C \le 10^4$ | Hiệu hai diện tích hình học lồng nhau (THT lâm đồng) |
| 06 | `PYA-L03-P06` | Đổi giây sang giờ phút giây | `Luyện tập` | $0 \le S \le 10^8$ | Phân rã thời gian ngược dùng `// 3600`, `% 3600` |
| 07 | `PYA-L03-P07` | Lát gạch sân trường | `Luyện tập` | $1 \le D, R, K \le 1000$ | Số viên gạch lát diện tích hình chữ nhật |
| 08 | `PYA-L03-P08` | Thuận đi gặp ánh | `Luyện tập` | $0 \le x, y \le 10^9, 1 \le v \le 10^9$ | Vận tốc, khoảng cách và thời gian (THT từ sơn) |
| 09 | `PYA-L03-P09` | Rào quanh vườn hoa có cửa | `Luyện tập` | $1 \le a, b \le 10^4, 1 \le c < a$ | Chu vi trừ đi độ rộng lối vào cửa |
| 10 | `PYA-L03-P10` | Diện tích bồn hoa chữ thập | `Vận dụng` | $1 \le a, b \le 10^4$ | Phân tích hình học ghép, trừ phần giao nhau |

---

### Bài 1 (Cơ bản): Mảnh vườn chữ nhật (`PYA-L03-P01`)

* **Bối cảnh:** Bác Nông dân có một mảnh vườn trồng rau hình chữ nhật với chiều dài $a\text{ mét}$ và chiều rộng $b\text{ mét}$.
* **Yêu cầu:** Em hãy tính chu vi và diện tích của mảnh vườn đó.
* **Đầu vào (Input):** Gồm 2 dòng lần lượt chứa 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$).
* **Đầu ra (Output):** In ra trên một dòng 2 số nguyên cách nhau một dấu cách lần lượt là: Chu vi và Diện tích của mảnh vườn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`6` | `32 60` | Chu vi: $(10 + 6) \times 2 = 32$. Diện tích: $10 \times 6 = 60$. |
* **Gợi ý thuật toán:**
  ```python
  a = int(input())
  b = int(input())
  chu_vi = (a + b) * 2
  dien_tich = a * b
  print(chu_vi, dien_tich)
  ```

---

### Bài 2 (Cơ bản): Khung tranh hình vuông (`PYA-L03-P02`)

* **Bối cảnh:** Bạn Hoa vừa vẽ xong một bức tranh tuyệt đẹp hình vuông có cạnh là $a\text{ cm}$. Hoa muốn làm khung gỗ bọc viền xung quanh bức tranh và dán giấy kính lên toàn bộ bề mặt tranh.
* **Yêu cầu:** Hãy tính độ dài khung gỗ cần mua (chu vi) và diện tích giấy kính cần dán (diện tích).
* **Đầu vào (Input):** Một số tự nhiên $a$ ($1 \le a \le 10^4$).
* **Đầu ra (Output):** In ra 2 số nguyên cách nhau một khoảng trắng: Chu vi và Diện tích.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `8` | `32 64` |

---

### Bài 3 (Cơ bản): Chu vi tam giác abc (`PYA-L03-P03`)
*(Lấy cảm hứng từ Bài 3 Đề thi Tin học trẻ tỉnh Hà Tĩnh)*

* **Bối cảnh:** Trong giờ học hình học, thầy giáo cho 3 số tự nhiên $a, b, c$ lần lượt là độ dài 3 cạnh của một tam giác $ABC$.
* **Yêu cầu:** Em hãy lập trình tính và đưa ra chu vi của tam giác $ABC$.
* **Đầu vào (Input):** Ba dòng lần lượt ghi 3 số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^8$).
* **Đầu ra (Output):** In ra một số tự nhiên duy nhất là chu vi tam giác.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`4`<br>`5` | `12` | Chu vi: $3 + 4 + 5 = 12$. |

---

### Bài 4 (Cơ bản): Cạnh còn lại của hình chữ nhật (`PYA-L03-P04`)
*(Lấy cảm hứng từ Bài 6 Đề thi Tin học trẻ tỉnh Bắc Giang)*

* **Bối cảnh:** Một cái ao hình chữ nhật có một cạnh bằng $a\text{ mét}$ và có chu vi là $P\text{ mét}$ ($P$ là số chẵn).
* **Yêu cầu:** Em hãy tính và in ra độ dài của cạnh còn lại của hình chữ nhật.
* **Đầu vào (Input):** Gồm 2 dòng: dòng 1 chứa chu vi $P$ ($P$ chẵn, $P \le 10^6$), dòng 2 chứa độ dài cạnh đã biết $a$ ($1 \le a < P // 2$).
* **Đầu ra (Output):** Một số tự nhiên là độ dài cạnh còn lại.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `30`<br>`5` | `10` | Nửa chu vi là: $30 : 2 = 15$. Cạnh còn lại: $15 - 5 = 10$. |
* **Gợi ý thuật toán:** `P = int(input()); a = int(input()); print((P // 2) - a)`.

---

### Bài 5 (Luyện tập): Hồ cá sấu và đảo nhỏ (`PYA-L03-P05`)
*(Lấy cảm hứng từ Bài 2 Đề thi Tin học trẻ tỉnh Lâm Đồng)*

* **Bối cảnh:** Một trang trại nuôi cá sấu có một hồ nước hình vuông cạnh $A$. Ở chính giữa hồ, người ta xây một hòn đảo nhỏ hình chữ nhật có kích thước $B \times C$ để cá sấu bò lên phơi nắng (hòn đảo nằm trọn trong hồ nước và không chạm vào bờ hồ).
* **Yêu cầu:** Hãy tính diện tích phần mặt nước còn lại sau khi đã xây hòn đảo nhỏ.
* **Đầu vào (Input):** Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le B, C < A \le 10^4$).
* **Đầu ra (Output):** Một số nguyên duy nhất là diện tích mặt nước còn lại.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`3`<br>`4` | `88` | Diện tích hồ: $10 \times 10 = 100$. Diện tích đảo: $3 \times 4 = 12$.<br>Mặt nước còn lại: $100 - 12 = 88$. |
* **Gợi ý thuật toán:** `print(A * A - B * C)`.

---

### Bài 6 (Luyện tập): Đổi giây sang giờ phút giây (`PYA-L03-P06`)
*(Lấy cảm hứng từ Bài 7 Đề thi Tin học trẻ tỉnh Đồng Nai)*

* **Bối cảnh:** Một vệ tinh bay quanh trái đất hết $S$ giây. Nhân vật Robot muốn thông báo khoảng thời gian này dưới dạng dễ hiểu: gồm bao nhiêu Giờ, bao nhiêu Phút và bao nhiêu Giây.
* **Yêu cầu:** Nhập vào tổng số giây $S$. Hãy phân rã thành $H$ giờ, $M$ phút, $S$ giây.
* **Đầu vào (Input):** Một số nguyên $S$ ($0 \le S \le 10^8$).
* **Đầu ra (Output):** In ra ba số nguyên $H, M, S$ cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3665` | `1 1 5` | 3665 giây = 1 giờ (3600s) + 1 phút (60s) + 5 giây. |
* **Gợi ý thuật toán:**
  ```python
  tong_giay = int(input())
  gio = tong_giay // 3600
  giay_du = tong_giay % 3600
  phut = giay_du // 60
  giay = giay_du % 60
  print(gio, phut, giay)
  ```

---

### Bài 7 (Luyện tập): Lát gạch sân trường (`PYA-L03-P07`)

* **Bối cảnh:** Sân trường của trường Tiểu học iKHEDU có hình chữ nhật dài $D\text{ mét}$ và rộng $R\text{ mét}$. Nhà trường muốn lát gạch men cho toàn bộ sân trường bằng các viên gạch hình vuông có cạnh là $K\text{ mét}$ ($D$ và $R$ đều chia hết cho $K$).
* **Yêu cầu:** Tính số lượng viên gạch men cần dùng để lát kín mặt sân.
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số tự nhiên $D, R, K$ ($1 \le K \le R \le D \le 1000$).
* **Đầu ra (Output):** Một số nguyên duy nhất là số viên gạch.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `20`<br>`10`<br>`2` | `50` | Diện tích sân: $20 \times 10 = 200$. Diện tích 1 viên gạch: $2 \times 2 = 4$.<br>Số gạch cần: $200 : 4 = 50$ viên. |
* **Gợi ý thuật toán:** `(D * R) // (K * K)`.

---

### Bài 8 (Luyện tập): Thuận đi gặp ánh (`PYA-L03-P08`)
*(Lấy cảm hứng từ Bài 5 Đề thi Tin học trẻ Huyện Từ Sơn - Bắc Ninh)*

* **Bối cảnh:** Thuận và Ánh sống trên một con đường thẳng có các mốc tọa độ tính bằng kilomet. Thuận đang đứng ở vị trí $x$, còn Ánh đang đứng ở vị trí $y$ ($x < y$). Thuận bắt đầu đi xe đạp về phía nhà Ánh với vận tốc không đổi là $v\text{ km/h}$.
* **Biết rằng:** Khoảng cách $y - x$ chia hết cho vận tốc $v$.
* **Yêu cầu:** Sau bao nhiêu giờ thì Thuận sẽ gặp được Ánh?
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số tự nhiên $x, y, v$ ($0 \le x < y \le 10^9, 1 \le v \le 10^9$).
* **Đầu ra (Output):** Số giờ để Thuận gặp Ánh.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`70`<br>`15` | `4` | Khoảng cách giữa 2 bạn: $70 - 10 = 60\text{ km}$.<br>Thời gian gặp nhau: $60 : 15 = 4$ giờ. |
* **Gợi ý thuật toán:** `print((y - x) // v)`.

---

### Bài 9 (Luyện tập): Rào quanh vườn hoa có cửa (`PYA-L03-P09`)

* **Bối cảnh:** Bác thợ làm vườn có một vườn hoa hình chữ nhật kích thước chiều dài $a\text{ mét}$, chiều rộng $b\text{ mét}$. Bác muốn dựng một hàng rào thép gai xung quanh vườn hoa, nhưng chừa lại một lối đi ở một góc vườn làm cổng ra vào rộng đúng $c\text{ mét}$ (không rào cửa).
* **Biết giá thành làm rào:** Mỗi mét hàng rào tốn $15$ nghìn đồng.
* **Yêu cầu:** Tính tổng số tiền (nghìn đồng) bác thợ cần dùng để mua đủ rào thép.
* **Đầu vào (Input):** Ba dòng lần lượt là $a, b, c$ ($1 \le a, b \le 10^4, 1 \le c < (a + b) * 2$).
* **Đầu ra (Output):** Một số nguyên là số tiền (nghìn đồng).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12`<br>`8`<br>`2` | `570` | Chu vi cả vườn: $(12 + 8) \times 2 = 40\text{ m}$.<br>Độ dài rào cần mua: $40 - 2 = 38\text{ m}$.<br>Số tiền: $38 \times 15 = 570$ nghìn đồng. |
* **Gợi ý thuật toán:** `((a + b) * 2 - c) * 15`.

---

### Bài 10 (Vận dụng): Diện tích bồn hoa chữ thập (`PYA-L03-P10`)

* **Bối cảnh:** Trong công viên có một bồn hoa hình chữ thập (dấu cộng) được tạo thành bởi hai luống hoa hình chữ nhật đặt chồng lên nhau:
  * Một luống hoa nằm ngang có kích thước $a \times b$ ($a$ là chiều dài, $b$ là chiều rộng).
  * Một luống hoa nằm dọc có kích thước $b \times a$ ($b$ là chiều rộng, $a$ là chiều dài).
  * Hai luống hoa giao nhau ở chính giữa tạo thành một hình vuông kích thước $b \times b$.
* **Yêu cầu:** Em hãy tính diện tích thực tế của toàn bộ bồn hoa chữ thập này (không được tính trùng lặp phần diện tích giao nhau ở chính giữa).
* **Đầu vào (Input):** Nhập 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$) trên 2 dòng.
* **Đầu ra (Output):** Diện tích thực tế của bồn hoa.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`3` | `51` | - Luống ngang: $10 \times 3 = 30$.<br>- Luống dọc: $3 \times 10 = 30$.<br>- Phần giao nhau ở giữa: $3 \times 3 = 9$.<br>- Diện tích bồn hoa: $30 + 30 - 9 = 51$. |
* **Gợi ý thuật toán:**
  * Công thức gộp: $S = (a \times b) + (a \times b) - (b \times b) = 2ab - b^2$ hoặc $b \times (2a - b)$.
  * Code: `print(2 * a * b - b * b)`.
