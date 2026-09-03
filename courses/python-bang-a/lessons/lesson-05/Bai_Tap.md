# Hệ thống bài tập thực hành — bài 05: Rẽ nhánh nhiều hướng với elif

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L05-P01` | Đèn giao thông ngã tư | `Cơ bản` | Ký tự `D, V, X` | Cấu trúc 3 nhánh `if - elif - else` cơ bản |
| 02 | `PYA-L05-P02` | Dấu của số nguyên | `Cơ bản` | $-10^9 \le N \le 10^9$ | Phân biệt: Dương (`DUONG`), âm (`AM`), không (`KHONG`) |
| 03 | `PYA-L05-P03` | Số lớn nhất trong ba số | `Cơ bản` | $-10^9 \le a, b, c \le 10^9$ | Kỹ thuật tìm max 3 số hoặc dùng lính canh |
| 04 | `PYA-L05-P04` | Xếp loại học lực | `Cơ bản` | $0.0 \le diem \le 10.0$ | Phân loại bậc thang điểm số số thực |
| 05 | `PYA-L05-P05` | Vé gửi xe bến bãi | `Cơ bản` | Loại xe $1, 2, 3$ | Tính tiền gửi xe theo từng mức quy định |
| 06 | `PYA-L05-P06` | Mario cứu công chúa | `Luyện tập` | $1 \le K, P, N \le 1000$ | Mô phỏng di chuyển năng lượng (THT củ chi) |
| 07 | `PYA-L05-P07` | Tính cước taxi bậc thang | `Luyện tập` | $1 \le km \le 100$ | Bài toán tính cước lũy tiến kinh điển |
| 08 | `PYA-L05-P08` | Phân loại tam giác | `Luyện tập` | $1 \le a, b, c \le 1000$ | Phân biệt tam giác đều, cân hay thường |
| 09 | `PYA-L05-P09` | Thuận đi tìm ánh đa vận tốc | `Luyện tập` | $0 \le x, y \le 10^9, v \ge 0$ | Bắt bẫy $x == y$ hoặc $v == 0$ (THT từ sơn) |
| 10 | `PYA-L05-P10` | Thứ mấy trong tuần? | `Luyện tập` | $1 \le k \le 365$ | Đổi số ngày sang thứ hai đến chủ nhật |
| 11 | `PYA-L05-P11` | Cửa hàng bánh bột lọc khuyến mãi | `Luyện tập` | $1 \le N \le 1000$ | Bài toán mua theo gói bậc thang (THT Bảng A) |
| 12 | `PYA-L05-P12` | Bốn mùa trong năm | `Vận dụng` | $1 \le thang \le 12$ | Gom nhóm nhiều giá trị vào các mùa xuân, hạ, thu, đông |

---

### Bài 1 (Cơ bản): Đèn giao thông ngã tư (`PYA-L05-P01`)

* **Yêu cầu:** Nhập vào một chữ cái in hoa đại diện cho màu đèn: `D` (Đỏ), `V` (Vàng), `X` (Xanh).
  * Nếu là `D`: in ra `DUNG LAI`.
  * Nếu là `V`: in ra `DI CHAM`.
  * Nếu là `X`: in ra `DUOC DI`.
* **Input:** Một ký tự `D`, `V` hoặc `X`.
* **Output:** Thông báo tương ứng.

---

### Bài 2 (Cơ bản): Dấu của số nguyên (`PYA-L05-P02`)

* **Yêu cầu:** Nhập vào số nguyên $N$. Hãy in ra:
  * `DUONG` nếu $N > 0$.
  * `AM` nếu $N < 0$.
  * `KHONG` nếu $N == 0$.
* **Input:** Một số nguyên $N$ ($-10^9 \le N \le 10^9$).
* **Output:** Chuỗi kết quả.

---

### Bài 3 (Cơ bản): Số lớn nhất trong ba số (`PYA-L05-P03`)

* **Yêu cầu:** Nhập vào 3 số nguyên $a, b, c$ mỗi số trên một dòng. Hãy tìm và in ra số có giá trị lớn nhất trong 3 số đó.
* **Input:** Ba số nguyên $a, b, c$ ($-10^9 \le a, b, c \le 10^9$).
* **Output:** Một số nguyên duy nhất là số lớn nhất.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `15`<br>`28`<br>`9` | `28` |
* **Gợi ý thuật toán:** `print(max(a, b, c))`.

---

### Bài 4 (Cơ bản): Xếp loại học lực (`PYA-L05-P04`)

* **Yêu cầu:** Nhập vào điểm trung bình môn Tin học của một bạn nhỏ (số thực $0.0 \le diem \le 10.0$).
  * Điểm $\ge 9.0$: in `XUAT SAC`.
  * Điểm $\ge 8.0$ và $< 9.0$: in `GIOI`.
  * Điểm $\ge 6.5$ và $< 8.0$: in `KHA`.
  * Điểm $< 6.5$: in `CAN CO GANG`.
* **Input:** Một số thực $diem$.
* **Output:** Xếp loại tương ứng.

---

### Bài 5 (Cơ bản): Vé gửi xe bến bãi (`PYA-L05-P05`)

* **Bối cảnh:** Bãi giữ xe thông minh quy định giá vé theo loại phương tiện:
  * Loại `1` (Xe đạp): giá $2$ nghìn đồng.
  * Loại `2` (Xe máy): giá $5$ nghìn đồng.
  * Loại `3` (Xe ô tô): giá $30$ nghìn đồng.
  * Các loại khác: in `LOI PHUONG TIEN`.
* **Input:** Một số nguyên mã loại xe.
* **Output:** Số tiền gửi xe hoặc chữ `LOI PHUONG TIEN`.

---

### Bài 6 (Luyện tập): Mario cứu công chúa (`PYA-L05-P06`)
*(Lấy cảm hứng từ Bài 3 Đề thi THT Huyện Củ Chi - TP.HCM)*

* **Bối cảnh:** Mario có $K$ năng lượng, Công chúa có $P$ năng lượng. Chiếc cầu thang ngăn cách giữa hai người có đỉnh cao $N$ bậc: Mario đứng ở chân cầu thang bên trái (cần đi lên $N$ bậc và đi xuống $N$ bậc), Công chúa đứng ở chân cầu thang bên phải (cần đi lên $N$ bậc).
  * Mỗi bậc thang Mario đi tốn $1$ năng lượng.
  * Mỗi bậc thang Công chúa đi tốn $2$ năng lượng.
* **Yêu cầu:** Hỏi với mức năng lượng hiện có, Mario và Công chúa có thể gặp được nhau ở một điểm nào đó trên cầu thang hay không? Nếu gặp được in `YES`, ngược lại in `NO`.
* **Biết rằng:** Tổng số bậc cầu thang từ chân bên này sang chân bên kia là $2N$. Để gặp nhau, tổng số bậc mà Mario leo được cộng với tổng số bậc mà Công chúa leo được phải $\ge 2N$.
* **Input:** Ba số tự nhiên $K, P, N$ ($1 \le K, P, N \le 1000$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`3`<br>`2` | `YES` | Cầu thang $2N = 4$ bậc. Mario đi được $\min(3, 4) = 3$ bậc. Công chúa có 3 năng lượng đi được $3 // 2 = 1$ bậc. Tổng số bậc đi được là $3 + 1 = 4 \ge 4 \implies$ Gặp nhau! |
* **Gợi ý thuật toán:**
  * Bậc Mario đi được: `bac_mario = min(K, 2 * N)`
  * Bậc Công chúa đi được: `bac_cong_chua = min(P // 2, 2 * N)`
  * Nếu `bac_mario + bac_cong_chua >= 2 * N` in `YES`, ngược lại in `NO`.

---

### Bài 7 (Luyện tập): Tính cước taxi bậc thang (`PYA-L05-P07`)

* **Bối cảnh:** Hãng taxi "Rùa Con" tính cước đi xe như sau:
  * Giá mở cửa (cho $1\text{ km}$ đầu tiên): $10$ nghìn đồng.
  * Từ kilomet thứ 2 đến kilomet thứ 10: giá $8$ nghìn đồng mỗi km.
  * Từ kilomet thứ 11 trở đi: giá $6$ nghìn đồng mỗi km.
* **Yêu cầu:** Nhập vào số kilomet $N$ mà khách đã đi (số nguyên $N \ge 1$). Tính tổng số tiền cước (nghìn đồng).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 100$).
* **Output:** Tổng tiền cước taxi.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1` | `10` | Đúng 1 km đầu: 10 nghìn. |
  | `5` | `42` | 1 km đầu: 10k + 4 km tiếp theo: $4 \times 8 = 32$k $\implies 10 + 32 = 42$k. |
  | `12` | `94` | 1 km đầu (10k) + 9 km tiếp theo ($9 \times 8 = 72$k) + 2 km cuối ($2 \times 6 = 12$k) $\implies 10 + 72 + 12 = 94$k. |
* **Gợi ý thuật toán:** Dùng `if - elif - else` chia 3 nấc: $N = 1$, $1 < N \le 10$, và $N > 10$.

---

### Bài 8 (Luyện tập): Phân loại tam giác (`PYA-L05-P08`)

* **Bối cảnh:** Cho 3 số tự nhiên $a, b, c$ đã đảm bảo là độ dài 3 cạnh của một tam giác hợp lệ.
* **Yêu cầu:** Hãy phân loại tam giác đó:
  * Nếu 3 cạnh bằng nhau ($a == b == c$): in `TAM GIAC DEU`.
  * Nếu có 2 cạnh bằng nhau ($a == b$ hoặc $b == c$ hoặc $c == a$): in `TAM GIAC CAN`.
  * Các trường hợp còn lại: in `TAM GIAC THUONG`.
* **Input:** Ba số tự nhiên $a, b, c$ trên 3 dòng ($1 \le a, b, c \le 1000$).
* **Output:** Tên phân loại tam giác.

---

### Bài 9 (Luyện tập): Thuận đi tìm ánh đa vận tốc (`PYA-L05-P09`)
*(Lấy cảm hứng từ Bài 5 Đề thi THT Huyện Từ Sơn)*

* **Bối cảnh:** Thuận đứng ở vị trí $x$, Ánh đứng ở vị trí $y$. Thuận đi về phía Ánh với vận tốc $v\text{ km/h}$.
* **Yêu cầu:** Hãy phân tích các tình huống:
  * Nếu $x == y$: in `DA GAP NHAU` (vì đang đứng cùng một chỗ).
  * Nếu $x \ne y$ nhưng $v == 0$: in `KHONG THE GAP` (vì Thuận đứng yên).
  * Nếu $x \ne y$ và $v > 0$:
    * Nếu khoảng cách $|y - x|$ chia hết cho $v$: in ra số giờ để gặp nhau.
    * Nếu không chia hết: in `GAP NHAU LE GIO`.
* **Input:** Ba số nguyên $x, y, v$ ($-10^9 \le x, y \le 10^9, 0 \le v \le 10^9$).
* **Output:** Thông báo tương ứng hoặc số giờ nguyên.

---

### Bài 10 (Luyện tập): Thứ mấy trong tuần? (`PYA-L05-P10`)

* **Bối cảnh:** Ngày mùng 1 tháng Giêng là ngày **Thứ Hai**.
* **Yêu cầu:** Cho biết ngày thứ $K$ trong năm đó là thứ mấy?
  * Biết rằng: ngày 1 là Thứ Hai, ngày 2 là Thứ Ba, ..., ngày 7 là Chủ Nhật, ngày 8 lại quay về Thứ Hai.
* **Input:** Một số tự nhiên $K$ ($1 \le K \le 365$).
* **Output:** In ra một trong các chuỗi: `THU HAI`, `THU BA`, `THU TU`, `THU NAM`, `THU SAU`, `THU BAY`, `CHU NHAT`.
* **Gợi ý thuật toán:** Tính số dư `du = K % 7`. Nếu `du == 1`: Thứ Hai, `du == 2`: Thứ Ba, ..., `du == 0`: Chủ Nhật.

---

### Bài 11 (Luyện tập): Cửa hàng bánh bột lọc khuyến mãi (`PYA-L05-P11`)

* **Bối cảnh:** Cửa hàng bánh bột lọc bán bánh với chương trình ưu đãi số lượng:
  * Mua dưới 10 cái: giá $5$ nghìn đồng/cái.
  * Mua từ 10 đến 49 cái: giá $4$ nghìn đồng/cái.
  * Mua từ 50 cái trở lên: giá chỉ còn $3$ nghìn đồng/cái.
* **Yêu cầu:** Nhập vào số lượng bánh $N$ mà khách muốn mua. Tính tổng số tiền khách phải trả.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** Tổng số tiền (nghìn đồng).

---

### Bài 12 (Vận dụng): Bốn mùa trong năm (`PYA-L05-P12`)

* **Bối cảnh:** Một năm có 12 tháng được chia thành 4 mùa:
  * **Mùa Xuân:** Tháng 1, 2, 3.
  * **Mùa Hạ (Hè):** Tháng 4, 5, 6.
  * **Mùa Thu:** Tháng 7, 8, 9.
  * **Mùa Đông:** Tháng 10, 11, 12.
* **Yêu cầu:** Nhập vào một số nguyên $M$.
  * Nếu $1 \le M \le 12$, hãy in ra tên mùa tương ứng (`XUAN`, `HA`, `THU`, `DONG`).
  * Nếu $M$ không nằm từ 1 đến 12, in ra `THANG KHONG HOP LE`.
* **Input:** Một số nguyên $M$ ($-100 \le M \le 100$).
* **Output:** Tên mùa hoặc thông báo lỗi.
