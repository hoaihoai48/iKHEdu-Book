# Danh Sách Bài Tập Thực Hành: Bài 11: Danh sách và thao tác cơ bản

> Nguồn problems: l16 | Tổng 26 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-6
* P1 (Cơ bản): Bài 7-12
* P2 (Luyện tập): Bài 13-18
* P3 (Vận dụng): Bài 19-26
---

### Bài 1 (P0): Thưởng đọc sách
* **Mã bài toán:** `pya_l16_p23_thuong_doc_sach`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Để khuyến khích đọc sách, thư viện treo giải: bạn nào đọc hết $N$ quyển sách sẽ được thưởng sao. Quyển thứ 1 được 1 sao, quyển thứ 2 được 2 sao, cứ thế quyển thứ $N$ được $N$ sao. An quyết tâm đọc hết $N$ quyển và muốn biết trước mình sẽ nhận được bao nhiêu sao.
* **Nhiệm vụ:** Cho số $N$. Hãy tính tổng số sao từ quyển 1 đến quyển $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^{12}$).
* **Output:** In ra một số nguyên duy nhất là tổng số sao.
* **Sample:** ### Input

```text
5
```

### Output

```text
15
```

### Giải thích

$1 + 2 + 3 + 4 + 5 = 15$ sao.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 10^4$. Cộng từng quyển vẫn kịp giờ.

* Subtask 2 (50% số điểm): $10^4 < N \le 10^{12}$. Cộng từng quyển sẽ không kịp, cần công thức tính nhanh.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 2 (P0): Số ghế đối xứng
* **Mã bài toán:** `pya_l16_p21_so_ghe_doi_xung`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Rạp xiếc trong thành phố có một hàng ghế đặc biệt: những ghế mang số đối xứng (đọc từ trái sang phải hay từ phải sang trái đều giống nhau, như 121 hay 44) được gọi là ghế vàng và ngồi xem rất rõ. Mi mua được vé ghế số $N$ và muốn biết ghế của mình có phải ghế vàng không.
* **Nhiệm vụ:** Hãy kiểm tra số $N$ có phải số đối xứng không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** In ra `YES` hoặc `NO`.
* **Sample:** ### Input

```text
121
```

### Output

```text
YES
```

### Giải thích

Số 121 đọc xuôi là 121, đọc ngược cũng là 121 nên đây là ghế vàng.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 9999$.

* Subtask 2 (50% số điểm): $10000 \le N \le 10^{18}$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 3 (P0): Tìm vị trí đầu tiên của X
* **Mã bài toán:** `pya_l16_p08_tim_vi_tri_dau_tien_cua_x`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên và số $X$. Hãy tìm vị trí (chỉ số index từ 0) xuất hiện **đầu tiên** của số $X$ trong dãy. Nếu số $X$ không có trong dãy, in ra `-1`.
* **Input:** * Dòng 1: Hai số nguyên $N$ và $X$.
 * Dòng 2: $N$ số nguyên.
* **Output:** Vị trí index đầu tiên của $X$, hoặc `-1`.
* **Sample:** ### Input
```text
5 7
3 5 7 9 7
```
### Output
```text
2
```
### Giải thích

Với dữ liệu đầu vào là `5 7
3 5 7 9 7`, kết quả thu được tương ứng là `2`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 4 (P0): Nhập dãy số & in phần tử đầu - cuối
* **Mã bài toán:** `pya_l16_p01_nhap_day_so_in_phan_tu_dau_cuoi`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Truy xuất phần tử biên (đầu dãy và cuối dãy) là thao tác truy cập nhanh có độ phức tạp $\mathcal{O}(1)$ trên cấu trúc dữ liệu danh sách.
* **Nhiệm vụ:** Cho một dãy gồm $N$ số nguyên. Hãy in ra phần tử đầu tiên và phần tử cuối cùng của dãy số đó.
* **Input:** * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
 * Dòng 2: Gồm $N$ số nguyên cách nhau bởi khoảng trắng.
* **Output:** In phần tử đầu tiên và phần tử cuối cùng trên một dòng, cách nhau một khoảng trắng.
* **Sample:** ### Input
```text
5
10 25 3 47 99
```
### Output
```text
10 99
```
### Giải thích

Với dữ liệu đầu vào là `5
10 25 3 47 99`, kết quả thu được tương ứng là `10 99`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 5 (P0): Tính tổng các phần tử trong dãy
* **Mã bài toán:** `pya_l16_p03_tinh_tong_cac_phan_tu_trong_day`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.
* **Nhiệm vụ:** Cho một dãy gồm $N$ số nguyên. Hãy tính tổng tất cả các phần tử trong dãy số.
* **Input:** * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).
* **Output:** Tổng các phần tử trong dãy.
* **Sample:** ### Input
```text
4
10 20 30 40
```
### Output
```text
100
```
### Giải thích

Với dữ liệu đầu vào là `4
10 20 30 40`, kết quả thu được tương ứng là `100`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 6 (P0): Tìm số lớn nhất & nhỏ nhất
* **Mã bài toán:** `pya_l16_p05_tim_so_lon_nhat_nho_nhat`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn nhất và giá trị nhỏ nhất trong dãy số.
* **Input:** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Output:** Giá trị lớn nhất, theo sau là giá trị nhỏ nhất, cách nhau một khoảng trắng.
* **Sample:** ### Input
```text
5
12 5 89 3 45
```
### Output
```text
89 3
```
### Giải thích

Với dữ liệu đầu vào là `5
12 5 89 3 45`, kết quả thu được tương ứng là `89 3`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 7 (P1): In dãy số theo thứ tự đảo ngược
* **Mã bài toán:** `pya_l16_p06_in_day_so_theo_thu_tu_dao_nguoc`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Đảo ngược thứ tự các phần tử trong danh sách dữ liệu thường được yêu cầu khi cần phân tích luồng sự kiện theo trình tự thời gian từ mới nhất về cũ nhất.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên. Hãy in ra dãy số theo thứ tự ngược lại (từ phần tử cuối cùng về phần tử đầu tiên).
* **Input:** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi đảo ngược trên một dòng.
* **Sample:** ### Input
```text
4
1 2 3 4
```
### Output
```text
4 3 2 1
```
### Giải thích

Với dữ liệu đầu vào là `4
1 2 3 4`, kết quả thu được tương ứng là `4 3 2 1`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 8 (P1): Đếm số lần xuất hiện của X
* **Mã bài toán:** `pya_l16_p07_dem_so_lan_xuat_hien_cua_x`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Đếm số lần xuất hiện của một giá trị mục tiêu trong danh sách hỗ trợ xác định tần suất dữ liệu và kiểm tra trùng lặp.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên và một số nguyên $X$. Hãy đếm xem số $X$ xuất hiện bao nhiêu lần trong dãy số.
* **Input:** * Dòng 1: Hai số nguyên $N$ và $X$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Output:** Số lần xuất hiện của $X$.
* **Sample:** ### Input
```text
6 5
5 2 5 7 5 9
```
### Output
```text
3
```
### Giải thích

Với dữ liệu đầu vào là `6 5
5 2 5 7 5 9`, kết quả thu được tương ứng là `3`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 9 (P1): Thay thế tất cả số âm bằng số 0
* **Mã bài toán:** `pya_l16_p11_thay_the_tat_ca_so_am_bang_so_0`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong chuẩn hóa tín hiệu số, các giá trị âm không hợp lệ thường được quy chuẩn về ngưỡng giá trị sàn bằng 0.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên gồm cả số âm và số dương. Hãy thay thế toàn bộ các số âm trong dãy bằng số 0 và in ra dãy mới.
* **Input:** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi thay thế.
* **Sample:** ### Input
```text
5
3 -5 8 -2 0
```
### Output
```text
3 0 8 0 0
```
### Giải thích

Với dữ liệu đầu vào là `5
3 -5 8 -2 0`, kết quả thu được tương ứng là `3 0 8 0 0`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 10 (P1): Heo đất tiết kiệm
* **Mã bài toán:** `pya_l16_p15_heo_dat_tiet_kiem`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Na có một chú heo đất màu hồng rất xinh. Mỗi ngày, nhỏ bỏ vào heo $A$ đồng tiền ăn sáng để dành. Đặc biệt, cứ vào các ngày chẵn (ngày thứ 2, 4, 6, ...) nhỏ còn được mẹ thưởng thêm $B$ đồng vì chăm ngoan. Sau $N$ ngày, Na hồi hộp muốn biết trong heo có tất cả bao nhiêu tiền.
* **Nhiệm vụ:** Hãy tính tổng số tiền trong heo đất sau $N$ ngày.
* **Input:** Một dòng gồm ba số nguyên $N$, $A$, $B$ ($1 \le N \le 10^6$, $1 \le A, B \le 10^4$).
* **Output:** In ra một số nguyên duy nhất là tổng số tiền.
* **Sample:** ### Input

```text
5 10 3
```

### Output

```text
56
```

### Giải thích

5 ngày, mỗi ngày 10 đồng được 50 đồng. Các ngày chẵn là ngày 2 và ngày 4, được thưởng thêm $2 \times 3 = 6$ đồng. Tổng cộng $50 + 6 = 56$ đồng.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 1000$. Vòng lặp từng ngày vẫn chạy kịp.

* Subtask 2 (50% số điểm): $1000 < N \le 10^6$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 11 (P1): Đếm số lượng số chẵn trong mảng
* **Mã bài toán:** `pya_l16_p04_dem_so_luong_so_chan_trong_mang`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Thống kê số lượng phần tử chẵn trong mảng dữ liệu là bài toán lọc dữ liệu cơ bản để phân loại luồng số liệu đầu vào.
* **Nhiệm vụ:** Cho một dãy gồm $N$ số nguyên dương. Hãy đếm xem có bao nhiêu số chẵn trong dãy.
* **Input:** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Output:** Số lượng số chẵn.
* **Sample:** ### Input
```text
5
2 5 8 10 13
```
### Output
```text
3
```
### Giải thích

Với dữ liệu đầu vào là `5
2 5 8 10 13`, kết quả thu được tương ứng là `3`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 12 (P1): Thêm điểm vào danh sách
* **Mã bài toán:** `pya_l16_p02_them_diem_vao_danh_sach`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Lớp của bạn Na vừa làm bài kiểm tra nên cô giáo có một danh sách điểm kiểm tra ban đầu. Sáng nay, bạn Tí nộp bài muộn và cô đã chấm cho bạn điểm $X$. Cô muốn viết thêm điểm $X$ này vào cuối danh sách mà không làm mất điểm của các bạn khác. Hãy giúp cô thêm điểm mới vào danh sách.
* **Nhiệm vụ:** Cho danh sách các số nguyên ban đầu và số $X$. Hãy thêm $X$ vào cuối danh sách và in ra toàn bộ danh sách mới.
* **Input:** * Dòng 1: Danh sách các số nguyên cách nhau bởi khoảng trắng.
 * Dòng 2: Số nguyên $X$.
* **Output:** Danh sách các số sau khi thêm $X$, cách nhau bởi khoảng trắng.
* **Sample:** ### Input
```text
8 9 7 10
9
```
### Output
```text
8 9 7 10 9
```
### Giải thích

Với dữ liệu đầu vào là `8 9 7 10
9`, kết quả thu được tương ứng là `8 9 7 10 9`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 13 (P2): Chèn số vào vị trí K
* **Mã bài toán:** `pya_l16_p12_chen_so_vao_vi_tri_k`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Chèn thêm phần tử mới vào một vị trí chỉ định trong danh sách là thao tác cấu trúc dữ liệu phổ biến khi bổ sung dữ liệu có thứ tự.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên, số nguyên $X$ và vị trí index $K$ ($0 \le K \le N$). Hãy chèn số $X$ vào đúng vị trí $K$ của dãy số và in ra dãy mới gồm $(N + 1)$ phần tử.
* **Input:** * Dòng 1: Số nguyên $N$.
 * Dòng 2: $N$ số nguyên.
 * Dòng 3: Hai số nguyên $X$ và $K$.
* **Output:** Dãy số sau khi chèn.
* **Sample:** ### Input
```text
4
10 20 30 40
99 1
```
### Output
```text
10 99 20 30 40
```
### Giải thích

Với dữ liệu đầu vào là `4
10 20 30 40
99 1`, kết quả thu được tương ứng là `10 99 20 30 40`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 14 (P2): Mật khẩu bị ẩn
* **Mã bài toán:** `pya_l16_p18_mat_khau_bi_an`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bo đặt mật khẩu cho nhật ký điện tử của mình bằng một chuỗi gồm chữ cái và chữ số, ví dụ như `Abc123x`. Để kiểm tra độ mạnh, nhỏ muốn biết mật khẩu của mình chứa bao nhiêu ký tự là chữ số. Hãy đếm.
* **Nhiệm vụ:** Cho chuỗi $S$. Hãy đếm xem có bao nhiêu ký tự trong $S$ là chữ số từ `0` đến `9`.
* **Input:** Một dòng chứa chuỗi $S$ ($1 \le |S| \le 10^5$, gồm chữ cái, chữ số và khoảng trắng).
* **Output:** In ra một số nguyên duy nhất là số lượng chữ số.
* **Sample:** ### Input

```text
Abc123x
```

### Output

```text
3
```

### Giải thích

Trong chuỗi `Abc123x` có 3 ký tự là chữ số: `1`, `2` và `3`.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le |S| \le 100$.

* Subtask 2 (50% số điểm): $100 < |S| \le 10^5$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 15 (P2): Xếp hàng chiều cao
* **Mã bài toán:** `pya_l16_p22_xep_hang_chieu_cao`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Giờ thể dục, thầy giáo yêu cầu $N$ người dùng xếp thành một hàng từ thấp đến cao để tập đội hình đội ngũ. Thầy đọc chiều cao của từng bạn và nhờ Na xếp lại giúp. Hãy in ra chiều cao của các bạn theo thứ tự tăng dần.
* **Nhiệm vụ:** Cho chiều cao của $N$ bạn. Hãy in ra chiều cao theo thứ tự tăng dần, cách nhau bởi một dấu cách.
* **Input:** Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên là chiều cao ($100 \le A_i \le 200$).
* **Output:** In ra $N$ số theo thứ tự tăng dần trên một dòng.
* **Sample:** ### Input

```text
5
160 150 175 165 155
```

### Output

```text
150 155 160 165 175
```

### Giải thích

Sắp xếp 5 chiều cao từ thấp đến cao được dãy 150 155 160 165 175.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 100$.

* Subtask 2 (50% số điểm): $100 < N \le 10^5$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 16 (P2): Xóa phần tử đầu tiên bằng X
* **Mã bài toán:** `pya_l16_p10_xoa_phan_tu_dau_tien_bang_x`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Xóa phần tử đầu tiên thỏa mãn điều kiện là thao tác cơ bản trong quản lý danh sách đợi và cập nhật trạng thái dữ liệu.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên và số $X$. Nếu $X$ có trong dãy, hãy xóa phần tử đầu tiên có giá trị bằng $X$ và in ra dãy số còn lại. Nếu $X$ không có trong dãy, in ra `KHONG CO`.
* **Input:** * Dòng 1: Hai số $N, X$.
 * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi xóa, hoặc `KHONG CO`.
* **Sample:** ### Input
```text
5 3
1 3 5 3 7
```
### Output
```text
1 5 3 7
```
### Giải thích

Với dữ liệu đầu vào là `5 3
1 3 5 3 7`, kết quả thu được tương ứng là `1 5 3 7`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 17 (P2): Xoay vòng danh sách sang phải
* **Mã bài toán:** `pya_l16_p13_xoay_vong_danh_sach_sang_phai`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Các người dùng lớp 3A đang chơi trò đoàn tàu, mỗi bạn cầm một tấm thẻ số và nối đuôi nhau thành một hàng dài. Cô giáo hô hiệu lệnh "xoay phải $K$ vị trí", nghĩa là cả lớp sẽ nhấc $K$ phần tử cuối cùng của mảng đem gắn lên đầu mảng. Các người dùng xoay xong thì rối hết cả hàng mà vẫn cười khúc khích. Hãy giúp cả lớp tìm xem sau trò chơi, hàng thẻ số sẽ trông như thế nào.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên và số $K$ ($1 \le K \le N \le 10^5$). Hãy in ra dãy số sau khi xoay phải $K$ vị trí.
* **Input:** * Dòng 1: Hai số $N$ và $K$.
 * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi xoay phải.
* **Sample:** ### Input
```text
5 2
1 2 3 4 5
```
### Output
```text
4 5 1 2 3
```
### Giải thích

Hai phần tử cuối là 4, 5 được đưa lên đầu.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 18 (P2): Tách mảng chẵn và mảng lẻ
* **Mã bài toán:** `pya_l16_p09_tach_mang_chan_va_mang_le`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Tách một mảng tổng hợp thành hai luồng số chẵn và số lẻ độc lập giúp tối ưu hóa việc phân luồng xử lý dữ liệu chuyên biệt.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên. Hãy tách dãy thành 2 danh sách: một danh sách gồm các số chẵn, một danh sách gồm các số lẻ (giữ nguyên thứ tự xuất hiện ban đầu).
* **Input:** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Output:** * Dòng 1: Các số chẵn (cách nhau bởi khoảng trắng).
 * Dòng 2: Các số lẻ (cách nhau bởi khoảng trắng).
* **Sample:** ### Input
```text
6
1 4 7 8 2 9
```
### Output
```text
4 8 2
1 7 9
```
### Giải thích

Với dữ liệu đầu vào là `6
1 4 7 8 2 9`, kết quả thu được tương ứng là `4 8 2
1 7 9`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 19 (P3): Đếm từ dài
* **Mã bài toán:** `pya_l16_p24_dem_tu_dai`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Cô giáo ra trò chơi: cho một câu văn và một số $K$, bạn nào đếm đúng có bao nhiêu từ dài hơn $K$ ký tự sẽ được điểm 10. Từ là một nhóm ký tự liền nhau, các từ cách nhau bởi dấu cách. Na nhờ em đếm giúp để chắc chắn được điểm 10.
* **Nhiệm vụ:** Cho số $K$ và câu văn $S$. Hãy đếm số từ có độ dài lớn hơn $K$.
* **Input:** Dòng 1: số nguyên $K$ ($0 \le K \le 100$). Dòng 2: câu văn $S$ ($1 \le |S| \le 10^4$).
* **Output:** In ra một số nguyên duy nhất là số từ thỏa mãn.
* **Sample:** ### Input

```text
3
Hom nay Bin di hoc cung ban Na
```

### Output

```text
1
```

### Giải thích

Các từ là: Hom, nay, Bin, di, hoc, cung, ban, Na. Chỉ có từ `cung` dài 4 ký tự, lớn hơn 3 nên đáp án là 1.
* **Ràng buộc:** Subtask 1 (50% số điểm): $|S| \le 100$.

* Subtask 2 (50% số điểm): $100 < |S| \le 10^4$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 20 (P3): Bảng điểm lớp học
* **Mã bài toán:** `pya_l16_p17_bang_diem_lop_hoc`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Cuối tuần, cô giáo muốn tổng kết điểm thi đua của cả lớp. Cả lớp có $N$ bạn, mỗi bạn có một điểm số là số nguyên từ 0 đến 10. Cô nhờ Na tìm giúp điểm cao nhất, điểm thấp nhất và điểm trung bình của cả lớp để ghi vào sổ thi đua.
* **Nhiệm vụ:** Cho điểm của $N$ bạn. Hãy in ra điểm cao nhất, điểm thấp nhất và điểm trung bình (lấy 1 chữ số thập phân).
* **Input:** Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên là điểm của các bạn ($0 \le A_i \le 10$).
* **Output:** In ra 3 dòng: dòng 1 là điểm cao nhất, dòng 2 là điểm thấp nhất, dòng 3 là điểm trung bình với đúng 1 chữ số thập phân.
* **Sample:** ### Input

```text
5
8 7 10 6 9
```

### Output

```text
10
6
8.0
```

### Giải thích

Điểm cao nhất là 10, thấp nhất là 6. Trung bình là $(8 + 7 + 10 + 6 + 9) / 5 = 8.0$.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 100$.

* Subtask 2 (50% số điểm): $100 < N \le 10^5$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 21 (P3): Cặp số có tổng bằng S
* **Mã bài toán:** `pya_l16_p14_cap_so_co_tong_bang_s`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.
* **Nhiệm vụ:** Cho dãy gồm $N$ số nguyên đôi một khác nhau và một số nguyên mục tiêu $S$. Hãy đếm xem có bao nhiêu cặp chỉ số $(i, j)$ với $i < j$ thỏa mãn:
 $$A_i + A_j = S$$
* **Input:** * Dòng 1: Hai số nguyên $N$ và $S$ ($1 \le N \le 10^4, |S| \le 10^9$).
 * Dòng 2: $N$ số nguyên.
* **Output:** Số lượng cặp thỏa mãn.
* **Sample:** ### Input
```text
5 10
2 4 6 8 3
```
### Output
```text
2
```
### Giải thích

Có 2 cặp là $(2, 8)$ và $(4, 6)$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 22 (P3): Vé số may mắn
* **Mã bài toán:** `pya_l16_p16_ve_so_may_man`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Hội chợ trường em tổ chức trò chơi quay số trúng thưởng. Mỗi người dùng được phát một tấm vé in một số tự nhiên $N$. Ban tổ chức gọi đó là vé may mắn nếu tổng các chữ số của $N$ chia hết cho $7$. Một khối hộp cầm vé số $1234$ trên tay, hồi hộp không biết mình có trúng thưởng không.
* **Nhiệm vụ:** Hãy kiểm tra xem tấm vé số $N$ có phải là vé may mắn không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** In ra `YES` hoặc `NO`.
* **Sample:** ### Input

```text
1234
```

### Output

```text
NO
```

### Giải thích

Tổng các chữ số là $1 + 2 + 3 + 4 = 10$. Vì 10 không chia hết cho 7 nên đáp án là `NO`. (Ví dụ vé số $16$ có tổng là 7 nên đáp án là `YES`.)
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 9999$ (tối đa 4 chữ số).

* Subtask 2 (50% số điểm): $10000 \le N \le 10^{18}$ (tối đa 19 chữ số).

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 23 (P3): Chuyến tàu vượt đèo
* **Mã bài toán:** `pya_l16_p26_chuyen_tau_vuot_deo`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Một đoàn tàu đồ chơi chạy qua $N$ ngọn đèo, ngọn thứ $i$ cao $A_i$ mét. Học sinh lái tàu reo lên mỗi khi tàu chinh phục một ngọn đèo cao hơn tất cả các ngọn đèo đã đi qua trước đó (ngọn đầu tiên luôn được reo một lần). Hãy đếm xem nhỏ reo lên tất cả bao nhiêu lần.
* **Nhiệm vụ:** Cho dãy $N$ số. Hãy đếm số lần phần tử lớn hơn tất cả các phần tử đứng trước nó.
* **Input:** Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).
* **Output:** In ra một số nguyên duy nhất là số lần reo.
* **Sample:** ### Input

```text
6
1 3 5 2 4 7
```

### Output

```text
4
```

### Giải thích

Các kỷ lục mới là 1, 3, 5 rồi 7, tổng cộng 4 lần reo.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 1000$.

* Subtask 2 (50% số điểm): $1000 < N \le 10^5$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 24 (P3): Tổng chữ số lớn nhất
* **Mã bài toán:** `pya_l16_p20_tong_chu_so_lon_nhat`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong giờ ra chơi, các bạn thi nhau khoe số báo danh của mình. Bạn nào có tổng các chữ số lớn nhất sẽ được làm lớp trưởng ngày mai. Có $N$ bạn tham gia, mỗi bạn có một số báo danh. Nếu hai bạn có tổng chữ số bằng nhau thì bạn có số báo danh nhỏ hơn sẽ thắng.
* **Nhiệm vụ:** Hãy tìm số báo danh của bạn thắng cuộc.
* **Input:** Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số tự nhiên ($0 \le A_i \le 10^{18}$).
* **Output:** In ra số báo danh thắng cuộc.
* **Sample:** ### Input

```text
5
12 99 45 100 38
```

### Output

```text
99
```

### Giải thích

Tổng chữ số của 12 là 3, của 99 là 18, của 45 là 9, của 100 là 1, của 38 là 11. Tổng lớn nhất là 18 của số 99.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 1000$, $A_i \le 9999$.

* Subtask 2 (50% số điểm): $1000 < N \le 10^5$, $A_i \le 10^{18}$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 25 (P3): Đếm kẹo chẵn lẻ
* **Mã bài toán:** `pya_l16_p19_dem_keo_chan_le`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Liên hoan cuối năm, cô giáo mua $N$ gói kẹo, mỗi gói có $A_i$ viên kẹo. Cô muốn chia các gói kẹo thành hai mâm: mâm gói chẵn (số kẹo là số chẵn) và mâm gói lẻ (số kẹo là số lẻ). Hãy giúp cô đếm xem mỗi mâm có bao nhiêu gói.
* **Nhiệm vụ:** Cho $N$ số nguyên. Hãy đếm số lượng số chẵn và số lượng số lẻ, in trên một dòng.
* **Input:** Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên ($0 \le A_i \le 10^9$).
* **Output:** In ra hai số trên một dòng: số lượng số chẵn trước, số lượng số lẻ sau.
* **Sample:** ### Input

```text
6
1 2 3 4 5 6
```

### Output

```text
3 3
```

### Giải thích

Các số chẵn là 2, 4, 6 (3 gói). Các số lẻ là 1, 3, 5 (3 gói).
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 1000$.

* Subtask 2 (50% số điểm): $1000 < N \le 10^5$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 26 (P3): Đếm sao nguyên tố
* **Mã bài toán:** `pya_l16_p25_dem_sao_nguyen_to`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Đêm hội trăng rằm, các người dùng dán lên bầu trời giấy $N$ ngôi sao được đánh số từ 1 đến $N$. Thầy giáo đố: có bao nhiêu ngôi sao mang số nguyên tố (số chỉ chia hết cho 1 và chính nó, số 1 không phải số nguyên tố)? Bạn nào đếm đúng sẽ được rước đèn đầu tiên.
* **Nhiệm vụ:** Cho số $N$. Hãy đếm có bao nhiêu số nguyên tố từ 1 đến $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** In ra một số nguyên duy nhất là số lượng số nguyên tố.
* **Sample:** ### Input

```text
10
```

### Output

```text
4
```

### Giải thích

Từ 1 đến 10 có 4 số nguyên tố là 2, 3, 5 và 7.
* **Ràng buộc:** Subtask 1 (50% số điểm): $1 \le N \le 1000$. Kiểm tra từng số vẫn kịp.

* Subtask 2 (50% số điểm): $1000 < N \le 10^6$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---
