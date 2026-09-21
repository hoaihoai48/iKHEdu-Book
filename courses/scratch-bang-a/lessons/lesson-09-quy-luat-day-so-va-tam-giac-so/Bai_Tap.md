# DANH SÁCH BÀI TẬP THỰC HÀNH: BÀI 09 — QUY LUẬT DÃY SỐ VÀ TAM GIÁC SỐ

**Khóa học:** iKHEDU Scratch  
**Chuyên đề:** Chương 4: Số Học & Thuật Toán Tách Số  
> **Tổng số bài tập thực hành:** `14 bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  

---

## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện

| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |
|:---:|---|---|:---:|:---:|---|
| 1 | `sca_l09_p01_trao_doi_hai_chiec_coc` | Tráo đổi hai chiếc cốc | **P0** | Khởi động & Quan sát | Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của ch... |
| 2 | `sca_l09_p02_day_so_nhan_doi` | Dãy số nhân đôi | **P0** | Khởi động & Quan sát | Nhập số nguyên $N$ ($1 \le N \le 30$). Hãy in ra $N$ số đầu ... |
| 3 | `sca_l09_p03_so_hang_day_cap_so_cong` | Số hạng dãy cấp số cộng | **P0** | Khởi động & Quan sát | Cho một dãy số cách đều có số đầu tiên là $u_1$ và khoảng cá... |
| 4 | `sca_l09_p04_so_fibonacci_thu_n` | Số Fibonacci thứ N | **P1** | Cơ bản & Hoàn thành | Dãy Fibonacci được định nghĩa: $F_1 = 1, F_2 = 1, F_n = F_{n... |
| 5 | `sca_l09_p05_day_so_dan_dau` | Dãy số đan dấu | **P1** | Cơ bản & Hoàn thành | Cho số nguyên dương $N$. Hãy tính tổng của dãy số đan dấu:
 ... |
| 6 | `sca_l09_p06_tong_tich_hai_so_lien_nhau` | Tổng tích hai số liền nhau | **P1** | Cơ bản & Hoàn thành | Cho số nguyên dương $N$. Hãy tính tổng:
 $$S = 1 \times 2 + ... |
| 7 | `sca_l09_p07_day_so_boi_ba_boi_nam` | Dãy số bội ba bội năm | **P1** | Cơ bản & Hoàn thành | Xét dãy các số nguyên dương chia hết cho 3 hoặc chia hết cho... |
| 8 | `sca_l09_p08_tam_giac_so_don_gian` | Tam giác số đơn giản | **P2** | Luyện tập & Vận dụng | In ra tháp tam giác số có $N$ dòng theo quy luật minh họa ở ... |
| 9 | `sca_l09_p09_tam_giac_sao_can` | Tam giác sao cân | **P2** | Luyện tập & Vận dụng | In ra một tháp sao tam giác cân đối xứng có độ cao $N$.
* **... |
| 10 | `sca_l09_p10_day_so_tam_giac_triangular_numbers` | Dãy số tam giác (triangular numbers) | **P2** | Luyện tập & Vận dụng | Cho số tự nhiên $K$. Hãy kiểm tra xem $K$ có phải là một "Số... |
| 11 | `sca_l09_p11_day_so_tribonacci` | Dãy số Tribonacci | **P3** | Vận dụng cao & Sáng tạo | Dãy Tribonacci mở rộng từ Fibonacci với 3 số đầu tiên là $1,... |
| 12 | `sca_l09_p12_ma_tran_so_ban_co_dan_xen` | Ma trận số bàn cờ đan xen | **P3** | Vận dụng cao & Sáng tạo | In ra một bảng ma trận vuông kích thước $N \times N$ gồm các... |
| 13 | `sca_l09_p13_tam_giac_floyd` | Tam giác Floyd | **P3** | Vận dụng cao & Sáng tạo | In ra tam giác Floyd có $N$ dòng (điền liên tiếp các số tự n... |
| 14 | `sca_l09_p14_tim_vi_tri_trong_day_tu_nhien_dai` | Tìm vị trí trong dãy tự nhiên dài | **P3** | Vận dụng cao & Sáng tạo | Cho số nguyên dương $K$ ($1 \le K \le 10^5$). Hãy xác định c... |

---

## 2. Chi Tiết Từng Bài Tập Thực Hành

### Bài 1 (P0): Tráo đổi hai chiếc cốc
* **Mã bài toán:** `sca_l09_p01_trao_doi_hai_chiec_coc`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Trong bài toán quản lý bộ nhớ, hai biến lưu trữ giá trị $A$ và $B$ cần được hoán đổi nội dung cho nhau. Bài toán yêu cầu tráo đổi dữ liệu của hai biến và xuất ra màn hình theo đúng thứ tự mới.
* **Nhiệm vụ:** Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của chúng và in ra theo thứ tự $A$ trước, $B$ sau.
* **Dữ liệu vào (Input):** Hai số nguyên $A$ và $B$ trên một dòng, cách nhau bởi khoảng trắng.
* **Kết quả ra (Output):** Giá trị mới của $A$ và $B$ sau khi hoán đổi.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5 12
```
### Output
```text
12 5
```
### Giải thích

Ban đầu $A=5, B=12$. Sau khi đổi $A=12, B=5$.

---

### Bài 2 (P0): Dãy số nhân đôi
* **Mã bài toán:** `sca_l09_p02_day_so_nhan_doi`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Thí sinh viết dãy số: bắt đầu từ 1, mỗi số tiếp theo gấp đôi số trước. Hãy in ra $N$ số đầu tiên của dãy.
* **Nhiệm vụ:** Nhập số nguyên $N$ ($1 \le N \le 30$). Hãy in ra $N$ số đầu tiên của dãy số nhân đôi: $1, 2, 4, 8, 16, 32, \dots$ trên cùng một dòng.
* **Dữ liệu vào (Input):** Một số nguyên $N$.
* **Kết quả ra (Output):** Dãy $N$ số, cách nhau bởi dấu cách.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
```
### Output
```text
1 2 4 8 16
```
### Giải thích

Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `1 2 4 8 16`.

---

### Bài 3 (P0): Số hạng dãy cấp số cộng
* **Mã bài toán:** `sca_l09_p03_so_hang_day_cap_so_cong`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Cấp số cộng là dãy số mà hiệu giữa hai số liên tiếp luôn bằng nhau. Cho số hạng đầu $u_1$ và công sai $d$, tìm số hạng thứ $N$.
* **Nhiệm vụ:** Cho một dãy số cách đều có số đầu tiên là $u_1$ và khoảng cách giữa 2 số liền kề là $d$. Cho số nguyên dương $N$. Hãy tìm số hạng thứ $N$ của dãy số.
* **Dữ liệu vào (Input):** Ba số nguyên $u_1, d, N$ ($1 \le u_1, d, N \le 10^6$).
* **Kết quả ra (Output):** Một số nguyên là số hạng thứ $N$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3 4 5
```
### Output
```text
19
```
### Giải thích

Dãy số là: 3, 7, 11, 15, 19. Số thứ 5 là 19.
* **Công thức toán học:** $u_N = u_1 + (N - 1) \times d$.

---

### Bài 4 (P1): Số Fibonacci thứ N
* **Mã bài toán:** `sca_l09_p04_so_fibonacci_thu_n`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Dãy Fibonacci: $1, 1, 2, 3, 5, 8, 13, \dots$ — mỗi số bằng tổng hai số liền trước. Đây là dãy số kỳ diệu xuất hiện khắp nơi trong tự nhiên, từ cánh hoa hướng dương đến vỏ ốc biển.
* **Nhiệm vụ:** Dãy Fibonacci được định nghĩa: $F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2}$ với $n \ge 3$. Nhập vào số tự nhiên $N$. Hãy tìm và in ra số Fibonacci thứ $N$.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 40$).
* **Kết quả ra (Output):** Giá trị $F_N$.
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

Dãy là 1, 1, 2, 3, 5, 8. Số thứ 6 là 8.

---

### Bài 5 (P1): Dãy số đan dấu
* **Mã bài toán:** `sca_l09_p05_day_so_dan_dau`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Thí sinh tạo ra dãy số với quy luật đặc biệt: số đầu tiên cho trước, các số tiếp theo tuân theo một công thức biến đổi nhất định. Hãy in $N$ số đầu tiên.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy tính tổng của dãy số đan dấu:
 $$S = 1 - 2 + 3 - 4 + 5 - 6 + \dots + (-1)^{N+1} N$$
* **Dữ liệu vào (Input):** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Kết quả ra (Output):** Giá trị của tổng $S$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
```
### Output
```text
3
```
### Giải thích

$1 - 2 + 3 - 4 + 5 = 3$.

---

### Bài 6 (P1): Tổng tích hai số liền nhau
* **Mã bài toán:** `sca_l09_p06_tong_tich_hai_so_lien_nhau`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Tính tổng hoặc tích của các cặp số liên tiếp trong một dãy số. Đây là bài toán luyện kỹ thuật cuốn chiếu (rolling variables).
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy tính tổng:
 $$S = 1 \times 2 + 2 \times 3 + 3 \times 4 + \dots + N \times (N + 1)$$
* **Dữ liệu vào (Input):** Một số nguyên dương $N$ ($1 \le N \le 10^5$).
* **Kết quả ra (Output):** Tổng $S$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3
```
### Output
```text
20
```
### Giải thích

$1 \times 2 + 2 \times 3 + 3 \times 4 = 2 + 6 + 12 = 20$.

---

### Bài 7 (P1): Dãy số bội ba bội năm
* **Mã bài toán:** `sca_l09_p07_day_so_boi_ba_boi_nam`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Liệt kê các số từ 1 đến $N$ chia hết cho 3 hoặc chia hết cho 5. Đây là bài toán kinh điển rèn luyện điều kiện logic phức hợp.
* **Nhiệm vụ:** Xét dãy các số nguyên dương chia hết cho 3 hoặc chia hết cho 5 theo thứ tự tăng dần: $3, 5, 6, 9, 10, 12, 15, \dots$. Cho số tự nhiên $N$. Hãy in ra $N$ số đầu tiên của dãy này.
* **Dữ liệu vào (Input):** Một số nguyên dương $N$ ($1 \le N \le 10^4$).
* **Kết quả ra (Output):** $N$ số đầu tiên của dãy trên một dòng, cách nhau bởi dấu cách.
* **Dữ liệu mẫu (Sample):**

### Input
```text
6
```
### Output
```text
3 5 6 9 10 12
```
### Giải thích

Với dữ liệu đầu vào là `6`, kết quả thu được tương ứng là `3 5 6 9 10 12`.

---

### Bài 8 (P2): Tam giác số đơn giản
* **Mã bài toán:** `sca_l09_p08_tam_giac_so_don_gian`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** In ra tam giác số với chiều cao $N$: hàng thứ $i$ chứa các số từ 1 đến $i$. Đây là bài toán kinh điển rèn luyện vòng lặp lồng nhau.
* **Nhiệm vụ:** In ra tháp tam giác số có $N$ dòng theo quy luật minh họa ở Sample 1 (dòng thứ $i$ in các số từ $1$ đến $i$).
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 20$).
* **Kết quả ra (Output):** Tháp tam giác số có $N$ dòng đúng quy luật trên.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
```
### Output
```text
1
1 2
1 2 3
1 2 3 4
```
### Giải thích

Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `1
1 2
1 2 3
1 2 3 4`.

---

### Bài 9 (P2): Tam giác sao cân
* **Mã bài toán:** `sca_l09_p09_tam_giac_sao_can`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Vẽ tam giác cân bằng dấu sao `*` với chiều cao $N$. Mỗi hàng cần tính số khoảng trắng và số sao phù hợp để hình tam giác cân đối.
* **Nhiệm vụ:** In ra một tháp sao tam giác cân đối xứng có độ cao $N$.
* **Quy luật:** Dòng thứ $i$ (từ 1 đến $N$) có $(N - i)$ dấu cách phía trước, tiếp theo là $(2i - 1)$ dấu sao `*`.
* **Dữ liệu vào (Input):** Độ cao $N$ của tam giác ($1 \le N \le 20$).
* **Kết quả ra (Output):** Tháp sao tam giác cân có $N$ dòng đúng quy luật trên.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3
```
### Output
```text
  *
 ***
*****
```
### Giải thích

Với dữ liệu đầu vào là `3`, kết quả thu được tương ứng là `*
 ***
*****`.

---

### Bài 10 (P2): Dãy số tam giác (triangular numbers)
* **Mã bài toán:** `sca_l09_p10_day_so_tam_giac_triangular_numbers`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Trong giờ kể chuyện lịch sử, cô giáo kể rằng người Hy Lạp cổ đại ngày xưa rất thích xếp các viên sỏi nhỏ thành hình tam giác đều để chơi:

 * Tầng 1: 1 viên
 * Tầng 2: 1 + 2 = 3 viên
 * Tầng 3: 1 + 2 + 3 = 6 viên
 * Tầng 4: 1 + 2 + 3 + 4 = 10 viên
Cả lớp ai cũng muốn tự xếp sỏi giống như vậy. Hãy giúp các bạn kiểm tra xem một số sỏi có xếp được thành hình tam giác không.
* **Nhiệm vụ:** Cho số tự nhiên $K$. Hãy kiểm tra xem $K$ có phải là một "Số tam giác" hay không (nghĩa là có tồn tại số nguyên dương $N$ sao cho $\frac{N(N+1)}{2} = K$)? Nếu có, in ra `YES` và số $N$, ngược lại in `NO`.
* **Dữ liệu vào (Input):** Một số nguyên $K$ ($1 \le K \le 10^9$).
* **Kết quả ra (Output):** `YES <N>` hoặc `NO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
10
```
### Output
```text
YES 4
```
### Giải thích

Với dữ liệu đầu vào là `10`, kết quả thu được tương ứng là `YES 4`.

---

### Bài 11 (P3): Dãy số Tribonacci
* **Mã bài toán:** `sca_l09_p11_day_so_tribonacci`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Dãy Tribonacci mở rộng từ Fibonacci: mỗi số bằng tổng ba số liền trước. Hãy tính số hạng thứ $N$ của dãy.
* **Nhiệm vụ:** Dãy Tribonacci mở rộng từ Fibonacci với 3 số đầu tiên là $1, 1, 2$. Kể từ số thứ tư, mỗi số bằng tổng của 3 số liền kề trước nó:
 $$T_1 = 1, T_2 = 1, T_3 = 2, \quad T_n = T_{n-1} + T_{n-2} + T_{n-3} \quad (n \ge 4)$$
 Nhập vào số tự nhiên $N$ ($1 \le N \le 35$). Hãy in ra số Tribonacci thứ $N$.
* **Dữ liệu vào (Input):** Một số nguyên $N$.
* **Kết quả ra (Output):** Giá trị $T_N$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
```
### Output
```text
7
```
### Giải thích

Dãy là: 1, 1, 2, 4, 7... Số thứ 5 là $1+2+4=7$.

---

### Bài 12 (P3): Ma trận số bàn cờ đan xen
* **Mã bài toán:** `sca_l09_p12_ma_tran_so_ban_co_dan_xen`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** In bảng số $N \times M$ với các giá trị xen kẽ theo quy luật bàn cờ: ô đen ô trắng luân phiên.
* **Nhiệm vụ:** In ra một bảng ma trận vuông kích thước $N \times N$ gồm các số $0$ và $1$ xếp so le như bàn cờ vua, với ô góc trên cùng bên trái luôn là số $1$.
* **Dữ liệu vào (Input):** Một số tự nhiên $N$ ($1 \le N \le 50$).
* **Kết quả ra (Output):** Ma trận vuông $N \times N$ đúng quy luật trên, mỗi dòng in $N$ số cách nhau một khoảng trắng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
```
### Output
```text
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
```
### Giải thích

Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1`.

---

### Bài 13 (P3): Tam giác Floyd
* **Mã bài toán:** `sca_l09_p13_tam_giac_floyd`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Trong câu lạc bộ toán vui, bạn Xoài đố cả nhóm xếp một tháp số thật đẹp. Luật chơi là tam giác Floyd: một tam giác số vuông được điền liên tiếp các số tự nhiên tăng dần bắt đầu từ 1. Các bạn xếp mãi mà tháp cứ lệch, ai cũng bật cười vui vẻ. Hãy giúp nhóm bạn Xoài xếp tháp số này cho ngay ngắn.
* **Nhiệm vụ:** In ra tam giác Floyd có $N$ dòng (điền liên tiếp các số tự nhiên từ 1 như minh họa ở Sample 1).
* **Dữ liệu vào (Input):** Một số nguyên dương $N$ ($1 \le N \le 20$).
* **Kết quả ra (Output):** Tam giác Floyd có $N$ dòng đúng quy luật trên.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
```
### Output
```text
1
2 3
4 5 6
7 8 9 10
```
### Giải thích

Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `1
2 3
4 5 6
7 8 9 10`.

---

### Bài 14 (P3): Tìm vị trí trong dãy tự nhiên dài
* **Mã bài toán:** `sca_l09_p14_tim_vi_tri_trong_day_tu_nhien_dai`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Giờ học vui, An lấy phấn viết liên tiếp các số tự nhiên bắt đầu từ 1 thành một dải số dài vô tận khắp sân trường:
 `123456789101112131415161718192021...`
Các bạn xúm lại đọc to từng chữ số, vừa đọc vừa cười khanh khách. Đến chữ số ở xa thì không ai đếm nổi bằng mắt nữa. Hãy tìm nhanh chữ số đó.
* **Nhiệm vụ:** Cho số nguyên dương $K$ ($1 \le K \le 10^5$). Hãy xác định chữ số thứ $K$ trong dải số trên là chữ số nào?
* **Dữ liệu vào (Input):** Một số nguyên $K$.
* **Kết quả ra (Output):** Chữ số tại vị trí $K$ (đếm từ 1).
* **Dữ liệu mẫu (Sample):**

### Input
```text
7
```
### Output
```text
7
```
### Giải thích

Ký tự thứ 7 là số 7.

---
