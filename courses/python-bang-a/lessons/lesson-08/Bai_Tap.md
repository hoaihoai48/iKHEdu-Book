# Hệ thống bài tập thực hành — bài 08: Tách chữ số với chia nguyên và chia dư

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L10-P01` | Lấy chữ số đơn vị & chục | `Cơ bản` | $10 \le N \le 99$ | Thuần thục `% 10` và `// 10` với số 2 chữ số |
| 02 | `PYA-L10-P02` | Tổng chữ số của số 3 chữ số | `Cơ bản` | $100 \le N \le 999$ | Tách hàng trăm, chục, đơn vị |
| 03 | `PYA-L10-P03` | Tổng các chữ số của N | `Cơ bản` | $0 \le N \le 10^{18}$ | Vòng lặp `while n > 0` tính tổng chữ số |
| 04 | `PYA-L10-P04` | Đếm số lượng chữ số | `Cơ bản` | $0 \le N \le 10^{18}$ | Đếm số lượng chữ số có xử lý biên $N = 0$ |
| 05 | `PYA-L10-P05` | Tích các chữ số khác không | `Cơ bản` | $1 \le N \le 10^9$ | Bỏ qua chữ số 0 khi nhân dồn |
| 06 | `PYA-L10-P06` | Đếm chữ số chẵn và lẻ | `Luyện tập` | $1 \le N \le 10^{12}$ | Phân loại chẵn/lẻ cho từng chữ số |
| 07 | `PYA-L10-P07` | Chữ số lớn nhất & nhỏ nhất | `Luyện tập` | $1 \le N \le 10^{12}$ | Cập nhật `max` và `min` qua từng chữ số |
| 08 | `PYA-L10-P08` | Số đảo ngược | `Luyện tập` | $1 \le N \le 10^{12}$ | Thuật toán `dao = dao * 10 + cs` |
| 09 | `PYA-L10-P09` | Kiểm tra số đối xứng (palindrome) | `Luyện tập` | $1 \le N \le 10^{15}$ | So sánh số gốc và số đảo ngược |
| 10 | `PYA-L10-P10` | Số toàn chẵn hoặc toàn lẻ | `Luyện tập` | $1 \le N \le 10^{15}$ | Kiểm tra tính đồng nhất của toàn bộ chữ số |
| 11 | `PYA-L10-P11` | Số may mắn chứa số 7 | `Luyện tập` | $1 \le N \le 10^9$ | Kiểm tra sự tồn tại của một chữ số cụ thể |
| 12 | `PYA-L10-P12` | Đếm số lượng số đối xứng trong đoạn | `Vận dụng` | $1 \le A \le B \le 10^5$ | Kết hợp hàm kiểm tra số đối xứng trong đoạn $[A, B]$ |
| 13 | `PYA-L10-P13` | Căn bậc số học (digital root) | `Vận dụng` | $1 \le N \le 10^{18}$ | Tính tổng chữ số liên tục đến khi còn 1 chữ số |
| 14 | `PYA-L10-P14` | Số tăng giảm đẹp | `Thử thách` | $10 \le N \le 10^{12}$ | Kiểm tra các chữ số có tăng dần nghiêm ngặt từ trái qua phải |

---

### Bài 1 (Cơ bản): Lấy chữ số đơn vị & chục (`PYA-L10-P01`)

* **Yêu cầu:** Nhập một số nguyên dương $N$ có đúng 2 chữ số. Hãy in ra chữ số hàng chục và chữ số hàng đơn vị của $N$ trên cùng một dòng, cách nhau một khoảng trắng.
* **Input:** Một số nguyên $N$ ($10 \le N \le 99$).
* **Output:** Chữ số hàng chục, tiếp theo là chữ số hàng đơn vị.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `47` | `4 7` |
* **Gợi ý:** `chuc = n // 10`, `don_vi = n % 10`.

---

### Bài 2 (Cơ bản): Tổng chữ số của số 3 chữ số (`PYA-L10-P02`)

* **Yêu cầu:** Nhập một số nguyên dương $N$ có đúng 3 chữ số. Hãy tính tổng của 3 chữ số đó.
* **Input:** Một số tự nhiên $N$ ($100 \le N \le 999$).
* **Output:** Tổng 3 chữ số.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `358` | `16` | $3 + 5 + 8 = 16$. |

---

### Bài 3 (Cơ bản): Tổng các chữ số của N (`PYA-L10-P03`)

* **Yêu cầu:** Cho một số tự nhiên $N$ bất kỳ. Hãy tính tổng tất cả các chữ số cấu tạo nên số $N$.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^{18}$).
* **Output:** Tổng các chữ số của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `2024` | `8` | $2 + 0 + 2 + 4 = 8$. |
  | `0` | `0` | Chữ số 0 có tổng bằng 0. |

---

### Bài 4 (Cơ bản): Đếm số lượng chữ số (`PYA-L10-P04`)

* **Yêu cầu:** Cho số nguyên không âm $N$. Hãy cho biết số $N$ có bao nhiêu chữ số.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^{18}$).
* **Output:** Số lượng chữ số.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `123456` | `6` | Có 6 chữ số. |
  | `0` | `1` | Số 0 có đúng 1 chữ số. |
* **Lưu ý:** Chú ý xử lý trường hợp đặc biệt $N = 0$.

---

### Bài 5 (Cơ bản): Tích các chữ số khác không (`PYA-L10-P05`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tính tích của tất cả các chữ số **khác 0** của $N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Tích các chữ số khác 0.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `205` | `10` | Bỏ qua chữ số 0, tích là $2 \times 5 = 10$. |

---

### Bài 6 (Luyện tập): Đếm chữ số chẵn và lẻ (`PYA-L10-P06`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy đếm xem trong số $N$ có bao nhiêu chữ số chẵn (0, 2, 4, 6, 8) và bao nhiêu chữ số lẻ (1, 3, 5, 7, 9).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{12}$).
* **Output:** In hai số nguyên cách nhau một khoảng trắng: số lượng chữ số chẵn trước, số lượng chữ số lẻ sau.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `2035` | `2 2` | Chữ số chẵn: 2, 0 (2 số). Chữ số lẻ: 3, 5 (2 số). |

---

### Bài 7 (Luyện tập): Chữ số lớn nhất & nhỏ nhất (`PYA-L10-P07`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tìm chữ số lớn nhất và chữ số nhỏ nhất xuất hiện trong số $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^{12}$).
* **Output:** Chữ số lớn nhất, theo sau là chữ số nhỏ nhất, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `9418` | `9 1` | Chữ số lớn nhất là 9, nhỏ nhất là 1. |

---

### Bài 8 (Luyện tập): Số đảo ngược (`PYA-L10-P08`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy in ra số đảo ngược của $N$ (bỏ qua các chữ số 0 ở đầu nếu có sau khi đảo).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{12}$).
* **Output:** Số đảo ngược.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1234` | `4321` | Đảo ngược các chữ số. |
  | `2500` | `52` | Đảo ngược là 0052, giá trị số học là 52. |

---

### Bài 9 (Luyện tập): Kiểm tra số đối xứng (palindrome) (`PYA-L10-P09`)
*(Đề thi Tin học trẻ Bảng A)*

* **Bối cảnh:** Một số được gọi là số đối xứng (Palindrome) nếu đọc từ trái sang phải hay từ phải sang trái đều thu được số giống hệt nhau (ví dụ: $121$, $1331$, $5$, $88$).
* **Yêu cầu:** Nhập vào số tự nhiên $N$. Kiểm tra xem $N$ có phải số đối xứng không. Nếu có in `YES`, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^{15}$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `12321` | `YES` |
  | `1234` | `NO` |

---

### Bài 10 (Luyện tập): Số toàn chẵn hoặc toàn lẻ (`PYA-L10-P10`)

* **Bối cảnh:** Số "Toàn chẵn" là số mà mọi chữ số của nó đều là số chẵn. Số "Toàn lẻ" là số mà mọi chữ số của nó đều là số lẻ.
* **Yêu cầu:** Nhập số nguyên dương $N$. In ra `TOAN CHAN` nếu $N$ là số toàn chẵn, in `TOAN LE` nếu $N$ toàn lẻ, ngược lại in `BINH THUONG`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{15}$).
* **Output:** `TOAN CHAN`, `TOAN LE` hoặc `BINH THUONG`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2468` | `TOAN CHAN` |
  | `1395` | `TOAN LE` |
  | `2418` | `BINH THUONG` |

---

### Bài 11 (Luyện tập): Số may mắn chứa số 7 (`PYA-L10-P11`)

* **Yêu cầu:** Bé An coi số 7 là con số mang lại may mắn. Một số tự nhiên $N$ được gọi là "May mắn" nếu trong các chữ số của nó có ít nhất một chữ số 7. Cho số $N$, hãy kiểm tra xem $N$ có may mắn không. In `YES` nếu có, `NO` nếu không.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `372` | `YES` |
  | `2024` | `NO` |

---

### Bài 12 (Vận dụng): Đếm số lượng số đối xứng trong đoạn (`PYA-L10-P12`)

* **Yêu cầu:** Cho hai số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^5$). Hãy đếm xem có bao nhiêu số đối xứng nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số nguyên $A, B$ trên cùng một dòng.
* **Output:** Số lượng số đối xứng trong đoạn $[A, B]$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1 20` | `10` | Các số đối xứng là: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 (tổng cộng 10 số). |

---

### Bài 13 (Vận dụng): Căn bậc số học (digital root) (`PYA-L10-P13`)

* **Bối cảnh:** Căn bậc số học của một số tự nhiên là giá trị thu được sau khi cộng dồn liên tục các chữ số của nó cho đến khi chỉ còn lại đúng **một chữ số duy nhất**.
  Ví dụ: $9875 \to 9 + 8 + 7 + 5 = 29 \to 2 + 9 = 11 \to 1 + 1 = 2$. Căn bậc số học của 9875 là 2.
* **Yêu cầu:** Nhập vào số tự nhiên $N$. Hãy tìm căn bậc số học của $N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** Một chữ số duy nhất (từ 1 đến 9).
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `9875` | `2` |

---

### Bài 14 (Thử thách): Số tăng giảm đẹp (`PYA-L10-P14`)
*(Đề thi Tin học trẻ cấp Tỉnh/Thành phố)*

* **Bối cảnh:** Một số tự nhiên được gọi là:
  * **Số tăng dần:** Nếu mỗi chữ số đứng sau luôn lớn hơn chữ số đứng trước nó (ví dụ: $1379, 258$).
  * **Số giảm dần:** Nếu mỗi chữ số đứng sau luôn nhỏ hơn chữ số đứng trước nó (ví dụ: $9641, 852$).
* **Yêu cầu:** Cho số $N$. In ra `TANG` nếu $N$ là số tăng dần, in `GIAM` nếu $N$ là số giảm dần, và in `KHONG` nếu không thỏa mãn cả 2 tính chất trên.
* **Input:** Một số nguyên $N$ ($10 \le N \le 10^{12}$).
* **Output:** `TANG`, `GIAM` hoặc `KHONG`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `1379` | `TANG` |
  | `9520` | `GIAM` |
  | `1335` | `KHONG` (Có hai chữ số 3 bằng nhau) |
