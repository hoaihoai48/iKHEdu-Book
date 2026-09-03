# Hệ thống bài tập thực hành — bài 06: Điều kiện ghép với and-or-not

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L06-P01` | Số chẵn có hai chữ số | `Cơ bản` | $1 \le N \le 1000$ | Điều kiện kết hợp `and`: $10 \le N \le 99$ và chẵn |
| 02 | `PYA-L06-P02` | Bội chung của 3 và 5 | `Cơ bản` | $1 \le N \le 10^9$ | Chia hết đồng thời cho cả 3 và 5 |
| 03 | `PYA-L06-P03` | Ngày nghỉ cuối tuần | `Cơ bản` | $2 \le d \le 8$ | Điều kiện `or`: Thứ bảy hoặc chủ nhật |
| 04 | `PYA-L06-P04` | Điểm nằm trong hình chữ nhật | `Cơ bản` | $0 \le x, y \le 100$ | Kiểm tra tọa độ kẹp: $0 \le x \le W$ và $0 \le y \le H$ |
| 05 | `PYA-L06-P05` | Ba cạnh tam giác hợp lệ | `Cơ bản` | $1 \le a, b, c \le 10^9$ | Bất đẳng thức tam giác 3 điều kiện `and` |
| 06 | `PYA-L06-P06` | Kiểm tra năm nhuận | `Luyện tập` | $1 \le Y \le 10^5$ | Quy tắc năm nhuận thiên văn học kết hợp `and`/`or` |
| 07 | `PYA-L06-P07` | Số ngày trong tháng | `Luyện tập` | $1 \le M \le 12, 1 \le Y \le 10^5$ | Xác định 28, 29, 30 hay 31 ngày (THT bắc giang) |
| 08 | `PYA-L06-P08` | Tam giác vuông hay không? | `Luyện tập` | $1 \le a, b, c \le 10^4$ | Định lý pytago kết hợp 3 trường hợp cạnh huyền |
| 09 | `PYA-L06-P09` | Rút thẻ may mắn | `Luyện tập` | $1 \le N \le 10^9$ | Thẻ trúng thưởng chia hết cho 7 hoặc tận cùng bằng 7 |
| 10 | `PYA-L06-P10` | Ngày kế tiếp trong năm | `Luyện tập` | Ngày, tháng, năm hợp lệ | Xử lý chuyển ngày cuối tháng, cuối năm nhuận |
| 11 | `PYA-L06-P11` | Cặp đôi cùng dấu hay trái dấu | `Vận dụng` | $-10^9 \le a, b \le 10^9$ | Bắt bẫy số 0, cùng dương, cùng âm hoặc trái dấu |
| 12 | `PYA-L06-P12` | Giao nhau của hai đoạn thẳng | `Thử thách` | $-10^9 \le L_1, R_1, L_2, R_2 \le 10^9$ | Xác định hai đoạn trên trục số có giao nhau không |

---

### Bài 1 (Cơ bản): Số chẵn có hai chữ số (`PYA-L06-P01`)

* **Yêu cầu:** Nhập vào một số tự nhiên $N$. Kiểm tra xem $N$ có phải là **số chẵn có đúng hai chữ số** hay không? Nếu đúng in `YES`, ngược lại in `NO`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `24` | `YES` | 24 là số chẵn và có 2 chữ số. |
  | `8` | `NO` | 8 là số chẵn nhưng chỉ có 1 chữ số. |
  | `35` | `NO` | 35 có 2 chữ số nhưng là số lẻ. |
* **Gợi ý thuật toán:** `if (10 <= N <= 99) and (N % 2 == 0): print("YES") else: print("NO")`.

---

### Bài 2 (Cơ bản): Bội chung của 3 và 5 (`PYA-L06-P02`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$. Nếu $N$ chia hết cho cả 3 và 5 thì in `FIZZBUZZ`. Ngược lại in `KHONG`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** `FIZZBUZZ` hoặc `KHONG`.
* **Gợi ý:** `if N % 3 == 0 and N % 5 == 0: print("FIZZBUZZ") else: print("KHONG")`.

---

### Bài 3 (Cơ bản): Ngày nghỉ cuối tuần (`PYA-L06-P03`)

* **Bối cảnh:** Quy ước các ngày trong tuần bằng số: `2` (Thứ Hai), `3` (Thứ Ba), ..., `7` (Thứ Bảy), `8` (Chủ Nhật).
* **Yêu cầu:** Nhập vào một số nguyên $d$ đại diện cho một ngày. Nếu $d$ là Thứ Bảy hoặc Chủ Nhật thì in `NGHI HOC`, ngược lại in `DI HOC`.
* **Input:** Một số nguyên $d$ ($2 \le d \le 8$).
* **Output:** `NGHI HOC` hoặc `DI HOC`.
* **Gợi ý:** `if d == 7 or d == 8: print("NGHI HOC") else: print("DI HOC")`.

---

### Bài 4 (Cơ bản): Điểm nằm trong hình chữ nhật (`PYA-L06-P04`)

* **Bối cảnh:** Trong mặt phẳng tọa độ, một hình chữ nhật có góc dưới-trái tại $(0, 0)$ và góc trên-phải tại $(W, H)$.
* **Yêu cầu:** Nhập vào $W, H$ và tọa độ của một điểm $(x, y)$. Kiểm tra xem điểm $(x, y)$ có nằm bên trong hoặc trên mép biên của hình chữ nhật hay không? Nếu có in `TRONG`, ngược lại in `NGOAI`.
* **Input:** Bốn số tự nhiên $W, H, x, y$ trên 4 dòng ($1 \le W, H \le 1000, 0 \le x, y \le 1000$).
* **Output:** `TRONG` hoặc `NGOAI`.
* **Gợi ý:** `if (0 <= x <= W) and (0 <= y <= H): print("TRONG") else: print("NGOAI")`.

---

### Bài 5 (Cơ bản): Ba cạnh tam giác hợp lệ (`PYA-L06-P05`)
*(Lấy cảm hứng từ Bài 11 Đề thi THT Toàn quốc)*

* **Yêu cầu:** Nhập vào 3 số tự nhiên $a, b, c$ trên 3 dòng. Kiểm tra xem 3 số này có thể tạo thành độ dài 3 cạnh của một tam giác hay không? Nếu có in `HOP LE`, ngược lại in `KHONG HOP LE`.
* **Input:** Ba số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^9$).
* **Output:** `HOP LE` hoặc `KHONG HOP LE`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`4`<br>`5` | `HOP LE` | $3+4>5$, $3+5>4$, $4+5>3$ đều đúng. |
  | `2`<br>`3`<br>`6` | `KHONG HOP LE` | $2 + 3 = 5 < 6$ (Sai bất đẳng thức tam giác). |

---

### Bài 6 (Luyện tập): Kiểm tra năm nhuận (`PYA-L06-P06`)

* **Yêu cầu:** Nhập vào một năm dương lịch $Y$. Hãy in ra `NAM NHUAN` nếu năm đó là năm nhuận, ngược lại in `NAM THUONG`.
* **Quy tắc:** Năm nhuận là năm chia hết cho 400, HOẶC chia hết cho 4 nhưng không chia hết cho 100.
* **Input:** Một số tự nhiên $Y$ ($1 \le Y \le 10^5$).
* **Output:** `NAM NHUAN` hoặc `NAM THUONG`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2024` | `NAM NHUAN` |
  | `1900` | `NAM THUONG` |
  | `2000` | `NAM NHUAN` |

---

### Bài 7 (Luyện tập): Số ngày trong tháng (`PYA-L06-P07`)
*(Lấy cảm hứng từ Bài 114, 115 Đề thi THT Bắc Giang)*

* **Yêu cầu:** Nhập vào tháng $M$ ($1 \le M \le 12$) và năm $Y$ ($1 \le Y \le 10^5$). Hãy in ra số lượng ngày của tháng đó trong năm $Y$.
* **Biết rằng:**
  * Tháng 1, 3, 5, 7, 8, 10, 12 có đúng 31 ngày.
  * Tháng 4, 6, 9, 11 có đúng 30 ngày.
  * Tháng 2: có 29 ngày nếu $Y$ là năm nhuận, có 28 ngày nếu $Y$ là năm thường.
* **Input:** Hai dòng lần lượt là $M$ và $Y$.
* **Output:** Một số nguyên duy nhất là số ngày của tháng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2`<br>`2024` | `29` |
  | `2`<br>`2023` | `28` |
  | `4`<br>`2025` | `30` |

---

### Bài 8 (Luyện tập): Tam giác vuông hay không? (`PYA-L06-P08`)

* **Bối cảnh:** Theo định lý Pytago, tam giác có 3 cạnh $a, b, c$ là tam giác vuông nếu bình phương một cạnh bằng tổng bình phương hai cạnh còn lại ($a^2 + b^2 = c^2$ hoặc $a^2 + c^2 = b^2$ hoặc $b^2 + c^2 = a^2$).
* **Yêu cầu:** Cho 3 số dương $a, b, c$. Nếu chúng tạo thành một tam giác vuông thì in `VUONG`, ngược lại in `KHONG VUONG`.
* **Input:** Ba số nguyên $a, b, c$ ($1 \le a, b, c \le 10^4$).
* **Output:** `VUONG` hoặc `KHONG VUONG`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`4`<br>`5` | `VUONG` | $3^2 + 4^2 = 9 + 16 = 25 = 5^2$. |

---

### Bài 9 (Luyện tập): Rút thẻ may mắn (`PYA-L06-P09`)
*(Lấy cảm hứng từ Bài 113 Đề thi THT Nghệ An – Khánh Hòa)*

* **Bối cảnh:** Trong hội chợ xuân, mỗi bạn nhỏ được bốc một chiếc thẻ có ghi một số tự nhiên $N$. Chiếc thẻ được coi là "Thẻ Trúng Thưởng" nếu:
  * Số $N$ chia hết cho 7, **HOẶC**
  * Số $N$ có chữ số tận cùng là 7.
* **Yêu cầu:** Nhập vào số $N$ trên thẻ. In ra `TRUNG THUONG` nếu trúng thưởng, ngược lại in `CHUC MAY MAN LAN SAU`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Thông báo tương ứng.
* **Gợi ý thuật toán:** `if N % 7 == 0 or N % 10 == 7: print("TRUNG THUONG")`.

---

### Bài 10 (Luyện tập): Ngày kế tiếp trong năm (`PYA-L06-P10`)

* **Bối cảnh:** Nhập vào một ngày hợp lệ gồm 3 số: ngày $D$, tháng $M$, năm $Y$.
* **Yêu cầu:** Hãy tính và in ra ngày, tháng, năm của **ngày kế tiếp ngay sau đó**.
* **Input:** Ba số tự nhiên $D, M, Y$ trên 3 dòng.
* **Output:** Ba số nguyên cách nhau một dấu cách `D_tiep M_tiep Y_tiep`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `31`<br>`12`<br>`2024` | `1 1 2025` | Ngày cuối năm chuyển sang ngày đầu năm mới! |
  | `28`<br>`2`<br>`2024` | `29 2 2024` | Năm 2024 là năm nhuận nên tháng 2 có ngày 29. |
  | `28`<br>`2`<br>`2023` | `1 3 2023` | Năm 2023 thường nên sau 28/2 là sang 1/3. |

---

### Bài 11 (Vận dụng): Cặp đôi cùng dấu hay trái dấu (`PYA-L06-P11`)

* **Yêu cầu:** Nhập vào hai số nguyên $a$ và $b$ (có thể âm, dương hoặc bằng 0).
  * In `CO SO KHONG` nếu có ít nhất một số bằng 0 ($a == 0$ hoặc $b == 0$).
  * In `CUNG DAU` nếu cả hai số cùng mang dấu dương hoặc cùng mang dấu âm ($a \times b > 0$).
  * In `TRAI DAU` nếu một số dương và một số âm ($a \times b < 0$).
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Thông báo theo quy định.

---

### Bài 12 (Thử thách): Giao nhau của hai đoạn thẳng (`PYA-L06-P12`)

* **Bối cảnh:** Trên trục số thực, đoạn thẳng thứ nhất nối từ điểm $L_1$ đến $R_1$ ($L_1 \le R_1$). Đoạn thẳng thứ hai nối từ điểm $L_2$ đến $R_2$ ($L_2 \le R_2$).
* **Yêu cầu:** Em hãy kiểm tra xem hai đoạn thẳng này có điểm chung (giao nhau) hay không?
  * Nếu có giao nhau: in ra `GIAO NHAU` và độ dài của đoạn giao nhau đó.
  * Nếu không giao nhau: in `KHONG GIAO NHAU`.
* **Input:** Bốn số nguyên $L_1, R_1, L_2, R_2$ trên 4 dòng ($-10^9 \le L_1 \le R_1 \le 10^9, -10^9 \le L_2 \le R_2 \le 10^9$).
* **Output:** `GIAO NHAU [do_dai]` hoặc `KHONG GIAO NHAU`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1`<br>`6`<br>`4`<br>`9` | `GIAO NHAU 2` | Đoạn giao nhau từ 4 đến 6, độ dài: $6 - 4 = 2$. |
  | `1`<br>`3`<br>`5`<br>`8` | `KHONG GIAO NHAU` | Hai đoạn rời nhau hoàn toàn. |
* **Gợi ý thuật toán:**
  * Điểm bắt đầu giao: `start = max(L1, L2)`
  * Điểm kết thúc giao: `end = min(R1, R2)`
  * Nếu `start <= end`: in `GIAO NHAU`, độ dài là `end - start`. Ngược lại in `KHONG GIAO NHAU`.
