# DANH SÁCH BÀI TẬP THỰC HÀNH: BÀI 16 — DUYỆT CHUỖI, BIẾN ĐỔI KÝ TỰ VÀ TÁCH TỪ

**Khóa học:** iKHEDU Scratch  
**Chuyên đề:** Chương 6: Xử Lý Chuỗi Ký Tự  
> **Tổng số bài tập thực hành:** `24 bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  

---

## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện

| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |
|:---:|---|---|:---:|:---:|---|
| 1 | `sca_l16_p01_in_tung_chu_cai_xuong_dong` | In từng chữ cái xuống dòng | **P0** | Khởi động & Quan sát | Nhập vào một từ $S$. Hãy in ra từng chữ cái của từ đó, mỗi c... |
| 2 | `sca_l16_p02_chuyen_toan_bo_thanh_chu_hoa` | Chuyển toàn bộ thành chữ hoa | **P0** | Khởi động & Quan sát | Nhập một dòng văn bản $S$. Hãy chuyển tất cả các chữ cái tro... |
| 3 | `sca_l16_p03_dem_ky_tu_a_ca_hoa_lan_thuong` | Đếm ký tự 'A' (cả hoa lẫn thường) | **P0** | Khởi động & Quan sát | Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu chữ cái `'... |
| 4 | `sca_l16_p04_dem_chu_cai_in_hoa_in_thuong` | Đếm chữ cái in hoa & in thường | **P0** | Khởi động & Quan sát | Cho một chuỗi $S$. Hãy đếm xem có bao nhiêu chữ cái in hoa v... |
| 5 | `sca_l16_p05_tach_rieng_chu_so_ra_khoi_van_ban` | Tách riêng chữ số ra khỏi văn bản | **P0** | Khởi động & Quan sát | Cho chuỗi $S$. Hãy nhặt ra toàn bộ các ký tự là chữ số ('0' ... |
| 6 | `sca_l16_p06_tinh_tong_cac_chu_so_trong_chuoi` | Tính tổng các chữ số trong chuỗi | **P0** | Khởi động & Quan sát | Cho một chuỗi văn bản $S$. Hãy tính tổng giá trị của tất cả ... |
| 7 | `sca_l16_p07_doi_chu_hoa_thanh_thuong_nguoc_lai` | Đổi chữ hoa thành thường & ngược lại | **P1** | Cơ bản & Hoàn thành | Cho chuỗi ký tự $S$. Hãy biến đổi chuỗi bằng quy tắc: chữ ho... |
| 8 | `sca_l16_p08_thay_the_ky_tu_bi_mat` | Thay thế ký tự bí mật | **P1** | Cơ bản & Hoàn thành | Nhập một chuỗi $S$. Hãy thay thế tất cả các ký tự khoảng trắ... |
| 9 | `sca_l16_p09_xoa_bo_toan_bo_dau_cach` | Xóa bỏ toàn bộ dấu cách | **P1** | Cơ bản & Hoàn thành | Cho một dòng văn bản $S$. Hãy xóa bỏ tất cả các ký tự khoảng... |
| 10 | `sca_l16_p10_dem_so_luong_nguyen_am` | Đếm số lượng nguyên âm | **P1** | Cơ bản & Hoàn thành | Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu ký tự nguy... |
| 11 | `sca_l16_p11_nen_chuoi_ky_tu_runlength_encoding` | Nén chuỗi ký tự (Run-Length encoding) | **P1** | Cơ bản & Hoàn thành | Cho một chuỗi $S$ chỉ gồm các chữ cái in hoa. Hãy in ra dạng... |
| 12 | `sca_l16_p12_trich_xuat_so_lon_nhat_trong_van_ban` | Trích xuất số lớn nhất trong văn bản | **P1** | Cơ bản & Hoàn thành | Cho chuỗi văn bản $S$. Hãy tìm và in ra giá trị của **con số... |
| 13 | `sca_l16_p13_dem_so_tu_trong_cau` | Đếm số từ trong câu | **P2** | Luyện tập & Vận dụng | Nhập một dòng văn bản $S$ có thể chứa nhiều khoảng trắng thừ... |
| 14 | `sca_l16_p14_tu_dau_tien_tu_cuoi_cung` | Từ đầu tiên & từ cuối cùng | **P2** | Luyện tập & Vận dụng | Cho một câu văn $S$. Hãy in ra từ đầu tiên và từ cuối cùng c... |
| 15 | `sca_l16_p15_ma_ascii_cua_ky_tu` | Mã ASCII của ký tự | **P2** | Luyện tập & Vận dụng | Nhập một ký tự bất kỳ từ bàn phím. Hãy in ra mã số ASCII của... |
| 16 | `sca_l16_p16_ky_tu_ke_tiep_trong_bang_chu_cai` | Ký tự kế tiếp trong bảng chữ cái | **P2** | Luyện tập & Vận dụng | Nhập vào một chữ cái in hoa từ `'A'` đến `'Y'`. Hãy in ra ch... |
| 17 | `sca_l16_p17_tim_tu_dai_nhat_trong_cau` | Tìm từ dài nhất trong câu | **P2** | Luyện tập & Vận dụng | Cho một câu văn $S$. Hãy tìm và in ra từ có độ dài dài nhất ... |
| 18 | `sca_l16_p18_chuan_hoa_khoang_trang` | Chuẩn hóa khoảng trắng | **P2** | Luyện tập & Vận dụng | Cho chuỗi văn bản $S$. Hãy chuẩn hóa câu văn sao cho: không ... |
| 19 | `sca_l16_p19_viet_hoa_chu_cai_dau_moi_tu_title_case` | Viết hoa chữ cái đầu mỗi từ (title case) | **P3** | Vận dụng cao & Sáng tạo | Nhập họ và tên của một bạn học sinh viết chưa đúng quy tắc (... |
| 20 | `sca_l16_p20_dao_nguoc_tung_tu_trong_cau` | Đảo ngược từng từ trong câu | **P3** | Vận dụng cao & Sáng tạo | Cho một câu văn. Hãy đảo ngược thứ tự các chữ cái trong từng... |
| 21 | `sca_l16_p21_mat_ma_caesar_dich_chuyen_k` | Mật mã Caesar dịch chuyển K | **P3** | Vận dụng cao & Sáng tạo | Cho chuỗi $S$ chỉ gồm các chữ cái in hoa và số nguyên $K$ ($... |
| 22 | `sca_l16_p22_giai_ma_mat_thu_caesar` | Giải mã mật thư Caesar | **P3** | Vận dụng cao & Sáng tạo | Cho một bản mật mã $S$ (chỉ gồm các chữ cái in hoa) đã bị mã... |
| 23 | `sca_l16_p23_tu_xuat_hien_nhieu_nhat_trong_doan` | Từ xuất hiện nhiều nhất trong đoạn | **P3** | Vận dụng cao & Sáng tạo | Cho một đoạn văn bản chỉ gồm các từ cách nhau bởi khoảng trắ... |
| 24 | `sca_l16_p24_mat_ma_thay_the_hoan_vi_anagram` | Mật mã thay thế hoán vị (anagram) | **P3** | Vận dụng cao & Sáng tạo | Cho 2 từ $S_1$ và $S_2$. Kiểm tra xem chúng có phải là Anagr... |

---

## 2. Chi Tiết Từng Bài Tập Thực Hành

### Bài 1 (P0): In từng chữ cái xuống dòng
* **Mã bài toán:** `sca_l16_p01_in_tung_chu_cai_xuong_dong`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Duyệt tuần tự qua từng ký tự của văn bản là thao tác nền tảng để phân tích cú pháp và kiểm định luồng dữ liệu ký tự.
* **Nhiệm vụ:** Nhập vào một từ $S$. Hãy in ra từng chữ cái của từ đó, mỗi chữ cái nằm trên một dòng riêng biệt.
* **Dữ liệu vào (Input):** Một chuỗi ký tự $S$ ($1 \le |S| \le 100$).
* **Kết quả ra (Output):** Mỗi ký tự trên một dòng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
CAT
```
### Output
```text
C
A
T
```
### Giải thích

Với dữ liệu đầu vào là `CAT`, kết quả thu được tương ứng là `C
A
T`.

---

### Bài 2 (P0): Chuyển toàn bộ thành chữ hoa
* **Mã bài toán:** `sca_l16_p02_chuyen_toan_bo_thanh_chu_hoa`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Chuẩn hóa toàn bộ văn bản sang dạng chữ in hoa giúp việc đối sánh chuỗi trong các cơ sở dữ liệu không bị ảnh hưởng bởi quy cách gõ phím.
* **Nhiệm vụ:** Nhập một dòng văn bản $S$. Hãy chuyển tất cả các chữ cái trong $S$ thành chữ in hoa và nhân vật nói ra màn hình.
* **Dữ liệu vào (Input):** Một dòng văn bản $S$.
* **Kết quả ra (Output):** Chuỗi sau khi đã in hoa toàn bộ.
* **Dữ liệu mẫu (Sample):**

### Input
```text
ikhedu vietnam
```
### Output
```text
IKHEDU VIETNAM
```
### Giải thích

Với dữ liệu đầu vào là `ikhedu vietnam`, kết quả thu được tương ứng là `IKHEDU VIETNAM`.

---

### Bài 3 (P0): Đếm ký tự 'A' (cả hoa lẫn thường)
* **Mã bài toán:** `sca_l16_p03_dem_ky_tu_a_ca_hoa_lan_thuong`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Thống kê tần suất xuất hiện của một chữ cái cụ thể (không phân biệt hoa thường) là thao tác căn bản trong phân tích văn bản ngôn ngữ.
* **Nhiệm vụ:** Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu chữ cái `'A'` hoặc `'a'` xuất hiện trong chuỗi $S$.
* **Dữ liệu vào (Input):** Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** Số lượng chữ cái 'A' hoặc 'a'.
* **Dữ liệu mẫu (Sample):**

### Input
```text
An va Ba hoc bai
```
### Output
```text
4
```
### Giải thích

Gồm chữ 'A' (1 lần) và 'a' (3 lần trong 'va', 'Ba', 'bai').

---

### Bài 4 (P0): Đếm chữ cái in hoa & in thường
* **Mã bài toán:** `sca_l16_p04_dem_chu_cai_in_hoa_in_thuong`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Đo lường tỉ lệ giữa chữ cái in hoa và in thường giúp hệ thống tự động đánh giá độ phức tạp và độ an toàn của mật khẩu.
* **Nhiệm vụ:** Cho một chuỗi $S$. Hãy đếm xem có bao nhiêu chữ cái in hoa và bao nhiêu chữ cái in thường trong chuỗi đó.
* **Dữ liệu vào (Input):** Chuỗi ký tự $S$.
* **Kết quả ra (Output):** Hai số nguyên cách nhau một khoảng trắng: số lượng chữ in hoa trước, số lượng chữ in thường sau.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Lap Trinh Scratch
```
### Output
```text
3 11
```
### Giải thích

Chữ in hoa: 'L', 'T', 'P' (3 chữ).

---

### Bài 5 (P0): Tách riêng chữ số ra khỏi văn bản
* **Mã bài toán:** `sca_l16_p05_tach_rieng_chu_so_ra_khoi_van_ban`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Bạn An nhận được một bức thư mật mã, trong đó có các chữ số bị giấu lẫn vào giữa các chữ cái. An phải thật tinh mắt mới thấy những con số trốn kỹ trong dòng chữ. Cả nhóm bạn quyết tâm nhặt hết các chữ số ra để đọc mật thư. Hãy giúp bạn An nhặt hết các chữ số bí mật này.
* **Nhiệm vụ:** Cho chuỗi $S$. Hãy nhặt ra toàn bộ các ký tự là chữ số ('0' - '9') và ghép chúng lại theo thứ tự ban đầu để nhân vật nói ra màn hình. Nếu không có chữ số nào, in ra `KHONG CO`.
* **Dữ liệu vào (Input):** Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** Chuỗi các chữ số ghép lại, hoặc `KHONG CO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Toi sinh nam 2014 vao thang 08
```
### Output
```text
201408
```
### Giải thích

Với dữ liệu đầu vào là `Toi sinh nam 2014 vao thang 08`, kết quả thu được tương ứng là `201408`.

---

### Bài 6 (P0): Tính tổng các chữ số trong chuỗi
* **Mã bài toán:** `sca_l16_p06_tinh_tong_cac_chu_so_trong_chuoi`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.
* **Nhiệm vụ:** Cho một chuỗi văn bản $S$. Hãy tính tổng giá trị của tất cả các chữ số xuất hiện trong chuỗi đó.
* **Dữ liệu vào (Input):** Chuỗi văn bản $S$ ($1 \le |S| \le 10^5$).
* **Kết quả ra (Output):** Một số nguyên duy nhất là tổng các chữ số.
* **Dữ liệu mẫu (Sample):**

### Input
```text
A1B2C3D4
```
### Output
```text
10
```
### Giải thích

$1 + 2 + 3 + 4 = 10$.

---

### Bài 7 (P1): Đổi chữ hoa thành thường & ngược lại
* **Mã bài toán:** `sca_l16_p07_doi_chu_hoa_thanh_thuong_nguoc_lai`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Đảo ngược trạng thái viết hoa và viết thường trên toàn bộ văn bản là thao tác chuyển đổi định dạng thường gặp trong các trình biên tập mã nguồn.
* **Nhiệm vụ:** Cho chuỗi ký tự $S$. Hãy biến đổi chuỗi bằng quy tắc: chữ hoa đổi thành chữ thường, chữ thường đổi thành chữ hoa, các ký tự khác (số, dấu câu, khoảng trắng) giữ nguyên.
* **Dữ liệu vào (Input):** Một chuỗi văn bản $S$.
* **Kết quả ra (Output):** Chuỗi sau khi biến đổi.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Hello World 123
```
### Output
```text
hELLO wORLD 123
```
### Giải thích

Với dữ liệu đầu vào là `Hello World 123`, kết quả thu được tương ứng là `hELLO wORLD 123`.

---

### Bài 8 (P1): Thay thế ký tự bí mật
* **Mã bài toán:** `sca_l16_p08_thay_the_ky_tu_bi_mat`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Để chuẩn hóa định dạng văn bản cho đường dẫn liên kết, hệ thống cần thay thế toàn bộ khoảng trống bằng ký tự gạch dưới phân tách.
* **Nhiệm vụ:** Nhập một chuỗi $S$. Hãy thay thế tất cả các ký tự khoảng trắng `" "` trong $S$ bằng dấu gạch dưới `"_"` và in ra kết quả.
* **Dữ liệu vào (Input):** Một chuỗi $S$.
* **Kết quả ra (Output):** Chuỗi sau khi thay thế.
* **Dữ liệu mẫu (Sample):**

### Input
```text
hoc lap trinh de vui
```
### Output
```text
hoc_lap_trinh_de_vui
```
### Giải thích

Với dữ liệu đầu vào là `hoc lap trinh de vui`, kết quả thu được tương ứng là `hoc_lap_trinh_de_vui`.

---

### Bài 9 (P1): Xóa bỏ toàn bộ dấu cách
* **Mã bài toán:** `sca_l16_p09_xoa_bo_toan_bo_dau_cach`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Loại bỏ toàn bộ khoảng trắng thừa giúp nén kích thước chuỗi và chuẩn hóa dữ liệu khóa tìm kiếm.
* **Nhiệm vụ:** Cho một dòng văn bản $S$. Hãy xóa bỏ tất cả các ký tự khoảng trắng trong chuỗi để thu được một chuỗi viết liền hoàn toàn.
* **Dữ liệu vào (Input):** Một dòng văn bản $S$ ($1 \le |S| \le 10^5$).
* **Kết quả ra (Output):** Chuỗi viết liền không còn khoảng trắng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Lap Trinh Scratch Bang A
```
### Output
```text
LapTrinhScratchBangA
```
### Giải thích

Với dữ liệu đầu vào là `Lap Trinh Scratch Bang A`, kết quả thu được tương ứng là `LapTrinhScratchBangA`.

---

### Bài 10 (P1): Đếm số lượng nguyên âm
* **Mã bài toán:** `sca_l16_p10_dem_so_luong_nguyen_am`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Trong giờ tiếng Anh, cô giáo dạy cả lớp bài hát về các chữ cái vui nhộn. Cô nói trong tiếng Anh, 5 chữ cái: `A, E, I, O, U` (cả hoa lẫn thường) được gọi là nguyên âm (vowels). Bạn nào đếm đúng số nguyên âm trong một từ sẽ được hát trước cả lớp. Hãy giúp cả lớp đếm số nguyên âm thật nhanh.
* **Nhiệm vụ:** Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu ký tự nguyên âm trong chuỗi $S$.
* **Dữ liệu vào (Input):** Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** Số lượng nguyên âm.
* **Dữ liệu mẫu (Sample):**

### Input
```text
EDUCATION
```
### Output
```text
5
```
### Giải thích

Các nguyên âm: E, U, A, I, O (có 5 nguyên âm).

---

### Bài 11 (P1): Nén chuỗi ký tự (Run-Length encoding)
* **Mã bài toán:** `sca_l16_p11_nen_chuoi_ky_tu_runlength_encoding`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Bạn Nam gấp thật nhiều ngôi sao giấy cùng màu rồi xếp chúng thành hàng dài trên bàn. Cô giáo dạy thuật toán nén chuỗi đơn giản thay thế một dãy các ký tự giống nhau liên tiếp bằng ký tự đó kèm theo số lần lặp lại.
 Ví dụ: `AAABBC` nén thành `A3B2C1`.
Nam muốn ghi lại hàng ngôi sao thật gọn vào sổ. Hãy giúp bạn Nam viết chương trình nén chuỗi thật gọn.
* **Nhiệm vụ:** Cho một chuỗi $S$ chỉ gồm các chữ cái in hoa. Hãy in ra dạng nén của chuỗi $S$.
* **Dữ liệu vào (Input):** Một chuỗi $S$ ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** Chuỗi sau khi nén.
* **Dữ liệu mẫu (Sample):**

### Input
```text
AAABBCCCC
```
### Output
```text
A3B2C4
```
### Giải thích

Với dữ liệu đầu vào là `AAABBCCCC`, kết quả thu được tương ứng là `A3B2C4`.

---

### Bài 12 (P1): Trích xuất số lớn nhất trong văn bản
* **Mã bài toán:** `sca_l16_p12_trich_xuat_so_lon_nhat_trong_van_ban`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Lớp trưởng ghi một bài báo cáo, trong đó có các con số nằm rải rác giữa các câu chữ. Một con số có thể có nhiều chữ số liên tiếp nhau. Cả lớp muốn biết con số nào to nhất để khen bạn được điểm cao. Hãy giúp lớp trưởng tìm ra con số lớn nhất trong bài báo cáo.
* **Nhiệm vụ:** Cho chuỗi văn bản $S$. Hãy tìm và in ra giá trị của **con số nguyên lớn nhất** xuất hiện trong chuỗi đó. Dữ liệu đảm bảo có ít nhất 1 chữ số.
* **Dữ liệu vào (Input):** Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** Số nguyên lớn nhất tìm được.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Lop 5A co 38 hoc sinh va 105 quyen sach
```
### Output
```text
105
```
### Giải thích

Các con số xuất hiện là: 5, 38, 105. Số lớn nhất là 105.

---

### Bài 13 (P2): Đếm số từ trong câu
* **Mã bài toán:** `sca_l16_p13_dem_so_tu_trong_cau`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Đếm số lượng từ trong một đoạn văn bản là chỉ số cơ bản nhất của các phần mềm xử lý soạn thảo và phân tích ngôn ngữ tự nhiên.
* **Nhiệm vụ:** Nhập một dòng văn bản $S$ có thể chứa nhiều khoảng trắng thừa ở đầu, cuối hoặc giữa các từ. Hãy đếm xem câu văn đó có bao nhiêu từ.
* **Dữ liệu vào (Input):** Một dòng văn bản $S$ ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** Số lượng từ trong câu.
* **Dữ liệu mẫu (Sample):**

### Input
```text
 Chuc mung nam moi 
```
### Output
```text
4
```
### Giải thích

Có 4 từ: 'Chuc', 'mung', 'nam', 'moi'.

---

### Bài 14 (P2): Từ đầu tiên & từ cuối cùng
* **Mã bài toán:** `sca_l16_p14_tu_dau_tien_tu_cuoi_cung`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Trích xuất từ mở đầu và từ kết thúc hỗ trợ xác định cấu trúc ngữ pháp và tiêu đề của một câu lệnh truy vấn.
* **Nhiệm vụ:** Cho một câu văn $S$. Hãy in ra từ đầu tiên và từ cuối cùng của câu văn đó trên 2 dòng riêng biệt.
* **Dữ liệu vào (Input):** Một dòng văn bản có ít nhất 1 từ.
* **Kết quả ra (Output):** Dòng 1 in từ đầu tiên, dòng 2 in từ cuối cùng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Hoc Scratch cuc vui
```
### Output
```text
Hoc
vui
```
### Giải thích

Với dữ liệu đầu vào là `Hoc Scratch cuc vui`, kết quả thu được tương ứng là `Hoc
vui`.

---

### Bài 15 (P2): Mã ASCII của ký tự
* **Mã bài toán:** `sca_l16_p15_ma_ascii_cua_ky_tu`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Mỗi ký tự hiển thị trên máy tính đều được mã hóa bằng một số nguyên duy nhất theo chuẩn ASCII. Việc tra cứu mã này là kiến thức cốt lõi về biểu diễn dữ liệu.
* **Nhiệm vụ:** Nhập một ký tự bất kỳ từ bàn phím. Hãy in ra mã số ASCII của ký tự đó.
* **Dữ liệu vào (Input):** Một ký tự duy nhất $C$.
* **Kết quả ra (Output):** Một số nguyên là mã ASCII.
* **Dữ liệu mẫu (Sample):**

### Input
```text
A
```
### Output
```text
65
```
### Giải thích

Với dữ liệu đầu vào là `A`, kết quả thu được tương ứng là `65`.

---

### Bài 16 (P2): Ký tự kế tiếp trong bảng chữ cái
* **Mã bài toán:** `sca_l16_p16_ky_tu_ke_tiep_trong_bang_chu_cai`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Xác định ký tự liền sau trong bảng chữ cái dựa trên phép tịnh tiến mã số ASCII là nền tảng của nhiều thuật toán sinh khóa và mã hóa cổ điển.
* **Nhiệm vụ:** Nhập vào một chữ cái in hoa từ `'A'` đến `'Y'`. Hãy in ra chữ cái đứng ngay liền sau nó trong bảng chữ cái tiếng Anh.
* **Dữ liệu vào (Input):** Một ký tự in hoa $C \in ['A' \dots 'Y']$.
* **Kết quả ra (Output):** Chữ cái liền sau.
* **Dữ liệu mẫu (Sample):**

### Input
```text
C
```
### Output
```text
D
```
### Giải thích

Với dữ liệu đầu vào là `C`, kết quả thu được tương ứng là `D`.

---

### Bài 17 (P2): Tìm từ dài nhất trong câu
* **Mã bài toán:** `sca_l16_p17_tim_tu_dai_nhat_trong_cau`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.
* **Nhiệm vụ:** Cho một câu văn $S$. Hãy tìm và in ra từ có độ dài dài nhất trong câu. Nếu có nhiều từ cùng độ dài dài nhất, in ra từ đầu tiên xuất hiện.
* **Dữ liệu vào (Input):** Một dòng văn bản $S$.
* **Kết quả ra (Output):** Từ dài nhất tìm được.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Hoc lap trinh rat thu vi
```
### Output
```text
trinh
```
### Giải thích

Từ 'trinh' có 5 chữ cái (dài nhất).

---

### Bài 18 (P2): Chuẩn hóa khoảng trắng
* **Mã bài toán:** `sca_l16_p18_chuan_hoa_khoang_trang`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Na tập đánh máy để viết thiệp mời sinh nhật cho cả lớp. Khi đánh máy, một bạn học sinh lỡ tay bấm rất nhiều dấu cách thừa giữa các từ và ở hai đầu câu văn. Tấm thiệp trông rời rạc và chưa đẹp mắt chút nào. Hãy giúp Na dọn dẹp tấm thiệp cho gọn gàng.
* **Nhiệm vụ:** Cho chuỗi văn bản $S$. Hãy chuẩn hóa câu văn sao cho: không còn khoảng trắng ở đầu và cuối câu, giữa mỗi từ chỉ có duy nhất **một dấu cách**.
* **Dữ liệu vào (Input):** Một dòng văn bản $S$ ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** Câu văn chuẩn hóa.
* **Dữ liệu mẫu (Sample):**

### Input
```text
 Scratch rat la tuyet 
```
### Output
```text
Scratch rat la tuyet
```
### Giải thích

Với dữ liệu đầu vào là `Scratch rat la tuyet`, kết quả thu được tương ứng là `Scratch rat la tuyet`.

---

### Bài 19 (P3): Viết hoa chữ cái đầu mỗi từ (title case)
* **Mã bài toán:** `sca_l16_p19_viet_hoa_chu_cai_dau_moi_tu_title_case`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Quy tắc viết hoa chữ cái đầu mỗi từ là chuẩn mực định dạng bắt buộc khi lưu trữ danh tính người dùng trong hệ thống cơ sở dữ liệu.
* **Nhiệm vụ:** Nhập họ và tên của một bạn học sinh viết chưa đúng quy tắc (ví dụ: `nguyen van an`). Hãy chuẩn hóa họ tên bằng cách viết hoa chữ cái đầu tiên của mỗi từ và viết thường các chữ cái còn lại.
* **Dữ liệu vào (Input):** Một chuỗi họ tên.
* **Kết quả ra (Output):** Họ tên sau khi chuẩn hóa.
* **Dữ liệu mẫu (Sample):**

### Input
```text
nguyen van an
```
### Output
```text
Nguyen Van An
```
### Giải thích

Với dữ liệu đầu vào là `nguyen van an`, kết quả thu được tương ứng là `Nguyen Van An`.

---

### Bài 20 (P3): Đảo ngược từng từ trong câu
* **Mã bài toán:** `sca_l16_p20_dao_nguoc_tung_tu_trong_cau`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Đảo ngược các ký tự nội bộ của từng từ trong khi vẫn bảo toàn thứ tự các từ trong câu là bài toán rèn luyện kỹ năng kết hợp tách từ và cắt lát chuỗi.
* **Nhiệm vụ:** Cho một câu văn. Hãy đảo ngược thứ tự các chữ cái trong từng từ một, nhưng giữ nguyên vị trí của các từ trong câu.
* **Dữ liệu vào (Input):** Một dòng văn bản.
* **Kết quả ra (Output):** Câu văn mới với từng từ bị đảo ngược.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Toi yeu Viet Nam
```
### Output
```text
ioT uey teiV maN
```
### Giải thích

'Toi' -> 'ioT', 'yeu' -> 'uey'...

---

### Bài 21 (P3): Mật mã Caesar dịch chuyển K
* **Mã bài toán:** `sca_l16_p21_mat_ma_caesar_dich_chuyen_k`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Bạn Bin và cả nhóm chơi trò điệp viên gửi thư bí mật cho nhau trong sân trường. Hoàng đế Caesar mã hóa bức thư gồm các chữ cái in hoa (`'A'` đến `'Z'`) bằng cách dịch chuyển mỗi chữ cái sang phải $K$ bước theo vòng tròn 26 chữ cái ($A \to B \dots Z \to A$). Cả nhóm háo hức muốn tự mã hóa thư của riêng mình. Hãy giúp bạn Bin viết chương trình mã hóa thư.
* **Nhiệm vụ:** Cho chuỗi $S$ chỉ gồm các chữ cái in hoa và số nguyên $K$ ($1 \le K \le 25$). Hãy in ra bản mật mã sau khi mã hóa.
* **Dữ liệu vào (Input):** Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số $K$.
* **Kết quả ra (Output):** Chuỗi sau khi mã hóa.
* **Dữ liệu mẫu (Sample):**

### Input
```text
ABCXYZ
3
```
### Output
```text
DEFABC
```
### Giải thích

'A'->'D', 'B'->'E', 'X'->'A', 'Y'->'B', 'Z'->'C'.
* **Công thức toán học:** `chr((ord(ch) - ord('A') + k) % 26 + ord('A'))`.

---

### Bài 22 (P3): Giải mã mật thư Caesar
* **Mã bài toán:** `sca_l16_p22_giai_ma_mat_thu_caesar`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Mật mã Caesar là một trong những phương pháp mã hóa thay thế lâu đời nhất, hoạt động bằng cách dịch chuyển từng chữ cái trong bảng mã theo một bước nhảy cố định.
* **Nhiệm vụ:** Cho một bản mật mã $S$ (chỉ gồm các chữ cái in hoa) đã bị mã hóa Caesar với bước nhảy $K$. Hãy giải mã để tìm lại thông điệp ban đầu.
* **Dữ liệu vào (Input):** Dòng 1 chứa bản mật mã $S$. Dòng 2 chứa số nguyên $K$ ($1 \le K \le 25$).
* **Kết quả ra (Output):** Thông điệp ban đầu trước khi mã hóa.
* **Dữ liệu mẫu (Sample):**

### Input
```text
DEFABC
3
```
### Output
```text
ABCXYZ
```
### Giải thích

Với dữ liệu đầu vào là `DEFABC
3`, kết quả thu được tương ứng là `ABCXYZ`.

---

### Bài 23 (P3): Từ xuất hiện nhiều nhất trong đoạn
* **Mã bài toán:** `sca_l16_p23_tu_xuat_hien_nhieu_nhat_trong_doan`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Tìm từ xuất hiện với tần suất cao nhất trong một văn bản là bài toán quan trọng trong trích xuất từ khóa và khai phá dữ liệu văn bản.
* **Nhiệm vụ:** Cho một đoạn văn bản chỉ gồm các từ cách nhau bởi khoảng trắng. Hãy tìm xem từ nào xuất hiện nhiều lần nhất trong đoạn văn đó và xuất hiện bao nhiêu lần. Dữ liệu đảm bảo chỉ có 1 từ xuất hiện nhiều nhất.
* **Dữ liệu vào (Input):** Một đoạn văn bản $S$ gồm các chữ cái viết thường.
* **Kết quả ra (Output):** Từ xuất hiện nhiều nhất và số lần xuất hiện, cách nhau một khoảng trắng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
cam quyt mit dua cam xoai cam dua
```
### Output
```text
cam 3
```
### Giải thích

Với dữ liệu đầu vào là `cam quyt mit dua cam xoai cam dua`, kết quả thu được tương ứng là `cam 3`.

---

### Bài 24 (P3): Mật mã thay thế hoán vị (anagram)
* **Mã bài toán:** `sca_l16_p24_mat_ma_thay_the_hoan_vi_anagram`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Trong giờ thủ công, hai bạn cùng xáo trộn các thẻ chữ cái để xếp thành từ mới. Hai từ được gọi là "Anagram" (hoán vị ký tự của nhau) nếu chúng có thể tạo thành từ nhau bằng cách xáo trộn lại thứ tự các chữ cái (ví dụ: `silent` và `listen`, `heart` và `earth`). Cả lớp thi xem ai xếp được cặp từ trùng khớp nhau. Hãy giúp các bạn kiểm tra xem hai từ có phải Anagram không.
* **Nhiệm vụ:** Cho 2 từ $S_1$ và $S_2$. Kiểm tra xem chúng có phải là Anagram của nhau không. In `YES` nếu đúng, ngược lại in `NO`.
* **Dữ liệu vào (Input):** Hai dòng, mỗi dòng chứa một từ viết thường ($1 \le |S_1|, |S_2| \le 10^5$).
* **Kết quả ra (Output):** `YES` hoặc `NO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
listen
silent
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `listen
silent`, kết quả thu được tương ứng là `YES`.

---
