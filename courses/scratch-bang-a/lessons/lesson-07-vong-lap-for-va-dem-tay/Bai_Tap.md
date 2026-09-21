# DANH SÁCH BÀI TẬP THỰC HÀNH: BÀI 07 — Vòng lặp for và hàm range

**Khóa học:** iKHEDU Scratch  
**Chuyên đề:** Chương 3: Cấu Trúc Rẽ Nhánh & Vòng Lặp  
> **Tổng số bài tập thực hành:** `14 bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  

---

## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện

| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |
|:---:|---|---|:---:|:---:|---|
| 1 | `sca_l07_p01_dem_sao_len_troi` | Đếm sao lên trời | **P0** | Khởi động & Quan sát | Nhập vào một số tự nhiên $N$. Hãy in các số từ $1$ đến $N$ t... |
| 2 | `sca_l07_p02_dem_nguoc_phong_ten_lua` | Đếm ngược phóng tên lửa | **P0** | Khởi động & Quan sát | Trước khi phóng tàu vũ trụ, đồng hồ đếm ngược từ $N$ về 1, c... |
| 3 | `sca_l07_p03_tong_cac_so_tu_nhien` | Tổng các số tự nhiên | **P0** | Khởi động & Quan sát | Nhập số nguyên dương $N$. Hãy tính tổng $S = 1 + 2 + 3 + \do... |
| 4 | `sca_l07_p04_bang_cuu_chuong` | Bảng cửu chương | **P1** | Cơ bản & Hoàn thành | Nhập vào một số nguyên $K$ ($1 \le K \le 9$). Hãy in ra bảng... |
| 5 | `sca_l07_p05_tong_so_chan_trong_doan` | Tổng số chẵn trong đoạn | **P1** | Cơ bản & Hoàn thành | Cho hai số nguyên dương $A$ và $B$ ($A \le B$). Hãy tính tổn... |
| 6 | `sca_l07_p06_dem_boi_so_cua_k` | Đếm bội số của K | **P1** | Cơ bản & Hoàn thành | Nhập vào 3 số tự nhiên $A, B, K$ ($A \le B$). Hãy đếm xem có... |
| 7 | `sca_l07_p07_tinh_giai_thua_n` | Tính giai thừa $N!$ | **P1** | Cơ bản & Hoàn thành | Nhập số tự nhiên $N$ ($1 \le N \le 20$). Hãy tính và in ra g... |
| 8 | `sca_l07_p08_day_so_cach_deu` | Dãy số cách đều | **P2** | Luyện tập & Vận dụng | Nhập vào số bắt đầu $a$, khoảng cách $d$ và số lượng phần tử... |
| 9 | `sca_l07_p09_tim_uoc_so_cua_n` | Tìm ước số của N | **P2** | Luyện tập & Vận dụng | Nhập vào số tự nhiên $N$. Hãy in ra tất cả các ước số dương ... |
| 10 | `sca_l07_p10_tong_binh_phuong` | Tổng bình phương | **P2** | Luyện tập & Vận dụng | Nhập vào số nguyên dương $N$. Hãy tính tổng:
 $$S = 1^2 + 2^... |
| 11 | `sca_l07_p11_doc_sach_moi_ngay` | Đọc sách mỗi ngày | **P3** | Vận dụng cao & Sáng tạo | Hỏi sau đúng bao nhiêu ngày thì Hoa sẽ đọc hết (hoặc vượt qu... |
| 12 | `sca_l07_p12_hang_cot_dau_sao` | Hàng cột dấu sao | **P3** | Vận dụng cao & Sáng tạo | Nhập vào số hàng $R$ và số cột $C$. Hãy in ra một hình chữ n... |
| 13 | `sca_l07_p13_tam_giac_vuong_dau_sao` | Tam giác vuông dấu sao | **P3** | Vận dụng cao & Sáng tạo | Nhập vào chiều cao $N$ của tam giác vuông. Hãy in ra tam giá... |
| 14 | `sca_l07_p14_tong_day_sieu_lon_khong_lap` | Tổng dãy siêu lớn không lặp | **P3** | Vận dụng cao & Sáng tạo | Hãy tính tổng $S = 1 + 2 + \dots + N$ với thời gian chạy tức... |

---

## 2. Chi Tiết Từng Bài Tập Thực Hành

### Bài 1 (P0): Đếm sao lên trời
* **Mã bài toán:** `sca_l07_p01_dem_sao_len_troi`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Đêm hè, người dùng ngước nhìn bầu trời đầy sao và bắt đầu đếm: 1, 2, 3... Hãy giúp in dãy số đếm sao từ 1 đến $N$.
* **Nhiệm vụ:** Nhập vào một số tự nhiên $N$. Hãy in các số từ $1$ đến $N$ trên cùng một dòng, mỗi số cách nhau một khoảng trắng.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 100$).
* **Kết quả ra (Output):** Dãy số từ 1 đến $N$.
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

Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `1 2 3 4 5`.

---

### Bài 2 (P0): Đếm ngược phóng tên lửa
* **Mã bài toán:** `sca_l07_p02_dem_nguoc_phong_ten_lua`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Trạm phóng tên lửa bắt đầu đếm ngược: 10, 9, 8... 1, PHONG! Hãy lập trình mô phỏng đếm ngược phóng tên lửa.
* **Nhiệm vụ:** Trước khi phóng tàu vũ trụ, đồng hồ đếm ngược từ $N$ về 1, cuối cùng in ra chữ `PHONG!`.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 20$).
* **Kết quả ra (Output):** Mỗi số trên một dòng, dòng cuối in `PHONG!`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3
```
### Output
```text
3
2
1
PHONG!
```
### Giải thích

Với dữ liệu đầu vào là `3`, kết quả thu được tương ứng là `3
2
1
PHONG!`.

---

### Bài 3 (P0): Tổng các số tự nhiên
* **Mã bài toán:** `sca_l07_p03_tong_cac_so_tu_nhien`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Nhà toán học Gauss khi còn đã tìm ra cách tính nhanh tổng các số từ 1 đến 100. Hãy viết chương trình tính tổng $1 + 2 + \dots + N$.
* **Nhiệm vụ:** Nhập số nguyên dương $N$. Hãy tính tổng $S = 1 + 2 + 3 + \dots + N$.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 10^5$).
* **Kết quả ra (Output):** Một số nguyên duy nhất là tổng $S$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
```
### Output
```text
10
```
### Giải thích

$1 + 2 + 3 + 4 = 10$.

---

### Bài 4 (P1): Bảng cửu chương
* **Mã bài toán:** `sca_l07_p04_bang_cuu_chuong`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Trong giờ Toán, cô giáo yêu cầu học sinh in bảng cửu chương của một số $K$ bất kỳ. Hãy viết chương trình in bảng nhân tự động.
* **Nhiệm vụ:** Nhập vào một số nguyên $K$ ($1 \le K \le 9$). Hãy in ra bảng cửu chương nhân của số $K$ từ 1 đến 10 theo đúng mẫu.
* **Dữ liệu vào (Input):** Một số nguyên $K$.
* **Kết quả ra (Output):** Gồm 10 dòng, mỗi dòng có định dạng: `K x i = [ket_qua]`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
```
### Output
```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```
### Giải thích

Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50`.

---

### Bài 5 (P1): Tổng số chẵn trong đoạn
* **Mã bài toán:** `sca_l07_p05_tong_so_chan_trong_doan`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Thí sinh muốn tính tổng tất cả các số chẵn nằm trong đoạn từ $A$ đến $B$. Hãy giúp bạn ấy viết chương trình tính nhanh.
* **Nhiệm vụ:** Cho hai số nguyên dương $A$ và $B$ ($A \le B$). Hãy tính tổng tất cả các số chẵn nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$ nếu chúng là số chẵn).
* **Dữ liệu vào (Input):** Hai số tự nhiên $A$ và $B$ trên 2 dòng ($1 \le A \le B \le 10^4$).
* **Kết quả ra (Output):** Tổng các số chẵn.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3
8
```
### Output
```text
18
```
### Giải thích

Các số chẵn là: 4, 6, 8. Tổng: $4 + 6 + 8 = 18$.

---

### Bài 6 (P1): Đếm bội số của K
* **Mã bài toán:** `sca_l07_p06_dem_boi_so_cua_k`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Cô giáo hỏi: "Trong đoạn từ $A$ đến $B$, có bao nhiêu số chia hết cho $K$?". Hãy viết chương trình đếm nhanh.
* **Nhiệm vụ:** Nhập vào 3 số tự nhiên $A, B, K$ ($A \le B$). Hãy đếm xem có bao nhiêu số trong đoạn $[A, B]$ chia hết cho $K$.
* **Dữ liệu vào (Input):** Ba số $A, B, K$ trên 3 dòng ($1 \le A \le B \le 10^5, 1 \le K \le 100$).
* **Kết quả ra (Output):** Số lượng số chia hết cho $K$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
1
10
3
```
### Output
```text
3
```
### Giải thích

Gồm các số: 3, 6, 9. Tổng cộng 3 số.

---

### Bài 7 (P1): Tính giai thừa $N!$
* **Mã bài toán:** `sca_l07_p07_tinh_giai_thua_n`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Cuối tuần, bạn Tý mở một gian hàng kẹo nhỏ trước cổng trường. Tý xếp kẹo thành từng hàng vui nhộn: hàng có số tự nhiên $N$ thì Tý nhân tất cả các số tự nhiên từ 1 đến $N$ với nhau. Cách nhân dồn này được gọi là giai thừa, ký hiệu là $N!$, và được tính bằng công thức:
 $$N! = 1 \times 2 \times 3 \times \dots \times N$$
Hôm nay khách đông quá, Tý tính không kịp. Hãy giúp Tý tính nhanh giá trị $N!$.
* **Nhiệm vụ:** Nhập số tự nhiên $N$ ($1 \le N \le 20$). Hãy tính và in ra giá trị $N!$.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$.
* **Kết quả ra (Output):** Giá trị $N!$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
```
### Output
```text
120
```
### Giải thích

$1 \times 2 \times 3 \times 4 \times 5 = 120$.

---

### Bài 8 (P2): Dãy số cách đều
* **Mã bài toán:** `sca_l07_p08_day_so_cach_deu`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Lớp bạn Na chơi trò nhảy ô số rất vui trên sân trường. Cả lớp thống nhất chọn số bắt đầu là số $a$, rồi mỗi bước nhảy phải dài đúng $d$ đơn vị, nghĩa là số tiếp theo hơn số đứng trước nó đúng $d$ đơn vị. Các bạn xếp thành một hàng dài và đọc to từng số mình nhảy tới. Na đếm mãi mà quên mất, hãy Na viết tiếp dãy số này.
* **Nhiệm vụ:** Nhập vào số bắt đầu $a$, khoảng cách $d$ và số lượng phần tử cần in $n$. Hãy in ra $n$ số đầu tiên của dãy trên một dòng, cách nhau dấu cách.
* **Dữ liệu vào (Input):** Ba số tự nhiên $a, d, n$ ($1 \le a, d, n \le 100$).
* **Kết quả ra (Output):** Dãy số gồm $n$ phần tử.
* **Dữ liệu mẫu (Sample):**

### Input
```text
2
3
5
```
### Output
```text
2 5 8 11 14
```
### Giải thích

Với dữ liệu đầu vào là `2
3
5`, kết quả thu được tương ứng là `2 5 8 11 14`.

---

### Bài 9 (P2): Tìm ước số của N
* **Mã bài toán:** `sca_l07_p09_tim_uoc_so_cua_n`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Thí sinh đang học về ước số trong giờ Toán. Hãy viết chương trình liệt kê tất cả các ước số của một số $N$ cho trước.
* **Nhiệm vụ:** Nhập vào số tự nhiên $N$. Hãy in ra tất cả các ước số dương của $N$ theo thứ tự tăng dần trên một dòng.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 10^4$).
* **Kết quả ra (Output):** Các ước số của $N$ cách nhau một dấu cách.
* **Dữ liệu mẫu (Sample):**

### Input
```text
12
```
### Output
```text
1 2 3 4 6 12
```
### Giải thích

Với dữ liệu đầu vào là `12`, kết quả thu được tương ứng là `1 2 3 4 6 12`.

---

### Bài 10 (P2): Tổng bình phương
* **Mã bài toán:** `sca_l07_p10_tong_binh_phuong`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Nhà toán học muốn tính tổng bình phương của các số từ 1 đến $N$: $1^2 + 2^2 + 3^2 + \dots + N^2$. Hãy viết chương trình tính.
* **Nhiệm vụ:** Nhập vào số nguyên dương $N$. Hãy tính tổng:
 $$S = 1^2 + 2^2 + 3^2 + \dots + N^2$$
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Kết quả ra (Output):** Một số nguyên duy nhất là tổng $S$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3
```
### Output
```text
14
```
### Giải thích

$1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$.

---

### Bài 11 (P3): Đọc sách mỗi ngày
* **Mã bài toán:** `sca_l07_p11_doc_sach_moi_ngay`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Nghỉ hè, bạn Hoa mượn ở thư viện một cuốn truyện thật dày có tổng cộng $N$ trang để rèn thói quen đọc sách mỗi ngày. Ngày thứ nhất Hoa đọc được 1 trang thật ngon lành.
 * Ngày thứ hai Hoa đọc được 2 trang.
 * Ngày thứ ba Hoa đọc được 3 trang.
 * Cứ như vậy, ngày thứ $k$ Hoa đọc được $k$ trang.
Hoa háo hức muốn biết mình đọc hết truyện sau mấy ngày. Hãy đếm số ngày.
* **Nhiệm vụ:** Hỏi sau đúng bao nhiêu ngày thì Hoa sẽ đọc hết (hoặc vượt quá) $N$ trang của cuốn sách?
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 10^4$).
* **Kết quả ra (Output):** Số ngày ít nhất để Hoa đọc xong cuốn sách.
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

Ngày 1: 1 trang; ngày 2: 2 trang (tổng 3); ngày 3: 3 trang (tổng 6); ngày 4: 4 trang (tổng 10 $\ge 10$). Sau 4 ngày đọc xong.

---

### Bài 12 (P3): Hàng cột dấu sao
* **Mã bài toán:** `sca_l07_p12_hang_cot_dau_sao`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Trong giờ tin học, thầy giáo yêu cầu vẽ một hình chữ nhật bằng dấu sao `*`. Hãy viết chương trình vẽ hình.
* **Nhiệm vụ:** Nhập vào số hàng $R$ và số cột $C$. Hãy in ra một hình chữ nhật đặc gồm các dấu sao `*` có kích thước $R$ hàng và $C$ cột.
* **Dữ liệu vào (Input):** Hai số tự nhiên $R$ và $C$ ($1 \le R, C \le 50$).
* **Kết quả ra (Output):** Hình chữ nhật dấu `*`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3
5
```
### Output
```text
*****
*****
*****
```
### Giải thích

Với dữ liệu đầu vào là `3
5`, kết quả thu được tương ứng là `*****
*****
*****`.

---

### Bài 13 (P3): Tam giác vuông dấu sao
* **Mã bài toán:** `sca_l07_p13_tam_giac_vuong_dau_sao`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Thí sinh muốn vẽ một tam giác vuông bằng dấu sao, mỗi hàng tăng thêm một ngôi sao. Hãy giúp bạn ấy.
* **Nhiệm vụ:** Nhập vào chiều cao $N$ của tam giác vuông. Hãy in ra tam giác vuông cân gồm các dấu sao theo mẫu:

 * Dòng 1 có 1 dấu `*`
 * Dòng 2 có 2 dấu `*`
 * ...
 * Dòng $N$ có $N$ dấu `*`.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 50$).
* **Kết quả ra (Output):** Tam giác vuông dấu `*`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
```
### Output
```text
*
**
***
****
```
### Giải thích

Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `*
**
***
****`.

---

### Bài 14 (P3): Tổng dãy siêu lớn không lặp
* **Mã bài toán:** `sca_l07_p14_tong_day_sieu_lon_khong_lap`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Trong hội thi lập trình của trường, ban giám khảo đố cả lớp một số $N$ cực lớn lên tới $10^9$ ($1$ tỷ) bạn nào cũng tròn mắt ngạc nhiên. Cô giáo dặn rằng nếu em dùng vòng lặp `for i in range(1, N + 1):` thì chương trình sẽ bị chạy quá thời gian quy định (Time Limit Exceeded - TLE) vì máy tính phải lặp 1 tỷ lần mất hơn 10 giây! Cả lớp đang loay hoay chưa biết làm sao cho nhanh. Hãy giúp cả lớp tìm cách tính thật nhanh.
* **Nhiệm vụ:** Hãy tính tổng $S = 1 + 2 + \dots + N$ với thời gian chạy tức thì ($< 0.001$ giây) bằng công thức toán học.
* **Dữ liệu vào (Input):** Một số nguyên $N$ ($1 \le N \le 10^9$).
* **Kết quả ra (Output):** Giá trị tổng $S$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
1000000000
```
### Output
```text
500000000500000000
```
### Giải thích

Với dữ liệu đầu vào là `1000000000`, kết quả thu được tương ứng là `500000000500000000`.

---
