# Hệ thống bài tập thực hành — bài 04: Rẽ nhánh có điều kiện với if-else

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L04-P01` | Kiểm tra số chẵn lẻ | `Cơ bản` | $0 \le N \le 10^9$ | Cú pháp `if - else` với phép `% 2` |
| 02 | `PYA-L04-P02` | Vé vào công viên | `Cơ bản` | $1 \le h \le 200$ | So sánh chiều cao $\ge 130\text{ cm}$ |
| 03 | `PYA-L04-P03` | Ai cao hơn? | `Cơ bản` | $50 \le a, b \le 200$ | So sánh 2 số, in tên bạn cao hơn |
| 04 | `PYA-L04-P04` | Số lớn nhất trong hai số | `Cơ bản` | $-10^9 \le a, b \le 10^9$ | Tìm max giữa 2 số nguyên bất kỳ |
| 05 | `PYA-L04-P05` | Chia kẹo công bằng | `Cơ bản` | $1 \le a, b \le 10^6$ | Kiểm tra tính chia hết `a % b == 0` |
| 06 | `PYA-L04-P06` | Điền phép tính lớn nhất | `Luyện tập` | $0 \le A \le 100$ | So sánh kết quả các phép tính (THT bắc giang) |
| 07 | `PYA-L04-P07` | Giảm giá siêu thị | `Luyện tập` | $1 \le N \le 10^6$ | Điều kiện giảm giá khi tổng tiền $\ge 500$K |
| 08 | `PYA-L04-P08` | Cặp số bằng nhau hay khác? | `Luyện tập` | $0 \le a, b \le 10^9$ | Ba trường hợp: Lớn hơn, nhỏ hơn hay bằng nhau |
| 09 | `PYA-L04-P09` | Trị tuyệt đối của một số | `Luyện tập` | $-10^9 \le N \le 10^9$ | Tự cài đặt hàm trị tuyệt đối đổi dấu số âm |
| 10 | `PYA-L04-P10` | Bác thợ mộc cắt gỗ | `Luyện tập` | $1 \le L, K \le 10^9$ | So sánh xem thanh gỗ có đủ dài để cắt không |
| 11 | `PYA-L04-P11` | Cạnh thứ tư hình chữ nhật | `Luyện tập` | $1 \le A, B, C \le 1000$ | Nhận diện 2 cặp cạnh bằng nhau (THT miền bắc) |
| 12 | `PYA-L04-P12` | Trò chơi oẳn tù tì | `Vận dụng` | $a, b \in \{1, 2, 3\}$ | Logic thắng thua vòng tròn quy ước số |

---

### Bài 1 (Cơ bản): Kiểm tra số chẵn lẻ (`PYA-L04-P01`)

* **Yêu cầu:** Nhập vào một số tự nhiên $N$. Nếu $N$ là số chẵn, in ra `CHAN`. Ngược lại in ra `LE`.
* **Input:** Một số tự nhiên $N$ ($0 \le N \le 10^9$).
* **Output:** Chuỗi `CHAN` hoặc `LE`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `18` | `CHAN` |
  | `7` | `LE` |
* **Gợi ý thuật toán:** `if N % 2 == 0: print("CHAN") else: print("LE")`.

---

### Bài 2 (Cơ bản): Vé vào công viên (`PYA-L04-P02`)

* **Bối cảnh:** Ở công viên nước, các bạn nhỏ có chiều cao từ $130\text{ cm}$ trở lên phải mua vé người lớn (`VE NGUOI LON`), còn dưới $130\text{ cm}$ được mua vé trẻ em (`VE TRE EM`).
* **Yêu cầu:** Nhập vào chiều cao $h$ (cm) của bạn nhỏ. In ra loại vé tương ứng.
* **Input:** Một số nguyên $h$ ($1 \le h \le 200$).
* **Output:** `VE NGUOI LON` hoặc `VE TRE EM`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `135` | `VE NGUOI LON` |
  | `120` | `VE TRE EM` |

---

### Bài 3 (Cơ bản): Ai cao hơn? (`PYA-L04-P03`)

* **Bối cảnh:** Bạn Minh cao $a\text{ cm}$, bạn Nam cao $b\text{ cm}$. Biết chiều cao của hai bạn không bằng nhau.
* **Yêu cầu:** Hãy in ra tên của bạn cao hơn (`Minh` hoặc `Nam`).
* **Input:** Hai số tự nhiên $a$ và $b$ trên 2 dòng ($50 \le a, b \le 200, a \ne b$).
* **Output:** Tên bạn cao hơn.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `142`<br>`138` | `Minh` |

---

### Bài 4 (Cơ bản): Số lớn nhất trong hai số (`PYA-L04-P04`)

* **Yêu cầu:** Nhập vào hai số nguyên $a$ và $b$. Hãy in ra số lớn hơn trong hai số đó. Nếu hai số bằng nhau thì in ra giá trị đó.
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Một số nguyên là giá trị lớn nhất.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `-15`<br>`8` | `8` |

---

### Bài 5 (Cơ bản): Chia kẹo công bằng (`PYA-L04-P05`)

* **Bối cảnh:** Cô giáo có $a$ chiếc kẹo muốn chia đều cho $b$ bạn học sinh sao cho tất cả các bạn đều nhận được số kẹo bằng nhau và không còn thừa cái nào.
* **Yêu cầu:** Kiểm tra xem số kẹo có chia đều được hay không? Nếu chia đều được thì in `YES`, ngược lại in `NO`.
* **Input:** Hai số nguyên dương $a, b$ ($1 \le a, b \le 10^6$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `20`<br>`4` | `YES` | 20 chia hết cho 4, mỗi bạn 5 cái kẹo. |
  | `20`<br>`6` | `NO` | 20 không chia hết cho 6 (dư 2). |

---

### Bài 6 (Luyện tập): Điền phép tính lớn nhất (`PYA-L04-P06`)
*(Lấy cảm hứng từ Bài 1 Đề thi THT tỉnh Bắc Giang)*

* **Bối cảnh:** Cho số tự nhiên $A$ và biểu thức sau: $A \text{ ? } A = B$.
* **Yêu cầu:** Hãy dùng một trong các phép tính $+$, $-$, $\times$ điền vào dấu $?$ để giá trị $B$ đạt được là **lớn nhất**. In ra số $B$ lớn nhất tìm được.
* **Input:** Một số tự nhiên $A$ ($0 \le A \le 100$).
* **Output:** Một số nguyên duy nhất là số $B$ lớn nhất.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3` | `9` | $3 + 3 = 6$, $3 - 3 = 0$, $3 \times 3 = 9$. Số lớn nhất là 9. |
  | `1` | `2` | $1 + 1 = 2$, $1 - 1 = 0$, $1 \times 1 = 1$. Số lớn nhất là 2! |
* **Gợi ý thuật toán:**
  * Chú ý bẫy: Với $A = 0$ hoặc $A = 1$, phép cộng $A + A$ lại cho kết quả lớn hơn phép nhân $A \times A$!
  * Tính 3 giá trị: `cong = A + A`, `tru = 0`, `nhan = A * A`.
  * Dùng lệnh: `print(max(cong, nhan))`.

---

### Bài 7 (Luyện tập): Giảm giá siêu thị (`PYA-L04-P07`)

* **Bối cảnh:** Siêu thị có chương trình khuyến mãi: Khách hàng mua đơn hàng có tổng giá trị từ $500$ nghìn đồng trở lên sẽ được giảm giá ngay $50$ nghìn đồng. Các đơn hàng dưới $500$ nghìn đồng giữ nguyên giá.
* **Yêu cầu:** Nhập vào tổng tiền đơn hàng $N$ (nghìn đồng). Hãy in ra số tiền thực tế khách hàng phải trả sau khi đã áp dụng khuyến mãi.
* **Input:** Một số nguyên dương $N$ ($1 \le N \le 10^6$).
* **Output:** Số tiền phải trả.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `620` | `570` | Được giảm 50 nghìn: $620 - 50 = 570$. |
  | `450` | `450` | Dưới 500 nghìn, không được giảm. |

---

### Bài 8 (Luyện tập): Cặp số bằng nhau hay khác? (`PYA-L04-P08`)

* **Yêu cầu:** Nhập vào 2 số nguyên $a$ và $b$. Hãy so sánh và in ra màn hình một trong ba thông báo:
  * `a LON HON b` (nếu $a > b$)
  * `a NHO HON b` (nếu $a < b$)
  * `HAI SO BANG NHAU` (nếu $a == b$)
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Một dòng thông báo theo đúng mẫu.

---

### Bài 9 (Luyện tập): Trị tuyệt đối của một số (`PYA-L04-P09`)

* **Bối cảnh:** Trị tuyệt đối $|N|$ của một số là khoảng cách từ số đó đến số 0 trên trục số:
  * Nếu $N \ge 0$, thì $|N| = N$.
  * Nếu $N < 0$, thì $|N| = -N$ (đổi dấu thành số dương).
* **Yêu cầu:** Nhập vào số nguyên $N$ (có thể là số âm). Không dùng hàm `abs()` có sẵn, hãy dùng cấu trúc `if - else` để in ra giá trị tuyệt đối của $N$.
* **Input:** Một số nguyên $N$ ($-10^9 \le N \le 10^9$).
* **Output:** Giá trị tuyệt đối của $N$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `-25` | `25` |
  | `10` | `10` |

---

### Bài 10 (Luyện tập): Bác thợ mộc cắt gỗ (`PYA-L04-P10`)

* **Bối cảnh:** Bác thợ mộc có một thanh gỗ dài $L\text{ cm}$. Bác cần cắt ra các đoạn gỗ nhỏ dài $K\text{ cm}$ để đóng bàn ghế.
* **Yêu cầu:**
  * Nếu thanh gỗ đủ dài để cắt được ít nhất một đoạn (nghĩa là $L \ge K$), hãy in ra số đoạn gỗ cắt được và phần gỗ thừa còn lại.
  * Nếu thanh gỗ quá ngắn ($L < K$), in ra chữ `KHONG DU`.
* **Input:** Hai số tự nhiên $L$ và $K$ trên 2 dòng ($1 \le L, K \le 10^9$).
* **Output:** Hai số cách nhau dấu cách `so_doan go_thua` hoặc in chữ `KHONG DU`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `17`<br>`5` | `3 2` |
  | `4`<br>`10` | `KHONG DU` |

---

### Bài 11 (Luyện tập): Cạnh thứ tư hình chữ nhật (`PYA-L04-P11`)
*(Lấy cảm hứng từ Bài 4 Đề thi THTA Khu vực Miền Bắc)*

* **Bối cảnh:** Một hình chữ nhật luôn có 4 cạnh tạo thành 2 cặp cạnh đối bằng nhau (2 chiều dài bằng nhau và 2 chiều rộng bằng nhau). Bạn Nam nhặt được 3 thanh gỗ có độ dài là $A, B, C$ và biết chắc chắn 3 thanh này là 3 cạnh của một hình chữ nhật.
* **Yêu cầu:** Em hãy tìm độ dài thanh gỗ thứ 4 còn thiếu để ghép vừa khít thành hình chữ nhật.
* **Input:** Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le A, B, C \le 1000$).
* **Output:** Độ dài cạnh thứ 4.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`5`<br>`3` | `5` | Đã có 2 cạnh bằng 3, vậy cạnh còn lại phải là 5. |
  | `8`<br>`6`<br>`8` | `6` | Cạnh còn lại là 6. |
* **Gợi ý thuật toán:**
  * Nếu $A == B$ thì cạnh còn lại là $C$.
  * Ngược lại nếu $A == C$ thì cạnh còn lại là $B$.
  * Ngược lại thì cạnh còn lại là $A$.
  *(Hoặc dùng phép XOR: `A ^ B ^ C`!)*

---

### Bài 12 (Vận dụng): Trò chơi oẳn tù tì (`PYA-L04-P12`)

* **Bối cảnh:** Hai bạn Tí và Tèo chơi trò Oẳn Tù Tì. Quy ước các lựa chọn bằng số:
  * `1`: Búa (Đấm)
  * `2`: Kéo
  * `3`: Bao (Lá)
* **Luật chơi:** Búa (1) thắng Kéo (2); Kéo (2) thắng Bao (3); Bao (3) thắng Búa (1). Nếu ra cùng số thì hòa nhau.
* **Yêu cầu:** Nhập vào lựa chọn của Tí và Tèo. Hãy in ra kết quả: `TI THANG`, `TEO THANG` hoặc `HOA`.
* **Input:** Hai số tự nhiên lần lượt là lựa chọn của Tí và Tèo ($1, 2, 3$).
* **Output:** `TI THANG`, `TEO THANG` hoặc `HOA`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1`<br>`2` | `TI THANG` | Tí ra Búa (1), Tèo ra Kéo (2) $\to$ Tí thắng. |
  | `1`<br>`3` | `TEO THANG` | Tí ra Búa (1), Tèo ra Bao (3) $\to$ Tèo thắng. |
  | `2`<br>`2` | `HOA` | Cả hai cùng ra Kéo. |
