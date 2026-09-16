# DANH SÁCH BÀI TẬP THỰC HÀNH: BÀI 08 — VÒNG LẶP CHO ĐẾN KHI VÀ BIẾN CỜ DỪNG

**Khóa học:** iKHEDU Scratch — Bảng A (Level 1)  
**Chuyên đề:** Chương 3: Cấu Trúc Rẽ Nhánh & Vòng Lặp  
> **Tổng số bài tập thực hành:** `12 bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  

---

## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện

| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |
|:---:|---|---|:---:|:---:|---|
| 1 | `sca_l08_p01_dem_xuoi_bang_while` | Đếm xuôi bằng while | **P0** | Khởi động & Quan sát | Nhập vào số tự nhiên $N$. Dùng vòng lặp `while`, hãy in ra c... |
| 2 | `sca_l08_p02_rut_tham_den_khi_trung` | Rút thăm đến khi trúng | **P0** | Khởi động & Quan sát | Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 7... |
| 3 | `sca_l08_p03_nhap_so_den_khi_gap_so_0` | Nhập số đến khi gặp số 0 | **P0** | Khởi động & Quan sát | Viết chương trình nhập liên tiếp các số nguyên từ bàn phím. ... |
| 4 | `sca_l08_p04_tong_day_so_ket_thuc_bang_0` | Tổng dãy số kết thúc bằng 0 | **P1** | Cơ bản & Hoàn thành | Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 0... |
| 5 | `sca_l08_p05_dem_so_chan_den_khi_gap_0` | Đếm số chẵn đến khi gặp 0 | **P1** | Cơ bản & Hoàn thành | Nhập liên tiếp các số nguyên từ bàn phím cho đến khi nhập số... |
| 6 | `sca_l08_p06_gap_doi_to_giay_len_mat_trang` | Gấp đôi tờ giấy lên mặt trăng | **P1** | Cơ bản & Hoàn thành | Hỏi cần phải gấp đôi tờ giấy ít nhất bao nhiêu lần để độ dày... |
| 7 | `sca_l08_p07_ong_heo_mua_xe_may` | Ống heo mua xe máy | **P2** | Luyện tập & Vận dụng | Hỏi sau bao nhiêu ngày thì tổng số tiền trong ống heo của bá... |
| 8 | `sca_l08_p08_tim_luy_thua_cua_2_lon_hon_n` | Tìm lũy thừa của 2 lớn hơn N | **P2** | Luyện tập & Vận dụng | Nhập vào số tự nhiên $N$. Hãy tìm số có dạng lũy thừa của 2 ... |
| 9 | `sca_l08_p09_chu_oc_sen_leo_cot_co` | Chú ốc sên leo cột cờ | **P2** | Luyện tập & Vận dụng | Hỏi chú ốc sên mất bao nhiêu ngày để leo lên tới đỉnh cột cờ... |
| 10 | `sca_l08_p10_dem_so_luong_chu_so_cua_n` | Đếm số lượng chữ số của N | **P3** | Vận dụng cao & Sáng tạo | Nhập vào một số nguyên dương $N$. Dùng vòng lặp `while` và p... |
| 11 | `sca_l08_p11_tro_choi_doan_so_nhi_phan` | Trò chơi đoán số nhị phân | **P3** | Vận dụng cao & Sáng tạo | Hỏi trong trường hợp xấu nhất, Bình phải đoán **nhiều nhất b... |
| 12 | `sca_l08_p12_day_so_collatz_3n_1` | Dãy số Collatz (3n + 1) | **P3** | Vận dụng cao & Sáng tạo | Nhập vào số tự nhiên $N$. Hãy in ra số bước biến đổi để $N$ ... |

---

## 2. Chi Tiết Từng Bài Tập Thực Hành

### Bài 1 (P0): Đếm xuôi bằng while
* **Mã bài toán:** `sca_l08_p01_dem_xuoi_bang_while`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Bạn robot đang tập đếm số từ 1 đến $N$ bằng vòng lặp `while`. Hãy giúp robot hoàn thành nhiệm vụ.
* **Nhiệm vụ:** Nhập vào số tự nhiên $N$. Dùng vòng lặp `while`, hãy in ra các số từ $1$ đến $N$ trên một dòng.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 100$).
* **Kết quả ra (Output):** Dãy số từ 1 đến $N$.
 ```python
 N = int(câu trả lời)
 i = 1
 while i <= N:
 print(i, end=" ")
 i = i + 1
 ```
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
```
### Output
```text
1 2 3 4 5
```
### Giải thích
In các số từ 1 đến 5 trên một dòng cách nhau khoảng trắng.

---

### Bài 2 (P0): Rút thăm đến khi trúng
* **Mã bài toán:** `sca_l08_p02_rut_tham_den_khi_trung`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Giờ ra chơi, Bo tổ chức trò bốc thăm trúng thưởng cho cả lớp thật rộn ràng. Bo bỏ vào hộp thật nhiều lá phiếu có ghi số, rồi bốc lên từng lá một. Cả lớp reo hò vì ai cũng mong chờ, và Bo sẽ dừng lại ngay khi bốc trúng lá phiếu ghi số **7**. Trò chơi vui quá nên ai cũng muốn biết kết quả. Hãy giúp Bo công bố kết quả bốc thăm.
* **Nhiệm vụ:** Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 7 thì dừng lại. Hãy in ra dòng chữ: `DA TRUNG THUONG!`
* **Dữ liệu vào (Input):** Một dãy các số nguyên, mỗi số trên một dòng, số cuối cùng chắc chắn là số 7.
* **Kết quả ra (Output):** In `DA TRUNG THUONG!` sau khi vòng lặp dừng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
10
25
7
```
### Output
```text
DA TRUNG THUONG!
```
### Giải thích
Sau khi nhập hai số 10 và 25, số thứ ba nhập vào là 7 nên vòng lặp dừng và in ra thông báo `DA TRUNG THUONG!`.

---

### Bài 3 (P0): Nhập số đến khi gặp số 0
* **Mã bài toán:** `sca_l08_p03_nhap_so_den_khi_gap_so_0`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Trò chơi nhập số: Người chơi nhập liên tục các số, chương trình đếm tổng số lượng số đã nhập cho đến khi gặp số 0 thì dừng lại.
* **Nhiệm vụ:** Viết chương trình nhập liên tiếp các số nguyên từ bàn phím. Việc nhập kết thúc khi người dùng nhập số 0. Hãy đếm xem người dùng đã nhập **bao nhiêu số** (không tính số 0 cuối cùng).
* **Dữ liệu vào (Input):** Một dãy các số nguyên, kết thúc bằng số 0.
* **Kết quả ra (Output):** Một số nguyên duy nhất là số lượng các số đã nhập trước số 0.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
12
8
0
```
### Output
```text
3
```
### Giải thích

Có 3 số: 5, 12, 8 đã được nhập trước khi gặp 0.

---

### Bài 4 (P1): Tổng dãy số kết thúc bằng 0
* **Mã bài toán:** `sca_l08_p04_tong_day_so_ket_thuc_bang_0`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Thí sinh nhập liên tiếp các số nguyên. Khi nhập số 0, chương trình dừng lại và in ra tổng tất cả các số đã nhập trước đó.
* **Nhiệm vụ:** Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 0. Hãy tính và in ra **tổng của tất cả các số** đã nhập.
* **Dữ liệu vào (Input):** Một dãy số nguyên kết thúc bằng 0.
* **Kết quả ra (Output):** Tổng các số.
* **Dữ liệu mẫu (Sample):**

### Input
```text
10
20
5
0
```
### Output
```text
35
```
### Giải thích

$10 + 20 + 5 = 35$.

---

### Bài 5 (P1): Đếm số chẵn đến khi gặp 0
* **Mã bài toán:** `sca_l08_p05_dem_so_chan_den_khi_gap_0`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Trong trò chơi đếm số, người dùng nhập các số liên tục. Chương trình đếm xem có bao nhiêu số chẵn đã được nhập, cho đến khi gặp số 0 thì dừng.
* **Nhiệm vụ:** Nhập liên tiếp các số nguyên từ bàn phím cho đến khi nhập số 0. Hãy đếm xem có bao nhiêu số chẵn trong các số đã nhập (không tính số 0).
* **Dữ liệu vào (Input):** Dãy số nguyên kết thúc bằng 0.
* **Kết quả ra (Output):** Số lượng số chẵn.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
7
8
12
0
```
### Output
```text
3
```
### Giải thích

Có 3 số chẵn là 4, 8, 12.

---

### Bài 6 (P1): Gấp đôi tờ giấy lên mặt trăng
* **Mã bài toán:** `sca_l08_p06_gap_doi_to_giay_len_mat_trang`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Trong giờ thủ công, bạn Mít lấy ra một tờ giấy siêu mỏng ban đầu có độ dày là $1\text{ mm}$ để làm thí nghiệm vui. Mít gấp đôi tờ giấy lại, và lạ chưa: cứ mỗi lần gấp đôi tờ giấy lại, độ dày của nó lại tăng gấp đôi ($2\text{ mm}, 4\text{ mm}, 8\text{ mm}, \dots$). Mít mơ ước chồng giấy của mình sẽ cao chạm tới mặt trăng. Hãy giúp Mít đếm số lần gấp.
* **Nhiệm vụ:** Hỏi cần phải gấp đôi tờ giấy ít nhất bao nhiêu lần để độ dày của nó đạt hoặc vượt quá độ cao $H\text{ mm}$?
* **Dữ liệu vào (Input):** Một số tự nhiên $H$ ($1 \le H \le 10^9$).
* **Kết quả ra (Output):** Số lần gấp đôi tối thiểu.
* **Dữ liệu mẫu (Sample):**

### Input
```text
10
```
### Output
```text
4
```
### Giải thích

Lần 1: 2mm, lần 2: 4mm, lần 3: 8mm, lần 4: 16mm ($\ge 10$). Cần 4 lần.

---

### Bài 7 (P2): Ống heo mua xe máy
* **Mã bài toán:** `sca_l08_p07_ong_heo_mua_xe_may`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Bác Nam có một chú heo đất thật xinh đặt ở góc nhà. Bác muốn tiết kiệm tiền để mua một chiếc xe máy có giá $P$ nghìn đồng cho cả gia đình đi chơi.
 * Ngày thứ nhất bác bỏ vào ống heo 1 nghìn đồng.
 * Ngày thứ hai bác bỏ vào 2 nghìn đồng.
 * Ngày thứ $k$ bác bỏ vào đúng $k$ nghìn đồng.
Mỗi tối bác đều lắc heo nghe kêu leng keng rất vui. Hãy giúp bác Nam đếm xem sau mấy ngày thì đủ tiền.
* **Nhiệm vụ:** Hỏi sau bao nhiêu ngày thì tổng số tiền trong ống heo của bác Nam đạt hoặc vượt quá $P$ nghìn đồng?
* **Dữ liệu vào (Input):** Một số tự nhiên $P$ ($1 \le P \le 10^7$).
* **Kết quả ra (Output):** Số ngày ít nhất.
* **Dữ liệu mẫu (Sample):**

### Input
```text
15
```
### Output
```text
5
```
### Giải thích

Ngày 1: 1k, ngày 2: 2k (tổng 3k), ngày 3: 3k (tổng 6k), ngày 4: 4k (tổng 10k), ngày 5: 5k (tổng 15k $\ge 15$). Sau 5 ngày.

---

### Bài 8 (P2): Tìm lũy thừa của 2 lớn hơn N
* **Mã bài toán:** `sca_l08_p08_tim_luy_thua_cua_2_lon_hon_n`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Tìm lũy thừa nhỏ nhất của 2 mà lớn hơn hoặc bằng số $N$ cho trước. Đây là bài toán cơ bản trong khoa học máy tính liên quan đến cấp phát bộ nhớ.
* **Nhiệm vụ:** Nhập vào số tự nhiên $N$. Hãy tìm số có dạng lũy thừa của 2 ($1, 2, 4, 8, 16, 32, \dots$) **nhỏ nhất mà lớn hơn $N$**.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Kết quả ra (Output):** Số lũy thừa của 2 tìm được.
* **Dữ liệu mẫu (Sample):**

### Input
```text
10
```
### Output
```text
16
```
### Giải thích

Lũy thừa của 2 gồm 1, 2, 4, 8, 16... Số nhỏ nhất $> 10$ là 16.

---

### Bài 9 (P2): Chú ốc sên leo cột cờ
* **Mã bài toán:** `sca_l08_p09_chu_oc_sen_leo_cot_co`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Sáng nay, chú ốc sên chăm chỉ thức dậy dưới chân một cột cờ cao $H$ mét trong sân trường và quyết tâm leo lên đỉnh để ngắm mây trời.
 * Ban ngày, chú ốc sên bò lên được $A$ mét.
 * Ban đêm, khi ngủ chú bị tụt xuống $B$ mét ($B < A$).
 * Khi chú chạm tới hoặc vượt qua đỉnh cột cờ vào ban ngày, chú sẽ dừng lại và cắm cờ (không bị tụt nữa).
Các bạn kiến đứng dưới cổ vũ ầm ĩ. Hãy giúp chú ốc sên tính xem mình leo mất mấy ngày.
* **Nhiệm vụ:** Hỏi chú ốc sên mất bao nhiêu ngày để leo lên tới đỉnh cột cờ?
* **Dữ liệu vào (Input):** Ba số tự nhiên $H, A, B$ trên 3 dòng ($1 \le B < A \le H \le 10^6$).
* **Kết quả ra (Output):** Số ngày để ốc sên chạm đỉnh.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
3
1
```
### Output
```text
2
```
### Giải thích

Ngày 1: leo lên 3m, đêm tụt 1m còn 2m.
Ngày 2: từ 2m leo thêm 3m lên 5m (chạm đỉnh ngay trong ngày!). Vậy mất 2 ngày.

---

### Bài 10 (P3): Đếm số lượng chữ số của N
* **Mã bài toán:** `sca_l08_p10_dem_so_luong_chu_so_cua_n`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Cho một số nguyên dương $N$. Hãy đếm xem số đó có bao nhiêu chữ số. Ví dụ: $12345$ có $5$ chữ số.
* **Nhiệm vụ:** Nhập vào một số nguyên dương $N$. Dùng vòng lặp `while` và phép chia nguyên `// 10`, hãy đếm xem số $N$ có bao nhiêu chữ số.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Kết quả ra (Output):** Số lượng chữ số của $N$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
2026
```
### Output
```text
4
```
### Giải thích

Với dữ liệu đầu vào là `2026`, kết quả thu được tương ứng là `4`.

---

### Bài 11 (P3): Trò chơi đoán số nhị phân
* **Mã bài toán:** `sca_l08_p11_tro_choi_doan_so_nhi_phan`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Giờ ra chơi, bạn An nghĩ ra một số bí mật từ 1 đến $N$ rồi đố cả lớp cùng đoán. Bạn Bình xung phong với chiến thuật rất hay tên là "Chặt đôi khoảng tìm kiếm" (Tìm kiếm nhị phân) để đoán số: mỗi câu hỏi Bình chia đôi khoảng đang xét ($N = N // 2$). Cả lớp nín thở theo dõi từng lượt đoán của Bình. Hãy giúp Bình tính trước xem mình cần đoán mấy lượt.
* **Nhiệm vụ:** Hỏi trong trường hợp xấu nhất, Bình phải đoán **nhiều nhất bao nhiêu lần** thì chắc chắn tìm ra số của An (lặp cho đến khi khoảng chỉ còn 1 số: $N == 1$)?
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Kết quả ra (Output):** Số bước đoán tối đa.
* **Dữ liệu mẫu (Sample):**

### Input
```text
8
```
### Output
```text
4
```
### Giải thích

Các bước: $8 \to 4 \to 2 \to 1$ (cần 4 bước).

---

### Bài 12 (P3): Dãy số Collatz (3n + 1)
* **Mã bài toán:** `sca_l08_p12_day_so_collatz_3n_1`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Bạn Tí vừa đọc được một câu đố toán học kỳ bí tên là giả thuyết Collatz trong quyển truyện tranh khoa học ở thư viện. Trò biến hình số bắt đầu từ số tự nhiên $N > 0$ như sau:
 * Nếu $N$ là số chẵn: chia đôi $N = N // 2$.
 * Nếu $N$ là số lẻ: nhân ba cộng một $N = 3 \times N + 1$.
 * Lặp lại quy trình trên cho đến khi số $N$ biến thành số $1$ thì dừng lại!
Tí khoe với cả lớp mà chưa bạn nào đếm đúng số bước. Hãy giúp Tí đếm số bước biến hình.
* **Nhiệm vụ:** Nhập vào số tự nhiên $N$. Hãy in ra số bước biến đổi để $N$ trở thành 1.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 10^5$).
* **Kết quả ra (Output):** Số bước biến đổi.
* **Dữ liệu mẫu (Sample):**

### Input
```text
6
```
### Output
```text
8
```
### Giải thích

Dãy biến đổi: $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$ (qua 8 bước biến đổi).

---
