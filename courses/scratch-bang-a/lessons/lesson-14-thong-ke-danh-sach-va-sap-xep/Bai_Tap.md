# DANH SÁCH BÀI TẬP THỰC HÀNH: BÀI 14 — THỐNG KÊ DANH SÁCH VÀ THUẬT TOÁN SẮP XẾP

**Khóa học:** iKHEDU Scratch  
**Chuyên đề:** Chương 5: Danh Sách & Thống Kê Dữ Liệu  
> **Tổng số bài tập thực hành:** `14 bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  

---

## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện

| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |
|:---:|---|---|:---:|:---:|---|
| 1 | `sca_l14_p01_diem_so_cao_nhat_thap_nhat` | Điểm số cao nhất & thấp nhất | **P0** | Khởi động & Quan sát | Cho danh sách điểm thi của $N$ bạn học sinh. Hãy in ra điểm ... |
| 2 | `sca_l14_p02_sap_xep_tang_dan_don_gian` | Sắp xếp tăng dần đơn giản | **P0** | Khởi động & Quan sát | Cho dãy $N$ số nguyên. Hãy sắp xếp dãy số theo thứ tự tăng d... |
| 3 | `sca_l14_p03_diem_trung_binh_mon_hoc` | Điểm trung bình môn học | **P0** | Khởi động & Quan sát | Cho danh sách điểm kiểm tra của $N$ bài thi. Hãy tính điểm t... |
| 4 | `sca_l14_p04_sap_xep_giam_dan_bang_xep_hang` | Sắp xếp giảm dần bảng xếp hạng | **P1** | Cơ bản & Hoàn thành | Cho danh sách điểm số của $N$ thí sinh tham gia cuộc thi. Hã... |
| 5 | `sca_l14_p05_tim_so_lon_thu_nhi_trong_mang` | Tìm số lớn thứ nhì trong mảng | **P1** | Cơ bản & Hoàn thành | Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn thứ nhì trong dãy... |
| 6 | `sca_l14_p06_dem_so_luong_hoc_sinh_tren_diem_trung_binh` | Đếm số lượng học sinh trên điểm trung bình | **P1** | Cơ bản & Hoàn thành | Cho điểm thi của $N$ học sinh. Hãy đếm xem có bao nhiêu bạn ... |
| 7 | `sca_l14_p07_loc_bo_cac_so_trung_lap` | Lọc bỏ các số trùng lặp | **P1** | Cơ bản & Hoàn thành | Cho dãy gồm $N$ số nguyên có thể chứa nhiều số bị trùng lặp.... |
| 8 | `sca_l14_p08_diem_olympic_bo_max_bo_min` | Điểm olympic bỏ max bỏ min | **P2** | Luyện tập & Vận dụng | Cho $N$ điểm số. Hãy tính điểm chính thức của vận động viên ... |
| 9 | `sca_l14_p09_sap_xep_ten_theo_thu_tu_bang_chu_cai` | Sắp xếp tên theo thứ tự bảng chữ cái | **P2** | Luyện tập & Vận dụng | Cho danh sách gồm $N$ từ tiếng Anh. Hãy sắp xếp danh sách từ... |
| 10 | `sca_l14_p10_chenh_lech_nho_nhat_giua_hai_so` | Chênh lệch nhỏ nhất giữa hai số | **P2** | Luyện tập & Vận dụng | Cho dãy $N$ số nguyên đôi một khác nhau. Hãy tìm độ chênh lệ... |
| 11 | `sca_l14_p11_trung_vi_cua_day_so_median` | Trung vị của dãy số (Median) | **P3** | Vận dụng cao & Sáng tạo | Cho dãy $N$ số nguyên ($N$ lẻ). Hãy tìm số trung vị của dãy ... |
| 12 | `sca_l14_p12_so_xuat_hien_nhieu_lan_nhat_mode` | Số xuất hiện nhiều lần nhất (Mode) | **P3** | Vận dụng cao & Sáng tạo | Cho dãy $N$ số nguyên. Hãy tìm số xuất hiện nhiều lần nhất t... |
| 13 | `sca_l14_p13_ghep_hai_day_da_sap_xep` | Ghép hai dãy đã sắp xếp | **P3** | Vận dụng cao & Sáng tạo | Cho hai dãy số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ ... |
| 14 | `sca_l14_p14_xep_hang_mua_tra_sua_greedy` | Xếp hàng mua trà sữa (Greedy) | **P3** | Vận dụng cao & Sáng tạo | Hãy tìm cách sắp xếp thứ tự các bạn vào mua trà sữa sao cho ... |

---

## 2. Chi Tiết Từng Bài Tập Thực Hành

### Bài 1 (P0): Điểm số cao nhất & thấp nhất
* **Mã bài toán:** `sca_l14_p01_diem_so_cao_nhat_thap_nhat`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Xác định giá trị cực đại và cực tiểu trong tập số liệu điểm số là chỉ số đánh giá tổng quan phổ điểm của một đợt khảo sát.
* **Nhiệm vụ:** Cho danh sách điểm thi của $N$ bạn học sinh. Hãy in ra điểm số cao nhất và điểm số thấp nhất trong danh sách.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
 * Dòng 2: $N$ số nguyên là điểm của các bạn ($0 \le A_i \le 100$).
* **Kết quả ra (Output):** Điểm cao nhất, theo sau là điểm thấp nhất.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
80 95 60 100 75
```
### Output
```text
100 60
```
### Giải thích

Với dữ liệu đầu vào là `5
80 95 60 100 75`, kết quả thu được tương ứng là `100 60`.

---

### Bài 2 (P0): Sắp xếp tăng dần đơn giản
* **Mã bài toán:** `sca_l14_p02_sap_xep_tang_dan_don_gian`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Cô giáo cần sắp xếp lại danh sách điểm số của học sinh theo thứ tự. Yêu cầu sắp xếp dãy số tăng dần để phục vụ thống kê và tra cứu.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên. Hãy sắp xếp dãy số theo thứ tự tăng dần và nhân vật nói ra màn hình trên một dòng.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
 * Dòng 2: $N$ số nguyên.
* **Kết quả ra (Output):** Dãy số sau khi sắp xếp tăng dần, cách nhau bởi khoảng trắng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
9 2 7 1 5
```
### Output
```text
1 2 5 7 9
```
### Giải thích

Với dữ liệu đầu vào là `5
9 2 7 1 5`, kết quả thu được tương ứng là `1 2 5 7 9`.

---

### Bài 3 (P0): Điểm trung bình môn học
* **Mã bài toán:** `sca_l14_p03_diem_trung_binh_mon_hoc`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Tính trung bình cộng của một tập hợp giá trị đo lường là phép toán thống kê cơ bản nhất trong xử lý số liệu thực nghiệm.
* **Nhiệm vụ:** Cho danh sách điểm kiểm tra của $N$ bài thi. Hãy tính điểm trung bình cộng của các bài thi và in ra với đúng 2 chữ số sau dấu phẩy.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
 * Dòng 2: $N$ số thực hoặc số nguyên là điểm các bài thi.
* **Kết quả ra (Output):** Điểm trung bình cộng (định dạng `f"{tb:.2f}"`).
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
8 9 7 10
```
### Output
```text
8.50
```
### Giải thích

$(8 + 9 + 7 + 10) / 4 = 8.5$.

---

### Bài 4 (P1): Sắp xếp giảm dần bảng xếp hạng
* **Mã bài toán:** `sca_l14_p04_sap_xep_giam_dan_bang_xep_hang`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Cô giáo cần sắp xếp lại danh sách điểm số của học sinh theo thứ tự. Hãy viết chương trình sắp xếp.
* **Nhiệm vụ:** Cho danh sách điểm số của $N$ thí sinh tham gia cuộc thi. Hãy sắp xếp bảng điểm theo thứ tự từ cao xuống thấp (giảm dần) để trao giải.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Kết quả ra (Output):** Bảng điểm sắp xếp giảm dần trên một dòng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
20 80 40 100 60
```
### Output
```text
100 80 60 40 20
```
### Giải thích

Với dữ liệu đầu vào là `5
20 80 40 100 60`, kết quả thu được tương ứng là `100 80 60 40 20`.

---

### Bài 5 (P1): Tìm số lớn thứ nhì trong mảng
* **Mã bài toán:** `sca_l14_p05_tim_so_lon_thu_nhi_trong_mang`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn thứ nhì trong dãy số (nghĩa là giá trị lớn nhất trong số các phần tử nhỏ hơn giá trị cực đại). Nếu tất cả các phần tử trong mảng đều bằng nhau, in ra `KHONG CO`.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Kết quả ra (Output):** Giá trị lớn thứ nhì, hoặc `KHONG CO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
10 20 20 15 5
```
### Output
```text
15
```
### Giải thích

Số lớn nhất là 20. Số lớn thứ hai nhỏ hơn 20 là 15.

---

### Bài 6 (P1): Đếm số lượng học sinh trên điểm trung bình
* **Mã bài toán:** `sca_l14_p06_dem_so_luong_hoc_sinh_tren_diem_trung_binh`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** So sánh từng phần tử với giá trị trung bình của cả tập hợp giúp đánh giá độ phân tán và chất lượng của các chỉ số thành phần.
* **Nhiệm vụ:** Cho điểm thi của $N$ học sinh. Hãy đếm xem có bao nhiêu bạn học sinh có điểm số lớn hơn hoặc bằng điểm trung bình cộng của cả lớp.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số thực.
* **Kết quả ra (Output):** Số lượng học sinh đạt điểm $\ge$ điểm trung bình.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
8 6 10 4
```
### Output
```text
2
```
### Giải thích

Điểm TB: $(8+6+10+4)/4 = 7.0$. Các bạn có điểm $\ge 7$ là 8 và 10 (có 2 bạn).

---

### Bài 7 (P1): Lọc bỏ các số trùng lặp
* **Mã bài toán:** `sca_l14_p07_loc_bo_cac_so_trung_lap`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Loại bỏ các phần tử trùng lặp và sắp xếp lại tập hợp là bước tiền xử lý quan trọng trong làm sạch dữ liệu.
* **Nhiệm vụ:** Cho dãy gồm $N$ số nguyên có thể chứa nhiều số bị trùng lặp. Hãy lọc bỏ các phần tử trùng lặp và in ra các số độc nhất theo thứ tự tăng dần.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Kết quả ra (Output):** Các số độc nhất sắp xếp tăng dần trên một dòng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
7
3 1 4 1 5 9 2
```
### Output
```text
1 2 3 4 5 9
```
### Giải thích

Với dữ liệu đầu vào là `7
3 1 4 1 5 9 2`, kết quả thu được tương ứng là `1 2 3 4 5 9`.

---

### Bài 8 (P2): Điểm olympic bỏ max bỏ min
* **Mã bài toán:** `sca_l14_p08_diem_olympic_bo_max_bo_min`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Cuối tuần này, trường em tổ chức hội thi Bơi lội Olympic thật vui nhộn. Có $N$ giám khảo cùng ngồi chấm điểm cho mỗi người dùng ($N \ge 3$). Để cho thật công bằng, điểm số chính thức của vận động viên sẽ là trung bình cộng sau khi đã **bỏ đi một điểm cao nhất và một điểm thấp nhất**. Trọng tài đang lúng túng với đống bảng điểm nên hãy bác ấy tính điểm thật chính xác.
* **Nhiệm vụ:** Cho $N$ điểm số. Hãy tính điểm chính thức của vận động viên (làm tròn 2 chữ số thập phân).
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($3 \le N \le 1000$).
 * Dòng 2: $N$ số thực cách nhau bởi khoảng trắng.
* **Kết quả ra (Output):** Điểm trung bình sau khi loại bỏ 1 điểm max và 1 điểm min.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
7.0 9.0 8.0 10.0 6.0
```
### Output
```text
8.00
```
### Giải thích

Bỏ min là 6.0, bỏ max là 10.0. Còn lại: 7.0, 8.0, 9.0. Trung bình là 8.00.

---

### Bài 9 (P2): Sắp xếp tên theo thứ tự bảng chữ cái
* **Mã bài toán:** `sca_l14_p09_sap_xep_ten_theo_thu_tu_bang_chu_cai`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Cô giáo cần sắp xếp lại danh sách điểm số của học sinh theo thứ tự. Hãy viết chương trình sắp xếp.
* **Nhiệm vụ:** Cho danh sách gồm $N$ từ tiếng Anh. Hãy sắp xếp danh sách từ theo thứ tự từ điển A-Z (tăng dần).
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
 * Dòng 2: $N$ từ viết thường cách nhau bởi khoảng trắng.
* **Kết quả ra (Output):** Danh sách từ sau khi sắp xếp trên một dòng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
orange apple banana grape
```
### Output
```text
apple banana grape orange
```
### Giải thích

Với dữ liệu đầu vào là `4
orange apple banana grape`, kết quả thu được tương ứng là `apple banana grape orange`.

---

### Bài 10 (P2): Chênh lệch nhỏ nhất giữa hai số
* **Mã bài toán:** `sca_l14_p10_chenh_lech_nho_nhat_giua_hai_so`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Thí sinh cần tìm giá trị lớn nhất hoặc nhỏ nhất trong một tập dữ liệu. Hãy viết chương trình tìm kiếm.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên đôi một khác nhau. Hãy tìm độ chênh lệch nhỏ nhất giữa 2 phần tử bất kỳ trong dãy (tức là giá trị $|A_i - A_j|$ nhỏ nhất với $i \ne j$).
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Kết quả ra (Output):** Độ chênh lệch nhỏ nhất.
* **Dữ liệu mẫu (Sample):**

### Input
```text
4
10 1 8 15
```
### Output
```text
2
```
### Giải thích

Sắp xếp: [1, 8, 10, 15]. Chênh lệch giữa 8 và 10 là $

---

### Bài 11 (P3): Trung vị của dãy số (Median)
* **Mã bài toán:** `sca_l14_p11_trung_vi_cua_day_so_median`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Giờ ra chơi, các người dùng xếp thành một hàng dọc gồm $N$ bạn, trong đó $N$ là số lẻ. Cô giáo muốn tìm bạn đứng chính giữa sau khi cả hàng đã xếp theo chiều cao tăng dần, và bạn đó được gọi là trung vị của dãy: tức là phần tử nằm chính giữa sau khi dãy đã được sắp xếp tăng dần. Các bạn cứ nhốn nháo đổi chỗ mãi không xong. Hãy giúp cô tìm ra bạn đứng ở vị trí chính giữa.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên ($N$ lẻ). Hãy tìm số trung vị của dãy số.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên lẻ $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Kết quả ra (Output):** Giá trị trung vị.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5
10 2 8 4 6
```
### Output
```text
6
```
### Giải thích

Sắp xếp: [2, 4, 6, 8, 10]. Số chính giữa là 6.

---

### Bài 12 (P3): Số xuất hiện nhiều lần nhất (Mode)
* **Mã bài toán:** `sca_l14_p12_so_xuat_hien_nhieu_lan_nhat_mode`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Tìm giá trị có tần số xuất hiện cao nhất (giá trị mốt - mode) là bài toán thống kê đặc trưng để nhận diện xu hướng dữ liệu phổ biến nhất.
* **Nhiệm vụ:** Cho dãy $N$ số nguyên. Hãy tìm số xuất hiện nhiều lần nhất trong dãy. Nếu có nhiều số có cùng số lần xuất hiện nhiều nhất, hãy in ra số có giá trị nhỏ nhất trong các số đó.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.
* **Kết quả ra (Output):** Số xuất hiện nhiều nhất.
* **Dữ liệu mẫu (Sample):**

### Input
```text
7
2 3 5 2 3 7 2
```
### Output
```text
2
```
### Giải thích

Với dữ liệu đầu vào là `7
2 3 5 2 3 7 2`, kết quả thu được tương ứng là `2`.

---

### Bài 13 (P3): Ghép hai dãy đã sắp xếp
* **Mã bài toán:** `sca_l14_p13_ghep_hai_day_da_sap_xep`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Cô giáo cần sắp xếp lại danh sách điểm số của học sinh theo thứ tự. Hãy viết chương trình sắp xếp.
* **Nhiệm vụ:** Cho hai dãy số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy ghép hai dãy lại thành một dãy duy nhất gồm $(N + M)$ phần tử cũng được sắp xếp tăng dần.
* **Dữ liệu vào (Input):** * Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 10^5$).
 * Dòng 2: $N$ số nguyên của dãy $A$.
 * Dòng 3: $M$ số nguyên của dãy $B$.
* **Kết quả ra (Output):** Dãy hợp nhất gồm $(N + M)$ phần tử tăng dần trên một dòng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3 4
1 4 7
2 3 5 8
```
### Output
```text
1 2 3 4 5 7 8
```
### Giải thích

Với dữ liệu đầu vào là `3 4
1 4 7
2 3 5 8`, kết quả thu được tương ứng là `1 2 3 4 5 7 8`.

---

### Bài 14 (P3): Xếp hàng mua trà sữa (Greedy)
* **Mã bài toán:** `sca_l14_p14_xep_hang_mua_tra_sua_greedy`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Giờ tan học, có $N$ bạn học sinh cùng ríu rít xếp hàng mua trà sữa ở căng tin trường. Bạn thứ $i$ cần $T_i$ phút để người bán hàng pha chế xong cốc trà sữa của mình. Tổng thời gian chờ đợi của tất cả các bạn sẽ là tổng thời gian mà mỗi bạn phải đứng xếp hàng chờ cho đến khi nhận được trà sữa. Nhìn hàng dài mà các bạn ai cũng mỏi chân, hãy cô bán hàng tìm cách xếp hàng sao cho mọi người chờ ít nhất.
* **Nhiệm vụ:** Hãy tìm cách sắp xếp thứ tự các bạn vào mua trà sữa sao cho **tổng thời gian chờ đợi của tất cả các bạn là NHỎ NHẤT CÓ THỂ**. Hãy in ra tổng thời gian chờ đợi nhỏ nhất đó.
* **Dữ liệu vào (Input):** * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên $T_i$ ($1 \le T_i \le 1000$).
* **Kết quả ra (Output):** Một số nguyên duy nhất là tổng thời gian chờ đợi nhỏ nhất.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3
3 1 2
```
### Output
```text
10
```
### Giải thích

Sắp xếp người làm nhanh lên trước: thời gian làm lần lượt là 1, 2, 3.
- Bạn 1 chờ 1 phút.
- Bạn 2 chờ $1 + 2 = 3$ phút.
- Bạn 3 chờ $1 + 2 + 3 = 6$ phút.
Tổng thời gian chờ: $1 + 3 + 6 = 10$ phút (tối ưu nhất).

---
