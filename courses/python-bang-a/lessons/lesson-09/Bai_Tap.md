# Hệ thống bài tập thực hành — bài 09: Ước số, bội số và số nguyên tố

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L11-P01` | Liệt kê tất cả ước số | `Cơ bản` | $1 \le N \le 1000$ | Vòng lặp `for` kiểm tra `N % i == 0` |
| 02 | `PYA-L11-P02` | Đếm số lượng ước số | `Cơ bản` | $1 \le N \le 10^5$ | Đếm số ước của $N$ |
| 03 | `PYA-L11-P03` | Tính tổng các ước số | `Cơ bản` | $1 \le N \le 10^5$ | Cộng dồn các ước số |
| 04 | `PYA-L11-P04` | Kiểm tra số nguyên tố | `Cơ bản` | $0 \le N \le 10^7$ | Thuật toán kiểm tra số nguyên tố chuẩn |
| 05 | `PYA-L11-P05` | Kiểm tra số chính phương | `Cơ bản` | $1 \le N \le 10^9$ | Kiểm tra $N = K^2$ |
| 06 | `PYA-L11-P06` | Ước chung lớn nhất & bcnn | `Luyện tập` | $1 \le A, B \le 10^9$ | Dùng `math.gcd` và công thức bcnn |
| 07 | `PYA-L11-P07` | Đếm ước chẵn của N | `Luyện tập` | $1 \le N \le 10^6$ | Kết hợp `N % i == 0 and i % 2 == 0` |
| 08 | `PYA-L11-P08` | Tìm ước số lớn thứ hai | `Luyện tập` | $2 \le N \le 10^9$ | Tìm ước thực sự lớn nhất khác $N$ |
| 09 | `PYA-L11-P09` | Đếm số nguyên tố trong đoạn | `Luyện tập` | $1 \le A \le B \le 10^4$ | Vòng lặp lồng hoặc hàm đếm số nguyên tố |
| 10 | `PYA-L11-P10` | Hai số nguyên tố cùng nhau | `Luyện tập` | $1 \le A, B \le 10^9$ | Kiểm tra $\text{gcd}(A, B) == 1$ |
| 11 | `PYA-L11-P11` | Cặp số nguyên tố sinh đôi | `Luyện tập` | $1 \le N \le 10^4$ | Tìm các cặp số nguyên tố $(P, P+2) \le N$ |
| 12 | `PYA-L11-P12` | Số siêu nguyên tố (super prime) | `Vận dụng` | $10 \le N \le 10^6$ | Cắt dần bên phải vẫn là số nguyên tố |
| 13 | `PYA-L11-P13` | Phân tích ra thừa số nguyên tố | `Vận dụng` | $2 \le N \le 10^6$ | Phân tích $N = p_1^{a_1} \times p_2^{a_2} \dots$ |
| 14 | `PYA-L11-P14` | Tìm số có đúng 3 ước số | `Thử thách` | $1 \le N \le 10^9$ | Nhận diện bản chất số $P^2$ với $P$ là nguyên tố |

---

### Bài 1 (Cơ bản): Liệt kê tất cả ước số (`PYA-L11-P01`)

* **Yêu cầu:** Nhập một số tự nhiên $N$. Hãy in ra tất cả các ước số nguyên dương của $N$ theo thứ tự tăng dần trên một dòng, cách nhau bởi khoảng trắng.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** Dãy các ước số của $N$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `12` | `1 2 3 4 6 12` |

---

### Bài 2 (Cơ bản): Đếm số lượng ước số (`PYA-L11-P02`)

* **Yêu cầu:** Cho số tự nhiên $N$. Hãy cho biết số $N$ có tất cả bao nhiêu ước số nguyên dương.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^5$).
* **Output:** Một số nguyên duy nhất là số lượng ước số của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `4` | Số 10 có 4 ước: 1, 2, 5, 10. |

---

### Bài 3 (Cơ bản): Tính tổng các ước số (`PYA-L11-P03`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy tính tổng tất cả các ước số của $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^5$).
* **Output:** Tổng các ước số của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `6` | `12` | Các ước là 1, 2, 3, 6 $\implies 1 + 2 + 3 + 6 = 12$. |

---

### Bài 4 (Cơ bản): Kiểm tra số nguyên tố (`PYA-L11-P04`)
*(Bài toán nền tảng thi Tin học trẻ)*

* **Yêu cầu:** Nhập vào số nguyên $N$. Hãy kiểm tra xem $N$ có phải là số nguyên tố hay không. Nếu có in `YES`, nếu không in `NO`.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^7$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `7` | `YES` |
  | `1` | `NO` |
  | `9` | `NO` |

---

### Bài 5 (Cơ bản): Kiểm tra số chính phương (`PYA-L11-P05`)

* **Bối cảnh:** Số chính phương là số bằng bình phương của một số tự nhiên (ví dụ: $0, 1, 4, 9, 16, 25, \dots$).
* **Yêu cầu:** Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số chính phương không. Nếu đúng in `YES`, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `25` | `YES` |
  | `20` | `NO` |

---

### Bài 6 (Luyện tập): Ước chung lớn nhất & bcnn (`PYA-L11-P06`)

* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$. Hãy tìm Ước chung lớn nhất ($\text{GCD}$) và Bội chung nhỏ nhất ($\text{LCM}$) của 2 số này.
* **Input:** Hai số nguyên $A, B$ cách nhau bởi khoảng trắng ($1 \le A, B \le 10^9$).
* **Output:** Hai số nguyên: $\text{GCD}$ trước, $\text{LCM}$ sau, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12 18` | `6 36` | $\text{GCD}(12, 18) = 6$, $\text{LCM}(12, 18) = (12 \times 18) // 6 = 36$. |

---

### Bài 7 (Luyện tập): Đếm ước chẵn của N (`PYA-L11-P07`)

* **Yêu cầu:** Cho số nguyên dương $N$. Hãy đếm xem có bao nhiêu ước số của $N$ là số chẵn.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^6$).
* **Output:** Số lượng ước chẵn của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `12` | `4` | Các ước của 12 là: 1, 2, 3, 4, 6, 12. Trong đó các ước chẵn là: 2, 4, 6, 12 (có 4 số). |

---

### Bài 8 (Luyện tập): Tìm ước số lớn thứ hai (`PYA-L11-P08`)

* **Yêu cầu:** Cho số nguyên dương $N$ ($N \ge 2$). Ước số lớn nhất của $N$ luôn là chính nó ($N$). Hãy tìm ước số lớn thứ hai của $N$ (tức là ước số lớn nhất nhưng nhỏ hơn $N$).
* **Input:** Một số tự nhiên $N$ ($2 \le N \le 10^9$).
* **Output:** Ước số lớn thứ hai của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `24` | `12` | Ước lớn nhất là 24, lớn thứ hai là 12. |
  | `7` | `1` | Ước của 7 là 1 và 7, lớn thứ hai là 1. |

---

### Bài 9 (Luyện tập): Đếm số nguyên tố trong đoạn (`PYA-L11-P09`)

* **Yêu cầu:** Cho hai số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^4$). Hãy đếm xem có bao nhiêu số nguyên tố nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số $A, B$ trên cùng một dòng.
* **Output:** Số lượng số nguyên tố trong đoạn $[A, B]$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10 20` | `4` | Có 4 số nguyên tố: 11, 13, 17, 19. |

---

### Bài 10 (Luyện tập): Hai số nguyên tố cùng nhau (`PYA-L11-P10`)

* **Bối cảnh:** Hai số $A$ và $B$ được gọi là nguyên tố cùng nhau nếu Ước chung lớn nhất của chúng bằng 1 ($\text{GCD}(A, B) = 1$).
* **Yêu cầu:** Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng nguyên tố cùng nhau, ngược lại in `NO`.
* **Input:** Hai số $A, B$ ($1 \le A, B \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `8 9` | `YES` |
  | `12 18` | `NO` |

---

### Bài 11 (Luyện tập): Cặp số nguyên tố sinh đôi (`PYA-L11-P11`)

* **Bối cảnh:** Hai số nguyên tố được gọi là "Sinh đôi" (Twin Primes) nếu chúng hơn kém nhau đúng 2 đơn vị (ví dụ: $(3, 5), (5, 7), (11, 13), (17, 19)$).
* **Yêu cầu:** Cho số tự nhiên $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các cặp số nguyên tố sinh đôi $(P, P+2)$ sao cho $P+2 \le N$.
* **Input:** Một số nguyên $N$.
* **Output:** Mỗi dòng in một cặp số nguyên tố sinh đôi cách nhau bởi khoảng trắng, theo thứ tự tăng dần.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `15` | `3 5`<br>`5 7`<br>`11 13` |

---

### Bài 12 (Vận dụng): Số siêu nguyên tố (super prime) (`PYA-L11-P12`)
*(Đề thi Tin học trẻ Bảng A)*

* **Bối cảnh:** Một số tự nhiên được gọi là "Siêu nguyên tố" nếu bản thân nó là số nguyên tố, và khi ta lần lượt xóa bớt chữ số tận cùng bên phải thì các số thu được vẫn luôn là số nguyên tố!
  * Ví dụ: Số $239$ là số nguyên tố.
  * Cắt đuôi 9 còn $23$ (vẫn là số nguyên tố).
  * Cắt đuôi 3 còn $2$ (vẫn là số nguyên tố).
  $\implies 239$ là một Siêu nguyên tố!
* **Yêu cầu:** Cho số tự nhiên $N$. Hãy kiểm tra xem $N$ có phải là Siêu nguyên tố hay không. In `YES` hoặc `NO`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^7$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `239` | `YES` |
  | `23` | `YES` |
  | `27` | `NO` |

---

### Bài 13 (Vận dụng): Phân tích ra thừa số nguyên tố (`PYA-L11-P13`)

* **Yêu cầu:** Mọi số tự nhiên $N \ge 2$ đều có thể phân tích thành tích của các thừa số nguyên tố. Cho số tự nhiên $N$. Hãy in ra dạng phân tích của $N$.
* **Input:** Một số tự nhiên $N$ ($2 \le N \le 10^6$).
* **Output:** Dãy các thừa số nguyên tố tăng dần theo định dạng `p1 * p2 * ...`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `60` | `2 * 2 * 3 * 5` |
  | `17` | `17` |

---

### Bài 14 (Thử thách): Tìm số có đúng 3 ước số (`PYA-L11-P14`)
*(Đề thi Tin học trẻ Quốc gia Bảng A)*

* **Bối cảnh:** Một số tự nhiên $X$ có đúng 3 ước số nguyên dương khi và chỉ khi $X$ là bình phương của một số nguyên tố ($X = P^2$, ví dụ: $4 = 2^2, 9 = 3^2, 25 = 5^2, 49 = 7^2$).
* **Yêu cầu:** Cho số nguyên dương $N$. Hãy đếm xem có bao nhiêu số nhỏ hơn hoặc bằng $N$ mà có **đúng 3 ước số**.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Số lượng các số có đúng 3 ước số $\le N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `30` | `3` | Có 3 số là: 4 ($2^2$), 9 ($3^2$), 25 ($5^2$). |
