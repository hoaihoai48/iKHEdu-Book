# Hệ thống bài tập thực hành — bài 02: Phép toán số học, chia nguyên và chia dư

---

## Bảng ma trận bài tập (16 bài tập phân tầng cơ bản → vận dụng)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L02-P01` | Chia đều bánh quy | `Cơ bản` | $1 \le a, b \le 1000$ | Thành thạo phép chia nguyên `//` và chia dư `%` |
| 02 | `PYA-L02-P02` | Nhân đôi lũy thừa | `Cơ bản` | $1 \le n \le 30$ | Lũy thừa `**` cơ số 2 |
| 03 | `PYA-L02-P03` | Số kẹo còn thừa | `Cơ bản` | $1 \le N, K \le 10^9$ | Phép modulo `%`, xử lý số nguyên lớn |
| 04 | `PYA-L02-P04` | Đổi giờ ra phút giây | `Cơ bản` | $0 \le H, M, S \le 59$ | Biểu thức nhân cộng liên hoàn |
| 05 | `PYA-L02-P05` | Bóng đèn viền biển hiệu | `Luyện tập` | $1 \le a \le 10^7$ | Phép nhân chia đổi đơn vị (THT đà nẵng) |
| 06 | `PYA-L02-P06` | Trồng cây đại lộ | `Luyện tập` | $1 \le N, K \le 10^6$ | Phép chia khoảng cách cộng 1 ở đầu mút |
| 07 | `PYA-L02-P07` | Vòng chạy điền kinh | `Luyện tập` | $1 \le N \le 10^9$ | Chu kỳ vòng lặp sân thể thao qua modulo |
| 08 | `PYA-L02-P08` | Kim đồng hồ 12 giờ | `Luyện tập` | $1 \le H \le 12, 1 \le K \le 10^9$ | Phép chia dư xử lý chu kỳ đồng hồ |
| 09 | `PYA-L02-P09` | Tách chữ số tận cùng | `Luyện tập` | $10 \le N \le 10^9$ | Tách hàng đơn vị `% 10` và hàng chục |
| 10 | `PYA-L02-P10` | Đảo ngược số 2 chữ số | `Luyện tập` | $10 \le N \le 99$ | Hoán vị vị trí chữ số bằng `//` và `%` |
| 11 | `PYA-L02-P11` | Xe buýt chở học sinh | `Luyện tập` | $1 \le N, K \le 10^6$ | Kỹ thuật làm tròn lên: `(N + K - 1) // K` |
| 12 | `PYA-L02-P12` | Bàn cờ ca-rô vô tận | `Vận dụng` | $1 \le K, W \le 10^6$ | Xác định tọa độ hàng cột $(row, col)$ từ số thứ tự |
| 13 | `PYA-L02-P13` | Lũy thừa cầu thang | `Luyện tập` | $1 \le a \le 10, 0 \le n \le 10$ | Lũy thừa tổng quát `a ** n` |
| 14 | `PYA-L02-P14` | Đổi phút ra giờ phút | `Luyện tập` | $0 \le T \le 10000$ | Đổi đơn vị thời gian bằng `// 60` và `% 60` |
| 15 | `PYA-L02-P15` | Giá trị biểu thức PEMDAS | `Vận dụng` | $1 \le a, b, c \le 100$ | Thứ tự ưu tiên mũ nhân cộng `a + b * c ** 2` |
| 16 | `PYA-L02-P16` | Đu quay vòng tròn | `Vận dụng` | $1 \le N, C \le 10^9$ | Chu kỳ vòng tròn tổng quát `N // C`, `N % C` |

---

### Bài 1 (Cơ bản): Chia đều bánh quy (`PYA-L02-P01`)

* **Bối cảnh:** Mẹ làm được $a$ chiếc bánh quy và muốn chia đều vào $b$ chiếc đĩa.
* **Yêu cầu:** Em hãy tính xem mỗi chiếc đĩa có bao nhiêu chiếc bánh, và còn dư lại bao nhiêu chiếc bánh không đủ chia đều.
* **Đầu vào (Input):** Nhập vào 2 số nguyên dương $a$ và $b$ trên 2 dòng ($1 \le a, b \le 1000$).
* **Đầu ra (Output):** In ra 2 số trên một dòng cách nhau một dấu cách: số bánh trên mỗi đĩa và số bánh còn dư.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `17`<br>`5` | `3 2` | $17 : 5 = 3$ dư $2$. Mỗi đĩa 3 cái, còn dư 2 cái bánh. |
* **Gợi ý thuật toán:** `print(a // b, a % b)`.

---

### Bài 2 (Cơ bản): Nhân đôi lũy thừa (`PYA-L02-P02`)

* **Bối cảnh:** Trong một thí nghiệm vi sinh vật, ban đầu có 1 tế bào. Cứ sau mỗi giờ, số lượng tế bào lại nhân đôi một lần ($2^1, 2^2, 2^3, \dots$).
* **Yêu cầu:** Hỏi sau $n$ giờ thì có tất cả bao nhiêu tế bào?
* **Đầu vào (Input):** Một số tự nhiên $n$ ($1 \le n \le 30$).
* **Đầu ra (Output):** In ra số lượng tế bào sau $n$ giờ ($2^n$).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4` | `16` | Sau 4 giờ: $2^4 = 16$ tế bào. |
* **Gợi ý thuật toán:** `n = int(input()); print(2 ** n)`.

---

### Bài 3 (Cơ bản): Số kẹo còn thừa (`PYA-L02-P03`)
*(Lấy cảm hứng từ Bài 9 Đề thi THT Toàn quốc)*

* **Bối cảnh:** Nhà máy sản xuất bánh kẹo vừa đóng gói được $N$ viên kẹo. Người ta đóng các viên kẹo này vào các hộp quà, mỗi hộp quà chứa đúng $K$ viên kẹo. Những viên kẹo còn thừa lại không đủ đóng thành một hộp quà sẽ được tặng cho các em nhỏ đi tham quan nhà máy.
* **Yêu cầu:** Hãy tính số kẹo được tặng cho các em nhỏ.
* **Đầu vào (Input):** Gồm 2 dòng lần lượt chứa hai số tự nhiên $N$ và $K$ ($1 \le N, K \le 10^9$).
* **Đầu ra (Output):** In ra số viên kẹo còn thừa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `100`<br>`8` | `4` |
* **Gợi ý thuật toán:** `print(N % K)`. Nhờ Python hỗ trợ số lớn, $N = 10^9$ vẫn chạy tức thì trong 0.001 giây!

---

### Bài 4 (Cơ bản): Đổi giờ ra phút giây (`PYA-L02-P04`)

* **Bối cảnh:** Đồng hồ điện tử hiển thị thời gian gồm $H$ giờ, $M$ phút và $S$ giây.
* **Yêu cầu:** Em hãy tính xem tổng cộng khoảng thời gian đó tương đương với bao nhiêu giây?
* **Biết rằng:** $1\text{ giờ} = 60\text{ phút} = 3600\text{ giây}$, $1\text{ phút} = 60\text{ giây}$.
* **Đầu vào (Input):** Ba dòng lần lượt chứa 3 số tự nhiên $H, M, S$ ($0 \le H \le 23, 0 \le M, S \le 59$).
* **Đầu ra (Output):** Một số nguyên duy nhất là tổng số giây.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1`<br>`20`<br>`15` | `4815` | $1 \times 3600 + 20 \times 60 + 15 = 3600 + 1200 + 15 = 4815$ giây. |

---

### Bài 5 (Luyện tập): Bóng đèn viền biển hiệu (`PYA-L02-P05`)
*(Lấy cảm hứng từ Bài 1 THT Sơn Trà - Đà Nẵng)*

* **Bối cảnh:** Người ta muốn mắc các bóng đèn màu trang trí xung quanh viền của một bảng quảng cáo hình vuông. Bảng quảng cáo có chiều dài cạnh là $a\text{ dm}$. Các bóng đèn được mắc liên tiếp nhau và cách nhau đúng $5\text{ cm}$ dọc theo chu vi hình vuông (bao gồm cả các góc).
* **Yêu cầu:** Em hãy tính số lượng bóng đèn cần mắc.
* **Biết rằng:** $1\text{ dm} = 10\text{ cm}$.
* **Đầu vào (Input):** Một số nguyên dương $a$ ($1 \le a \le 10^7$).
* **Đầu ra (Output):** Một số nguyên duy nhất là số bóng đèn cần mắc.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `1` | `8` | Cạnh $1\text{ dm} = 10\text{ cm}$. Chu vi bảng hình vuông là $10 \times 4 = 40\text{ cm}$.<br>Khoảng cách giữa các đèn là $5\text{ cm}$. Số đèn mắc là: $40 : 5 = 8$ bóng đèn. |
* **Gợi ý thuật toán:**
  * Đổi cạnh sang cm: `canh_cm = a * 10`
  * Chu vi viền: `chu_vi = canh_cm * 4`
  * Số bóng đèn: `chu_vi // 5`

---

### Bài 6 (Luyện tập): Trồng cây đại lộ (`PYA-L02-P06`)
*(Lấy cảm hứng từ Bài 7 Đề thi THT Toàn quốc)*

* **Bối cảnh:** Trên một đại lộ thẳng tắp có chiều dài $N$ mét, người ta cần trồng các cây xanh thẳng hàng ở một bên đường để tạo bóng mát. Bắt đầu trồng một cây ngay tại điểm xuất phát (mét thứ 0), và cứ sau mỗi khoảng cách đúng $K$ mét lại trồng tiếp một cây.
* **Yêu cầu:** Hãy tính tổng số lượng cây xanh được trồng trên đoạn đường từ mét thứ 0 đến mét thứ $N$.
* **Đầu vào (Input):** Gồm 2 số tự nhiên $N$ và $K$ ($1 \le N, K \le 10^6$) mỗi số trên một dòng.
* **Đầu ra (Output):** Một số nguyên duy nhất là số cây trồng được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`3` | `4` | Các cây được trồng tại các vị trí mét thứ: 0, 3, 6, 9. Tổng cộng có 4 cây. |
* **Gợi ý thuật toán:**
  * Số khoảng cách $K$ mét trọn vẹn là: `N // K`.
  * Do có thêm 1 cây ở điểm mút đầu tiên (vị trí 0), nên số cây trồng được là: `(N // K) + 1`.

---

### Bài 7 (Luyện tập): Vòng chạy điền kinh (`PYA-L02-P07`)
*(Lấy cảm hứng từ Bài 8 Đề thi THT Bắc Giang)*

* **Bối cảnh:** Một đường chạy thể thao hình chữ nhật có chu vi đúng $100\text{ mét}$. Vận động viên An xuất phát từ vạch số 0 và chạy liên tục theo một chiều dọc theo mép sân được tổng quãng đường là $N\text{ mét}$.
* **Yêu cầu:** Em hãy cho biết:
  1. An đã chạy được bao nhiêu vòng sân trọn vẹn?
  2. Hiện tại An đang dừng lại ở vị trí cách vạch xuất phát bao nhiêu mét?
* **Đầu vào (Input):** Một số nguyên $N$ ($1 \le N \le 10^9$).
* **Đầu ra (Output):** Hai số nguyên trên một dòng cách nhau dấu cách lần lượt là số vòng chạy trọn vẹn và khoảng cách tính từ vạch xuất phát.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `250` | `2 50` | $250 = 2 \times 100 + 50$. Đã chạy 2 vòng trọn vẹn và đang ở mét thứ 50. |
* **Gợi ý thuật toán:** `print(N // 100, N % 100)`.

---

### Bài 8 (Luyện tập): Kim đồng hồ 12 giờ (`PYA-L02-P08`)

* **Bối cảnh:** Đồng hồ kim treo tường có 12 số đánh dấu từ 1 đến 12. Hiện tại kim giờ đang chỉ vào đúng số $H$.
* **Yêu cầu:** Sau đúng $K$ giờ nữa, hỏi kim giờ sẽ chỉ vào số mấy?
* **Đầu vào (Input):** Nhập vào 2 số nguyên $H$ ($1 \le H \le 12$) và $K$ ($1 \le K \le 10^9$).
* **Đầu ra (Output):** In ra một số nguyên từ 1 đến 12 là số mà kim giờ đang chỉ.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `10`<br>`5` | `3` | Lúc 10 giờ, sau 5 giờ nữa là 15 giờ. Trên đồng hồ 12 số tương ứng số 3. |
  | `9`<br>`3` | `12` | Lúc 9 giờ, sau 3 giờ nữa là 12 giờ. |
* **Gợi ý thuật toán:**
  * Lưu ý bẫy số 12: Khi tính chia dư, số 12 chia 12 dư 0.
  * Công thức chuẩn: `gio_moi = (H + K) % 12`. Nếu `gio_moi == 0` thì kết quả là `12`! Hoặc dùng mẹo: `(H + K - 1) % 12 + 1`.

---

### Bài 9 (Luyện tập): Tách chữ số tận cùng (`PYA-L02-P09`)

* **Bối cảnh:** Bé Na có một mã số may mắn là một số tự nhiên $N$. Na muốn tìm ra chữ số hàng đơn vị và chữ số hàng chục của số này.
* **Yêu cầu:** Nhập vào số tự nhiên $N$ ($10 \le N \le 10^9$). Hãy in ra:
  * Dòng 1: Chữ số hàng đơn vị của $N$.
  * Dòng 2: Chữ số hàng chục của $N$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `857` | `7`<br>`5` | Chữ số hàng đơn vị là 7, hàng chục là 5. |
* **Gợi ý thuật toán:**
  * Chữ số hàng đơn vị: `don_vi = N % 10`
  * Chữ số hàng chục: Bỏ hàng đơn vị đi `tam = N // 10`, rồi lấy chữ số cuối của phần còn lại `chuc = tam % 10` (hoặc gộp lại `(N // 10) % 10`).

---

### Bài 10 (Luyện tập): Đảo ngược số 2 chữ số (`PYA-L02-P10`)

* **Bối cảnh:** Trong một mật thư thám tử, các con số 2 chữ số đã bị đảo ngược vị trí hai chữ số cho nhau (ví dụ số 27 bị biến thành 72).
* **Yêu cầu:** Nhập vào một số tự nhiên $N$ có đúng 2 chữ số ($10 \le N \le 99$). Hãy in ra số sau khi đảo ngược hai chữ số.
* **Đầu vào (Input):** Một số tự nhiên $N$.
* **Đầu ra (Output):** Số nguyên sau khi đảo ngược. (Lưu ý: Nếu số là 30 thì đảo lại là 3).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `49` | `94` | Hàng chục là 4, hàng đơn vị là 9 $\to$ Đảo lại thành 94. |
  | `50` | `5` | Hàng chục là 5, đơn vị là 0 $\to$ Đảo lại thành $0 \times 10 + 5 = 5$. |
* **Gợi ý thuật toán:**
  ```python
  N = int(input())
  chuc = N // 10
  don_vi = N % 10
  dao_nguoc = don_vi * 10 + chuc
  print(dao_nguoc)
  ```

---

### Bài 11 (Luyện tập): Xe buýt chở học sinh (`PYA-L02-P11`)

* **Bối cảnh:** Một trường tiểu học tổ chức dã ngoại cho $N$ học sinh. Nhà trường thuê các xe buýt loại $K$ chỗ ngồi. Mỗi xe buýt chở được tối đa $K$ bạn học sinh.
* **Yêu cầu:** Hỏi nhà trường cần thuê **ít nhất bao nhiêu xe buýt** để chở hết toàn bộ $N$ học sinh (không để bạn nào phải ở lại trường)?
* **Đầu vào (Input):** Nhập vào 2 số nguyên dương $N$ và $K$ ($1 \le N, K \le 10^6$).
* **Đầu ra (Output):** Một số nguyên duy nhất là số lượng xe buýt tối thiểu cần thuê.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `25`<br>`10` | `3` | 2 xe đầu chở được 20 bạn, còn 5 bạn nữa bắt buộc phải thuê thêm 1 xe thứ ba. |
  | `30`<br>`10` | `3` | 3 xe chở vừa khít 30 bạn. |
* **Gợi ý thuật toán (Kỹ thuật làm tròn lên kinh điển trong lập trình):**
  * Nếu dùng `N // K`: khi $N = 25, K = 10 \implies 25 // 10 = 2$ (bị thiếu 1 xe!).
  * Công thức làm tròn lên chuẩn mực thi đấu: `so_xe = (N + K - 1) // K`.
  * Thử lại: $(25 + 10 - 1) // 10 = 34 // 10 = 3$ (Đúng!).
  * Thử lại: $(30 + 10 - 1) // 10 = 39 // 10 = 3$ (Vẫn đúng!).

---

### Bài 12 (Vận dụng): Bàn cờ ca-rô vô tận (`PYA-L02-P12`)

* **Bối cảnh:** Một bàn cờ ô vuông vô tận được chia thành các hàng, mỗi hàng có đúng $W$ ô vuông. Các ô vuông được đánh số liên tiếp bắt đầu từ $1$:
  * Hàng 1 gồm các ô: $1, 2, \dots, W$.
  * Hàng 2 gồm các ô: $W+1, W+2, \dots, 2W$.
  * Cứ như vậy tiếp tục cho các hàng tiếp theo.
* **Yêu cầu:** Cho biết số thứ tự của một ô là $K$. Em hãy xác định xem ô đó nằm ở **Hàng thứ mấy** và **Cột thứ mấy** (Cột tính từ 1 đến $W$)?
* **Đầu vào (Input):** Gồm hai số tự nhiên $K$ và $W$ ($1 \le K, W \le 10^6$) mỗi số trên một dòng.
* **Đầu ra (Output):** In ra hai số nguyên trên một dòng cách nhau dấu cách: `hang cot`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `11`<br>`4` | `3 3` | Mỗi hàng có 4 ô.<br>Hàng 1: 1, 2, 3, 4<br>Hàng 2: 5, 6, 7, 8<br>Hàng 3: 9, 10, 11, 12.<br>Ô số 11 nằm ở Hàng 3, Cột 3. |
* **Gợi ý thuật toán:**
  * Chuyển về chỉ số bắt đầu từ 0: `idx = K - 1`
  * Hàng (tính từ 1): `hang = (idx // W) + 1`
  * Cột (tính từ 1): `cot = (idx % W) + 1`
  * In: `print(hang, cot)`.

---

### Bài 13 (Luyện tập): Lũy thừa cầu thang (`PYA-L02-P13`)

* **Bối cảnh:** Bạn Thỏ Nâu xếp các khối gỗ thành cầu thang toán học, mỗi tầng gấp $a$ lần tầng trước, cả cầu thang có $n$ tầng.
* **Yêu cầu:** Tính số khối gỗ ở tầng cao nhất, tức giá trị $a^n$.
* **Đầu vào (Input):** Hai dòng lần lượt là cơ số $a$ và số mũ $n$ ($1 \le a \le 10, 0 \le n \le 10$).
* **Đầu ra (Output):** Một số nguyên duy nhất là $a^n$.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`4` | `81` | $3^4 = 3 \times 3 \times 3 \times 3 = 81$. |
* **Gợi ý thuật toán:** `print(a ** n)`. Nhớ `**` mới là lũy thừa, `^` là phép XOR bit!

---

### Bài 14 (Luyện tập): Đổi phút ra giờ phút (`PYA-L02-P14`)

* **Bối cảnh:** Bạn Mèo Cam bấm giờ chạy bộ được tổng cộng $T$ phút và muốn khoe thành tích theo dạng mấy giờ mấy phút.
* **Yêu cầu:** Đổi tổng số phút $T$ thành số giờ trọn vẹn và số phút lẻ.
* **Đầu vào (Input):** Một số nguyên $T$ ($0 \le T \le 10000$).
* **Đầu ra (Output):** Hai số nguyên trên một dòng cách nhau dấu cách: giờ và phút dư.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `135` | `2 15` | $135 = 2 \times 60 + 15$. Được 2 giờ và dư 15 phút. |
* **Gợi ý thuật toán:** `print(T // 60, T % 60)`.

---

### Bài 15 (Vận dụng): Giá trị biểu thức PEMDAS (`PYA-L02-P15`)

* **Bối cảnh:** Cô giáo viết biểu thức bí mật $a + b \times c^2$ lên bảng, bạn nào tính đúng thứ tự ưu tiên sẽ thắng cuộc thi tính nhẩm.
* **Yêu cầu:** Cho ba số $a, b, c$, hãy tính giá trị biểu thức $a + b \times c^2$ (lũy thừa trước, nhân trước, cộng sau).
* **Đầu vào (Input):** Ba dòng lần lượt là $a, b, c$ ($1 \le a, b, c \le 100$).
* **Đầu ra (Output):** Một số nguyên duy nhất là giá trị biểu thức.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `2`<br>`3`<br>`4` | `50` | $4^2 = 16$, $3 \times 16 = 48$, $2 + 48 = 50$. |
* **Gợi ý thuật toán:** `print(a + b * c ** 2)`. Không được thêm ngoặc sai thành `(a + b) * c ** 2`!

---

### Bài 16 (Vận dụng): Đu quay vòng tròn (`PYA-L02-P16`)

* **Bối cảnh:** Chiếc đu quay mỗi vòng mất đúng $C$ phút, bạn Sóc Nâu ngồi liên tục $N$ phút để ngắm thành phố.
* **Yêu cầu:** Tính số vòng quay trọn vẹn và số phút dở dang của vòng hiện tại.
* **Đầu vào (Input):** Hai dòng lần lượt là $N$ và $C$ ($1 \le N, C \le 10^9$).
* **Đầu ra (Output):** Hai số nguyên trên một dòng cách nhau dấu cách: số vòng trọn và số phút dư.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `250`<br>`60` | `4 10` | $250 = 4 \times 60 + 10$. Đi được 4 vòng và dư 10 phút. |
* **Gợi ý thuật toán:** `print(N // C, N % C)`. Kiểm tra lại bằng $N = \text{vòng} \times C + \text{dư}$.
