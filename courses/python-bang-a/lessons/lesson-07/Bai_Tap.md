# Danh Sách Bài Tập Thực Hành: Bài 07: Quy luật dãy số và tam giác số

> Nguồn problems: l09 | Tổng 14 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-3
* P1 (Cơ bản): Bài 4-6
* P2 (Luyện tập): Bài 7-9
* P3 (Vận dụng): Bài 10-14
---

### Bài 1 (P0): Tráo đổi hai chiếc cốc
* **Mã bài toán:** `pya_l09_p01_trao_doi_hai_chiec_coc`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong bài toán quản lý bộ nhớ, hai biến lưu trữ giá trị $A$ và $B$ cần được hoán đổi nội dung cho nhau. Bài toán yêu cầu tráo đổi dữ liệu của hai biến và xuất ra màn hình theo đúng thứ tự mới.
* **Nhiệm vụ:** Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của chúng và in ra theo thứ tự $A$ trước, $B$ sau.
* **Input:** Hai số nguyên $A$ và $B$ trên một dòng, cách nhau bởi khoảng trắng.
* **Output:** Giá trị mới của $A$ và $B$ sau khi hoán đổi.
* **Sample:** ### Input
```text
5 12
```
### Output
```text
12 5
```
### Giải thích

Ban đầu $A=5, B=12$. Sau khi đổi $A=12, B=5$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 2 (P0): Số hạng dãy cấp số cộng
* **Mã bài toán:** `pya_l09_p03_so_hang_day_cap_so_cong`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Cấp số cộng là dãy số mà hiệu giữa hai số liên tiếp luôn bằng nhau. Cho số hạng đầu $u_1$ và công sai $d$, tìm số hạng thứ $N$.
* **Nhiệm vụ:** Cho một dãy số cách đều có số đầu tiên là $u_1$ và khoảng cách giữa 2 số liền kề là $d$. Cho số nguyên dương $N$. Hãy tìm số hạng thứ $N$ của dãy số.
* **Input:** Ba số nguyên $u_1, d, N$ ($1 \le u_1, d, N \le 10^6$).
* **Output:** Một số nguyên là số hạng thứ $N$.
* **Sample:** ### Input
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
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 3 (P0): Số Fibonacci thứ N
* **Mã bài toán:** `pya_l09_p04_so_fibonacci_thu_n`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Dãy Fibonacci: $1, 1, 2, 3, 5, 8, 13, \dots$ — mỗi số bằng tổng hai số liền trước. Đây là dãy số kỳ diệu xuất hiện khắp nơi trong tự nhiên, từ cánh hoa hướng dương đến vỏ ốc biển.
* **Nhiệm vụ:** Dãy Fibonacci được định nghĩa: $F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2}$ với $n \ge 3$. Nhập vào số tự nhiên $N$. Hãy tìm và in ra số Fibonacci thứ $N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 40$).
* **Output:** Giá trị $F_N$.
* **Sample:** ### Input
```text
6
```
### Output
```text
8
```
### Giải thích

Dãy là 1, 1, 2, 3, 5, 8. Số thứ 6 là 8.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 4 (P1): Tổng tích hai số liền nhau
* **Mã bài toán:** `pya_l09_p06_tong_tich_hai_so_lien_nhau`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Tính tổng hoặc tích của các cặp số liên tiếp trong một dãy số. Đây là bài toán luyện kỹ thuật cuốn chiếu.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy tính tổng:
 $$S = 1 \times 2 + 2 \times 3 + 3 \times 4 + \dots + N \times (N + 1)$$
* **Input:** Một số nguyên dương $N$ ($1 \le N \le 10^5$).
* **Output:** Tổng $S$.
* **Sample:** ### Input
```text
3
```
### Output
```text
20
```
### Giải thích

$1 \times 2 + 2 \times 3 + 3 \times 4 = 2 + 6 + 12 = 20$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 5 (P1): Tam giác số đơn giản
* **Mã bài toán:** `pya_l09_p08_tam_giac_so_don_gian`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** In ra tam giác số với chiều cao $N$: hàng thứ $i$ chứa các số từ 1 đến $i$. Đây là bài toán kinh điển rèn luyện vòng lặp lồng nhau.
* **Nhiệm vụ:** In ra tháp tam giác số có $N$ dòng theo quy luật minh họa ở Sample 1 (dòng thứ $i$ in các số từ $1$ đến $i$).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 20$).
* **Output:** Tháp tam giác số có $N$ dòng đúng quy luật trên.
* **Sample:** ### Input
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
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 6 (P1): Ma trận số bàn cờ đan xen
* **Mã bài toán:** `pya_l09_p12_ma_tran_so_ban_co_dan_xen`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** In bảng số $N \times M$ với các giá trị xen kẽ theo quy luật bàn cờ: ô đen ô trắng luân phiên.
* **Nhiệm vụ:** In ra một bảng ma trận vuông kích thước $N \times N$ gồm các số $0$ và $1$ xếp so le như bàn cờ vua, với ô góc trên cùng bên trái luôn là số $1$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 50$).
* **Output:** Ma trận vuông $N \times N$ đúng quy luật trên, mỗi dòng in $N$ số cách nhau một khoảng trắng.
* **Sample:** ### Input
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
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 7 (P2): Dãy số nhân đôi
* **Mã bài toán:** `pya_l09_p02_day_so_nhan_doi`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Thí sinh viết dãy số: bắt đầu từ 1, mỗi số tiếp theo gấp đôi số trước. Hãy in ra $N$ số đầu tiên của dãy.
* **Nhiệm vụ:** Nhập số nguyên $N$ ($1 \le N \le 30$). Hãy in ra $N$ số đầu tiên của dãy số nhân đôi: $1, 2, 4, 8, 16, 32, \dots$ trên cùng một dòng.
* **Input:** Một số nguyên $N$.
* **Output:** Dãy $N$ số, cách nhau bởi dấu cách.
* **Sample:** ### Input
```text
5
```
### Output
```text
1 2 4 8 16
```
### Giải thích

Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `1 2 4 8 16`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 8 (P2): Dãy số đan dấu
* **Mã bài toán:** `pya_l09_p05_day_so_dan_dau`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Thí sinh tạo ra dãy số với quy luật đặc biệt: số đầu tiên cho trước, các số tiếp theo tuân theo một công thức biến đổi nhất định. Hãy in $N$ số đầu tiên.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy tính tổng của dãy số đan dấu:
 $$S = 1 - 2 + 3 - 4 + 5 - 6 + \dots + (-1)^{N+1} N$$
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** Giá trị của tổng $S$.
* **Sample:** ### Input
```text
5
```
### Output
```text
3
```
### Giải thích

$1 - 2 + 3 - 4 + 5 = 3$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 9 (P2): Tam giác sao cân
* **Mã bài toán:** `pya_l09_p09_tam_giac_sao_can`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Vẽ tam giác cân bằng dấu sao `*` với chiều cao $N$. Mỗi hàng cần tính số khoảng trắng và số sao phù hợp để hình tam giác cân đối.
* **Nhiệm vụ:** In ra một tháp sao tam giác cân đối xứng có độ cao $N$.
* **Quy luật:** Dòng thứ $i$ (từ 1 đến $N$) có $(N - i)$ dấu cách phía trước, tiếp theo là $(2i - 1)$ dấu sao `*`.
* **Input:** Độ cao $N$ của tam giác ($1 \le N \le 20$).
* **Output:** Tháp sao tam giác cân có $N$ dòng đúng quy luật trên.
* **Sample:** ### Input
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
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 10 (P3): Dãy số tam giác
* **Mã bài toán:** `pya_l09_p10_day_so_tam_giac_triangular_numbers`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong giờ kể chuyện lịch sử, cô giáo kể rằng người Hy Lạp cổ đại ngày xưa rất thích xếp các viên sỏi nhỏ thành hình tam giác đều để chơi:
 * Tầng 1: 1 viên
 * Tầng 2: 1 + 2 = 3 viên
 * Tầng 3: 1 + 2 + 3 = 6 viên
 * Tầng 4: 1 + 2 + 3 + 4 = 10 viên
Cả lớp ai cũng muốn tự xếp sỏi giống như vậy. Hãy giúp các bạn kiểm tra xem một số sỏi có xếp được thành hình tam giác không.
* **Nhiệm vụ:** Cho số tự nhiên $K$. Hãy kiểm tra xem $K$ có phải là một "Số tam giác" hay không (nghĩa là có tồn tại số nguyên dương $N$ sao cho $\frac{N(N+1)}{2} = K$)? Nếu có, in ra `YES` và số $N$, ngược lại in `NO`.
* **Input:** Một số nguyên $K$ ($1 \le K \le 10^9$).
* **Output:** `YES <N>` hoặc `NO`.
* **Sample:** ### Input
```text
10
```
### Output
```text
YES 4
```
### Giải thích

Với dữ liệu đầu vào là `10`, kết quả thu được tương ứng là `YES 4`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 11 (P3): Tìm vị trí trong dãy tự nhiên dài
* **Mã bài toán:** `pya_l09_p14_tim_vi_tri_trong_day_tu_nhien_dai`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Giờ học vui, An lấy phấn viết liên tiếp các số tự nhiên bắt đầu từ 1 thành một dải số dài vô tận khắp sân trường:
 `123456789101112131415161718192021...`
Các bạn xúm lại đọc to từng chữ số, vừa đọc vừa cười khanh khách. Đến chữ số ở xa thì không ai đếm nổi bằng mắt nữa. Hãy tìm nhanh chữ số đó.
* **Nhiệm vụ:** Cho số nguyên dương $K$ ($1 \le K \le 10^5$). Hãy xác định chữ số thứ $K$ trong dải số trên là chữ số nào?
* **Input:** Một số nguyên $K$.
* **Output:** Chữ số tại vị trí $K$ (đếm từ 1).
* **Sample:** ### Input
```text
7
```
### Output
```text
7
```
### Giải thích

Ký tự thứ 7 là số 7.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 12 (P3): Tam giác Floyd
* **Mã bài toán:** `pya_l09_p13_tam_giac_floyd`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong câu lạc bộ toán vui, bạn Xoài đố cả nhóm xếp một tháp số thật đẹp. Luật chơi là tam giác Floyd: một tam giác số vuông được điền liên tiếp các số tự nhiên tăng dần bắt đầu từ 1. Các bạn xếp mãi mà tháp cứ lệch, ai cũng bật cười vui vẻ. Hãy giúp nhóm bạn Xoài xếp tháp số này cho ngay ngắn.
* **Nhiệm vụ:** In ra tam giác Floyd có $N$ dòng (điền liên tiếp các số tự nhiên từ 1 như minh họa ở Sample 1).
* **Input:** Một số nguyên dương $N$ ($1 \le N \le 20$).
* **Output:** Tam giác Floyd có $N$ dòng đúng quy luật trên.
* **Sample:** ### Input
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
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 13 (P3): Dãy số bội ba bội năm
* **Mã bài toán:** `pya_l09_p07_day_so_boi_ba_boi_nam`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Liệt kê các số từ 1 đến $N$ chia hết cho 3 hoặc chia hết cho 5. Đây là bài toán kinh điển rèn luyện điều kiện logic phức hợp.
* **Nhiệm vụ:** Xét dãy các số nguyên dương chia hết cho 3 hoặc chia hết cho 5 theo thứ tự tăng dần: $3, 5, 6, 9, 10, 12, 15, \dots$. Cho số tự nhiên $N$. Hãy in ra $N$ số đầu tiên của dãy này.
* **Input:** Một số nguyên dương $N$ ($1 \le N \le 10^4$).
* **Output:** $N$ số đầu tiên của dãy trên một dòng, cách nhau bởi dấu cách.
* **Sample:** ### Input
```text
6
```
### Output
```text
3 5 6 9 10 12
```
### Giải thích

Với dữ liệu đầu vào là `6`, kết quả thu được tương ứng là `3 5 6 9 10 12`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 14 (P3): Dãy số Tribonacci
* **Mã bài toán:** `pya_l09_p11_day_so_tribonacci`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Dãy Tribonacci mở rộng từ Fibonacci: mỗi số bằng tổng ba số liền trước. Hãy tính số hạng thứ $N$ của dãy.
* **Nhiệm vụ:** Dãy Tribonacci mở rộng từ Fibonacci với 3 số đầu tiên là $1, 1, 2$. Kể từ số thứ tư, mỗi số bằng tổng của 3 số liền kề trước nó:
 $$T_1 = 1, T_2 = 1, T_3 = 2, \quad T_n = T_{n-1} + T_{n-2} + T_{n-3} \quad (n \ge 4)$$
 Nhập vào số tự nhiên $N$ ($1 \le N \le 35$). Hãy in ra số Tribonacci thứ $N$.
* **Input:** Một số nguyên $N$.
* **Output:** Giá trị $T_N$.
* **Sample:** ### Input
```text
5
```
### Output
```text
7
```
### Giải thích

Dãy là: 1, 1, 2, 4, 7... Số thứ 5 là $1+2+4=7$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---
