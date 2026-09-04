# Hệ thống bài tập thực hành — bài 06: Vòng lặp while và biến cờ

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L08-P01` | Đếm xuôi bằng while | `Cơ bản` | $1 \le N \le 100$ | Cú pháp `while` cơ bản với biến tăng `i = i + 1` |
| 02 | `PYA-L08-P02` | Rút thăm đến khi trúng | `Cơ bản` | Dãy số kết thúc bằng 7 | Lặp cho đến khi gặp số mục tiêu |
| 03 | `PYA-L08-P03` | Nhập số đến khi gặp số 0 | `Cơ bản` | Số lượng phần tử $\le 1000$ | Đếm số lượng số đã nhập (THT đà lạt) |
| 04 | `PYA-L08-P04` | Tổng dãy số kết thúc bằng 0 | `Cơ bản` | Mỗi số $\le 10^6$ | Tính tổng các số đã nhập trước khi gặp 0 |
| 05 | `PYA-L08-P05` | Đếm số chẵn đến khi gặp 0 | `Cơ bản` | Số nguyên $\le 10^6$ | Lọc và đếm số chẵn trong luồng nhập (THT lâm đồng) |
| 06 | `PYA-L08-P06` | Gấp đôi tờ giấy lên mặt trăng | `Luyện tập` | $1 \le H \le 10^9$ | Đếm số lần nhân đôi $2 \times 2 \dots$ vượt ngưỡng $H$ |
| 07 | `PYA-L08-P07` | Ống heo mua xe máy | `Luyện tập` | $1 \le P \le 10^7$ | Tiết kiệm tiền mỗi ngày tăng dần đến khi đủ tiền (THT) |
| 08 | `PYA-L08-P08` | Tìm lũy thừa của 2 lớn hơn N | `Luyện tập` | $1 \le N \le 10^9$ | Vòng lặp tìm số $2^k > N$ nhỏ nhất |
| 09 | `PYA-L08-P09` | Chú ốc sên leo cột cờ | `Luyện tập` | $1 \le H, A, B \le 10^6 (A > B)$ | Ban ngày leo lên $A$, ban đêm tụt $B$ đến đỉnh $H$ |
| 10 | `PYA-L08-P10` | Đếm số lượng chữ số của N | `Luyện tập` | $1 \le N \le 10^{18}$ | Kỹ thuật chia nguyên liên tiếp `N = N // 10` |
| 11 | `PYA-L08-P11` | Trò chơi đoán số nhị phân | `Vận dụng` | $1 \le N \le 10^6$ | Mô phỏng số bước đoán số tối đa $\log_2 N$ |
| 12 | `PYA-L08-P12` | Dãy số collatz (3n + 1) | `Vận dụng` | $1 \le N \le 10^6$ | Mô phỏng giả thuyết toán học collatz nổi tiếng |

---

### Bài 1 (Cơ bản): Đếm xuôi bằng while (`PYA-L08-P01`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$. Dùng vòng lặp `while`, hãy in ra các số từ $1$ đến $N$ trên một dòng.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 100$).
* **Output:** Dãy số từ 1 đến $N$.
* **Gợi ý:**
  ```python
  N = int(input())
  i = 1
  while i <= N:
      print(i, end=" ")
      i = i + 1
  ```

---

### Bài 2 (Cơ bản): Rút thăm đến khi trúng (`PYA-L08-P02`)

* **Bối cảnh:** Bé Bo bốc thăm từng lá phiếu có ghi số. Bo sẽ dừng lại ngay khi bốc trúng lá phiếu ghi số **7**.
* **Yêu cầu:** Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 7 thì dừng lại. Hãy in ra dòng chữ: `DA TRUNG THUONG!`
* **Input:** Một dãy các số nguyên, số cuối cùng chắc chắn là số 7.
* **Output:** In `DA TRUNG THUONG!` sau khi vòng lặp dừng.

---

### Bài 3 (Cơ bản): Nhập số đến khi gặp số 0 (`PYA-L08-P03`)
*(Lấy cảm hứng từ Bài 6 Đề thi THT Đà Lạt - Lâm Đồng)*

* **Yêu cầu:** Viết chương trình nhập liên tiếp các số nguyên từ bàn phím. Việc nhập kết thúc khi người dùng nhập số 0. Hãy đếm xem người dùng đã nhập **bao nhiêu số** (không tính số 0 cuối cùng).
* **Input:** Một dãy các số nguyên, kết thúc bằng số 0.
* **Output:** Một số nguyên duy nhất là số lượng các số đã nhập trước số 0.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`12`<br>`8`<br>`0` | `3` | Có 3 số: 5, 12, 8 đã được nhập trước khi gặp 0. |

---

### Bài 4 (Cơ bản): Tổng dãy số kết thúc bằng 0 (`PYA-L08-P04`)

* **Yêu cầu:** Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 0. Hãy tính và in ra **tổng của tất cả các số** đã nhập.
* **Input:** Một dãy số nguyên kết thúc bằng 0.
* **Output:** Tổng các số.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`20`<br>`5`<br>`0` | `35` | $10 + 20 + 5 = 35$. |

---

### Bài 5 (Cơ bản): Đếm số chẵn đến khi gặp 0 (`PYA-L08-P05`)

* **Yêu cầu:** Nhập liên tiếp các số nguyên từ bàn phím cho đến khi nhập số 0. Hãy đếm xem có bao nhiêu số chẵn trong các số đã nhập (không tính số 0).
* **Input:** Dãy số nguyên kết thúc bằng 0.
* **Output:** Số lượng số chẵn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4`<br>`7`<br>`8`<br>`12`<br>`0` | `3` | Có 3 số chẵn là 4, 8, 12. |

---

### Bài 6 (Luyện tập): Gấp đôi tờ giấy lên mặt trăng (`PYA-L08-P06`)

* **Bối cảnh:** Một tờ giấy siêu mỏng ban đầu có độ dày là $1\text{ mm}$. Cứ mỗi lần gấp đôi tờ giấy lại, độ dày của nó lại tăng gấp đôi ($2\text{ mm}, 4\text{ mm}, 8\text{ mm}, \dots$).
* **Yêu cầu:** Hỏi cần phải gấp đôi tờ giấy ít nhất bao nhiêu lần để độ dày của nó đạt hoặc vượt quá độ cao $H\text{ mm}$?
* **Input:** Một số tự nhiên $H$ ($1 \le H \le 10^9$).
* **Output:** Số lần gấp đôi tối thiểu.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `4` | Lần 1: 2mm, lần 2: 4mm, lần 3: 8mm, lần 4: 16mm ($\ge 10$). Cần 4 lần. |

---

### Bài 7 (Luyện tập): Ống heo mua xe máy (`PYA-L08-P07`)
*(Lấy cảm hứng từ Bài 51 Đề thi Scratch THT Toàn quốc)*

* **Bối cảnh:** Bác Nam muốn tiết kiệm tiền để mua một chiếc xe máy có giá $P$ nghìn đồng.
  * Ngày thứ nhất bác bỏ vào ống heo 1 nghìn đồng.
  * Ngày thứ hai bác bỏ vào 2 nghìn đồng.
  * Ngày thứ $k$ bác bỏ vào đúng $k$ nghìn đồng.
* **Yêu cầu:** Hỏi sau bao nhiêu ngày thì tổng số tiền trong ống heo của bác Nam đạt hoặc vượt quá $P$ nghìn đồng?
* **Input:** Một số tự nhiên $P$ ($1 \le P \le 10^7$).
* **Output:** Số ngày ít nhất.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `15` | `5` | Ngày 1: 1k, ngày 2: 2k (tổng 3k), ngày 3: 3k (tổng 6k), ngày 4: 4k (tổng 10k), ngày 5: 5k (tổng 15k $\ge 15$). Sau 5 ngày. |

---

### Bài 8 (Luyện tập): Tìm lũy thừa của 2 lớn hơn N (`PYA-L08-P08`)

* **Yêu cầu:** Nhập vào số tự nhiên $N$. Hãy tìm số có dạng lũy thừa của 2 ($1, 2, 4, 8, 16, 32, \dots$) **nhỏ nhất mà lớn hơn $N$**.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Số lũy thừa của 2 tìm được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `16` | Lũy thừa của 2 gồm 1, 2, 4, 8, 16... Số nhỏ nhất $> 10$ là 16. |
  | `16` | `32` | Số phải lớn hơn 16 nên là 32. |

---

### Bài 9 (Luyện tập): Chú ốc sên leo cột cờ (`PYA-L08-P09`)

* **Bối cảnh:** Chú ốc sên muốn leo lên đỉnh một cột cờ cao $H$ mét.
  * Ban ngày, chú ốc sên bò lên được $A$ mét.
  * Ban đêm, khi ngủ chú bị tụt xuống $B$ mét ($B < A$).
  * Khi chú chạm tới hoặc vượt qua đỉnh cột cờ vào ban ngày, chú sẽ dừng lại và cắm cờ (không bị tụt nữa).
* **Yêu cầu:** Hỏi chú ốc sên mất bao nhiêu ngày để leo lên tới đỉnh cột cờ?
* **Input:** Ba số tự nhiên $H, A, B$ trên 3 dòng ($1 \le B < A \le H \le 10^6$).
* **Output:** Số ngày để ốc sên chạm đỉnh.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`3`<br>`1` | `2` | Ngày 1: leo lên 3m, đêm tụt 1m còn 2m.<br>Ngày 2: từ 2m leo thêm 3m lên 5m (chạm đỉnh ngay trong ngày!). Vậy mất 2 ngày. |

---

### Bài 10 (Luyện tập): Đếm số lượng chữ số của N (`PYA-L08-P10`)

* **Yêu cầu:** Nhập vào một số nguyên dương $N$. Dùng vòng lặp `while` và phép chia nguyên `// 10`, hãy đếm xem số $N$ có bao nhiêu chữ số.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** Số lượng chữ số của $N$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `2026` | `4` |
* **Gợi ý thuật toán:**
  ```python
  N = int(input())
  dem = 0
  while N > 0:
      N = N // 10
      dem = dem + 1
  print(dem)
  ```

---

### Bài 11 (Vận dụng): Trò chơi đoán số nhị phân (`PYA-L08-P11`)

* **Bối cảnh:** Bạn An nghĩ ra một số bí mật từ 1 đến $N$. Bạn Bình dùng chiến thuật "Chặt đôi khoảng tìm kiếm" (Tìm kiếm nhị phân) để đoán số: Mỗi câu hỏi Bình chia đôi khoảng đang xét ($N = N // 2$).
* **Yêu cầu:** Hỏi trong trường hợp xấu nhất, Bình phải đoán **nhiều nhất bao nhiêu lần** thì chắc chắn tìm ra số của An (lặp cho đến khi khoảng chỉ còn 1 số: $N == 1$)?
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Số bước đoán tối đa.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `8` | `4` | Các bước: $8 \to 4 \to 2 \to 1$ (cần 4 bước). |

---

### Bài 12 (Vận dụng): Dãy số collatz (3n + 1) (`PYA-L08-P12`)

* **Bối cảnh:** Giả thuyết Collatz là một bài toán toán học kỳ bí: Bắt đầu từ số tự nhiên $N > 0$:
  * Nếu $N$ là số chẵn: chia đôi $N = N // 2$.
  * Nếu $N$ là số lẻ: nhân ba cộng một $N = 3 \times N + 1$.
  * Lặp lại quy trình trên cho đến khi số $N$ biến thành số $1$ thì dừng lại!
* **Yêu cầu:** Nhập vào số tự nhiên $N$. Hãy in ra số bước biến đổi để $N$ trở thành 1.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^5$).
* **Output:** Số bước biến đổi.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `6` | `8` | Dãy biến đổi: $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$ (qua 8 bước biến đổi). |
