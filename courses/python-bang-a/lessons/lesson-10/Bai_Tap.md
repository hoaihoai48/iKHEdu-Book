# Hệ thống bài tập thực hành — bài 10: Đếm số theo quy luật và số đặc biệt

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L12-P01` | Đếm số chia hết cho K | `Cơ bản` | $1 \le N, K \le 10^9$ | Phép chia nguyên $N // K$ chuẩn xác |
| 02 | `PYA-L12-P02` | Đếm số lẻ trong đoạn | `Cơ bản` | $1 \le A \le B \le 10^9$ | Đếm số lượng số lẻ trong đoạn $[A, B]$ |
| 03 | `PYA-L12-P03` | Kiểm tra số hoàn hảo | `Cơ bản` | $1 \le N \le 10^6$ | Tính tổng ước nhỏ hơn $N$ và so sánh |
| 04 | `PYA-L12-P04` | Số armstrong ba chữ số | `Cơ bản` | $100 \le N \le 999$ | Kiểm tra $a^3 + b^3 + c^3 = N$ |
| 05 | `PYA-L12-P05` | Tìm tất cả số hoàn hảo nhỏ hơn N | `Cơ bản` | $1 \le N \le 10^4$ | Vòng lặp tìm số hoàn hảo (6, 28, 496...) |
| 06 | `PYA-L12-P06` | Đếm bội của 3 nhưng không chia hết cho 5 | `Luyện tập` | $1 \le A \le B \le 10^{12}$ | Áp dụng trừ tập hợp: Chia 3 trừ chia 15 |
| 07 | `PYA-L12-P07` | Đếm số chia hết cho 2 hoặc 3 | `Luyện tập` | $1 \le N \le 10^{12}$ | Nguyên lý bao hàm - loại trừ $\mathcal{O}(1)$ |
| 08 | `PYA-L12-P08` | Cặp số thân thiết | `Luyện tập` | $1 \le A, B \le 10^5$ | Kiểm tra tổng ước của $A$ bằng $B$ và ngược lại |
| 09 | `PYA-L12-P09` | Số phong phú (abundant number) | `Luyện tập` | $1 \le N \le 10^6$ | Kiểm tra tổng ước thực sự lớn hơn $N$ |
| 10 | `PYA-L12-P10` | Đếm số không chứa chữ số 0 | `Luyện tập` | $1 \le N \le 10^6$ | Đếm các số không chứa chữ số 0 |
| 11 | `PYA-L12-P11` | Đếm số chính phương trong đoạn | `Vận dụng` | $1 \le A \le B \le 10^{14}$ | Đếm số lượng chính phương bằng $\lfloor\sqrt{B}\rfloor - \lfloor\sqrt{A-1}\rfloor$ |
| 12 | `PYA-L12-P12` | Số tự mãn (narcissistic number K chữ số) | `Thử thách` | $1 \le N \le 10^9$ | Tổng lũy thừa bậc $K$ của các chữ số bằng chính nó |

---

### Bài 1 (Cơ bản): Đếm số chia hết cho K (`PYA-L12-P01`)

* **Yêu cầu:** Cho 2 số nguyên dương $N$ và $K$. Hãy đếm xem trong các số từ $1$ đến $N$, có bao nhiêu số chia hết cho $K$.
* **Input:** Hai số nguyên $N$ và $K$ ($1 \le N, K \le 10^9$) cách nhau bởi khoảng trắng.
* **Output:** Một số nguyên duy nhất là số lượng các số chia hết cho $K$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `20 3` | `6` | Có 6 số: 3, 6, 9, 12, 15, 18. |
* **Gợi ý:** Sử dụng công thức `N // K`.

---

### Bài 2 (Cơ bản): Đếm số lẻ trong đoạn (`PYA-L12-P02`)

* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^9$). Hãy đếm xem có bao nhiêu số lẻ nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số $A, B$ trên cùng một dòng.
* **Output:** Số lượng số lẻ.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3 8` | `3` | Có 3 số lẻ là: 3, 5, 7. |

---

### Bài 3 (Cơ bản): Kiểm tra số hoàn hảo (`PYA-L12-P03`)

* **Bối cảnh:** Một số nguyên dương $N$ được gọi là "Số hoàn hảo" nếu tổng tất cả các ước số nguyên dương nhỏ hơn $N$ bằng chính số $N$.
* **Yêu cầu:** Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số hoàn hảo không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `6` | `YES` |
  | `10` | `NO` |

---

### Bài 4 (Cơ bản): Số armstrong ba chữ số (`PYA-L12-P04`)

* **Bối cảnh:** Số Armstrong có 3 chữ số là số tự nhiên có dạng $\overline{abc}$ thỏa mãn $a^3 + b^3 + c^3 = \overline{abc}$.
* **Yêu cầu:** Cho một số có đúng 3 chữ số $N$. Kiểm tra xem $N$ có phải là số Armstrong không. In `YES` hoặc `NO`.
* **Input:** Một số nguyên $N$ ($100 \le N \le 999$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `153` | `YES` |
  | `200` | `NO` |

---

### Bài 5 (Cơ bản): Tìm tất cả số hoàn hảo nhỏ hơn N (`PYA-L12-P05`)

* **Yêu cầu:** Cho số nguyên dương $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các số hoàn hảo nhỏ hơn hoặc bằng $N$ theo thứ tự tăng dần.
* **Input:** Một số nguyên $N$.
* **Output:** Các số hoàn hảo, cách nhau bởi khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `30` | `6 28` |

---

### Bài 6 (Luyện tập): Đếm bội của 3 nhưng không chia hết cho 5 (`PYA-L12-P06`)

* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{12}$). Hãy đếm xem trong đoạn từ $A$ đến $B$ có bao nhiêu số chia hết cho 3 nhưng **không chia hết cho 5**.
* **Input:** Hai số $A$ và $B$ cách nhau bởi khoảng trắng.
* **Output:** Số lượng số thỏa mãn.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `1 30` | `8` |

---

### Bài 7 (Luyện tập): Đếm số chia hết cho 2 hoặc 3 (`PYA-L12-P07`)

* **Yêu cầu:** Cho số nguyên dương $N$ ($1 \le N \le 10^{12}$). Hãy đếm xem từ 1 đến $N$ có bao nhiêu số chia hết cho 2 hoặc chia hết cho 3.
* **Input:** Một số nguyên $N$.
* **Output:** Số lượng số thỏa mãn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `7` | Các số là: 2, 3, 4, 6, 8, 9, 10 (có 7 số). |
* **Gợi ý:** Dùng công thức $N // 2 + N // 3 - N // 6$.

---

### Bài 8 (Luyện tập): Cặp số thân thiết (`PYA-L12-P08`)

* **Bối cảnh:** Hai số $A$ và $B$ ($A \ne B$) được gọi là "Cặp số thân thiết" nếu tổng các ước số nhỏ hơn $A$ bằng $B$, và tổng các ước số nhỏ hơn $B$ bằng $A$.
* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng là cặp số thân thiết, ngược lại in `NO`.
* **Input:** Hai số $A, B$ ($1 \le A, B \le 10^5$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `220 284` | `YES` |
  | `10 20` | `NO` |

---

### Bài 9 (Luyện tập): Số phong phú (abundant number) (`PYA-L12-P09`)

* **Bối cảnh:** Một số tự nhiên được gọi là "Số phong phú" nếu tổng các ước số nhỏ hơn nó lớn hơn chính nó (ví dụ: số 12 có tổng các ước nhỏ hơn nó là $1+2+3+4+6=16 > 12$).
* **Yêu cầu:** Nhập số nguyên dương $N$. Hãy in ra tất cả các số phong phú nhỏ hơn hoặc bằng $N$.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^4$).
* **Output:** Dãy các số phong phú tăng dần trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `20` | `12 18 20` |

---

### Bài 10 (Luyện tập): Đếm số không chứa chữ số 0 (`PYA-L12-P10`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy đếm xem từ 1 đến $N$ có bao nhiêu số mà trong cách ghi thập phân của nó **không chứa bất kỳ chữ số 0 nào**.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** Số lượng số thỏa mãn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `15` | `14` | Từ 1 đến 15 chỉ có duy nhất số 10 chứa chữ số 0. Vậy có $15 - 1 = 14$ số. |

---

### Bài 11 (Vận dụng): Đếm số chính phương trong đoạn (`PYA-L12-P11`)
*(Đề thi Tin học trẻ Bảng A)*

* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{14}$). Hãy đếm xem có bao nhiêu số chính phương nằm trong đoạn từ $A$ đến $B$.
* **Input:** Hai số nguyên $A, B$ trên cùng một dòng.
* **Output:** Số lượng số chính phương trong đoạn $[A, B]$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5 25` | `3` | Có 3 số chính phương là 9, 16, 25. |
* **Gợi ý:** Một số $X$ là số chính phương trong $[A, B]$ thì $K = \sqrt{X}$ thỏa mãn $\sqrt{A} \le K \le \sqrt{B}$. Số lượng $K$ nguyên chính bằng: `int(B**0.5) - int((A - 1)**0.5)`.

---

### Bài 12 (Thử thách): Số tự mãn (narcissistic number K chữ số) (`PYA-L12-P12`)
*(Đề thi Tin học trẻ Quốc gia Bảng A)*

* **Bối cảnh:** Một số tự nhiên $N$ có $K$ chữ số được gọi là "Số tự mãn" (Narcissistic number) nếu tổng lũy thừa bậc $K$ của các chữ số của nó đúng bằng chính số $N$.
  Ví dụ:
  * $N = 153$ có 3 chữ số: $1^3 + 5^3 + 3^3 = 153$ $\implies$ Thỏa mãn.
  * $N = 1634$ có 4 chữ số: $1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$ $\implies$ Thỏa mãn.
* **Yêu cầu:** Cho số nguyên dương $N$ ($1 \le N \le 10^9$). Hãy kiểm tra xem $N$ có phải là số tự mãn không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một số nguyên $N$.
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `1634` | `YES` |
  | `2024` | `NO` |
